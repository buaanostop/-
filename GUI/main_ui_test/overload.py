from PyQt5 import QtCore, QtGui, QtWidgets
class MyCurrentQueue(QtWidgets.QListWidget):
    def __init__(self,parent = None):
        super(MyCurrentQueue,self).__init__(parent)
    def dropEvent(self,event):
        print('%d '%self.currentRow(),end = '')
        #这里换成给monkeyserver发送信息的函数
        super(MyCurrentQueue,self).dropEvent(event)
        print(self.currentRow())
    def dragMoveEvent(self,event):
        super(MyCurrentQueue,self).dragMoveEvent(event)
    def dragEnterEvent(self,event):
        super(MyCurrentQueue,self).dragEnterEvent(event)

