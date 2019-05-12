# -*- coding: utf-8 -*-
#因为文件不齐，现在只能把加进的函数注释掉才能看到界面
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QDockWidget, QListWidget
from PyQt5.QtGui import *
#from Test_Ui_Functions import *
from Ui_test_ui import Ui_TestWindow #import刚刚创建的GUI类
class myTestWindow(QtWidgets.QMainWindow,Ui_TestWindow):
    def __init__(self):#因为是继承自Qtwidgets.QMainWindow和Ui_MainWindow的，重载一下父类构造函数
        super(myTestWindow,self).__init__()
        self.setupUi(self) #初始化UI界面
        #self.pushButton.clicked.connect(self.hello_message)

if  __name__ == '__main__': #python的main函数
    app = QtWidgets.QApplication(sys.argv)
    # QApplication相当于main函数，也就是整个程序（很多文件）的主入口函数。
    # 对于GUI程序必须至少有一个这样的实例来让程序运行。
    test_window = myTestWindow()
    test_window.show()
    #close_monkeyrunner()
    #close_model()
    sys.exit(app.exec_()) #正常退出程序