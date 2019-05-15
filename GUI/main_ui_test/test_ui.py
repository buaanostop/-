# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test_ui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TestWindow(object):
    def setupUi(self, TestWindow):
        TestWindow.setObjectName("TestWindow")
        TestWindow.resize(1019, 756)
        self.centralwidget = QtWidgets.QWidget(TestWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(730, 10, 252, 196))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.con_dev_b = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.con_dev_b.setMinimumSize(QtCore.QSize(250, 60))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.con_dev_b.setFont(font)
        self.con_dev_b.setObjectName("con_dev_b")
        self.verticalLayout.addWidget(self.con_dev_b)
        self.in_ind_b = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.in_ind_b.setMinimumSize(QtCore.QSize(250, 60))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.in_ind_b.setFont(font)
        self.in_ind_b.setObjectName("in_ind_b")
        self.verticalLayout.addWidget(self.in_ind_b)
        self.cho_test_b = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.cho_test_b.setMinimumSize(QtCore.QSize(250, 60))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.cho_test_b.setFont(font)
        self.cho_test_b.setObjectName("cho_test_b")
        self.verticalLayout.addWidget(self.cho_test_b)
        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_2.setGeometry(QtCore.QRect(250, 40, 301, 161))
        self.listWidget_2.setObjectName("listWidget_2")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(210, 350, 271, 191))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(670, 330, 281, 261))
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(220, 230, 251, 81))
        self.textEdit.setObjectName("textEdit")
        TestWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TestWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1019, 26))
        self.menubar.setObjectName("menubar")
        TestWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(TestWindow)
        self.statusbar.setObjectName("statusbar")
        TestWindow.setStatusBar(self.statusbar)

        self.retranslateUi(TestWindow)
        QtCore.QMetaObject.connectSlotsByName(TestWindow)

    def retranslateUi(self, TestWindow):
        _translate = QtCore.QCoreApplication.translate
        TestWindow.setWindowTitle(_translate("TestWindow", "MainWindow"))
        self.con_dev_b.setText(_translate("TestWindow", "连接设备"))
        self.in_ind_b.setText(_translate("TestWindow", "输入连接的app参数"))
        self.cho_test_b.setText(_translate("TestWindow", "选择测试类型"))
        __sortingEnabled = self.listWidget_2.isSortingEnabled()
        self.listWidget_2.setSortingEnabled(False)
        item = self.listWidget_2.item(0)
        item.setText(_translate("TestWindow", "New Item"))
        item = self.listWidget_2.item(1)
        item.setText(_translate("TestWindow", "New Item"))
        item = self.listWidget_2.item(2)
        item.setText(_translate("TestWindow", "New Item"))
        item = self.listWidget_2.item(3)
        item.setText(_translate("TestWindow", "New Item"))
        item = self.listWidget_2.item(4)
        item.setText(_translate("TestWindow", "New Item"))
        item = self.listWidget_2.item(5)
        item.setText(_translate("TestWindow", "New Item"))
        item = self.listWidget_2.item(6)
        item.setText(_translate("TestWindow", "414"))
        item = self.listWidget_2.item(7)
        item.setText(_translate("TestWindow", "41"))
        item = self.listWidget_2.item(8)
        item.setText(_translate("TestWindow", "4"))
        item = self.listWidget_2.item(9)
        item.setText(_translate("TestWindow", "14245"))
        item = self.listWidget_2.item(10)
        item.setText(_translate("TestWindow", "2"))
        item = self.listWidget_2.item(11)
        item.setText(_translate("TestWindow", "7"))
        item = self.listWidget_2.item(12)
        item.setText(_translate("TestWindow", "2"))
        item = self.listWidget_2.item(13)
        item.setText(_translate("TestWindow", "752"))
        item = self.listWidget_2.item(14)
        item.setText(_translate("TestWindow", "78"))
        item = self.listWidget_2.item(15)
        item.setText(_translate("TestWindow", "57"))
        item = self.listWidget_2.item(16)
        item.setText(_translate("TestWindow", "2"))
        item = self.listWidget_2.item(17)
        item.setText(_translate("TestWindow", "4"))
        item = self.listWidget_2.item(18)
        item.setText(_translate("TestWindow", "1"))
        item = self.listWidget_2.item(19)
        item.setText(_translate("TestWindow", "New Item"))
        self.listWidget_2.setSortingEnabled(__sortingEnabled)
        self.textEdit_2.setHtml(_translate("TestWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">42</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">524</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">452</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">564</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">6464</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">11</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">65</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">331</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">33</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">31</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">131</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">31</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">33</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">56</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1651</p></body></html>"))
        self.textEdit_3.setHtml(_translate("TestWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<table border=\"0\" style=\" margin-top:5px; margin-bottom:5px; margin-left:0px; margin-right:0px;\" cellspacing=\"0\" cellpadding=\"0\" bgcolor=\"#f5f5f5\">\n"
"<tr>\n"
"<td style=\" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:36px; margin-right:36px; -qt-block-indent:0; text-indent:0px;\"><a name=\"best-content-1578791861\"></a><span style=\" font-family:\'Monaco,Menlo,Consolas,Courier New,monospace\'; font-size:13px; color:#333333;\"> </span><span style=\" font-family:\'Monaco,Menlo,Consolas,Courier New,monospace\'; font-size:13px; color:#000000;\">QScrollArea *pArea= </span><span style=\" font-family:\'Monaco,Menlo,Consolas,Courier New,monospace\'; font-size:13px; font-weight:696; color:#ff7800;\">new</span><span style=\" font-family:\'Monaco,Menlo,Consolas,Courier New,monospace\'; font-size:13px; color:#333333;\"> </span><span style=\" font-family:\'Monaco,Menlo,Consolas,Courier New,monospace\'; font-size:13px; color:#000000;\">QScrollArea(</span><span style=\" font-family:\'Monaco,Menlo,Consolas,Courier New,monospace\'; font-size:13px; font-weight:696; color:#ff7800;\">this</span><span style=\" font-family:\'Monaco,Menlo,Consolas,Courier New,monospace\'; font-size:13px; color:#000000;\">);</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:36px; margin-right:36px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Monaco,Menlo,Consolas,Courier New,monospace\'; font-size:13px; color:#333333;\">    </span><span style=\" font-family:\'Monaco,Menlo,Consolas,Courier New,monospace\'; font-size:13px; color:#000000;\">QWidget * qw = </span><span style=\" font-family:\'Monaco,Menlo,Consolas,Courier New,monospace\'; font-size:13px; font-weight:696; color:#ff7800;\">new</span><span style=\" font-family:\'Monaco,Menlo,Consolas,Courier New,monospace\'; font-size:13px; color:#333333;\"> </span><span style=\" font-family:\'Monaco,Menlo,Consolas,Courier New,monospace\'; font-size:13px; color:#000000;\">QWidget(pArea);</span><span style=\" font-family:\'Monaco,Menlo,Consolas,Courier New,monospace\'; font-size:13px; color:#008200;\">//需要滚动的是一个Qwidget，而如果是在设计器里面拖入控件，会自动添加一个</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:36px; margin-right:36px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Monaco,Menlo,Consolas,Courier New,monospace\'; font-size:13px; color:#333333;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:36px; margin-right:36px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Monaco,Menlo,Consolas,Courier New,monospace\'; font-size:13px; color:#333333;\">    </span><span style=\" font-family:\'Monaco,Menlo,Consolas,Courier New,monospace\'; font-size:13px; color:#000000;\">QPushButton * pb = </span><span style=\" font-family:\'Monaco,Menlo,Consolas,Courier New,monospace\'; font-size:13px; font-weight:696; color:#ff7800;\">new</span><span style=\" font-family:\'Monaco,Menlo,Consolas,Courier New,monospace\'; font-size:13px; color:#333333;\"> </span><span style=\" font-family:\'Monaco,Menlo,Consolas,Courier New,monospace\'; font-size:13px; color:#000000;\">QPushButton(qw);</span><span style=\" font-family:\'Monaco,Menlo,Consolas,Courier New,monospace\'; font-size:13px; color:#008200;\">//测试用，实际你使用就是把按钮设置父窗口，放进qw</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:36px; margin-right:36px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Monaco,Menlo,Consolas,Courier New,monospace\'; font-size:13px; color:#333333;\">    </span><span style=\" font-family:\'Monaco,Menlo,Consolas,Courier New,monospace\'; font-size:13px; color:#000000;\">pb-&gt;setText(</span><span style=\" font-family:\'Monaco,Menlo,Consolas,Courier New,monospace\'; font-size:13px; color:#0000ff;\">&quot;1235647&quot;</span><span style=\" font-family:\'Monaco,Menlo,Consolas,Courier New,monospace\'; font-size:13px; color:#000000;\">);</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:36px; margin-right:36px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Monaco,Menlo,Consolas,Courier New,monospace\'; font-size:13px; color:#333333;\">    </span><span style=\" font-family:\'Monaco,Menlo,Consolas,Courier New,monospace\'; font-size:13px; color:#000000;\">pb-&gt;move(130,50);</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:36px; margin-right:36px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Monaco,Menlo,Consolas,Courier New,monospace\'; font-size:13px; color:#333333;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:36px; margin-right:36px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Monaco,Menlo,Consolas,Courier New,monospace\'; font-size:13px; color:#333333;\">    </span><span style=\" font-family:\'Monaco,Menlo,Consolas,Courier New,monospace\'; font-size:13px; color:#000000;\">pArea-&gt;setWidget(qw);</span><span style=\" font-family:\'Monaco,Menlo,Consolas,Courier New,monospace\'; font-size:13px; color:#008200;\">//这里设置滚动窗口qw，</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:36px; margin-right:36px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Monaco,Menlo,Consolas,Courier New,monospace\'; font-size:13px; color:#333333;\">    </span><span style=\" font-family:\'Monaco,Menlo,Consolas,Courier New,monospace\'; font-size:13px; color:#000000;\">pArea-&gt;setGeometry(0,0,200,200);</span><span style=\" font-family:\'Monaco,Menlo,Consolas,Courier New,monospace\'; font-size:13px; color:#008200;\">//要显示的区域大小</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:36px; margin-right:36px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Monaco,Menlo,Consolas,Courier New,monospace\'; font-size:13px; color:#333333;\">    </span><span style=\" font-family:\'Monaco,Menlo,Consolas,Courier New,monospace\'; font-size:13px; color:#000000;\">qw-&gt;setGeometry(0,0,300,300);</span><span style=\" font-family:\'Monaco,Menlo,Consolas,Courier New,monospace\'; font-size:13px; color:#008200;\">//这里变大后，看出他实际滚动的是里面的QWidget窗口</span></p></td></tr></table>\n"
"<p style=\" margin-top:15px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:32px; background-color:#ffffff;\"><a name=\"wgt-eva-1578791861\"></a><span style=\" font-family:\'PingFang SC,Lantinghei SC,Microsoft YaHei,arial,宋体,sans-serif,tahoma\'; font-size:12px; color:#9eadb6; vertical-align:middle;\"> </span><span style=\" font-family:\'PingFangSC-Semibold\'; font-size:12px; font-weight:696; color:#34b458;\">29</span><span style=\" font-family:\'PingFang SC,Lantinghei SC,Microsoft YaHei,arial,宋体,sans-serif,tahoma\'; font-size:12px; color:#9eadb6; vertical-align:middle;\">  </span><a name=\"evaluate-bad-1578791861\"></a><span style=\" font-family:\'PingFang SC,Lantinghei SC,Microsoft YaHei,arial,宋体,sans-serif,tahoma\'; font-size:12px; color:#9eadb6; vertical-align:middle;\"> </span><span style=\" font-family:\'PingFangSC-Semibold\'; font-size:12px; font-weight:696; color:#34b458;\">3</span><span style=\" font-family:\'PingFang SC,Lantinghei SC,Microsoft YaHei,arial,宋体,sans-serif,tahoma\'; font-size:12px; color:#9eadb6;\"> </span><a name=\"comment-1578791861\"></a><span style=\" font-family:\'PingFangSC-Regular\'; font-size:14px; color:#7a8f9a;\">评</span><span style=\" font-family:\'PingFangSC-Regular\'; font-size:14px; color:#7a8f9a;\">论(1)</span><span style=\" font-family:\'PingFang SC,Lantinghei SC,Microsoft YaHei,arial,宋体,sans-serif,tahoma\'; font-size:12px; color:#9eadb6;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:34px;\"><span style=\" font-family:\'PingFangSC-Regular\'; font-size:14px; color:#7a8f9a;\">分享</span><span style=\" font-family:\'PingFang SC,Lantinghei SC,Microsoft YaHei,arial,宋体,sans-serif,tahoma\'; font-size:12px; color:#9eadb6;\"> </span><a href=\"javascript:void(0)\"><span style=\" font-family:\'PingFangSC-Regular\'; font-size:14px; text-decoration: underline; color:#7a8f9a; vertical-align:middle;\">举报</span></a></p></body></html>"))

