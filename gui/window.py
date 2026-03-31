from PySide6.QtWidgets import QMainWindow, QFileDialog, QDialog, QMessageBox, QApplication
from PySide6.QtCore import QTimer
from gui.uiPy.MainWindow import Ui_MainWindow
from gui.dialogs.dialogParameters import dialogParameters
from gui.dialogs.dialogCompareWithTrace import dialogCompareTrace
from gui.dialogs.dialogGradParams import gradParameters
from gui.canvas import CDFPlot
from core import analysisModule as am
from core import searchModule as sm
from core import SGD
from core.MAP import MAP
from core.GradDescent import Gradient
from multiprocessing import Process, Queue, Event

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

    # Переключение страниц
    def switch_page(self, button, page):
        # сброс кнопок
        for btn in [
            self.btnPageTrace,
            self.btnPageSearch,
            self.btnPageGenerate,
            self.btnPageCompare
            ]:
            btn.setChecked(False)
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
            counts1 = am.event_count_distribution(trace1, t)
            counts2 = am.event_count_distribution(trace2, t)
            v1, cdf1 = am.empirical_cdf(counts1)
            v2, cdf2 = am.empirical_cdf(counts2)
            ks, ksx = am.empirical_kolmogorov_distance(v1, cdf1, v2, cdf2)
            self.cdf_plot_compare.plot(v1, cdf1, ks, ksx, v2, cdf2,)
        except:
            return

    # сравнение потока с исходной трассой
    def compare_with_origin(self):
        if not self.originTraceIsLoaded:
            QMessageBox.warning(self, "Ошибка", "Прочитайте исходную трассу. Кнопка \"Чтение трассы\"")
            return
        tmp_map = MAP(self.tmp_Q, self.tmp_L, self.tmp_D, self.spinSize.value())
        n_max = max(self.counts) + 5
        probs = tmp_map.event_count_distribution(n_max, t=5)
        cdf_theory = am.np.cumsum(probs)
        values_theory = am.np.arange(len(cdf_theory))
        values_emp, cdf_emp = am.empirical_cdf(self.counts)
        ks, ksx = am.empirical_kolmogorov_distance(values_emp, cdf_emp, values_theory, cdf_theory)
        self._dialogView = dialogCompareTrace(values_emp, cdf_emp, values_theory, cdf_theory, ks, ksx, label1='Трасса', label2='MAP-поток')
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
            m = MAP(name=file_path)
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
            data = read_trace(file_path)
            if not data:
                QMessageBox.critical(self, "Критическая ошибка", "Ошибка чтения файла: файл пустой")
                return
            self.characteristics, error = am.analysis(data)
            if error:
                QMessageBox.critical(self, "Критическая ошибка", "Ошибка чтения файла:\n" + error)
            else:
                self.textEdit.setText(f"""Всего событий: {len(data)}
Среднее: {self.characteristics[0]:.6f}
Дисперсия:  {self.characteristics[1]:.6f}
Коэффициент вариации: {self.characteristics[2]:.6f}
Коэффициент корреляции: {self.characteristics[3]:.6f}
Коэффициент асимметрии: {self.characteristics[4]:.6f}
Коэффициент эксцесса: {self.characteristics[5]:.6f}
""")
                self.counts = am.event_count_distribution(data, 5)
                v, cdf = am.empirical_cdf(self.counts)
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
                f.write(f"{len(self.tmp_Q)}\n")
                for row in self.tmp_Q:
                    f.write(" ".join(f'{x:4f}' for x in row) + '\n')
                for i in range(len(self.tmp_L)):
                    f.write(f'{self.tmp_L[i][i]:4f}\n')
                for row in self.tmp_D:
                    f.write(" ".join(f'{x:4f}' for x in row) + '\n')
            del self.tmp_Q
            del self.tmp_L
            del self.tmp_D


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
                q = am.np.array(parse_matrix(self.matrixQ.toPlainText(), "Q"))
                l = am.np.array(parse_matrix(self.matrixL.toPlainText(), "Λ"))
                d = am.np.array(parse_matrix(self.matrixD.toPlainText(), "D"))
                if size != len(q) or size != len(l) or size != len(d):
                    QMessageBox.warning(self, "Ошибка", "Размеры матриц не совпадают. Проверьте входные данные")
                    return
            except:
                return
            total_events = self.spinTotalEvents.value()
            self.progressGenerate.setMaximum(total_events)
            self.btnGenerate.setText("Отмена")
            self.processStarted = True
            self.start_generation(q, l, d, size, total_events)
        else:
            self.processStarted = False
            self.cancel_generation()
            self.btnGenerate.setText("Сгенерировать")

        


    # старт процесса с имитационной моделью
    def start_generation(self, q, l, d, size, total_events):
        self.stop_event.clear()
        self.queue = Queue()

        self.process = Process(
            target=generate_worker,
            args=(q, l, d, size, total_events, self.stop_event, self.queue)
        )
        self.process.start()

        self.timer = QTimer()
        self.timer.timeout.connect(self.updateBar)
        self.timer.start(100)

    # функция остановки генерации
    def cancel_generation(self):
        if self.process and self.process.is_alive():
            self.stop_event.set()

            self.process.join(timeout=1)

            if self.process.is_alive():
                self.process.terminate()
                self.process.join()
        self.timer.stop()


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


    # запуск поиска
    def start_search(self):
        if not self.processStarted:
            self.processStarted = True
            self.btnStartSearch.setText("Отмена")
            self.queue = Queue()
            args = (
                self.spinSize.value(),
                self.spinMean.value(),
                self.spinCV.value(),
                self.spinCorr.value(),
                self.spinSkew.value() if self.checkSkew.isChecked() else None,
                self.spinKurt.value() if self.checkKurt.isChecked() else None,
                METHODS[self.selected_method],
                self.extra_params,
                self.gradParams
            )

            self.process = Process(
                target=_run_search_process,
                args=(args, self.queue)
            )

            self.process.start()
            self.processTimer.start(100)

            self.progressSearch.setMaximum(0)
            self.progressTimer = QTimer(self)
        else:
            self.process.terminate()
            self.progressSearch.setMaximum(1)
            self.progressSearch.setValue(1)
            self.processTimer.stop()
            self.processStarted = False
            self.btnStartSearch.setText("Подобрать MAP-поток")


    # открывает диалоговое окно с доп.параметрами
    def _open_dialog(self):
        methods = {
            "Последовательный перебор": 0,
            "Перебор в окрестности": 1,
            "Градиентный спуск": 2
        }
        if self._dialogParams is None:
            self._dialogParams = dialogParameters(start_page=methods[self.selected_method], parent=self)
        if self._dialogParams.exec() == QDialog.Accepted:
            self.extra_params = self._dialogParams.get_parameters()
            self.weights = self.extra_params['weights'] if not None else [1, 1, 1, 1]

    # Обновление результатов поиска параметров
    def checkProcess(self):
        if not self.queue.empty():
            Q, Lambda, D, R, characteristics, loss = self.queue.get()
            self.process.join()
            self.processTimer.stop()
            self.progressSearch.setMaximum(1)
            self.progressSearch.setValue(1)

            self._show_matrix(Q, Lambda, D)
            self.textInfoSearch.setText(
                INFO_TEMPLATE.format(
                    mean=characteristics[0],
                    var=characteristics[1],
                    cv=characteristics[2],
                    corr=characteristics[3],
                    skew=characteristics[4],
                    kurt=characteristics[5],
                    cvPer=sm.relativeErr(self.spinCV.value(), characteristics[2]),
                    corrPer=sm.relativeErr(self.spinCorr.value(), characteristics[3]),
                    skewPer=sm.relativeErr(self.spinSkew.value(), characteristics[4]),
                    kurtPer=sm.relativeErr(self.spinKurt.value(), characteristics[5]),
                    R=R.round(4),
                    loss=loss
                )
            )
            self.tmp_Q = Q
            self.tmp_L = Lambda
            self.tmp_D = D
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
    result = searchTask(args)
    queue.put(result)

