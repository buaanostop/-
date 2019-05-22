# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'guide_ui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_GuideWindow(object):
    def setupUi(self, GuideWindow):
        GuideWindow.setObjectName("GuideWindow")
        GuideWindow.resize(1068, 808)
        self.centralwidget = QtWidgets.QWidget(GuideWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.nextPictureButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nextPictureButton.sizePolicy().hasHeightForWidth())
        self.nextPictureButton.setSizePolicy(sizePolicy)
        self.nextPictureButton.setMinimumSize(QtCore.QSize(200, 100))
        self.nextPictureButton.setMaximumSize(QtCore.QSize(200, 100))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.nextPictureButton.setFont(font)
        self.nextPictureButton.setObjectName("nextPictureButton")
        self.gridLayout.addWidget(self.nextPictureButton, 1, 2, 1, 1)
        self.guidePictures = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.guidePictures.sizePolicy().hasHeightForWidth())
        self.guidePictures.setSizePolicy(sizePolicy)
        self.guidePictures.setMinimumSize(QtCore.QSize(0, 0))
        self.guidePictures.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.guidePictures.setStyleSheet("border-image: url(:/gp/1.png);")
        self.guidePictures.setText("")
        self.guidePictures.setAlignment(QtCore.Qt.AlignCenter)
        self.guidePictures.setObjectName("guidePictures")
        self.gridLayout.addWidget(self.guidePictures, 1, 1, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setMinimumSize(QtCore.QSize(0, 200))
        self.textEdit.setMaximumSize(QtCore.QSize(16777215, 200))
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 2, 1, 1, 1)
        self.lastPictureButton = QtWidgets.QPushButton(self.centralwidget)
        self.lastPictureButton.setMinimumSize(QtCore.QSize(200, 100))
        self.lastPictureButton.setMaximumSize(QtCore.QSize(200, 100))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lastPictureButton.setFont(font)
        self.lastPictureButton.setObjectName("lastPictureButton")
        self.gridLayout.addWidget(self.lastPictureButton, 1, 0, 1, 1)
        self.guideTitle = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.guideTitle.sizePolicy().hasHeightForWidth())
        self.guideTitle.setSizePolicy(sizePolicy)
        self.guideTitle.setMinimumSize(QtCore.QSize(630, 100))
        self.guideTitle.setMaximumSize(QtCore.QSize(630, 100))
        font = QtGui.QFont()
        font.setPointSize(27)
        font.setBold(True)
        font.setWeight(75)
        self.guideTitle.setFont(font)
        self.guideTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.guideTitle.setObjectName("guideTitle")
        self.gridLayout.addWidget(self.guideTitle, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        GuideWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(GuideWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1068, 26))
        self.menubar.setObjectName("menubar")
        GuideWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(GuideWindow)
        self.statusbar.setObjectName("statusbar")
        GuideWindow.setStatusBar(self.statusbar)

        self.retranslateUi(GuideWindow)
        self.nextPictureButton.clicked.connect(GuideWindow.click_right_b)
        self.lastPictureButton.clicked.connect(GuideWindow.click_left_b)
        QtCore.QMetaObject.connectSlotsByName(GuideWindow)

    def retranslateUi(self, GuideWindow):
        _translate = QtCore.QCoreApplication.translate
        GuideWindow.setWindowTitle(_translate("GuideWindow", "引导窗口"))
        self.nextPictureButton.setText(_translate("GuideWindow", "下一张"))
        self.guidePictures.setWhatsThis(_translate("GuideWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.textEdit.setHtml(_translate("GuideWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">主界面如上图所示。</p></body></html>"))
        self.lastPictureButton.setText(_translate("GuideWindow", "上一张"))
        self.guideTitle.setWhatsThis(_translate("GuideWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:600;\">title</span></p></body></html>"))
        self.guideTitle.setText(_translate("GuideWindow", "使用引导"))

import images.guide_p
