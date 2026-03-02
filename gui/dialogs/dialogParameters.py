from PySide6.QtWidgets import QDialog, QMessageBox
from gui.uiPy.DialogParameters import Ui_Dialog

class dialogParameters(QDialog, Ui_Dialog):
    def __init__(self, start_page, parent):
        super().__init__()
        self.setupUi(self)
        self.stackedWidget.setCurrentIndex(start_page)
        self.btnSaveParameters.clicked.connect(self.save)
        self.default = "Введите веса для функции потерь. Пример 1,1,1,1"
        self.weights = [1, 1, 1, 1]
        self.error = False

    def save(self):
        self.accept()

    def get_parameters(self):
        if self.stackedWidget.currentIndex() == 0:
            return {
                'pop_size': self.spinBruteSize.value(),
                'rQ': self.spinBruteQ.value(),
                'rLamb': self.spinBruteL.value(),
                'weights': self.parse_weights()
            }
        if self.stackedWidget.currentIndex() == 1:
            return {
                'pop_size': self.spinLocalSize.value(),
                'rQ': self.spinLocalQ.value(),
                'rLamb': self.spinLocalL.value(),
                'percent': self.spinPercent.value(),
                'enhanced': self.checkEnhanced.isChecked(),
                'weights': self.parse_weights()
            }
        if self.stackedWidget.currentIndex() == 2:
            try:
                eps = float(self.lineEpsilon.text())
            except:
                QMessageBox.warning(self, "Ошибка", "Перепроверьте точность. Должно быть либо число, либо запись в виде 1e-7")
            return {
                'lr': self.spinLR.value(),
                'eps': eps,
                'patience': self.spinPatience.value(),
                'weights': self.parse_weights()
            }
    def parse_weights(self):
        text = self.lineWeights.text()
        try:
            if text != self.default:
                self.weights = [float(x) for x in text.split(sep=',')]
        except Exception:
            QMessageBox.critical(self, "ОШИБКА", "Перепроверьте задание весов. Пример: 1.0, 1.0, 1.0, 1.0")
            self.error = True

