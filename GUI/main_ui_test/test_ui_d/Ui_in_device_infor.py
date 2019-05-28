# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\sickk\Documents\GitHub\nostop_Autotest\Autotest\GUI\main_ui_test\test_ui_d\in_device_infor.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_In_dev_infor(object):
    def setupUi(self, In_dev_infor):
        In_dev_infor.setObjectName("In_dev_infor")
        In_dev_infor.resize(796, 278)
        self.gridLayout = QtWidgets.QGridLayout(In_dev_infor)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(In_dev_infor)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout.addWidget(self.frame, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(15)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.finishInputButton = QtWidgets.QPushButton(In_dev_infor)
        self.finishInputButton.setMinimumSize(QtCore.QSize(110, 30))
        self.finishInputButton.setMaximumSize(QtCore.QSize(110, 30))
        self.finishInputButton.setObjectName("finishInputButton")
        self.horizontalLayout_2.addWidget(self.finishInputButton)
        self.exitButton = QtWidgets.QPushButton(In_dev_infor)
        self.exitButton.setMinimumSize(QtCore.QSize(110, 30))
        self.exitButton.setMaximumSize(QtCore.QSize(110, 30))
        self.exitButton.setObjectName("exitButton")
        self.horizontalLayout_2.addWidget(self.exitButton)
        self.cleanButton = QtWidgets.QPushButton(In_dev_infor)
        self.cleanButton.setMinimumSize(QtCore.QSize(110, 30))
        self.cleanButton.setMaximumSize(QtCore.QSize(110, 30))
        self.cleanButton.setObjectName("cleanButton")
        self.horizontalLayout_2.addWidget(self.cleanButton)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.p_name = QtWidgets.QLabel(In_dev_infor)
        self.p_name.setObjectName("p_name")
        self.verticalLayout_2.addWidget(self.p_name)
        self.a_name = QtWidgets.QLabel(In_dev_infor)
        self.a_name.setObjectName("a_name")
        self.verticalLayout_2.addWidget(self.a_name)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(27)
        self.verticalLayout.setObjectName("verticalLayout")
        self.packageNameValue = QtWidgets.QLineEdit(In_dev_infor)
        self.packageNameValue.setMinimumSize(QtCore.QSize(639, 30))
        self.packageNameValue.setMaximumSize(QtCore.QSize(639, 30))
        self.packageNameValue.setObjectName("packageNameValue")
        self.verticalLayout.addWidget(self.packageNameValue)
        self.PackageActivityName = QtWidgets.QLineEdit(In_dev_infor)
        self.PackageActivityName.setMinimumSize(QtCore.QSize(639, 30))
        self.PackageActivityName.setMaximumSize(QtCore.QSize(639, 30))
        self.PackageActivityName.setObjectName("PackageActivityName")
        self.verticalLayout.addWidget(self.PackageActivityName)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 2)

        self.retranslateUi(In_dev_infor)
        self.finishInputButton.clicked.connect(In_dev_infor.click_fin_b)
        self.cleanButton.clicked.connect(self.packageNameValue.clear)
        self.cleanButton.clicked.connect(self.PackageActivityName.clear)
        self.exitButton.clicked.connect(In_dev_infor.reject)
        self.finishInputButton.clicked.connect(In_dev_infor.click_fin_b)
        QtCore.QMetaObject.connectSlotsByName(In_dev_infor)

    def retranslateUi(self, In_dev_infor):
        _translate = QtCore.QCoreApplication.translate
        In_dev_infor.setWindowTitle(_translate("In_dev_infor", "输入参数窗口"))
        self.finishInputButton.setText(_translate("In_dev_infor", "输入完毕"))
        self.exitButton.setText(_translate("In_dev_infor", "退出"))
        self.cleanButton.setText(_translate("In_dev_infor", "清屏"))
        self.p_name.setWhatsThis(_translate("In_dev_infor", "<html><head/><body><p>应用的包名，例如：com.Jelly.JellyFish</p><p>（可以为空，默认对当前app进行测试）</p></body></html>"))
        self.p_name.setText(_translate("In_dev_infor", "应用的包名："))
        self.a_name.setWhatsThis(_translate("In_dev_infor", "<html><head/><body><p>应用的活动名，例如: com.unity3d.player.UnityPlayerActivity</p><p>（可以为空，默认对当前app进行测试）</p></body></html>"))
        self.a_name.setText(_translate("In_dev_infor", "应用的活动名："))
        self.packageNameValue.setPlaceholderText(_translate("In_dev_infor", "（后可以为空，默认对当前app进行测试）"))
        self.PackageActivityName.setPlaceholderText(_translate("In_dev_infor", "（后可以为空，默认对当前app进行测试）"))

