# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DialogParameters.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QDoubleSpinBox,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpinBox, QStackedWidget, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(331, 350)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QSize(331, 350))
        Dialog.setMaximumSize(QSize(331, 350))
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.stackedWidget = QStackedWidget(Dialog)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(0, 0))
        self.stackedWidget.setMaximumSize(QSize(99999, 99999))
        self.pageBruteForce = QWidget()
        self.pageBruteForce.setObjectName(u"pageBruteForce")
        self.verticalLayout = QVBoxLayout(self.pageBruteForce)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_4 = QLabel(self.pageBruteForce)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 40))
        font = QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setTextFormat(Qt.TextFormat.AutoText)
        self.label_4.setScaledContents(False)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_4.setWordWrap(True)

        self.verticalLayout.addWidget(self.label_4)

        self.label_3 = QLabel(self.pageBruteForce)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout.addWidget(self.label_3)

        self.spinBruteSize = QSpinBox(self.pageBruteForce)
        self.spinBruteSize.setObjectName(u"spinBruteSize")
        self.spinBruteSize.setValue(30)

        self.verticalLayout.addWidget(self.spinBruteSize)

        self.label = QLabel(self.pageBruteForce)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout.addWidget(self.label)

        self.spinBruteQ = QSpinBox(self.pageBruteForce)
        self.spinBruteQ.setObjectName(u"spinBruteQ")
        self.spinBruteQ.setMaximum(99999)
        self.spinBruteQ.setValue(10)

        self.verticalLayout.addWidget(self.spinBruteQ)

        self.label_2 = QLabel(self.pageBruteForce)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout.addWidget(self.label_2)

        self.spinBruteL = QSpinBox(self.pageBruteForce)
        self.spinBruteL.setObjectName(u"spinBruteL")
        self.spinBruteL.setMaximum(99999)
        self.spinBruteL.setValue(10)

        self.verticalLayout.addWidget(self.spinBruteL)

        self.stackedWidget.addWidget(self.pageBruteForce)
        self.pageLocalSearch = QWidget()
        self.pageLocalSearch.setObjectName(u"pageLocalSearch")
        self.verticalLayout_3 = QVBoxLayout(self.pageLocalSearch)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_5 = QLabel(self.pageLocalSearch)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)
        self.label_5.setTextFormat(Qt.TextFormat.AutoText)
        self.label_5.setScaledContents(False)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_5.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.label_5)

        self.label_6 = QLabel(self.pageLocalSearch)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_3.addWidget(self.label_6)

        self.spinLocalSize = QSpinBox(self.pageLocalSearch)
        self.spinLocalSize.setObjectName(u"spinLocalSize")
        self.spinLocalSize.setValue(30)

        self.verticalLayout_3.addWidget(self.spinLocalSize)

        self.label_7 = QLabel(self.pageLocalSearch)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_3.addWidget(self.label_7)

        self.spinLocalQ = QSpinBox(self.pageLocalSearch)
        self.spinLocalQ.setObjectName(u"spinLocalQ")
        self.spinLocalQ.setMaximum(99999)
        self.spinLocalQ.setValue(10)

        self.verticalLayout_3.addWidget(self.spinLocalQ)

        self.label_8 = QLabel(self.pageLocalSearch)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_3.addWidget(self.label_8)

        self.spinLocalL = QSpinBox(self.pageLocalSearch)
        self.spinLocalL.setObjectName(u"spinLocalL")
        self.spinLocalL.setMaximum(99999)
        self.spinLocalL.setValue(10)

        self.verticalLayout_3.addWidget(self.spinLocalL)

        self.label_9 = QLabel(self.pageLocalSearch)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_3.addWidget(self.label_9)

        self.spinPercent = QDoubleSpinBox(self.pageLocalSearch)
        self.spinPercent.setObjectName(u"spinPercent")
        self.spinPercent.setMaximum(1.000000000000000)
        self.spinPercent.setSingleStep(0.010000000000000)
        self.spinPercent.setValue(0.020000000000000)

        self.verticalLayout_3.addWidget(self.spinPercent)

        self.checkEnhanced = QCheckBox(self.pageLocalSearch)
        self.checkEnhanced.setObjectName(u"checkEnhanced")

        self.verticalLayout_3.addWidget(self.checkEnhanced)

        self.stackedWidget.addWidget(self.pageLocalSearch)
        self.pageSGD = QWidget()
        self.pageSGD.setObjectName(u"pageSGD")
        self.verticalLayout_4 = QVBoxLayout(self.pageSGD)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_10 = QLabel(self.pageSGD)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(16777215, 40))
        self.label_10.setFont(font)
        self.label_10.setTextFormat(Qt.TextFormat.AutoText)
        self.label_10.setScaledContents(False)
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_10.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.label_10)

        self.label_11 = QLabel(self.pageSGD)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_4.addWidget(self.label_11)

        self.lineEpsilon = QLineEdit(self.pageSGD)
        self.lineEpsilon.setObjectName(u"lineEpsilon")

        self.verticalLayout_4.addWidget(self.lineEpsilon)

        self.label_12 = QLabel(self.pageSGD)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_4.addWidget(self.label_12)

        self.spinLR = QDoubleSpinBox(self.pageSGD)
        self.spinLR.setObjectName(u"spinLR")
        self.spinLR.setDecimals(4)
        self.spinLR.setValue(0.050000000000000)

        self.verticalLayout_4.addWidget(self.spinLR)

        self.label_13 = QLabel(self.pageSGD)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_4.addWidget(self.label_13)

        self.spinPatience = QSpinBox(self.pageSGD)
        self.spinPatience.setObjectName(u"spinPatience")
        self.spinPatience.setMaximum(999999)
        self.spinPatience.setValue(500)

        self.verticalLayout_4.addWidget(self.spinPatience)

        self.stackedWidget.addWidget(self.pageSGD)

        self.verticalLayout_2.addWidget(self.stackedWidget)

        self.lineWeights = QLineEdit(Dialog)
        self.lineWeights.setObjectName(u"lineWeights")

        self.verticalLayout_2.addWidget(self.lineWeights)

        self.btnSaveParameters = QPushButton(Dialog)
        self.btnSaveParameters.setObjectName(u"btnSaveParameters")

        self.verticalLayout_2.addWidget(self.btnSaveParameters)


        self.retranslateUi(Dialog)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0435 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u0434\u043b\u044f \u0430\u043b\u0433\u043e\u0440\u0438\u0442\u043c\u0430 \u043f\u043e\u0441\u043b\u0435\u0434\u043e\u0432\u0430\u0442\u0435\u043b\u044c\u043d\u043e\u0433\u043e \u043f\u0435\u0440\u0435\u0431\u043e\u0440\u0430", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u0427\u0438\u0441\u043b\u043e \u043f\u043e\u0442\u043e\u043a\u043e\u0432 \u0434\u043b\u044f \u0432\u044b\u0431\u043e\u0440\u0430 \u043d\u0430\u0447\u0430\u043b\u044c\u043d\u043e\u0433\u043e \u0440\u0435\u0448\u0435\u043d\u0438\u044f", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u0412\u0435\u0440\u0445\u043d\u044f\u044f \u0433\u0440\u0430\u043d\u0438\u0446\u0430 \u0434\u043b\u044f Q", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u0412\u0435\u0440\u0445\u043d\u044f\u044f \u0433\u0440\u0430\u043d\u0438\u0446\u0430 \u0434\u043b\u044f \u039b", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0435 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u0434\u043b\u044f \u0430\u043b\u0433\u043e\u0440\u0438\u0442\u043c\u0430 \u0441 \u043f\u043e\u0438\u0441\u043a\u043e\u043c \u0432 \u043e\u043a\u0440\u0435\u0441\u0442\u043d\u043e\u0441\u0442\u0438", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"\u0427\u0438\u0441\u043b\u043e \u043f\u043e\u0442\u043e\u043a\u043e\u0432 \u0434\u043b\u044f \u0432\u044b\u0431\u043e\u0440\u0430 \u043d\u0430\u0447\u0430\u043b\u044c\u043d\u043e\u0433\u043e \u0440\u0435\u0448\u0435\u043d\u0438\u044f", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"\u0412\u0435\u0440\u0445\u043d\u044f\u044f \u0433\u0440\u0430\u043d\u0438\u0446\u0430 \u0434\u043b\u044f Q", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"\u0412\u0435\u0440\u0445\u043d\u044f\u044f \u0433\u0440\u0430\u043d\u0438\u0446\u0430 \u0434\u043b\u044f \u039b", None))
