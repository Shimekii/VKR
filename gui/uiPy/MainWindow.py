# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QFrame, QGroupBox, QHBoxLayout, QLabel,
    QMainWindow, QMenu, QMenuBar, QPlainTextEdit,
    QProgressBar, QPushButton, QSizePolicy, QSpinBox,
    QSplitter, QStackedWidget, QStatusBar, QTextBrowser,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1035, 823)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1035, 823))
        MainWindow.setMaximumSize(QSize(10000, 10000))
        MainWindow.setBaseSize(QSize(800, 5))
        font = QFont()
        font.setFamilies([u"Microsoft JhengHei"])
        font.setPointSize(18)
        font.setBold(True)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u"../../resources/icons/icon.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setDockOptions(QMainWindow.DockOption.AllowTabbedDocks|QMainWindow.DockOption.AnimatedDocks)
        self.lightTheme = QAction(MainWindow)
        self.lightTheme.setObjectName(u"lightTheme")
        font1 = QFont()
        font1.setFamilies([u"Microsoft JhengHei"])
        self.lightTheme.setFont(font1)
        self.darkTheme = QAction(MainWindow)
        self.darkTheme.setObjectName(u"darkTheme")
        self.darkTheme.setFont(font1)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_11 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.title = QLabel(self.centralwidget)
        self.title.setObjectName(u"title")
        self.title.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_11.addWidget(self.title)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_11.addWidget(self.line)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.buttons = QWidget(self.centralwidget)
        self.buttons.setObjectName(u"buttons")
        self.buttons.setStyleSheet(u"QPushButton {\n"
"    text-align: left;\n"
"    border-radius: 6px;\n"
"    padding: 4px;\n"
"    padding-right: 15px;\n"
"	color: palette(ButtonText);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: palette(mid);\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: palette(highlight);\n"
"    color: palette(highlighted-text);\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.buttons)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.btnPageTrace = QPushButton(self.buttons)
        self.btnPageTrace.setObjectName(u"btnPageTrace")
        font2 = QFont()
        font2.setFamilies([u"Microsoft JhengHei"])
        font2.setPointSize(11)
        font2.setBold(False)
        font2.setKerning(True)
        self.btnPageTrace.setFont(font2)
        self.btnPageTrace.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnPageTrace.setStyleSheet(u"QPushButton {\n"
"    text-align: left;\n"
"    border-radius: 6px;\n"
"    padding: 4px;\n"
"    padding-right: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: palette(mid);\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: palette(highlight);\n"
"    color: palette(highlighted-text);\n"
"}")
        self.btnPageTrace.setCheckable(True)
        self.btnPageTrace.setChecked(False)
        self.btnPageTrace.setAutoExclusive(False)

        self.verticalLayout_4.addWidget(self.btnPageTrace)

        self.btnPageSearch = QPushButton(self.buttons)
        self.btnPageSearch.setObjectName(u"btnPageSearch")
        font3 = QFont()
        font3.setFamilies([u"Microsoft JhengHei"])
        font3.setPointSize(11)
        font3.setBold(False)
        self.btnPageSearch.setFont(font3)
        self.btnPageSearch.setAcceptDrops(False)
        self.btnPageSearch.setAutoFillBackground(False)
        self.btnPageSearch.setStyleSheet(u"QPushButton {\n"
"    text-align: left;\n"
"    border-radius: 6px;\n"
"    padding: 4px;\n"
"    padding-right: 15px;\n"
"	color: palette(ButtonText);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: palette(mid);\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: palette(highlight);\n"
"    color: palette(highlighted-text);\n"
"}")
        self.btnPageSearch.setCheckable(True)
        self.btnPageSearch.setChecked(False)
        self.btnPageSearch.setAutoDefault(False)
        self.btnPageSearch.setFlat(False)

        self.verticalLayout_4.addWidget(self.btnPageSearch)

        self.btnPageGenerate = QPushButton(self.buttons)
        self.btnPageGenerate.setObjectName(u"btnPageGenerate")
        self.btnPageGenerate.setFont(font3)
        self.btnPageGenerate.setStyleSheet(u"QPushButton {\n"
"    text-align: left;\n"
"    border-radius: 6px;\n"
"    padding: 4px;\n"
"    padding-right: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: palette(mid);\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: palette(highlight);\n"
"    color: palette(highlighted-text);\n"
"}")
        self.btnPageGenerate.setCheckable(True)

        self.verticalLayout_4.addWidget(self.btnPageGenerate)

        self.btnPageCompare = QPushButton(self.buttons)
        self.btnPageCompare.setObjectName(u"btnPageCompare")
        self.btnPageCompare.setFont(font3)
        self.btnPageCompare.setStyleSheet(u"QPushButton {\n"
"    text-align: left;\n"
"    border-radius: 6px;\n"
"    padding: 4px;\n"
"    padding-right: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: palette(mid);\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: palette(highlight);\n"
"    color: palette(highlighted-text);\n"
"}")
        self.btnPageCompare.setCheckable(True)

        self.verticalLayout_4.addWidget(self.btnPageCompare)


        self.horizontalLayout_5.addWidget(self.buttons, 0, Qt.AlignmentFlag.AlignTop)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_5.addWidget(self.line_2)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        font4 = QFont()
        font4.setFamilies([u"Microsoft JhengHei"])
        font4.setPointSize(10)
        font4.setBold(False)
        self.stackedWidget.setFont(font4)
        self.stackedWidget.setAutoFillBackground(False)
        self.stackedWidget.setStyleSheet(u"")
        self.startPage = QWidget()
        self.startPage.setObjectName(u"startPage")
        self.verticalLayout_2 = QVBoxLayout(self.startPage)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.textBrowser = QTextBrowser(self.startPage)
        self.textBrowser.setObjectName(u"textBrowser")

        self.verticalLayout_2.addWidget(self.textBrowser)

        self.stackedWidget.addWidget(self.startPage)
        self.tracePage = QWidget()
        self.tracePage.setObjectName(u"tracePage")
        self.verticalLayout_9 = QVBoxLayout(self.tracePage)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label = QLabel(self.tracePage)
        self.label.setObjectName(u"label")
        font5 = QFont()
        font5.setFamilies([u"Microsoft JhengHei"])
        font5.setPointSize(10)
        font5.setBold(True)
        self.label.setFont(font5)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.label)

        self.textEdit = QTextEdit(self.tracePage)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setFont(font4)
        self.textEdit.setReadOnly(True)

        self.verticalLayout_9.addWidget(self.textEdit)

        self.splitter_5 = QSplitter(self.tracePage)
        self.splitter_5.setObjectName(u"splitter_5")
        self.splitter_5.setOrientation(Qt.Orientation.Horizontal)
        self.btnReadTrace = QPushButton(self.splitter_5)
        self.btnReadTrace.setObjectName(u"btnReadTrace")
        self.btnReadTrace.setFont(font5)
        self.splitter_5.addWidget(self.btnReadTrace)
        self.btnTranferCharacteristics = QPushButton(self.splitter_5)
        self.btnTranferCharacteristics.setObjectName(u"btnTranferCharacteristics")
        self.btnTranferCharacteristics.setFont(font5)
        self.splitter_5.addWidget(self.btnTranferCharacteristics)

        self.verticalLayout_9.addWidget(self.splitter_5)

        self.plotWidgetInReadTrace = QWidget(self.tracePage)
        self.plotWidgetInReadTrace.setObjectName(u"plotWidgetInReadTrace")
        self.plotWidgetInReadTrace.setMinimumSize(QSize(0, 250))
        self.plotWidgetInReadTrace.setMaximumSize(QSize(16777215, 250))
        self.verticalLayout_10 = QVBoxLayout(self.plotWidgetInReadTrace)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_12 = QLabel(self.plotWidgetInReadTrace)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(16777215, 15))
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_12)

        self.verticalLayoutPlotInReadTrace = QVBoxLayout()
        self.verticalLayoutPlotInReadTrace.setObjectName(u"verticalLayoutPlotInReadTrace")

        self.verticalLayout_10.addLayout(self.verticalLayoutPlotInReadTrace)


        self.verticalLayout_9.addWidget(self.plotWidgetInReadTrace)

        self.stackedWidget.addWidget(self.tracePage)
        self.searchPage = QWidget()
        self.searchPage.setObjectName(u"searchPage")
        self.searchPage.setFont(font4)
        self.horizontalLayout = QHBoxLayout(self.searchPage)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox = QGroupBox(self.searchPage)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        self.groupBox.setMinimumSize(QSize(0, 409))
        self.groupBox.setMaximumSize(QSize(250, 16777215))
        self.groupBox.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.comboSelectAlg = QComboBox(self.groupBox)
        self.comboSelectAlg.addItem("")
        self.comboSelectAlg.addItem("")
        self.comboSelectAlg.addItem("")
        self.comboSelectAlg.setObjectName(u"comboSelectAlg")

        self.verticalLayout_3.addWidget(self.comboSelectAlg)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_3.addWidget(self.label_3)

        self.spinSize = QSpinBox(self.groupBox)
        self.spinSize.setObjectName(u"spinSize")
        self.spinSize.setMinimum(2)
        self.spinSize.setMaximum(5)

        self.verticalLayout_3.addWidget(self.spinSize)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_3.addWidget(self.label_2)

        self.spinMean = QDoubleSpinBox(self.groupBox)
        self.spinMean.setObjectName(u"spinMean")
        self.spinMean.setMaximum(999.990000000000009)

        self.verticalLayout_3.addWidget(self.spinMean)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_3.addWidget(self.label_4)

        self.spinCV = QDoubleSpinBox(self.groupBox)
        self.spinCV.setObjectName(u"spinCV")
        self.spinCV.setMinimum(1.000000000000000)
        self.spinCV.setMaximum(999.990000000000009)

        self.verticalLayout_3.addWidget(self.spinCV)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_3.addWidget(self.label_5)

        self.spinCorr = QDoubleSpinBox(self.groupBox)
        self.spinCorr.setObjectName(u"spinCorr")
        self.spinCorr.setMinimum(-1.000000000000000)
        self.spinCorr.setMaximum(1.000000000000000)
        self.spinCorr.setSingleStep(0.010000000000000)

        self.verticalLayout_3.addWidget(self.spinCorr)

        self.checkSkew = QCheckBox(self.groupBox)
        self.checkSkew.setObjectName(u"checkSkew")

        self.verticalLayout_3.addWidget(self.checkSkew)

        self.spinSkew = QDoubleSpinBox(self.groupBox)
        self.spinSkew.setObjectName(u"spinSkew")
        self.spinSkew.setEnabled(False)
        self.spinSkew.setMaximum(999.990000000000009)

        self.verticalLayout_3.addWidget(self.spinSkew)

        self.checkKurt = QCheckBox(self.groupBox)
        self.checkKurt.setObjectName(u"checkKurt")

        self.verticalLayout_3.addWidget(self.checkKurt)

        self.spinKurt = QDoubleSpinBox(self.groupBox)
        self.spinKurt.setObjectName(u"spinKurt")
        self.spinKurt.setEnabled(False)
        self.spinKurt.setMaximum(9999.989999999999782)

        self.verticalLayout_3.addWidget(self.spinKurt)

        self.btnStartSearch = QPushButton(self.groupBox)
        self.btnStartSearch.setObjectName(u"btnStartSearch")

        self.verticalLayout_3.addWidget(self.btnStartSearch)

        self.btnAdditionalParameters = QPushButton(self.groupBox)
        self.btnAdditionalParameters.setObjectName(u"btnAdditionalParameters")

        self.verticalLayout_3.addWidget(self.btnAdditionalParameters)

        self.btnGradientParams = QPushButton(self.groupBox)
        self.btnGradientParams.setObjectName(u"btnGradientParams")

        self.verticalLayout_3.addWidget(self.btnGradientParams)


        self.horizontalLayout.addWidget(self.groupBox, 0, Qt.AlignmentFlag.AlignTop)

        self.groupBox_2 = QGroupBox(self.searchPage)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame = QFrame(self.groupBox_2)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.labelQ = QLabel(self.frame)
        self.labelQ.setObjectName(u"labelQ")

        self.horizontalLayout_2.addWidget(self.labelQ)

        self.labelLambda = QLabel(self.frame)
        self.labelLambda.setObjectName(u"labelLambda")

        self.horizontalLayout_2.addWidget(self.labelLambda)

        self.labelD = QLabel(self.frame)
        self.labelD.setObjectName(u"labelD")

        self.horizontalLayout_2.addWidget(self.labelD)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)


        self.verticalLayout_5.addWidget(self.frame)

        self.progressSearch = QProgressBar(self.groupBox_2)
        self.progressSearch.setObjectName(u"progressSearch")
        self.progressSearch.setMaximumSize(QSize(16777215, 5))
        self.progressSearch.setStyleSheet(u"QProgressBar::chunk{\n"
"	border-radius: 5px;\n"
"	background-color: green;\n"
"}")
        self.progressSearch.setValue(0)
        self.progressSearch.setTextVisible(False)
        self.progressSearch.setOrientation(Qt.Orientation.Horizontal)
        self.progressSearch.setTextDirection(QProgressBar.Direction.TopToBottom)

        self.verticalLayout_5.addWidget(self.progressSearch)

        self.textInfoSearch = QTextBrowser(self.groupBox_2)
        self.textInfoSearch.setObjectName(u"textInfoSearch")
        self.textInfoSearch.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_5.addWidget(self.textInfoSearch)

        self.splitter_4 = QSplitter(self.groupBox_2)
        self.splitter_4.setObjectName(u"splitter_4")
        self.splitter_4.setOrientation(Qt.Orientation.Horizontal)
        self.btnSave = QPushButton(self.splitter_4)
        self.btnSave.setObjectName(u"btnSave")
        self.splitter_4.addWidget(self.btnSave)
        self.btnCompareWithOrigin = QPushButton(self.splitter_4)
        self.btnCompareWithOrigin.setObjectName(u"btnCompareWithOrigin")
        self.btnCompareWithOrigin.setMinimumSize(QSize(230, 0))
        self.splitter_4.addWidget(self.btnCompareWithOrigin)

        self.verticalLayout_5.addWidget(self.splitter_4)


        self.horizontalLayout.addWidget(self.groupBox_2)

        self.stackedWidget.addWidget(self.searchPage)
        self.genTracePage = QWidget()
        self.genTracePage.setObjectName(u"genTracePage")
        font6 = QFont()
        font6.setFamilies([u"Segoe UI"])
        font6.setPointSize(9)
        font6.setBold(False)
        self.genTracePage.setFont(font6)
        self.genTracePage.setStyleSheet(u"")
        self.horizontalLayout_4 = QHBoxLayout(self.genTracePage)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.widget = QWidget(self.genTracePage)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(200, 16777215))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout.addWidget(self.label_6)

        self.spinSizeMap = QSpinBox(self.widget)
        self.spinSizeMap.setObjectName(u"spinSizeMap")
        font7 = QFont()
        font7.setFamilies([u"Segoe UI"])
        font7.setPointSize(10)
        font7.setBold(False)
        self.spinSizeMap.setFont(font7)
        self.spinSizeMap.setMinimum(2)
        self.spinSizeMap.setMaximum(5)

        self.verticalLayout.addWidget(self.spinSizeMap)

        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font7)

        self.verticalLayout.addWidget(self.label_7)

        self.matrixQ = QPlainTextEdit(self.widget)
        self.matrixQ.setObjectName(u"matrixQ")
        self.matrixQ.setFont(font7)

        self.verticalLayout.addWidget(self.matrixQ)

        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font7)

        self.verticalLayout.addWidget(self.label_8)

        self.matrixL = QPlainTextEdit(self.widget)
        self.matrixL.setObjectName(u"matrixL")
        self.matrixL.setFont(font7)

        self.verticalLayout.addWidget(self.matrixL)

        self.label_9 = QLabel(self.widget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font7)

        self.verticalLayout.addWidget(self.label_9)

        self.matrixD = QPlainTextEdit(self.widget)
        self.matrixD.setObjectName(u"matrixD")
        self.matrixD.setFont(font7)

        self.verticalLayout.addWidget(self.matrixD)

        self.label_10 = QLabel(self.widget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font7)

        self.verticalLayout.addWidget(self.label_10)

        self.spinTotalEvents = QSpinBox(self.widget)
        self.spinTotalEvents.setObjectName(u"spinTotalEvents")
        self.spinTotalEvents.setFont(font7)
        self.spinTotalEvents.setWrapping(False)
        self.spinTotalEvents.setFrame(True)
        self.spinTotalEvents.setMinimum(1000)
        self.spinTotalEvents.setMaximum(10000000)
        self.spinTotalEvents.setSingleStep(1000)

        self.verticalLayout.addWidget(self.spinTotalEvents)

        self.btnGenerate = QPushButton(self.widget)
        self.btnGenerate.setObjectName(u"btnGenerate")
        self.btnGenerate.setFont(font7)

        self.verticalLayout.addWidget(self.btnGenerate)

        self.btnLoadMap = QPushButton(self.widget)
        self.btnLoadMap.setObjectName(u"btnLoadMap")
        self.btnLoadMap.setFont(font7)

        self.verticalLayout.addWidget(self.btnLoadMap)


        self.horizontalLayout_4.addWidget(self.widget)

        self.widget_2 = QWidget(self.genTracePage)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_6 = QVBoxLayout(self.widget_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.textHistory = QTextBrowser(self.widget_2)
        self.textHistory.setObjectName(u"textHistory")

        self.verticalLayout_6.addWidget(self.textHistory)

        self.progressGenerate = QProgressBar(self.widget_2)
        self.progressGenerate.setObjectName(u"progressGenerate")
        self.progressGenerate.setValue(0)

        self.verticalLayout_6.addWidget(self.progressGenerate)

        self.btnSaveTrace = QPushButton(self.widget_2)
        self.btnSaveTrace.setObjectName(u"btnSaveTrace")

        self.verticalLayout_6.addWidget(self.btnSaveTrace)


        self.horizontalLayout_4.addWidget(self.widget_2)

        self.stackedWidget.addWidget(self.genTracePage)
        self.comparePage = QWidget()
        self.comparePage.setObjectName(u"comparePage")
        self.verticalLayout_7 = QVBoxLayout(self.comparePage)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.plotWidget = QWidget(self.comparePage)
        self.plotWidget.setObjectName(u"plotWidget")
        self.verticalLayout_8 = QVBoxLayout(self.plotWidget)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayoutPlot = QVBoxLayout()
        self.verticalLayoutPlot.setObjectName(u"verticalLayoutPlot")

        self.verticalLayout_8.addLayout(self.verticalLayoutPlot)

        self.splitter_3 = QSplitter(self.plotWidget)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setOrientation(Qt.Orientation.Horizontal)
        self.btnLoadTraces = QPushButton(self.splitter_3)
        self.btnLoadTraces.setObjectName(u"btnLoadTraces")
        self.splitter_3.addWidget(self.btnLoadTraces)
        self.btnCompareTraces = QPushButton(self.splitter_3)
        self.btnCompareTraces.setObjectName(u"btnCompareTraces")
        self.splitter_3.addWidget(self.btnCompareTraces)
        self.label_11 = QLabel(self.splitter_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.splitter_3.addWidget(self.label_11)
        self.spinTime = QSpinBox(self.splitter_3)
        self.spinTime.setObjectName(u"spinTime")
        self.spinTime.setMinimum(1)
        self.spinTime.setMaximum(100)
        self.splitter_3.addWidget(self.spinTime)

        self.verticalLayout_8.addWidget(self.splitter_3)


        self.verticalLayout_7.addWidget(self.plotWidget)

        self.stackedWidget.addWidget(self.comparePage)

        self.horizontalLayout_5.addWidget(self.stackedWidget)


        self.verticalLayout_11.addLayout(self.horizontalLayout_5)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setMinimumSize(QSize(800, 0))
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1035, 33))
        font8 = QFont()
        font8.setFamilies([u"Microsoft JhengHei"])
        font8.setPointSize(9)
        font8.setBold(False)
        self.menuBar.setFont(font8)
        self.menu = QMenu(self.menuBar)
        self.menu.setObjectName(u"menu")
        self.menu.setFont(font8)
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menu.menuAction())
        self.menu.addAction(self.lightTheme)
        self.menu.addAction(self.darkTheme)

        self.retranslateUi(MainWindow)

        self.btnPageSearch.setDefault(False)
        self.stackedWidget.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u0431\u043e\u0440 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u043e\u0432 MAP-\u043f\u043e\u0442\u043e\u043a\u0430", None))
        self.lightTheme.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0432\u0435\u0442\u043b\u0430\u044f \u0442\u0435\u043c\u0430", None))
        self.darkTheme.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043c\u043d\u0430\u044f \u0442\u0435\u043c\u0430", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430 \u0434\u043b\u044f \u043f\u043e\u0434\u0431\u043e\u0440\u0430 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u043e\u0432 MAP-\u043f\u043e\u0442\u043e\u043a\u0430", None))
        self.btnPageTrace.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0442\u0435\u043d\u0438\u0435 \u0442\u0440\u0430\u0441\u0441\u044b", None))
        self.btnPageSearch.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u043e\u0431\u0440\u0430\u0442\u044c MAP-\u043f\u043e\u0442\u043e\u043a", None))
        self.btnPageGenerate.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0433\u0435\u043d\u0435\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0442\u0440\u0430\u0441\u0441\u0443", None))
        self.btnPageCompare.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0440\u0430\u0432\u043d\u0438\u0442\u044c \u0434\u0432\u0435 \u0442\u0440\u0430\u0441\u0441\u044b", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft JhengHei'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">\u0414\u0430\u043d\u043d\u0430\u044f \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430 \u043f\u0440\u0435\u0434\u043d\u0430\u0437\u043d\u0430\u0447\u0435\u043d\u0430 \u0434\u043b\u044f \u043f\u043e\u0434\u0431\u043e\u0440\u0430 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u043e\u0432 MAP-\u043f\u043e\u0442\u043e\u043a\u0430. \u0414\u043b\u044f \u043d"
                        "\u0430\u0432\u0438\u0433\u0430\u0446\u0438\u0438 \u043f\u043e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435 \u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u043e \u043d\u0430\u0436\u0430\u0442\u044c \u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u044b\u0435 \u043a\u043d\u043e\u043f\u043a\u0438 \u0441\u043d\u0438\u0437\u0443.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">\u041a\u043d\u043e\u043f\u043a\u0430 &quot;</span><span style=\" font-size:12pt; font-weight:700;\">\u0421\u0447\u0438\u0442\u0430\u0442\u044c \u0442\u0440\u0430\u0441\u0441\u0443</span><span style=\" font-size:12pt;\">&quot; \u043f\u043e\u0437\u0432\u043e\u043b\u044f\u0435\u0442 \u043f\u0440\u043e\u0430\u043d\u0430\u043b\u0438"
                        "\u0437\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0438\u043c\u0435\u044e\u0449\u0443\u044e\u0441\u044f \u0432\u044b\u0431\u043e\u0440\u043a\u0443 \u0441 \u043c\u043e\u043c\u0435\u043d\u0442\u0430\u043c\u0438 \u043d\u0430\u0441\u0442\u0443\u043f\u043b\u0435\u043d\u0438\u044f \u0441\u043e\u0431\u044b\u0442\u0438\u0439 \u0438 \u043f\u043e\u043b\u0443\u0447\u0438\u0442\u044c \u0432\u044b\u0431\u043e\u0440\u043e\u0447\u043d\u044b\u0435 \u0447\u0438\u0441\u043b\u043e\u0432\u044b\u0435 \u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0438 \u0434\u043b\u044f \u0434\u043b\u0438\u043d \u0438\u043d\u0442\u0435\u0440\u0432\u0430\u043b\u043e\u0432.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">\u041a"
                        "\u043d\u043e\u043f\u043a\u0430 &quot;</span><span style=\" font-size:12pt; font-weight:700;\">\u041f\u043e\u0434\u043e\u0431\u0440\u0430\u0442\u044c MAP-\u043f\u043e\u0442\u043e\u043a</span><span style=\" font-size:12pt;\">&quot; \u043f\u043e\u0437\u0432\u043e\u043b\u044f\u0435\u0442 \u043f\u043e\u0434\u043e\u0431\u0440\u0430\u0442\u044c \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u0434\u043b\u044f MAP-\u043f\u043e\u0442\u043e\u043a\u0430 \u0442\u0430\u043a\u0438\u043c \u043e\u0431\u0440\u0430\u0437\u043e\u043c, \u0447\u0442\u043e\u0431\u044b \u0435\u0433\u043e \u0447\u0438\u0441\u043b\u043e\u0432\u044b\u0435 \u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0438 \u0434\u043b\u0438\u043d \u0438\u043d\u0442\u0435\u0440\u0432\u0430\u043b\u043e\u0432 \u0431\u044b\u043b\u0438 \u0431\u043b\u0438\u0437\u043a\u0438 \u043a \u0437\u0430\u0434\u0430\u043d\u043d\u044b\u043c.<br /></span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt"
                        "-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">\u041a\u043d\u043e\u043f\u043a\u0430 &quot;</span><span style=\" font-size:12pt; font-weight:700;\">\u0421\u0433\u0435\u043d\u0435\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0442\u0440\u0430\u0441\u0441\u0443&quot; </span><span style=\" font-size:12pt;\">\u043f\u043e\u0437\u0432\u043e\u043b\u044f\u0435\u0442 \u0441\u0433\u0435\u043d\u0435\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0432\u044b\u0431\u043e\u0440\u043a\u0443 \u0441 \u043c\u043e\u043c\u0435\u043d\u0442\u0430\u043c\u0438 \u043d\u0430\u0441\u0442\u0443\u043f\u043b\u0435\u043d\u0438\u044f \u0441\u043e\u0431\u044b\u0442\u0438\u0439 \u043f\u043e \u0437\u0430\u0434\u0430\u043d\u043d\u044b\u043c \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0430\u043c MAP-\u043f\u043e\u0442\u043e\u043a\u0430<br /><br />\u041a\u043d\u043e\u043f\u043a\u0430 &quot;</span><span style=\" font-size:12pt; font-weight:700;\">\u0421\u0440\u0430\u0432\u043d\u0438\u0442\u044c \u0434\u0432\u0435 \u0442"
                        "\u0440\u0430\u0441\u0441\u044b&quot; </span><span style=\" font-size:12pt;\">\u043f\u043e\u0437\u0432\u043e\u043b\u044f\u0435\u0442 \u0441\u0440\u0430\u0432\u043d\u0438\u0442\u044c \u0434\u0432\u0435 \u0442\u0440\u0430\u0441\u0441\u044b \u043f\u043e \u0440\u0430\u0441\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u0438\u044e \u0447\u0438\u0441\u043b\u0430 \u0441\u043e\u0431\u044b\u0442\u0438\u0439 \u0432 \u0432\u044b\u0431\u043e\u0440\u043a\u0435</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0438\u0441\u043b\u043e\u0432\u044b\u0435 \u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0438 \u0434\u043b\u0438\u043d \u0438\u043d\u0442\u0435\u0440\u0432\u0430\u043b\u043e\u0432 \u0442\u0440\u0430\u0441\u0441\u044b", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft JhengHei'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0414\u043b\u044f \u043a\u043e\u0440\u0440\u0435\u043a\u0442\u043d\u043e\u0433\u043e \u0441\u0447\u0438\u0442\u044b\u0432\u0430\u043d\u0438\u044f \u0442\u0440\u0430\u0441\u0441\u044b \u043c\u043e\u043c\u0435\u043d\u0442\u044b \u043d\u0430\u0441\u0442\u0443\u043f\u043b\u0435\u043d\u0438\u044f \u0441\u043e\u0431\u044b\u0442\u0438\u0439 \u0434\u043e\u043b\u0436\u043d\u044b \u0431\u044b\u0442\u044c"
                        " \u0432 \u0442\u0435\u043a\u0441\u0442\u043e\u0432\u043e\u043c \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u0435 (.txt). \u041a\u0430\u0436\u0434\u044b\u0439 \u043c\u043e\u043c\u0435\u043d\u0442 \u0434\u043e\u043b\u0436\u0435\u043d \u0431\u044b\u0442\u044c \u0440\u0430\u0441\u043f\u043e\u043b\u043e\u0436\u0435\u043d \u043d\u0430 \u043d\u043e\u0432\u043e\u0439 \u0441\u0442\u0440\u043e\u0447\u043a\u0435.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u041f\u0440\u0438\u043c\u0435\u0440:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0.12</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0.45</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0.64</p>\n"
