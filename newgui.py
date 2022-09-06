# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'firstuZrgKf.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

#import logo1_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(600, 674)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(u"QWidget#centralwidget{\n"
"background-color: qlineargradient(spread:pad, x1:0.0199005, y1:0.966, x2:1, y2:1, stop:0 rgba(234, 141, 141, 255), stop:1 rgba(168, 144, 254, 255));\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.voiceRecButton = QPushButton(self.centralwidget)
        self.voiceRecButton.setObjectName(u"voiceRecButton")
        self.voiceRecButton.setGeometry(QRect(40, 210, 191, 51))
        self.voiceRecButton.setStyleSheet(u"QPushButton#voiceRecButton{\n"
"border-radius:22px;\n"
"color: rgb(217, 252, 248);\n"
"font: 63 8pt \"JetBrains Mono SemiBold\";\n"
"background-color: rgb(120, 188, 230);\n"
"}\n"
"QPushButton#voiceRecButton:hover{\n"
"\n"
"	\n"
"	background-color: rgb(129, 204, 248);\n"
"}\n"
"QPushButton#voiceRecButton:pressed{\n"
"\n"
"background-color: rgb(50, 188, 241);\n"
"}")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 630, 131, 51))
        self.label.setStyleSheet(u"font: 81 18pt \"JetBrains Mono ExtraBold\";")
        self.icon1 = QLabel(self.centralwidget)
        self.icon1.setObjectName(u"icon1")
        self.icon1.setGeometry(QRect(10, 640, 31, 31))
        self.icon1.setPixmap(QPixmap(u"resources/logo.png"))
        self.icon1.setScaledContents(True)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(130, 648, 51, 21))
        self.label_2.setStyleSheet(u"\n"
"font: 25 14pt \"JetBrains Mono Light\";")
        self.botTalkButton = QPushButton(self.centralwidget)
        self.botTalkButton.setObjectName(u"botTalkButton")
        self.botTalkButton.setGeometry(QRect(369, 210, 191, 51))
        self.botTalkButton.setStyleSheet(u"QPushButton#botTalkButton{\n"
"border-radius:22px;\n"
"color: rgb(217, 252, 248);\n"
"font: 63 8pt \"JetBrains Mono SemiBold\";\n"
"background-color: rgb(120, 188, 230);\n"
"}\n"
"QPushButton#botTalkButton:hover{\n"
"\n"
"	\n"
"	background-color: rgb(129, 204, 248);\n"
"}\n"
"QPushButton#botTalkButton:pressed{\n"
"\n"
"background-color: rgb(50, 188, 241);\n"
"}")
        self.fileRecognizeButton = QPushButton(self.centralwidget)
        self.fileRecognizeButton.setObjectName(u"fileRecognizeButton")
        self.fileRecognizeButton.setGeometry(QRect(149, 550, 301, 51))
        self.fileRecognizeButton.setStyleSheet(u"QPushButton#fileRecognizeButton{\n"
"border-radius:22px;\n"
"color: rgb(217, 252, 248);\n"
"font: 63 8pt \"JetBrains Mono SemiBold\";\n"
"background-color: rgb(120, 188, 230);\n"
"}\n"
"QPushButton#fileRecognizeButton:hover{\n"
"\n"
"	\n"
"	background-color: rgb(129, 204, 248);\n"
"}\n"
"QPushButton#fileRecognizeButton:pressed{\n"
"\n"
"background-color: rgb(50, 188, 241);\n"
"}")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(174, 320, 251, 16))
        self.label_3.setStyleSheet(u"color: rgb(217, 252, 248);\n"
"font: 63 7pt \"JetBrains Mono SemiBold\";")
        self.voiceRecText = QPlainTextEdit(self.centralwidget)
        self.voiceRecText.setObjectName(u"voiceRecText")
        self.voiceRecText.setGeometry(QRect(10, 0, 256, 192))
        self.voiceRecText.setStyleSheet(u"border-radius:22px;\n"
"border: 0;\n"
"background-color: rgba(223, 201, 255,20);")
        self.botTalkText = QPlainTextEdit(self.centralwidget)
        self.botTalkText.setObjectName(u"botTalkText")
        self.botTalkText.setGeometry(QRect(334, 0, 256, 192))
        self.botTalkText.setStyleSheet(u"border-radius:22px;\n"
"border: 0;\n"
"background-color: rgba(223, 201, 255,20);")
        self.fileText = QPlainTextEdit(self.centralwidget)
        self.fileText.setObjectName(u"fileText")
        self.fileText.setGeometry(QRect(172, 340, 256, 192))
        self.fileText.setStyleSheet(u"border-radius:22px;\n"
"border: 0;\n"
"background-color: rgba(223, 201, 255,20);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 600, 26))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.voiceRecButton.setText(QCoreApplication.translate("MainWindow", u"Voice recognition", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"VRec", None))
        self.icon1.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"1.0", None))
        self.botTalkButton.setText(QCoreApplication.translate("MainWindow", u"Make it say something!", None))
        self.fileRecognizeButton.setText(QCoreApplication.translate("MainWindow", u"Choose file to recognize voice from", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Voice recognized from file is here:", None))
    # retranslateUi

