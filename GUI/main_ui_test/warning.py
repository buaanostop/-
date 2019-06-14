# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'warning.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_warning(object):
    def setupUi(self, warning):
        warning.setObjectName("warning")
        warning.resize(541, 155)
        font = QtGui.QFont()
        font.setPointSize(12)
        warning.setFont(font)
        self.label = QtWidgets.QLabel(warning)
        self.label.setGeometry(QtCore.QRect(90, 20, 361, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(warning)
        self.pushButton.setGeometry(QtCore.QRect(190, 100, 151, 41))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(warning)
        self.pushButton.clicked.connect(warning.close)
        QtCore.QMetaObject.connectSlotsByName(warning)

    def retranslateUi(self, warning):
        _translate = QtCore.QCoreApplication.translate
        warning.setWindowTitle(_translate("warning", "警告"))
        self.label.setText(_translate("warning", "超出可选范围！"))
        self.pushButton.setText(_translate("warning", "确定"))

