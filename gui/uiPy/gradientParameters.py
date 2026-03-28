# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gradientParameters.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDoubleSpinBox, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpinBox,
    QVBoxLayout, QWidget)

class Ui_gradParams(object):
    def setupUi(self, gradParams):
        if not gradParams.objectName():
            gradParams.setObjectName(u"gradParams")
        gradParams.resize(316, 366)
        self.verticalLayout = QVBoxLayout(gradParams)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.checkUseGrad = QCheckBox(gradParams)
        self.checkUseGrad.setObjectName(u"checkUseGrad")

        self.verticalLayout.addWidget(self.checkUseGrad)

        self.label_4 = QLabel(gradParams)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.lineThreshold = QLineEdit(gradParams)
        self.lineThreshold.setObjectName(u"lineThreshold")
        self.lineThreshold.setEnabled(False)

        self.verticalLayout.addWidget(self.lineThreshold)

        self.label_5 = QLabel(gradParams)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setScaledContents(False)
        self.label_5.setWordWrap(True)

        self.verticalLayout.addWidget(self.label_5)

        self.lineEps = QLineEdit(gradParams)
        self.lineEps.setObjectName(u"lineEps")
        self.lineEps.setEnabled(False)

        self.verticalLayout.addWidget(self.lineEps)

        self.label = QLabel(gradParams)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.spinMaxIters = QSpinBox(gradParams)
        self.spinMaxIters.setObjectName(u"spinMaxIters")
        self.spinMaxIters.setEnabled(False)
        self.spinMaxIters.setMinimum(100)
        self.spinMaxIters.setMaximum(20000)
        self.spinMaxIters.setValue(10000)

        self.verticalLayout.addWidget(self.spinMaxIters)

        self.label_2 = QLabel(gradParams)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.spinPatience = QSpinBox(gradParams)
        self.spinPatience.setObjectName(u"spinPatience")
        self.spinPatience.setEnabled(False)
        self.spinPatience.setMinimum(50)
        self.spinPatience.setMaximum(1000)
        self.spinPatience.setValue(250)

        self.verticalLayout.addWidget(self.spinPatience)

        self.label_3 = QLabel(gradParams)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.spinLr = QDoubleSpinBox(gradParams)
        self.spinLr.setObjectName(u"spinLr")
        self.spinLr.setEnabled(False)
        self.spinLr.setDecimals(2)
        self.spinLr.setMinimum(0.010000000000000)
        self.spinLr.setMaximum(1.000000000000000)
        self.spinLr.setSingleStep(0.010000000000000)
        self.spinLr.setValue(0.050000000000000)

        self.verticalLayout.addWidget(self.spinLr)

        self.btnSaveGradParams = QPushButton(gradParams)
        self.btnSaveGradParams.setObjectName(u"btnSaveGradParams")
        self.btnSaveGradParams.setEnabled(True)

        self.verticalLayout.addWidget(self.btnSaveGradParams)


        self.retranslateUi(gradParams)

        QMetaObject.connectSlotsByName(gradParams)
    # setupUi

    def retranslateUi(self, gradParams):
        gradParams.setWindowTitle(QCoreApplication.translate("gradParams", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u043f\u043e\u0434\u0433\u043e\u043d\u043a\u0438", None))
        self.checkUseGrad.setText(QCoreApplication.translate("gradParams", u"\u0418\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u044c \u043f\u043e\u0434\u0433\u043e\u043d\u043a\u0443", None))
        self.label_4.setText(QCoreApplication.translate("gradParams", u"\u041f\u043e\u0440\u043e\u0433 (\u0435\u0441\u043b\u0438 \u043e\u0448\u0438\u0431\u043a\u0430 \u0431\u043e\u043b\u044c\u0448\u0435 \u0437\u0430\u0434\u0430\u043d\u043d\u043e\u0433\u043e \u0437\u0430\u043d\u0430\u0447\u0435\u043d\u0438\u044f)", None))
        self.lineThreshold.setPlaceholderText(QCoreApplication.translate("gradParams", u"\u041f\u043e\u0440\u043e\u0433 \u0434\u043b\u044f \u043f\u043e\u0434\u0433\u043e\u043d\u043a\u0438, \u043f\u043e \u0443\u043c\u043e\u043b\u0447\u0430\u043d\u0438\u044e \u0434\u043e 1e-4", None))
        self.label_5.setText(QCoreApplication.translate("gradParams", u"Epsilon, \u043f\u043e\u043a\u0430 \u043e\u0448\u0438\u0431\u043a\u0430 \u043d\u0435 \u0434\u043e\u0441\u0442\u0438\u0433\u043d\u0435\u0442 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f \u043c\u0435\u043d\u044c\u0448\u0435 \u0437\u0430\u0434\u0430\u043d\u043d\u043e\u0433\u043e", None))
        self.lineEps.setPlaceholderText(QCoreApplication.translate("gradParams", u"\u0423\u043b\u0443\u0447\u0448\u0438\u0442\u044c \u0434\u043e... \u041f\u043e \u0443\u043c\u043e\u043b\u0447\u0430\u043d\u0438\u044e 5e-7", None))
        self.label.setText(QCoreApplication.translate("gradParams", u"\u041c\u0430\u043a\u0441\u0438\u043c\u0443\u043c \u0438\u0442\u0435\u0440\u0430\u0446\u0438\u0439", None))
        self.label_2.setText(QCoreApplication.translate("gradParams", u"\u0418\u0442\u0435\u0440\u0430\u0446\u0438\u0439 \u0434\u043b\u044f \u0440\u0430\u043d\u043d\u0435\u0439 \u043e\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0438", None))
        self.label_3.setText(QCoreApplication.translate("gradParams", u"Learning rate", None))
        self.btnSaveGradParams.setText(QCoreApplication.translate("gradParams", u"\u0421\u041e\u0425\u0420\u0410\u041d\u0418\u0422\u042c", None))
    # retranslateUi

