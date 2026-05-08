from PySide6.QtWidgets import QMainWindow, QFileDialog, QDialog, QMessageBox, QPushButton
from PySide6.QtCore import QTimer
from gui.uiPy.MainWindow import Ui_MainWindow
from gui.dialogs.dialogParameters import dialogParameters
from gui.dialogs.dialogCompareWithTrace import dialogCompareTrace
from gui.dialogs.dialogGradParams import gradParameters
from gui.canvas import CDFPlot
from multiprocessing import Process, Queue, Event
from services.search_service import search_run
from services.analysis_service import compareMapWithTrace, compareTraces, getCdfForTrace, getInfoForTrace, getRelativeErr
from services.io_service import info_text, loadMap, read_trace, parse_matrix
from services.simulation_service import start_generation_service
from services.theme_service import ThemeService

class window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.stackedWidget.setCurrentWidget(self.startPage)         # начальная страница
        self.selected_method = self.comboSelectAlg.currentText()    # инициализация начального алгоритма
        self._dialogParams = None
        self._dialogView = None
        self._dialogGrad = None
        self.extra_params = {}
        self.gradParams = [1, False, None]      # хранятся параметры для градиентного спука для подгона (порог, используем?, параметры)
        self.cdf_plot_compare = CDFPlot(self)
        self.cdf_plot_read_trace = CDFPlot(self)
        self.verticalLayoutPlot.addWidget(self.cdf_plot_compare)
        self.verticalLayoutPlotInReadTrace.addWidget(self.cdf_plot_read_trace)
        self.originTraceIsLoaded = False
        self.processTimer = QTimer(self)
        self.processStarted = False
        self.stop_event = Event()
        self.process = None
        self._connect_signals()
    

    def updateProgressBar(self):
        self.progressValue += 5
        if self.progressValue > 100:
            self.progressValue = 0
        self.progressSearch.setValue(self.progressValue)
    # сигналы
    def _connect_signals(self):
        # переключение страниц кнопками
        self.btnPageTrace.clicked.connect(
            lambda: self.switch_page(self.btnPageTrace, self.tracePage)
        )
        self.btnPageSearch.clicked.connect(
            lambda: self.switch_page(self.btnPageSearch, self.searchPage)
        )
        self.btnPageGenerate.clicked.connect(
            lambda: self.switch_page(self.btnPageGenerate, self.genTracePage)
        )
        self.btnPageCompare.clicked.connect(
            lambda: self.switch_page(self.btnPageCompare, self.comparePage)
        )
        self.btnReadTrace.clicked.connect(self._load_trace)         # сигнал на открытие файла для чтения трассы
        self.checkSkew.toggled.connect(self.spinSkew.setEnabled)    # сигнал на checkbox (включить/выключить асимметрию)
        self.checkKurt.toggled.connect(self.spinKurt.setEnabled)    # сигнал на checkbox (включить/выключить эксцесс)
        self.comboSelectAlg.currentIndexChanged.connect(self.on_method_changed) # сигнал на comboBox (выбор алгоритма)
        self.btnStartSearch.clicked.connect(self.start_search)            # сигнал на кнопку начала поиска
        self.btnSave.clicked.connect(self._save_map_to_file)               # сигнал на кнопку сохранения MAP-потока
        self.btnAdditionalParameters.clicked.connect(self._open_dialog) # открытие доп.параметров
        self.btnGenerate.clicked.connect(self.generateEvent)        # сигнал на кнопку генерация трассы
        self.btnSaveTrace.clicked.connect(self._save_trace_to_file) # сигнал на кнопку сохранения выборки
        self.btnLoadMap.clicked.connect(self._load_map)             # сигнал на кнопку для загрузки MAP-потока
        self.btnLoadTraces.clicked.connect(self._load_traces)       # сигнал на кнопку для загрузки трасс для сравнения
        self.btnCompareTraces.clicked.connect(self.compare_traces)  # сигнал на кнопку сравнения трасс
        self.btnCompareWithOrigin.clicked.connect(self.compare_with_origin) # сигнал на кнопку сравнения потока с трассой
        self.btnTranferCharacteristics.clicked.connect(self.transfer) # сигнал на кнопку для переноса характеристик над подбор
        self.processTimer.timeout.connect(self.checkProcess)        # сигнал на таймер для проверки завершения поиска
        self.btnGradientParams.clicked.connect(self._dialogGradParams) # сигнал на кнопку открытия параетров градиентного спуска для подгонки
        self.lightTheme.triggered.connect(lambda: self.update_theme('light'))
        self.darkTheme.triggered.connect(lambda: self.update_theme('dark'))

    # обновление темы и графиков
    def update_theme(self, theme):
        ThemeService.set_theme(theme)
        self.cdf_plot_compare.apply_theme()
        self.cdf_plot_read_trace.apply_theme()

    # Переключение страниц
    def switch_page(self, button, page):
        for obj in self.buttons.children():
            if isinstance(obj, QPushButton):
                obj.setChecked(False)

        button.setChecked(True)
        self.stackedWidget.setCurrentWidget(page)

    # загрузка трасс для сравнения
    def _load_traces(self):
        files, _ = QFileDialog.getOpenFileNames(self, "Выберите 2 файла", "", "Текстовые файлы(*.txt)")

        if files:
            if len(files) != 2:
                QMessageBox.warning(self, "Ошибка", "Выберите 2 файла")
            else:
                self.file1, self.file2 = files
                self.compare_traces()

    # сравнение трасс
    def compare_traces(self):
        try:
            trace1 = read_trace(self.file1)
            trace2 = read_trace(self.file2)
            t = self.spinTime.value()
            resultCompare = compareTraces(trace1, trace2, t)
            self.cdf_plot_compare.plot(*resultCompare)
        except Exception as e:
            QMessageBox.warning(
                self,
                'Ошибка',
                f'Ошибка чтения файла:{e}'
            )

    # сравнение потока с исходной трассой
    def compare_with_origin(self):
        if not self.originTraceIsLoaded:
            QMessageBox.warning(self, "Ошибка", "Прочитайте исходную трассу. Кнопка \"Чтение трассы\"")
            return
        resultCompare = compareMapWithTrace((self.Q, self.Lambda, self.D), self.counts)
        self._dialogView = dialogCompareTrace(*resultCompare, label1='Трасса', label2='MAP-поток')
        self._dialogView.exec()
        self._dialogView = None

    # перенос характеристик после чтения трассы
    def transfer(self):
        if not self.originTraceIsLoaded:
            QMessageBox.warning(self, "Ошибка", "Загрузите трассу")
        else:
            self.spinMean.setValue(self.characteristics[0])
            self.spinCV.setValue(self.characteristics[2])
            self.spinCorr.setValue(self.characteristics[3])
            self.spinSkew.setValue(self.characteristics[4])
            self.spinKurt.setValue(self.characteristics[5])
            del self.characteristics
            self.switch_page(self.btnPageSearch, self.searchPage)

    
    # загрузка MAP-потока
    def _load_map(self):
        self.matrixQ.clear()
        self.matrixL.clear()
        self.matrixD.clear()
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Выбор файла", "", "Текстовые файлы (*.txt)"
        )
        if file_path:
            try:
                m = loadMap(file_path)
            except Exception as e:
                QMessageBox.critical(self, "Ошибка чтения", f"{e} Проверьте файл с параметрами")
                return
            self.spinSizeMap.setValue(m.size)
            for i in range(m.size):
                for j in range(m.size):
                    self.matrixQ.insertPlainText(str(m.Q[i][j]) + ' ')
                    self.matrixD.insertPlainText(str(m.D[i][j]) + ' ')
                self.matrixQ.insertPlainText('\n')
                self.matrixD.insertPlainText('\n')
                self.matrixL.insertPlainText(str(m.lambda_[i][i]) + '\n')

    # чтение файла при нажатии на кнопку
    def _load_trace(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Выбор файла", "", "Текстовые файлы (*.txt)"
        )
        if file_path:
            try:
                data = read_trace(file_path)
                self.characteristics = getInfoForTrace(data)
            except Exception as e:
                QMessageBox.critical(self, "Критическая ошибка", f"Ошибка чтения файла: {e}")
                return 

            self.textEdit.setText(info_text(len(data), self.characteristics))
            self.counts, v, cdf = getCdfForTrace(data)
            self.cdf_plot_read_trace.plot(v, cdf, label1=None)
            self.originTraceIsLoaded = True
            del data
    
    # сохранение трассы в файл
    def _save_trace_to_file(self):
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Сохранение файла", "", "Текстовые файлы (*.txt)"
        )
        if file_path:
            with open(file_path, 'w') as f:
                f.write(self.textHistory.toPlainText())
            self.textHistory.clear()

    # сохранение потока в файл
    def _save_map_to_file(self):
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Сохранение файла", "", "Текстовые файлы (*.txt)"
        )
        if file_path:
            with open(file_path, 'w') as f:
                f.write(f"{len(self.Q)}\n")
                for row in self.Q:
                    f.write(" ".join(f'{x:4f}' for x in row) + '\n')
                for i in range(len(self.Lambda)):
                    f.write(f'{self.Lambda[i][i]:4f}\n')
                for row in self.D:
                    f.write(" ".join(f'{x:4f}' for x in row) + '\n')


    def _show_matrix(self, Q, Lambda, D):
        # Устанавливаем текст с переносами строк
        self.labelQ.setText(matrix_to_text(Q, "Q"))
        self.labelLambda.setText(matrix_to_text(Lambda, "Λ"))  # символ Lambda
        self.labelD.setText(matrix_to_text(D, "D"))

    # выбор метода
    def on_method_changed(self):
        self.selected_method = self.comboSelectAlg.currentText()
        self.extra_params = {}
        self._dialogParams = None

    # генерация событий
    def generateEvent(self):
        if not self.processStarted:
            self.textHistory.clear()
            size = self.spinSizeMap.value()
            try:
                q = parse_matrix(self.matrixQ.toPlainText(), "Q")
                l = parse_matrix(self.matrixL.toPlainText(), "Λ")
                d = parse_matrix(self.matrixD.toPlainText(), "D")
                if size != len(q) or size != len(l) or size != len(d):
                    QMessageBox.warning(self, "Ошибка", "Размеры матриц не совпадают. Проверьте входные данные")
                    return
            except:
                return
            total_events = self.spinTotalEvents.value()
            self.progressGenerate.setMaximum(total_events)
            self.btnGenerate.setText("Отмена")
            self.processStarted = True

            self.stop_event.clear()
            self.process, self.queue = start_generation_service(q, l, d, total_events, self.stop_event)
            self.timer = QTimer()
            self.timer.timeout.connect(self.updateBar)
            self.timer.start(100)
        else:
            self.processStarted = False
            self.cancel_generation()
            self.timer.stop()
            self.btnGenerate.setText("Сгенерировать")

    # функция остановки генерации
    def cancel_generation(self):
        if self.process and self.process.is_alive():
            self.processStarted = False
            # отправляем сигнал о завершении работы
            self.stop_event.set()
            # ждем завершения
            self.process.join(timeout=1)

            # если процесс не завершился, то принудительно завершаем
            if self.process.is_alive():
                self.process.terminate()
                self.process.join()
        self.timer.stop()
        del self.timer


    # обновление прогресс-бара в генераторе событий
    def updateBar(self):
        buffer = []
        last_progress = None

        while not self.queue.empty():
            msg = self.queue.get()
            if msg[0] == 'batch':
                values, count = msg[1], msg[2]
                buffer.extend(f"{v:6f}\n" for v in values)
                last_progress = count

        # обновляем отображение лога событий
        if buffer:
            self.textHistory.insertPlainText(''.join(buffer))

        # обновляем прогресс-бар
        if last_progress is not None:
            self.progressGenerate.setValue(last_progress)

        # при завершении генерации меняется название кнопки
        if last_progress == self.progressGenerate.maximum():
            self.btnGenerate.setText("Сгенерировать")
            self.processStarted = False
            self.timer.stop()
            del self.timer


    # запуск поиска
    def start_search(self):
        if not self.processStarted:
            self.processStarted = True
            self.btnStartSearch.setText("Отмена")
            # собираем параметры
            args = (
                self.spinSize.value(),
                self.spinMean.value(),
                self.spinCV.value(),
                self.spinCorr.value(),
                self.spinSkew.value() if self.checkSkew.isChecked() else None,
                self.spinKurt.value() if self.checkKurt.isChecked() else None,
                self.selected_method,
                self.extra_params,
                self.gradParams
            )
            self.queue = Queue()
            # создаем процесс
            self.process = Process(
                target=_run_search_process,
                args=(args, self.queue)
            )
            # запускам процесс
            self.process.start()
            self.processTimer.start(100)
            self.progressSearch.setMaximum(0)
        else:
            self.process.terminate()
            self.progressSearch.setMaximum(1)
            self.progressSearch.setValue(1)
            self.processTimer.stop()
            self.processStarted = False
            self.btnStartSearch.setText("Подобрать MAP-поток")
            self.textInfoSearch.setText("Поиск отменен.")


    # открывает диалоговое окно с доп.параметрами
    def _open_dialog(self):
        if self._dialogParams is None:
            self._dialogParams = dialogParameters(start_page=self.comboSelectAlg.currentIndex(), parent=self)
            
        if self._dialogParams.exec() == QDialog.Accepted:
            self.extra_params = self._dialogParams.get_parameters()

    # Обновление результатов поиска параметров
    def checkProcess(self):
        if not self.queue.empty():
            self.Q, self.Lambda, self.D, R, characteristics, loss = self.queue.get()
            self.process.join()
            self.processTimer.stop()
            self.progressSearch.setMaximum(1)
            self.progressSearch.setValue(1)

            self._show_matrix(self.Q, self.Lambda, self.D)
            self.textInfoSearch.setText(
                INFO_TEMPLATE.format(
                    mean=characteristics[0],
                    var=characteristics[1],
                    cv=characteristics[2],
                    corr=characteristics[3],
                    skew=characteristics[4],
                    kurt=characteristics[5],
                    cvPer=getRelativeErr(self.spinCV.value(), characteristics[2]),
                    corrPer=getRelativeErr(self.spinCorr.value(), characteristics[3]),
                    skewPer=getRelativeErr(self.spinSkew.value(), characteristics[4]),
                    kurtPer=getRelativeErr(self.spinKurt.value(), characteristics[5]),
                    R=R.round(4),
                    loss=loss
                )
            )
            # self.tmp_Q = Q
            # self.tmp_L = Lambda
            # self.tmp_D = D
            self.btnStartSearch.setText("Подобрать MAP-поток")
            self.processStarted = False

    # открывает диалоговое окно с параметрами градиентного спуска
    def _dialogGradParams(self):
        if self._dialogGrad is None:
            self._dialogGrad = gradParameters()
        if self._dialogGrad.exec() == QDialog.Accepted:
            self.gradParams = self._dialogGrad.getParameters()
            print(self.gradParams)
        

def _run_search_process(args, queue):
    result = search_run(args)
    queue.put(result)

def matrix_to_text(matrix, name="Q"):
    """Возвращает строку вида 'Q = [ ... ]' с переносами строк для QLabel"""
    lines = ["  ".join(f"{x: .3f}" for x in row) for row in matrix]
    body = "\n".join(lines)
    return f"{name} = \n{body}\n"



INFO_TEMPLATE="""Получившиеся числовые характеристики длин интервалов максимально возможно приближены к заданным
Ошибка (MSE): {loss:.2e}

Среднее: {mean:.4f}
Дисперсия: {var:.4f}
Коэффициент вариации: {cv} (погрешность {cvPer:.2f}%)
Коэффициент корреляции: {corr} (погрешность {corrPer:.2f}%)
Коэффициент асимметрии: {skew} (погрешность {skewPer:.2f}%)
Коэффициент эксцесса: {kurt} (погрешность {kurtPer:.2f}%)
Стационарное распределение вероятностей: {R}
"""