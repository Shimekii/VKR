# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DialogCompareWithTrace.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_dialogCompareTraceWithOrigin(object):
    def setupUi(self, dialogCompareTraceWithOrigin):
        if not dialogCompareTraceWithOrigin.objectName():
            dialogCompareTraceWithOrigin.setObjectName(u"dialogCompareTraceWithOrigin")
        dialogCompareTraceWithOrigin.resize(787, 473)
        self.verticalLayout = QVBoxLayout(dialogCompareTraceWithOrigin)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(dialogCompareTraceWithOrigin)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayoutCompareWithOrigin = QVBoxLayout()
        self.verticalLayoutCompareWithOrigin.setObjectName(u"verticalLayoutCompareWithOrigin")

        self.verticalLayout_3.addLayout(self.verticalLayoutCompareWithOrigin)

        self.btnCloseWindow = QPushButton(self.widget)
        self.btnCloseWindow.setObjectName(u"btnCloseWindow")
        self.btnCloseWindow.setMaximumSize(QSize(100, 16777215))
        self.btnCloseWindow.setLayoutDirection(Qt.LayoutDirection.RightToLeft)

        self.verticalLayout_3.addWidget(self.btnCloseWindow)


        self.verticalLayout.addWidget(self.widget)


        self.retranslateUi(dialogCompareTraceWithOrigin)

        QMetaObject.connectSlotsByName(dialogCompareTraceWithOrigin)
    # setupUi

    def retranslateUi(self, dialogCompareTraceWithOrigin):
        dialogCompareTraceWithOrigin.setWindowTitle(QCoreApplication.translate("dialogCompareTraceWithOrigin", u"\u0421\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u0435 \u0438\u0441\u0445\u043e\u0434\u043d\u043e\u0439 \u0442\u0440\u0430\u0441\u0441\u044b \u0441 \u043f\u043e\u0442\u043e\u043a\u043e\u043c", None))
        self.btnCloseWindow.setText(QCoreApplication.translate("dialogCompareTraceWithOrigin", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
    # retranslateUi