"<p style=\" margin-top:0px; margin-bo"
                        "ttom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1.42</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">6.25 \u0438 \u0442.\u0434</p></body></html>", None))
        self.btnReadTrace.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0442\u0440\u0430\u0441\u0441\u0443", None))
        self.btnTranferCharacteristics.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u044c \u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0438 \u0434\u043b\u044f \u043f\u043e\u0434\u0431\u043e\u0440\u0430", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u0438\u0435 \u0447\u0438\u0441\u043b\u0430 \u0441\u043e\u0431\u044b\u0442\u0438\u0439 \u043f\u0440\u0438 t=5", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b", None))
        self.comboSelectAlg.setItemText(0, QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u043b\u0435\u0434\u043e\u0432\u0430\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u043f\u0435\u0440\u0435\u0431\u043e\u0440", None))
        self.comboSelectAlg.setItemText(1, QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0431\u043e\u0440 \u0432 \u043e\u043a\u0440\u0435\u0441\u0442\u043d\u043e\u0441\u0442\u0438", None))
        self.comboSelectAlg.setItemText(2, QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0430\u0434\u0438\u0435\u043d\u0442\u043d\u044b\u0439 \u0441\u043f\u0443\u0441\u043a", None))

        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u043c\u0435\u0440\u043d\u043e\u0441\u0442\u044c", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0440\u0435\u0434\u043d\u0435\u0435", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u044d\u0444\u0444\u0438\u0446\u0438\u0435\u043d\u0442 \u0432\u0430\u0440\u0438\u0430\u0446\u0438\u0438 (cv)", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u044d\u0444\u0444\u0438\u0446\u0438\u0435\u043d\u0442 \u043a\u043e\u0440\u0440\u0435\u043b\u044f\u0446\u0438\u0438 (corr)", None))
        self.checkSkew.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u044d\u0444\u0444\u0438\u0446\u0438\u0435\u043d\u0442 \u0430\u0441\u0438\u043c\u043c\u0435\u0442\u0440\u0438\u0438 (skew)", None))
        self.checkKurt.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u044d\u0444\u0444\u0438\u0446\u0438\u0435\u043d\u0442 \u044d\u043a\u0441\u0446\u0435\u0441\u0441\u0430 (kurt)", None))
#if QT_CONFIG(tooltip)
        self.btnStartSearch.setToolTip(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0443\u0441\u043a\u0430\u0435\u0442 \u043f\u043e\u0434\u0431\u043e\u0440 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u043e\u0432", None))
#endif // QT_CONFIG(tooltip)
        self.btnStartSearch.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u043e\u0431\u0440\u0430\u0442\u044c MAP-\u043f\u043e\u0442\u043e\u043a", None))
#if QT_CONFIG(tooltip)
        self.btnAdditionalParameters.setToolTip(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0435 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u0434\u043b\u044f \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u043e\u0433\u043e \u0430\u043b\u0433\u043e\u0440\u0438\u0442\u043c\u0430", None))
#endif // QT_CONFIG(tooltip)
        self.btnAdditionalParameters.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u0430\u043b\u0433\u043e\u0440\u0438\u0442\u043c\u0430", None))
#if QT_CONFIG(tooltip)
        self.btnGradientParams.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0412 \u0441\u043b\u0443\u0447\u0430\u0435 \u043d\u0435\u0443\u0434\u0430\u0447\u043d\u043e\u0433\u043e \u043f\u043e\u0438\u0441\u043a\u0430 \u0440\u0435\u0448\u0435\u043d\u0438\u044f \u0431\u0443\u0434\u0435\u0442 \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u044c\u0441\u044f \u0433\u0440\u0430\u0434\u0438\u0435\u043d\u0442\u043d\u044b\u0439 \u0441\u043f\u0443\u0441\u043a \u0441 \u0446\u0435\u043b\u044c\u044e \u0443\u043b\u0443\u0447\u0448\u0435\u043d\u0438\u044f \u0440\u0435\u0448\u0435\u043d\u0438\u044f</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btnGradientParams.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u043f\u043e\u0434\u0433\u043e\u043d\u043a\u0438", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f", None))
        self.labelQ.setText("")
        self.labelLambda.setText("")
        self.labelD.setText("")
        self.progressSearch.setFormat(QCoreApplication.translate("MainWindow", u"%p%", None))
        self.btnSave.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u0432 \u0444\u0430\u0439\u043b", None))
        self.btnCompareWithOrigin.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0440\u0430\u0432\u043d\u0438\u0442\u044c \u0441 \u0438\u0441\u0445\u043e\u0434\u043d\u043e\u0439 \u0442\u0440\u0430\u0441\u0441\u043e\u0439", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u043c\u0435\u0440\u043d\u043e\u0441\u0442\u044c MAP", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0430\u0442\u0440\u0438\u0446\u0430 Q", None))
        self.matrixQ.setPlainText("")
        self.matrixQ.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u044b \u043c\u0430\u0442\u0440\u0438\u0446\u044b Q \u0431\u0435\u0437 \u043a\u0430\u043a\u0438\u0445-\u043b\u0438\u0431\u043e \u0437\u043d\u0430\u043a\u043e\u0432\u044b\u0445 \u0440\u0430\u0437\u0434\u0435\u043b\u0438\u0442\u0435\u043b\u0435\u0439, \u0442\u043e\u043b\u044c\u043a\u043e \u0447\u0435\u0440\u0435\u0437 \u043f\u0440\u043e\u0431\u0435\u043b", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0442\u0435\u043d\u0441\u0438\u0432\u043d\u043e\u0441\u0442\u0438 \u039b", None))
        self.matrixL.setPlainText("")
        self.matrixL.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0438\u043d\u0442\u0435\u043d\u0441\u0438\u0432\u043d\u043e\u0441\u0442\u0438 \u0440\u0430\u0441\u043f\u043e\u043b\u0430\u0433\u0430\u044f \u0438\u0445 \u0434\u0440\u0443\u0433 \u043f\u043e\u0434 \u0434\u0440\u0443\u0433\u043e\u043c", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0430\u0442\u0440\u0438\u0446\u0430 D", None))
        self.matrixD.setPlainText("")
        self.matrixD.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u044b \u043c\u0430\u0442\u0440\u0438\u0446\u044b D \u0431\u0435\u0437 \u043a\u0430\u043a\u0438\u0445-\u043b\u0438\u0431\u043e \u0437\u043d\u0430\u043a\u043e\u0432\u044b\u0445 \u0440\u0430\u0437\u0434\u0435\u043b\u0438\u0442\u0435\u043b\u0435\u0439, \u0442\u043e\u043b\u044c\u043a\u043e \u0447\u0435\u0440\u0435\u0437 \u043f\u0440\u043e\u0431\u0435\u043b", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0438\u0441\u043b\u043e \u0441\u043e\u0431\u044b\u0442\u0438\u0439", None))
        self.btnGenerate.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0433\u0435\u043d\u0435\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.btnLoadMap.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0444\u0430\u0439\u043b", None))
        self.btnSaveTrace.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0442\u0440\u0430\u0441\u0441\u0443", None))
        self.btnLoadTraces.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0444\u0430\u0439\u043b\u044b", None))
        self.btnCompareTraces.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0440\u0430\u0432\u043d\u0438\u0442\u044c", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"T:", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u0412\u0438\u0434", None))
    # retranslateUi

