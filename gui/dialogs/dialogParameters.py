from PySide6.QtWidgets import QDialog, QMessageBox
from gui.uiPy.DialogParameters import Ui_Dialog

class dialogParameters(QDialog, Ui_Dialog):
    def __init__(self, start_page, parent):
        super().__init__()
        self.setupUi(self)
        self.stackedWidget.setCurrentIndex(start_page)
        self.btnSaveParameters.clicked.connect(self.save)

    def save(self):
        self.accept()

    def get_parameters(self):
        if self.stackedWidget.currentIndex() == 0:
            return {
                'pop_size': self.spinBruteSize.value(),
                'rQ': self.spinBruteQ.value(),
                'rLamb': self.spinBruteL.value()
            }
        if self.stackedWidget.currentIndex() == 1:
            return {
                'pop_size': self.spinLocalSize.value(),
                'rQ': self.spinLocalQ.value(),
                'rLamb': self.spinLocalL.value(),
                'percent': self.spinPercent.value(),
                'enhanced': self.checkEnhanced.isChecked()
            }
        if self.stackedWidget.currentIndex() == 2:
            try:
                eps = float(self.lineEpsilon.text())
            except:
                QMessageBox.warning(self, "Ошибка", "Перепроверьте точность. Должно быть либо число, либо запись в виде 1e-7")
            return {
                'lr': self.spinLR.value(),
                'eps': eps,
                'patience': self.spinPatience.value()
            }