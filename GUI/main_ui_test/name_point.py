# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'name_point.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_NamePoint(object):
    def setupUi(self, NamePoint):
        NamePoint.setObjectName("NamePoint")
        NamePoint.resize(580, 80)
        font = QtGui.QFont()
        font.setPointSize(9)
        NamePoint.setFont(font)
        self.nameLine = QtWidgets.QLineEdit(NamePoint)
        self.nameLine.setGeometry(QtCore.QRect(30, 20, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.nameLine.setFont(font)
        self.nameLine.setObjectName("nameLine")
        self.confirmNameButton = QtWidgets.QPushButton(NamePoint)
        self.confirmNameButton.setGeometry(QtCore.QRect(350, 20, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.confirmNameButton.setFont(font)
        self.confirmNameButton.setObjectName("confirmNameButton")
        self.cancelButton = QtWidgets.QPushButton(NamePoint)
        self.cancelButton.setGeometry(QtCore.QRect(470, 20, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cancelButton.setFont(font)
        self.cancelButton.setObjectName("cancelButton")

        self.retranslateUi(NamePoint)
        self.cancelButton.clicked.connect(NamePoint.close)
        self.confirmNameButton.clicked.connect(NamePoint.name_point_confirm)
        QtCore.QMetaObject.connectSlotsByName(NamePoint)

    def retranslateUi(self, NamePoint):
        _translate = QtCore.QCoreApplication.translate
        NamePoint.setWindowTitle(_translate("NamePoint", "为该点命名"))
        self.confirmNameButton.setText(_translate("NamePoint", "确定"))
        self.cancelButton.setText(_translate("NamePoint", "取消"))