# задача для отдельного потока с поиском параметров
def searchTask(args):
    size, mean, cv, corr, skew, kurt, method, extra_params, grad_params = args

    (Q, Lambda, D), loss = method(
        sizeMap=size,
        cvTarget=cv,
        corrTarget=corr,
        skewnessTarget=skew,
        kurtosisTarget=kurt,
        **extra_params
    )

    threshold = grad_params[0]  # порог
    use = grad_params[1]        # флаг использования
    # если порог не перепрынут и стоит галочка на использование, то используем градиентный спуск
    if grad_params[1] is not None and threshold < loss and use:
        grad = Gradient([Q, Lambda, D], [cv, corr, skew, kurt], **grad_params[2])
        (Q, Lambda, D), loss = grad.search()

    Q, Lambda, D = sm.meanMap([Q, Lambda, D], mean)
    R = am.compute_stationary_distribution(Q)
    characteristics = am.characteristics(Q, Lambda, D)
    return Q, Lambda, D, R, characteristics, loss

# чтение трассы с файла
def read_trace(file_path):
    try:
        data = []
        with open(file_path, 'r') as file:
            for line in file:
                if not line.strip():
                    continue
                data.append(float(line.strip()))
            return data
    except Exception as e:
        QMessageBox.warning(None, "Ошибка", f"Ошибка чтения файла:\n{type(e).__name__} - {e}")
        return

