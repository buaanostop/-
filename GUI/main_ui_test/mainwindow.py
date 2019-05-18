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
from PyQt5.QtWidgets import QApplication, QMainWindow,QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from functools import wraps


now_point_index = 1
now_drag_index = 1
nowp = 2
empty_error_code = 0
number_error_code = 1
range_error_code = 2
resolution_ration_error_code = 3
something_else_error_code = 4
have_not_connect_error_code = 5
not_successful_connected_error_code = 6

min_click_times = 1
max_click_times = 9999
min_interval_time = 0.1
max_interval_time = 99.9
min_drag_times_number = 1
max_drag_times_number = 9999
min_drag_during_time =0.1
max_drag_during_time = 9.9
min_drag_interval_time = 0.1
max_drag_interval_time = 99.9
x_rate = 1024
y_rate = 768
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
def reset_test_window():
    test_window = t_window()
    test_window.setupUi(test_window)
    test_window.t_init()
class rangeErrorException(Exception):
    def __init__(self):
        pass

@singleton
class mywindow(QtWidgets.QMainWindow,Ui_MainWindow):
    #successfully_connect = 1

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
    def click_guide_b(self):
        #print("打开引导界面")
        g_ui.show()
    def click_test_b(self):
        #print("打开测试界面")
        t_ui.t_init()
        t_ui.show()
    def closeEvent(self,event):
        functions_class.close_monkeyrunner()
        #print("close window")
        event.accept()
        #super(mywindow,self).closeEvent(event)

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
    max_x = 1024
    max_y = 768
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_TestWindow.__init__(self)
        self.setupUi(self)
    def set_rate(self,x,y):
        global x_rate
        x_rate = x
        global y_rate
        y_rate = y
        self.max_x = x
        self.max_y = y
    def click_in_index_b(self):
        #print("点击 输入app参数 按钮")
        i_d_ui.show()
    def click_add_test(self):
        #print("点击 选择测试类型 按钮")
      #  a_t_ui.now_point_num.hide()
        a_t_ui.v_m_touch_point_num.setProperty("value", 1)
        a_t_ui.v_m_touch_point_num.show()
        a_t_ui.confirmMultiTouchTestButton.show()

        a_t_ui.now_drag_num.hide()
        a_t_ui.v_m_drag_num.setProperty("value", 1)
        a_t_ui.v_m_drag_num.show()
        #a_t_ui.confirm_m_drag_n_b.show()
        a_t_ui.confirmMultiDragButton.show()
        a_t_ui.show()

    def t_init(self):
        t_ui.loadButton.show()
        t_ui.saveButton.show()
        t_ui.startButton.show()
        t_ui.pauseButton.hide()
        t_ui.resumeButton.hide()
        t_ui.stopButton.hide()
        t_ui.InputAssignmentButton.setEnabled(False)
        t_ui.chooseTypeButton.setEnabled(False)

    '''点击连接设备按钮'''
    def click_connect_b(self):
        #print("点击连接设备按钮")
        '''
            todo:实际运行时把注释删掉
        '''
        self.connectDeviceButton.setText('连接中...')
        self.connectDeviceButton.setEnabled(False)
        successfully_connect = functions_class.connect()
        #if(successfully_connect == True):      
        self.InputAssignmentButton.setEnabled(True)
        self.connectDeviceButton.setText("重新连接")

    def click_load_b(self):
        print("点击读档按钮")
    def click_save_b(self):
        print("点击存档按钮")
    def click_start_b(self):
        functions_class.start()
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
        try:
            x_rate_value = int(self.xPositionValue.text())
            y_rate_value = int(self.yPositionValue.text())
            test_window = t_window()
            test_window.set_rate(x_rate_value,y_rate_value)
            if(i_d_ui.has_finished == 0):
                test_window.InputAssignmentButton.setText('重新输入')
                test_window.chooseTypeButton.setEnabled(True)

            self.has_finished = 1
        except ValueError:
            if(self.xPositionValue.text() == '' or self.yPositionValue.text() == ''):
                functions_class.error_message_prompt(self,empty_error_code)
            else:
                functions_class.error_message_prompt(self,number_error_code)
        #reset_test_window()
        test_window = t_window()
        test_window.loadButton.setEnabled(True)
        test_window.saveButton.setEnabled(True)
        test_window.startButton.setEnabled(True)
        self.close()
        #print("参数信息输入完毕")
