import sys
import os
new_path = sys.path[0] + '\\monkeys'
sys.path.insert(1,new_path)
from Test_Ui_Functions import TestUiFunctionsClass as func
from ui_main import Ui_MainWindow
from guide_ui import Ui_GuideWindow
from test_ui_d.test_ui import Ui_TestWindow
from test_ui_d.in_device_infor import Ui_In_dev_infor
from test_ui_d.add_test_ui import Ui_Add_test
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from functools import wraps


now_point_index = 1
now_drag_index = 1
nowp = 2
'''
    通过装饰器实现一个单例模式
    保证只有一个和窗体类功能类↓
'''
def singleton(cls):
    instances = {}
    @wraps(cls)
    def getinstance(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return getinstance
@singleton
class mywindow(QtWidgets.QMainWindow,Ui_MainWindow):
    #successfully_connect = 1
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
    def click_guide_b(self):
        print("打开引导界面")
        g_ui.show()
    def click_test_b(self):
        print("打开测试界面")
        t_ui.t_init()
        t_ui.show()
@singleton
class g_window(QtWidgets.QMainWindow,Ui_GuideWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_GuideWindow.__init__(self)
        self.setupUi(self)
    def click_left_b(self):
        print("引导界面图片左划")
        global nowp
        if(nowp == 1):
            nowp = 3
        else:
            nowp = nowp-1
        g_ui.label.setPixmap(QtGui.QPixmap(":/gp/"+str(nowp)+".png"))
        #g_ui.label.setStyleSheet("border-image: url(:/gp/"+str(nowp)+".png);")
    def click_right_b(self):
        print("引导界面图片右划")
        global nowp
        if (nowp == 3):
            nowp = 1
        else:
            nowp = nowp + 1
        g_ui.label.setPixmap(QtGui.QPixmap(":/gp/" + str(nowp) + ".png"))
        #g_ui.label.setStyleSheet("border-image: url(:/gp/"+str(nowp)+".png);")
@singleton
class t_window(QtWidgets.QMainWindow,Ui_TestWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_TestWindow.__init__(self)
        self.setupUi(self)
        self.InputAssignmentButton.setEnabled(False)
        self.chooseTypeButton.setEnabled(False)
    def click_in_index_b(self):
        print("点击 输入app参数 按钮")
        i_d_ui.show()



    def click_add_test(self):
        print("点击 选择测试类型 按钮")
        a_t_ui.now_point_num.hide()
        a_t_ui.v_m_touch_point_num.setProperty("value", 1)
        a_t_ui.v_m_touch_point_num.show()
        a_t_ui.confirm_m_touch_point_n_b.show()

        a_t_ui.now_drag_num.hide()
        a_t_ui.v_m_drag_num.setProperty("value", 1)
        a_t_ui.v_m_drag_num.show()
        a_t_ui.confirm_m_drag_n_b.show()
        a_t_ui.show()

    def t_init(self):
        t_ui.loadButton.show()
        t_ui.saveButton.show()
        t_ui.startButton.show()
        t_ui.pauseButton.hide()
        t_ui.resumeButton.hide()
        t_ui.stopButton.hide()

    '''点击连接设备按钮'''
    def click_connect_b(self):
        print("点击连接设备按钮")
        '''
            todo:调用connect函数
                之后根据连接成功与否判断其他两个键是否启用
        '''
        self.InputAssignmentButton.setEnabled(True)
        self.connectDeviceButton.setText("重新连接")

    def click_load_b(self):
        print("点击读档按钮")
    def click_save_b(self):
        print("点击存档按钮")
    def click_start_b(self):
        print("点击开始按钮")
    def click_pause_b(self):
        print("点击暂停按钮")
    def click_resume_b(self):
        print("点击继续按钮")
    def click_stop_b(self):
        print("点击终止按钮")
@singleton
class in_dev_infor(QtWidgets.QDialog,Ui_In_dev_infor):
    has_finished = 0
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        Ui_In_dev_infor.__init__(self)
        self.setupUi(self)
    

    def click_fin_b(self):
        '''
        加入对参数信息的异常处理
        '''

        '''
        把信息记录下来
        '''
        if(i_d_ui.has_finished == 0):
            test_window = t_window()
            test_window.InputAssignmentButton.setText('重新输入')
            test_window.chooseTypeButton.setEnabled(True)

        self.has_finished = 1
        self.close()
        print("参数信息输入完毕")
@singleton
class add_test(QtWidgets.QDialog,Ui_Add_test):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        Ui_Add_test.__init__(self)
        self.setupUi(self)
        #self.currentQueueList.clear()
        self.currentQueueList.setDragDropMode(self.currentQueueList.InternalMove)
    def delete_current_row(self):
        row = a_t_ui.currentQueueList.currentRow()
        #print("删除第"+str(row+1)+"条测试")
        a_t_ui.currentQueueList.takeItem(row)
    #多点点击测试
    def mul_touch_next_p(self):
        global now_point_index #注意
        if(now_point_index < int(a_t_ui.now_point_num.text())):
            now_point_index = now_point_index + 1
            text = "第"+str(now_point_index)+"点坐标:(X,Y)"
            a_t_ui.m_touch_pos.setText(text)

    def confirm_m_touch_p_num(self):
        a_t_ui.now_point_num.setText(a_t_ui.v_m_touch_point_num.text())

    def reset_point_no(self):
        global now_point_index
        a_t_ui.m_touch_pos.setText("第1点坐标:(X,Y)")
        now_point_index = 1
        print("清除参数")
    #多端滑动测试
    def mul_drag_next_l(self):
        global now_drag_index #注意
        if(now_drag_index < int(a_t_ui.now_drag_num.text())):
            now_drag_index = now_drag_index + 1
            text1 = "第" + str(now_drag_index)+"次滑动起点坐标:(X,Y)"
            text2 = "第" + str(now_drag_index) + "次滑动终点坐标:(X,Y)"
            a_t_ui.m_drag_start_p.setText(text1)
            a_t_ui.m_drag_end_p.setText(text2)

    def confirm_m_drag_num(self):
        a_t_ui.now_drag_num.setText(a_t_ui.v_m_drag_num.text())

    def reset_drag_no(self):
        global now_drag_index
        a_t_ui.m_drag_start_p.setText("第1次滑动起点坐标:(X,Y)")
        a_t_ui.m_drag_end_p.setText("第1次滑动终点坐标:(X,Y)")
        now_drag_index = 1

    def add_new_test_b(self):
        if(a_t_ui.tabWidget.currentIndex() == 0):
            #print(int(a_t_ui.v_touch_pos_x.text()))
            print("加入单点点击测试")
        elif(a_t_ui.tabWidget.currentIndex() == 1):
            print("加入单点长按测试")
        elif (a_t_ui.tabWidget.currentIndex() == 2):
            print("加入多点点击测试")
        elif (a_t_ui.tabWidget.currentIndex() == 3):
            print("加入随机点击测试")
        elif (a_t_ui.tabWidget.currentIndex() == 4):
            print("加入单线滑动测试")
        elif (a_t_ui.tabWidget.currentIndex() == 5):
            print("加入多线滑动测试")
        elif (a_t_ui.tabWidget.currentIndex() == 6):
            print("加入随机滑动测试")
        elif (a_t_ui.tabWidget.currentIndex() == 7):
            print("加入长按滑动测试")
    def fin_queue_edit(self):
        print("队列输入完毕")
        a_t_ui.close()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = mywindow()
    g_ui = g_window()
    t_ui = t_window()
    i_d_ui = in_dev_infor()
    a_t_ui = add_test()
    functions_class = func(t_ui,i_d_ui)
    ui.show()
    sys.exit(app.exec_())
# queueList
# reportList