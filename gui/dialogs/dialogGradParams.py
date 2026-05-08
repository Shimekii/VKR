from PySide6.QtWidgets import QDialog, QMessageBox
from gui.uiPy.gradientParameters import Ui_gradParams
class gradParameters(QDialog, Ui_gradParams):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.checkUseGrad.toggled.connect(self.useGrad)
        self.btnSaveGradParams.clicked.connect(self.save)

    def save(self):
        self.accept()

    def useGrad(self, check):
        self.lineThreshold.setEnabled(check)
        self.lineEps.setEnabled(check)
        self.spinMaxIters.setEnabled(check)
        self.spinPatience.setEnabled(check)
        self.spinLr.setEnabled(check)

    def getParameters(self):
        try:
            text = self.lineThreshold.text()
            if len(text) != 0:
                threshold = float(text)
            else:
                threshold = 1e-4
        except Exception:
            QMessageBox.warning(self, "Ошибка парсинга", "Проверьте порог, запись должна быть в формате числа с точкой, либо научной записи (0.01/1e-2)")

        try:
            text = self.lineEps.text()
            if len(text) != 0:
                eps = float(text)
            else:
                eps = 5e-7
        except Exception:
            QMessageBox.warning(self, "Ошибка парсинга", "Проверьте заданный Epsilon. Запись должна быть в формате числа с точкой, либо научной записи (0.01/1e-2)")

        steps = self.spinMaxIters.value()
        patience = self.spinPatience.value()
        lr = self.spinLr.value()

        return threshold, self.checkUseGrad.isChecked(), {
            "eps": eps,
            "max_iter": steps,
            "patience": patience,
            "lr": lr
        }