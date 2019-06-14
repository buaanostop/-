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
        addPointWindow.resize(979, 833)
        self.label = QtWidgets.QLabel(addPointWindow)
        self.label.setGeometry(QtCore.QRect(40, 40, 900, 600))
        self.label.setStyleSheet("")
        self.label.setText("")
        self.label.setObjectName("label")
        self.chooseDeletePointButton = QtWidgets.QPushButton(addPointWindow)
        self.chooseDeletePointButton.setGeometry(QtCore.QRect(810, 680, 111, 131))
        self.chooseDeletePointButton.setObjectName("chooseDeletePointButton")
        self.pointTable = QtWidgets.QTableWidget(addPointWindow)
        self.pointTable.setGeometry(QtCore.QRect(30, 660, 731, 161))
        self.pointTable.setObjectName("pointTable")
        self.pointTable.setColumnCount(3)
        self.pointTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.pointTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.pointTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.pointTable.setHorizontalHeaderItem(2, item)
        self.pointTable.horizontalHeader().setDefaultSectionSize(229)
        self.pointTable.verticalHeader().setDefaultSectionSize(37)

        self.retranslateUi(addPointWindow)
        self.chooseDeletePointButton.clicked.connect(addPointWindow.delete_current_point_row)
        QtCore.QMetaObject.connectSlotsByName(addPointWindow)

    def retranslateUi(self, addPointWindow):
        _translate = QtCore.QCoreApplication.translate
        addPointWindow.setWindowTitle(_translate("addPointWindow", "加入当前屏幕上的点"))
        self.chooseDeletePointButton.setText(_translate("addPointWindow", "删除选中点"))
        item = self.pointTable.horizontalHeaderItem(0)
        item.setText(_translate("addPointWindow", "名称"))
        item = self.pointTable.horizontalHeaderItem(1)
        item.setText(_translate("addPointWindow", "X"))
        item = self.pointTable.horizontalHeaderItem(2)
        item.setText(_translate("addPointWindow", "Y"))

