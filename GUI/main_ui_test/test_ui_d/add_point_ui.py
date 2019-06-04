# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_point_ui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_addPointWindow(object):
    def setupUi(self, addPointWindow):
        addPointWindow.setObjectName("addPointWindow")
        addPointWindow.resize(900, 598)
        self.label = QtWidgets.QLabel(addPointWindow)
        self.label.setGeometry(QtCore.QRect(0, 0, 900, 600))
        self.label.setStyleSheet("")
        self.label.setText("")
        self.label.setObjectName("label")

        self.retranslateUi(addPointWindow)
        QtCore.QMetaObject.connectSlotsByName(addPointWindow)

    def retranslateUi(self, addPointWindow):
        _translate = QtCore.QCoreApplication.translate
        addPointWindow.setWindowTitle(_translate("addPointWindow", "Dialog"))

