第1步：安装PyQt5和PyQt5-tools

pip3 install -i <https://mirrors.aliyun.com/pypi/simple/> PyQt5

pip3 install -i <https://mirrors.aliyun.com/pypi/simple/> PyQt5-tools

 

第2步：找到QtDesigner 安装路径

一般会自动安装在python安装目录中，如果安装了Anaconda3，则将会在如下Anaconda3路径中找到：

E:\Soft_dp\Anaconda3\Lib\site-packages\pyqt5_tools

将该文件夹中designer.exe生成桌面快捷方式，方便日后制作.ui文件。

 

第3步：打开designer.exe，并绘制你想要的UI界面，如下图所示：



 ![1557305002167](C:\Users\sickk\AppData\Roaming\Typora\typora-user-images\1557305002167.png)

绘制完后，起个名字，保存到你准备制作该项目的文件夹中，比如：welcome.ui

 

第4步：用VSCode转化.ui文件为.py文件

（1）打开VSCode，打开welcome.ui刚才存放的那个工程文件夹。

​	注意：必须打开工程文件夹 而不能直接打开welcome.ui文件

（2）搜索并安装PYQT Intergration插件

![img](https://img2018.cnblogs.com/blog/846029/201810/846029-20181019114127034-1243676992.png)

（3）在welcome.ui上右键选择如下图红色圈内操作。



 

![img](https://img2018.cnblogs.com/blog/846029/201810/846029-20181019113954497-160943599.png)

 点击后，会自动生成一个叫：UI_welcome.py的文件，里面就是刚才绘制界面的UI类。

 

第5步：新建一个.py文件，用于启动程序，并调用刚才制作的UI类，必要代码和解释如下：

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```python
# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QDockWidget, QListWidget
from PyQt5.QtGui import *

from Ui_study import Ui_MainWindow #import刚刚创建的GUI类
class myTestWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):#因为是继承自Qtwidgets.QMainWindow和Ui_MainWindow的，重载一下父类构造函数
        super(myTestWindow,self).__init__()
        self.setupUi(self) #初始化UI界面
if  __name__ == '__main__': #python的main函数
    app = QtWidgets.QApplication(sys.argv)
    # QApplication相当于main函数，也就是整个程序（很多文件）的主入口函数。
    # 对于GUI程序必须至少有一个这样的实例来让程序运行。
    my_window = myTestWindow()
    my_window.show()
    sys.exit(app.exec_()) #正常退出程序
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

然后，直接按F5运行该文件，就会弹出刚才绘制的窗口：

![1557305025709](C:\Users\sickk\AppData\Roaming\Typora\typora-user-images\1557305025709.png)

接下来我们尝试给PushButton绑定一个函数，点击按钮会弹出消息提示框，我们使用QMessageBox里的about方法来弹出消息框，about方法第二个参数是标题，第三个是内容，也可以初始化一个QMessageBox的实例，用该实例其他方法来更好地定制消息框内容。注意需从PyQt5.QtWidgets里mport QMessageBox。

```python
# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QDockWidget, QListWidget
from PyQt5.QtGui import *

from Ui_study import Ui_MainWindow #import刚刚创建的GUI类
class myTestWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):#因为是继承自Qtwidgets.QMainWindow和Ui_MainWindow的，重载一下父类构造函数
        super(myTestWindow,self).__init__()
        self.setupUi(self) #初始化UI界面
        self.pushButton.clicked.connect(self.hello_message)#绑定按钮到hello_message方法
    def hello_message(self):
        QMessageBox.about(self,"你好","hello world")#使用QMessageBox里的about方法来弹出消息框
if  __name__ == '__main__': #python的main函数
    app = QtWidgets.QApplication(sys.argv)
    # QApplication相当于main函数，也就是整个程序（很多文件）的主入口函数。
    # 对于GUI程序必须至少有一个这样的实例来让程序运行。
    my_window = myTestWindow()
    my_window.show()
    sys.exit(app.exec_()) #正常退出程序
```

运行后实际效果如下

![1557305672382](C:\Users\sickk\AppData\Roaming\Typora\typora-user-images\1557305672382.png)

更多关于PyQt的使用可以参考[官方文档](<https://www.riverbankcomputing.com/static/Docs/PyQt5/>)