def matrix_to_text(matrix, name="Q"):
    """Возвращает строку вида 'Q = [ ... ]' с переносами строк для QLabel"""
    lines = ["  ".join(f"{x: .3f}" for x in row) for row in matrix]
    body = "\n".join(lines)
    return f"{name} = \n{body}\n"

# парсер матриц из текста
def parse_matrix(text: str, m) -> list[list[float]]:
    if m == 'Λ':
        lines = text.strip().splitlines()
        matrix = [float(x) for x in lines]
        if not matrix: 
            QMessageBox.warning(None, "Ошибка", f"Матрица {m} пустая") 
            return
        return matrix

    lines = [line for line in text.strip().splitlines() if line.strip()]  # убираем пустые строки
    matrix = []

    for i, line in enumerate(lines, start=1):
        try:
            row = [float(x) for x in line.split()]
        except ValueError:
            QMessageBox.warning(None, "Ошибка", f"Ошибка в матрице {m} в строке {i}: некорректное число")
            return []

        matrix.append(row)

    if not matrix:
        QMessageBox.warning(None, "Ошибка", f"Матрица {m} пустая")
        return []

    # Проверка: все строки должны иметь одинаковое количество столбцов
    num_cols = len(matrix[0])
    for i, row in enumerate(matrix, start=1):
        if len(row) != num_cols:
            QMessageBox.warning(None, "Ошибка", f"Ошибка в матрице {m}: разное количество столбцов в строке {i}")
            return []

    # Проверка квадратной матрицы
    if len(matrix) != num_cols:
        QMessageBox.warning(None, "Ошибка", f"Матрица {m} не квадратная")
        return []

    return matrix

# генератор событий
def generate_worker(q, l, d, size, total_events, stop_event, queue):
    threat = MAP(q, l, d, size)
    count_events = 0
    batch_size = total_events / 10
    buffer = []
    while count_events < total_events:
        if stop_event.is_set():
            return
        
        events = threat.step()
        if events[0] == "event":
            count_events += 1
            buffer.append(events[1])
        elif events[0] == "transition" and events[4]:
            count_events += 1
            buffer.append(events[3])

        if len(buffer) >= batch_size:
            queue.put(("batch", buffer.copy(), count_events))
            buffer.clear()

    if buffer:
        queue.put(("batch", buffer, count_events))

METHODS = {
    "Последовательный перебор": sm.brute_force_search,
    "Перебор в окрестности": sm.local_search,
    "Градиентный спуск": SGD.sgd_optimization
}

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