@singleton
class add_test(QtWidgets.QDialog,Ui_Add_test):
    points_list = []#初始化
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        Ui_Add_test.__init__(self)
        self.setupUi(self)
        #self.currentQueueList.clear()
        self.currentQueueList.setDragDropMode(self.currentQueueList.InternalMove)
        self.pointSelectComboBox.currentIndexChanged.connect(self.change_final_point_button_text)
    def delete_current_row(self):
        row = a_t_ui.currentQueueList.currentRow()
        index = self.currentQueueList.currentIndex()
        #print("删除第"+str(row+1)+"条测试")
        functions_class.delete_from_queue(index + 1)
        a_t_ui.currentQueueList.takeItem(row)
    #多点点击测试
    '''多点点击测试选项卡下的
        确定并加输入下一点 按钮
        先读取当前输入框内的内容
        按下按钮后 左边comboBox变为下一个点 然后继续输入
        如果已经是最后一个点 按钮文本变为"确定"
    '''
    def mul_touch_next_p(self):
        '''global now_point_index #注意
        if(now_point_index < int(a_t_ui.now_point_num.text())):
            now_point_index = now_point_index + 1
            text = "第"+str(now_point_index)+"点坐标:(X,Y)"
            a_t_ui.m_touch_pos.setText(text)'''
        try:
            this_x = int(self.v_m_touch_pos_x.text())
            this_y = int(self.v_m_touch_pos_y.text())
            if(this_x > x_rate or this_y > y_rate):
                raise rangeErrorException()
            new_point = (this_x,this_y)
            point_index = self.pointSelectComboBox.currentIndex() 
            self.points_list[point_index] = new_point
            current_point = self.pointSelectComboBox.currentText()
            if('（未设置）' in current_point):
                current_point_text = current_point.replace('（未设置）',str(new_point))
                self.pointSelectComboBox.setItemText(point_index,current_point_text)
            else:
                current_point_text = '第%d点'%(point_index+1) + str(new_point)
                self.pointSelectComboBox.setItemText(point_index,current_point_text)
            if(point_index != self.pointSelectComboBox.count() - 1):
                self.pointSelectComboBox.setCurrentIndex(point_index + 1)
            self.v_m_touch_pos_x.clear()
            self.v_m_touch_pos_y.clear()
        except ValueError:
            if(self.v_m_touch_pos_x.text() == '' or self.v_m_touch_pos_y.text() == ''):
                functions_class.error_message_prompt(self,empty_error_code)
            else:
                functions_class.error_message_prompt(self,number_error_code)
        except rangeErrorException:
            functions_class.error_message_prompt(self,range_error_code)

        '''
            多点测试的确定按钮
            按下以后 按钮文本变为“修改”
            同时左侧的文本框不可选定 直到再按下按钮
            设置点个数以后 下一行的comboBox里出现与个数相同的item 同时右边的按钮变为enbale
        '''
    def confirm_m_touch_p_num(self):
        #a_t_ui.now_point_num.setText(a_t_ui.v_m_touch_point_num.text())
        if(self.confirmMultiTouchTestButton.text() == '确定'):
            self.multiTouchNextPointButton.setEnabled(True)
            self.v_m_touch_point_num.setEnabled(False)
            self.confirmMultiTouchTestButton.setText('修改')
            self.pointSelectComboBox.clear()
            point_num = int(self.v_m_touch_point_num.text())
            self.points_list = [(-1,-1) for p in range(point_num)]
            for i in range(1,point_num + 1):
                self.pointSelectComboBox.addItem("第%d点（未设置）"%i)
        else:
            self.confirmMultiTouchTestButton.setText('确定')
            self.v_m_touch_point_num.setEnabled(True)
    def reset_point_no(self):
        '''global now_point_index
        a_t_ui.m_touch_pos.setText("第1点坐标:(X,Y)")
        now_point_index = 1
        print("清除参数")'''
        pass
    #多端滑动测试
    def mul_drag_next_l(self):
        global now_drag_index #注意
        if(now_drag_index < int(a_t_ui.now_drag_num.text())):
            now_drag_index = now_drag_index + 1
            text1 = "第" + str(now_drag_index)+"次滑动起点坐标:(X,Y)"
            text2 = "第" + str(now_drag_index) + "次滑动终点坐标:(X,Y)"
            a_t_ui.m_drag_start_p.setText(text1)
            a_t_ui.m_drag_end_p.setText(text2)
    def change_final_point_button_text(self):
        if(self.pointSelectComboBox.count() == 0):
            return
        if(self.pointSelectComboBox.currentIndex() == self.pointSelectComboBox.count() - 1):
            self.multiTouchNextPointButton.setText('确定')
        else:
            self.multiTouchNextPointButton.setText('确定并输入下一个点')
    def confirm_m_drag_num(self):
        a_t_ui.now_drag_num.setText(a_t_ui.v_m_drag_num.text())

    def reset_drag_no(self):
        global now_drag_index
        a_t_ui.m_drag_start_p.setText("第1次滑动起点坐标:(X,Y)")
        a_t_ui.m_drag_end_p.setText("第1次滑动终点坐标:(X,Y)")
        now_drag_index = 1

    def add_new_test_b(self):
        if(a_t_ui.tabWidget.currentIndex() == 0):
            #print("加入单点点击测试")
            functions_class.add_single_point_test()
        elif(a_t_ui.tabWidget.currentIndex() == 1):
            #print("加入单点长按测试")
            functions_class.add_single_long_touch_test()
        elif (a_t_ui.tabWidget.currentIndex() == 2):
            functions_class.multi_touch_test()
            #print("加入多点点击测试")
        elif (a_t_ui.tabWidget.currentIndex() == 3):
            functions_class.random_touch_test()
            #print("加入随机点击测试")
        elif (a_t_ui.tabWidget.currentIndex() == 4):
            functions_class.drag_test()
            #print("加入单线滑动测试")
        elif (a_t_ui.tabWidget.currentIndex() == 5):
            print("加入多线滑动测试")
        elif (a_t_ui.tabWidget.currentIndex() == 6):
            functions_class.random_drag_test()
            #print("加入随机滑动测试")
        elif (a_t_ui.tabWidget.currentIndex() == 7):
            functions_class.long_touch_drag_test()
            #print("加入长按滑动测试")
    def update_queue_lists(self):
        test_window = t_window()
        queue_items = [self.currentQueueList.item(i).text() for i in range(self.currentQueueList.count())]
        #test_window.queueList.setFocus(True)
        test_window.tabWidget.setCurrentIndex(0)
        test_window.queueList.addItems(queue_items)
    def fin_queue_edit(self):
        print("队列输入完毕")
        self.update_queue_lists()
        self.currentQueueList.clear()
        a_t_ui.close()

if __name__ == '__main__':
    global functions_class

    app = QApplication(sys.argv)
    ui = mywindow()
    g_ui = g_window()
    t_ui = t_window()
    i_d_ui = in_dev_infor()
    a_t_ui = add_test()
    functions_class = func(t_ui,a_t_ui)
    ui.show()
    #print('close main window')
    sys.exit(app.exec_())
# queueList
# reportList