# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\sickk\Desktop\大三\大三下\se\test_ui_version_0.00.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TestWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1022, 629)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.clearQueueButton = QtWidgets.QPushButton(self.centralwidget)
        self.clearQueueButton.setGeometry(QtCore.QRect(110, 550, 75, 31))
        self.clearQueueButton.setObjectName("clearQueueButton")
        self.queueList = QtWidgets.QListWidget(self.centralwidget)
        self.queueList.setGeometry(QtCore.QRect(0, 0, 291, 541))
        self.queueList.setObjectName("queueList")
        self.reportList = QtWidgets.QListWidget(self.centralwidget)
        self.reportList.setGeometry(QtCore.QRect(290, 0, 411, 541))
        self.reportList.setObjectName("reportList")
        self.clearReportButton = QtWidgets.QPushButton(self.centralwidget)
        self.clearReportButton.setGeometry(QtCore.QRect(460, 550, 75, 31))
        self.clearReportButton.setObjectName("clearReportButton")
        self.connectDeviceButton = QtWidgets.QPushButton(self.centralwidget)
        self.connectDeviceButton.setGeometry(QtCore.QRect(700, 0, 321, 41))
        self.connectDeviceButton.setObjectName("connectDeviceButton")
        self.InputAssignmentButton = QtWidgets.QPushButton(self.centralwidget)
        self.InputAssignmentButton.setGeometry(QtCore.QRect(700, 40, 321, 41))
        self.InputAssignmentButton.setObjectName("InputAssignmentButton")
        self.chooseTypeButton = QtWidgets.QPushButton(self.centralwidget)
        self.chooseTypeButton.setGeometry(QtCore.QRect(700, 80, 321, 41))
        self.chooseTypeButton.setObjectName("chooseTypeButton")
        self.finishInputButton = QtWidgets.QPushButton(self.centralwidget)
        self.finishInputButton.setGeometry(QtCore.QRect(800, 530, 101, 31))
        self.finishInputButton.setObjectName("finishInputButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1022, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.clearQueueButton.setText(_translate("MainWindow", "清屏"))
        self.clearReportButton.setText(_translate("MainWindow", "清屏"))
        self.connectDeviceButton.setText(_translate("MainWindow", "连接设备"))
        self.InputAssignmentButton.setText(_translate("MainWindow", "输入要测试的app参数"))
        self.chooseTypeButton.setText(_translate("MainWindow", "选择测试类型"))
        self.finishInputButton.setText(_translate("MainWindow", "队列输入完毕"))
        self.menu.setTitle(_translate("MainWindow", "帮助"))

