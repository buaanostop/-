# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_point.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_addPointWindow(object):
    def setupUi(self, addPointWindow):
        addPointWindow.setObjectName("addPointWindow")
        addPointWindow.resize(1043, 855)
        self.label = QtWidgets.QLabel(addPointWindow)
        self.label.setGeometry(QtCore.QRect(10, 20, 1001, 781))
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(addPointWindow)
        self.pushButton.setGeometry(QtCore.QRect(930, 810, 93, 28))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(addPointWindow)
        self.pushButton.clicked.connect(addPointWindow.click_ap_b)
        QtCore.QMetaObject.connectSlotsByName(addPointWindow)

    def retranslateUi(self, addPointWindow):
        _translate = QtCore.QCoreApplication.translate
        addPointWindow.setWindowTitle(_translate("addPointWindow", "Dialog"))
        self.pushButton.setText(_translate("addPointWindow", "PushButton"))