#if QT_CONFIG(accessibility)
        self.label_9.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.label_9.setText(QCoreApplication.translate("Dialog", u"\u041e\u043a\u0440\u0435\u0441\u0442\u043d\u043e\u0441\u0442\u044c", None))
        self.checkEnhanced.setText(QCoreApplication.translate("Dialog", u"\u0423\u043b\u0443\u0447\u0448\u0435\u043d\u043d\u044b\u0439 \u043f\u043e\u0438\u0441\u043a", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0435 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u0434\u043b\u044f \u0433\u0440\u0430\u0434\u0438\u0435\u043d\u0442\u043d\u043e\u0433\u043e \u0441\u043f\u0443\u0441\u043a\u0430", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"\u0422\u043e\u0447\u043d\u043e\u0441\u0442\u044c", None))
        self.lineEpsilon.setText(QCoreApplication.translate("Dialog", u"1e-7", None))
        self.label_12.setText(QCoreApplication.translate("Dialog", u"Learning rate", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", u"\u0423\u0441\u043b\u043e\u0432\u0438\u0435 \u0440\u0430\u043d\u043d\u0435\u0439 \u043e\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0438", None))
        self.lineWeights.setText(QCoreApplication.translate("Dialog", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0432\u0435\u0441\u0430 \u0434\u043b\u044f \u0444\u0443\u043d\u043a\u0446\u0438\u0438 \u043f\u043e\u0442\u0435\u0440\u044c. \u041f\u0440\u0438\u043c\u0435\u0440 1,1,1,1", None))
        self.btnSaveParameters.setText(QCoreApplication.translate("Dialog", u"\u0421\u041e\u0425\u0420\u0410\u041d\u0418\u0422\u042c", None))
    # retranslateUi

