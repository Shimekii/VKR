from PySide6.QtWidgets import QDialog, QMessageBox
from gui.uiPy.DialogCompareWithTrace import Ui_dialogCompareTraceWithOrigin
from gui.canvas import CDFPlot

class dialogCompareTrace(QDialog, Ui_dialogCompareTraceWithOrigin):
    def __init__(self, values_emp, cdf_emp, values_theory, cdf_theory, ks, ksx, label1, label2):
        super().__init__()
        self.setupUi(self)
        self.CDFPlot = CDFPlot()
        self.verticalLayoutCompareWithOrigin.addWidget(self.CDFPlot)
        self.CDFPlot.plot(values_emp, cdf_emp, values2=values_theory, cdf2=cdf_theory, ks=ks, ksx=ksx, label1=label1, label2=label2)
        self.btnCloseWindow.clicked.connect(self.close)