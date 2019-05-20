import Monkey
from PyQt5 import QtCore, QtGui, QtWidgets
class MyCurrentQueue(QtWidgets.QListWidget):
    def __init__(self,parent = None):
        super(MyCurrentQueue,self).__init__(parent)
    def dropEvent(self,event):
        print('%d '%self.currentRow(),end = '')
        index1 = self.currentRow()
        
        super(MyCurrentQueue,self).dropEvent(event)
        index2 = self.currentRow()
        Monkey.change(index1+ 1, index2 + 1)
        print(self.currentRow())
    def dragMoveEvent(self,event):
        super(MyCurrentQueue,self).dragMoveEvent(event)
    def dragEnterEvent(self,event):
        super(MyCurrentQueue,self).dragEnterEvent(event)

