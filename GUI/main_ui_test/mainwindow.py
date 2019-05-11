import sys
from ui_main import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

class mywindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
    def click_button_1(self):
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = mywindow()
    ui.show()
    sys.exit(app.exec_())
