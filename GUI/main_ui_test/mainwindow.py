import sys
import os
new_path = sys.path[0] + '\\monkeys'
sys.path.insert(1,new_path)
import threading
import time
import webbrowser
from Test_Ui_Functions import TestUiFunctionsClass as func
from Test_Ui_Functions import rangeErrorException
from ui_main import Ui_MainWindow
from guide_ui import Ui_GuideWindow
from test_ui_d.test_ui import Ui_TestWindow
from test_ui_d.in_device_infor import Ui_In_dev_infor
from test_ui_d.add_test_ui import Ui_Add_test
from PyQt5.QtWidgets import QApplication, QMainWindow,QMessageBox,QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from functools import wraps
from datetime import datetime

now_point_index = 1
now_drag_index = 1
nowp = 1
empty_error_code = 0
number_error_code = 1
range_error_code = 2
resolution_ration_error_code = 3
something_else_error_code = 4
have_not_connect_error_code = 5
not_successful_connected_error_code = 6
lock = QtCore.QMutex()
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
begin_connect_time = None
test_count = 0
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
class GetCurrentTestThread(QtCore.QThread):
    before_count = -1
    def __init__(self,t,parent = None):
        super(GetCurrentTestThread,self).__init__(parent)
        self.t = t
        #self.finished.connect(get_current_test)
    def run(self):
        while(True):
            lock.lock()
            after_count = self.t.get_current_test()
            if(after_count != self.before_count):
                self.t.set_current_test(after_count)
                self.before_count = after_count
            lock.unlock()
            
class TimeWaitThread(QtCore.QThread):
    def __init__(self,t,parent = None):
        super(TimeWaitThread,self).__init__(parent)
        self.finished.connect(t.wait_about)
    def run(self):
        self.sleep(10)
class WaitConnect(QtCore.QThread):
    def __init__(self, t, parent=None):
        super(WaitConnect, self).__init__(parent)
        self.t = t
        self.finished.connect(t.after_connect)
    def run(self):
        self.t.successfully_connect = functions_class.connect()


class WaitMonkeyRunnerStart(QtCore.QThread):
    test_window = None
    def __init__(self,t,parent = None):
        super(WaitMonkeyRunnerStart,self).__init__(parent)
        self.finished.connect(t.wait_monkey)
    def run(self):
        self.sleep(6)
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

    def click_feedback_b(self):
        webbrowser.open("https://link.jiandaoyun.com/f/5cb9215b196c2d1d50253635")
    def closeEvent(self,event):
        functions_class.close_monkeyrunner()
        functions_class.close_model()
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
            nowp = 9
        else:
            nowp = nowp-1
        #g_ui.guidePictures.setPixmap(QtGui.QPixmap(":/gp/"+str(nowp)+".png"))
        g_ui.guidePictures.setStyleSheet("border-image: url(:/gp/"+str(nowp)+".png);")
        if (nowp == 1):
            g_ui.textEdit.setText("主界面如上图所示。")
        elif(nowp == 2):
            g_ui.textEdit.setText("打开测试界面，请先等待后台程序启动。然后点击连接按钮。")
        elif(nowp == 3):
            g_ui.textEdit.setText("点击“输入要测试的APP参数”按钮，输入各项参数。")
        elif (nowp == 4):
            g_ui.textEdit.setText("点击“选择测试”按钮，例如图中“单点点击测试”。")
        elif (nowp == 5):
            g_ui.textEdit.setText("这里以“完全随机”测试为例，点击“加入测试队列”按钮，确定测试队列后点击“测试队列创建完成”按钮")
        elif (nowp == 6):
            g_ui.textEdit.setText("返回到测试界面")
        elif (nowp == 7):
            g_ui.textEdit.setText("点击“开始测试”按钮，可以看到测试报告栏里已开始记录测试的报告")
        elif (nowp == 8):
            g_ui.textEdit.setText("如图，检测到异常！")
        elif (nowp == 9):
            g_ui.textEdit.setText("续上图，已在exception_1.txt文件中记录了本次测试队列。")
    def click_right_b(self):
        print("引导界面图片右划")
        global nowp
        if (nowp == 9):
            nowp = 1
        else:
            nowp = nowp + 1
        #g_ui.guidePictures.setPixmap(QtGui.QPixmap(":/gp/" + str(nowp) + ".png"))
        g_ui.guidePictures.setStyleSheet("border-image: url(:/gp/"+str(nowp)+".png);")
        if (nowp == 1):
            g_ui.textEdit.setText("主界面如上图所示。")
        elif(nowp == 2):
            g_ui.textEdit.setText("打开测试界面，请先等待后台程序启动。然后点击连接按钮。")
        elif(nowp == 3):
            g_ui.textEdit.setText("点击“输入要测试的APP参数”按钮，输入各项参数。")
        elif (nowp == 4):
            g_ui.textEdit.setText("点击“选择测试”按钮，例如图中“单点点击测试”。")
        elif (nowp == 5):
            g_ui.textEdit.setText("这里以“完全随机”测试为例，点击“加入测试队列”按钮，确定测试队列后点击“测试队列创建完成”按钮")
        elif (nowp == 6):
            g_ui.textEdit.setText("返回到测试界面")
        elif (nowp == 7):
            g_ui.textEdit.setText("点击“开始测试”按钮，可以看到测试报告栏里已开始记录测试的报告")
        elif (nowp == 8):
            g_ui.textEdit.setText("如图，检测到异常！")
        elif (nowp == 9):
            g_ui.textEdit.setText("续上图，已在exception_1.txt文件中记录了本次测试队列。")
@singleton
class t_window(QtWidgets.QMainWindow,Ui_TestWindow):
    max_x = 1024
    max_y = 768
    current_test = 0
    connect_thread = None
    successfully_connect = None
    time_counter_thread = None
    wait_monkey_thread = None
    rate_tuple = None
    #begin_connect_time = None
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_TestWindow.__init__(self)
        self.setupUi(self)
        self.connectDeviceButton.setEnabled(False)
        self.connectDeviceButton.setText('等待相关部件启动')
        self.wait_monkey_thread = WaitMonkeyRunnerStart(self)
        self.wait_monkey_thread.start()
        self.testButton.clicked.connect(self.to_test)
        self.queueList.itemClicked.connect(self.set_not_selectable)
        #self.queueList.itemChanged.connect(self.set_not_selectable)
        #self.queueList.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents,True)
        #self.queueList.itemChanged.connect(self.not_empty_set)
    def get_current_test(self):
        '''获取当前test的序号'''
        return test_count
    def set_not_selectable(self,item):
        current_flag = item.flags()
        item.setFlags(current_flag & (~QtCore.Qt.ItemIsSelectable))
    def set_current_test(self,counter):
        #self.queueList.set
        self.queueList.setCurrentRow(counter)
        try:
            if(counter > self.queueList.count()):
                raise AttributeError
            self.queueList.item(counter).setBackground(QtGui.QColor(16,109,156))
            if(counter > 0):
                self.queueList.item(counter - 1).setBackground(QtGui.QColor(255,255,255))
        except AttributeError:
            pass
        #self.queueList.setCurrentIndex()
        #self.current_test += 1
    def to_test(self):
        global test_count
        test_count += 1
        #self.set_current_test()
    def wait_monkey(self):
        self.connectDeviceButton.setEnabled(True)
        self.connectDeviceButton.setText('连接设备')
    def closeEvent(self,e):
        if(self.connectDeviceButton.text() == '连接中...'):
            e.ignore()
    def after_connect(self):
        if (isinstance(self.successfully_connect, tuple)):
            self.max_x = int(self.successfully_connect[0])
            self.max_y = int(self.successfully_connect[1])
            # self.rate_tuple = self.su
            self.InputAssignmentButton.setEnabled(True)
            self.connectDeviceButton.setEnabled(False)
            self.loadButton.setEnabled(True)
            self.connectDeviceButton.setText('已成功连接')
            # self.connectDeviceButton.setText("重新连接")
        elif (self.successfully_connect == False):
            self.connectDeviceButton.setEnabled(True)
            # self.successfully_connect = None
            self.connectDeviceButton.setText('重新连接')
    def wait_about(self):
        if(self.successfully_connect == None):
            QMessageBox.about(self,'提示','连接时间过长，请检查您的环境配置和连接状态')
            self.connectDeviceButton.setEnabled(True)
            self.successfully_connect = None
            self.connectDeviceButton.setText('重新连接')

    def set_rate(self,x,y):
        global x_rate
        x_rate = x
        global y_rate
        y_rate = y
        self.max_x = x
        self.max_y = y
    def not_empty_set(self):
        if(self.queueList.count() == 0):
            self.saveButton.setEnabled(False)
            self.loadButton.setEnabled(True)
        else:
            self.loadButton.setEnabled(False)
            self.saveButton.setEnabled(True)
            self.startButton.setEnabled(True)
    def click_in_index_b(self):
        i_d_window = in_dev_infor()
        '''i_d_window.xPositionValue.setPlaceholderText('手机分辨率:'+ str(self.max_x))
        i_d_window.yPositionValue.setPlaceholderText('手机分辨率:'+ str(self.max_y))'''
        #print("点击 输入app参数 按钮")
        i_d_ui.show()
    def click_add_test(self):
        #print("点击 选择测试类型 按钮")
      #  a_t_ui.now_point_num.hide()
        a_t_ui.v_m_touch_point_num.setProperty("value", 1)
        a_t_ui.v_m_touch_point_num.show()
        a_t_ui.confirmMultiTouchTestButton.show()

        '''a_t_ui.now_drag_num.hide()
        a_t_ui.v_m_drag_num.setProperty("value", 1)
        a_t_ui.v_m_drag_num.show()'''
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
        #t_ui.InputAssignmentButton.setEnabled(True)
        
        t_ui.chooseTypeButton.setEnabled(False)
        '''
            if debug
        '''
        #t_ui.chooseTypeButton.setEnabled(True)
    def thread_waitingfor_connect(self):
        while(self.successfully_connect == None ):
            self.successfully_connect = functions_class.connect()
            if(isinstance(self.successfully_connect,tuple)):
                test_window = t_window()
                self.max_x = int(self.successfully_connect[0])
                self.max_y = int(self.successfully_connect[1])
                #self.rate_tuple = self.su
                self.InputAssignmentButton.setEnabled(True)
                self.connectDeviceButton.setEnabled(False)
                self.loadButton.setEnabled(True)
                self.connectDeviceButton.setText('已成功连接')
                break
                #self.connectDeviceButton.setText("重新连接")
            elif(self.successfully_connect == False):
                self.connectDeviceButton.setEnabled(True)
                #self.successfully_connect = None
                self.connectDeviceButton.setText('重新连接')
                break
       

    '''点击连接设备按钮'''
    def click_connect_b(self):
        #print("点击连接设备按钮")

        self.connectDeviceButton.setText('连接中...')
        self.connectDeviceButton.setEnabled(False)

        '''self.connect_thread = threading.Thread(target = self.thread_waitingfor_connect)'''
        self.connect_thread = WaitConnect(self)
        self.connect_thread.start()

        self.time_counter_thread = TimeWaitThread(self)
        self.time_counter_thread.start()

        #elf.connectDeviceButton.setEnabled(()


    def click_load_b(self):
        test_window = t_window()
        load_file_name,_ = QFileDialog.getOpenFileName(self,'读档',os.getcwd() + '\\save','存档文件(*.save)')
        functions_class.load(load_file_name)
        if(test_window.queueList.count() == 0):
            test_window.saveButton.setEnabled(False)
            test_window.loadButton.setEnabled(True)
        else:
            test_window.loadButton.setEnabled(False)
            test_window.saveButton.setEnabled(True)
            test_window.startButton.setEnabled(True)
    '''"点击存档按钮"'''
    def click_save_b(self):
        #print("点击存档按钮")
        #file_set = QFileDialog.Options()
        save_file_name,_ = QFileDialog.getSaveFileName(self,"存档",os.getcwd() + "\\save","存档文件(*.save)")
        functions_class.save(save_file_name)
    def click_start_b(self):
        self.chooseTypeButton.setEnabled((False))
        functions_class.start()
        current_test_thread = GetCurrentTestThread(self)
        current_test_thread.start()
        print("点击开始按钮")
    def click_pause_b(self):
        self.pauseButton.setEnabled(False)
        functions_class.pause()
        self.resumeButton.setEnabled(True)
        #functions_class.test_found_exception()
        print("点击暂停按钮")
    def click_resume_b(self):
        self.resumeButton.setEnabled(False)
        functions_class.resume()
        self.pauseButton.setEnabled(True)

        print("点击继续按钮")
    def click_stop_b(self):
        if(self.stopButton.text() == '退出'):
            main_window = mywindow()
            main_window.close()
            self.close()
        self.chooseTypeButton.setEnabled((True))
        self.loadButton.setEnabled(True)
        functions_class.stop()
        print("点击终止按钮")
@singleton
class in_dev_infor(QtWidgets.QDialog,Ui_In_dev_infor):
    has_finished = 0
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        Ui_In_dev_infor.__init__(self)
        self.setupUi(self)
    def click_fin_b(self):
        '''try:
            x_rate_value = int(self.xPositionValue.text())
            y_rate_value = int(self.yPositionValue.text())
            if not functions_class.judge_input_ration(x_rate_value,y_rate_value):
                raise rangeErrorException
            functions_class.set_monkey_ration(x_rate_value,y_rate_value)
            test_window = t_window()
            test_window.set_rate(x_rate_value,y_rate_value)
            if(self.packageNameValue.text() != '' and self.PackageActivityName.text() != ''):
                functions_class.open_app(self.packageNameValue.text(),self.PackageActivityName.text())
            if(i_d_ui.has_finished == 0):
                test_window.InputAssignmentButton.setText('重新输入')
                test_window.chooseTypeButton.setEnabled(True)

            self.has_finished = 1
        except ValueError:
            functions_class.error_message_prompt(self,empty_error_code)
        #reset_test_window()
        except rangeErrorException:
            functions_class.error_message_prompt(self,functions_class.logic_error_code,"分辨率超出手机本身分辨率：")'''
        if(self.packageNameValue.text() != '' and self.PackageActivityName.text() != ''):
                functions_class.open_app(self.packageNameValue.text(),self.PackageActivityName.text())
        self.has_finished = 1
        test_window = t_window()
        test_window.chooseTypeButton.setEnabled(True)
        test_window.loadButton.setEnabled(True)
        test_window.InputAssignmentButton.setEnabled(False)
        self.close()
        #print("参数信息输入完毕")
@singleton
class add_test(QtWidgets.QDialog,Ui_Add_test):
    points_list_touch =None#初始化
    points_list_drag = None
    
    def __init__(self):

        QtWidgets.QDialog.__init__(self)

        Ui_Add_test.__init__(self)

        self.setupUi(self)
        #self.currentQueueList.clear()
        self.setFixedSize(self.width(),self.height())
        self.currentQueueList.setDragDropMode(self.currentQueueList.InternalMove)
        self.pointSelectComboBox.currentIndexChanged.connect(self.change_final_point_button_text)
        self.dragSelectComboBox.currentIndexChanged.connect(self.change_multi_drag_comboxBox)
        self.currentQueueList.clear()

    def delete_current_row(self):
        if(self.currentQueueList.count() == 0):
            return
        row = a_t_ui.currentQueueList.currentRow()
        if(row == -1):
            return
        #index = self.currentQueueList.currentIndex()
        print("删除第"+str(row+1)+"条测试")
        functions_class.delete_from_queue(row + 1)
        a_t_ui.currentQueueList.takeItem(row)
    #多点点击测试
    '''多点点击测试选项卡下的
        确定并加输入下一点 按钮
        先读取当前输入框内的内容
        按下按钮后 左边comboBox变为下一个点 然后继续输入
        如果已经是最后一个点 按钮文本变为"确定"
    '''
    def mul_touch_next_p(self):
        functions_class.mul_touch_next_p()
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
            self.points_list_touch = [(-1,-1) for p in range(point_num)]
            for i in range(1,point_num + 1):
                self.pointSelectComboBox.addItem("第%d点（未设置）"%i)
        else:
            self.confirmMultiTouchTestButton.setText('确定')
            self.v_m_touch_point_num.setEnabled(True)
    def reset_point_no(self):
        self.pointSelectComboBox.clear()
        self.pointSelectComboBox.addItem('未确认点的个数')
        self.confirmMultiTouchTestButton.setText('确定')
        self.multiTouchNextPointButton.setText('确定并输入下一个点')
        self.v_m_touch_point_num.setEnabled(True)
        self.multiTouchNextPointButton.setEnabled(False)

    #多端滑动测试

    '''多点点击测试选项卡下的
        确定并加输入下一点 按钮
        先读取当前输入框内的内容
        按下按钮后 左边comboBox变为下一个点 然后继续输入
        如果已经是最后一个点 按钮文本变为"确定"
    '''
    def mul_drag_next_l(self):

        '''global now_drag_index #注意
        if(now_drag_index < int(a_t_ui.now_drag_num.text())):
            now_drag_index = now_drag_index + 1
            text1 = "第" + str(now_drag_index)+"次滑动起点坐标:(X,Y)"
            text2 = "第" + str(now_drag_index) + "次滑动终点坐标:(X,Y)"
            a_t_ui.m_drag_start_p.setText(text1)
            a_t_ui.m_drag_end_p.setText(text2)'''
        functions_class.mul_drag_next_P()
    def change_final_point_button_text(self):
        if(self.pointSelectComboBox.count() == 0 or self.pointSelectComboBox.currentText == '未确认点的个数'):
            return
        if(self.pointSelectComboBox.currentIndex() == self.pointSelectComboBox.count() - 1):
            self.multiTouchNextPointButton.setText('确定')
        else:
            self.multiTouchNextPointButton.setText('确定并输入下一个点')
    def change_multi_drag_comboxBox(self):
        if(self.dragSelectComboBox.count() == 0 or self.dragSelectComboBox.currentText() == '待输入'):
            return
        if(not '待输入' in self.dragSelectComboBox.currentText()):
            points = self.points_list_drag
            index = self.dragSelectComboBox.currentIndex()
            self.v_m_drag_start_p_x.setText(str(points[index][0][0]))
            self.v_m_drag_start_p_y.setText(str(points[index][0][1]))
            self.v_m_drag_end_p_x.setText(str(points[index][1][0]))
            self.v_m_drag_end_p_y.setText(str(points[index][1][1]))
        else:
            self.v_m_drag_start_p_x.clear()
            self.v_m_drag_start_p_y.clear()
            self.v_m_drag_end_p_x.clear()
            self.v_m_drag_end_p_y.clear()
        if(self.dragSelectComboBox.currentIndex() == self.dragSelectComboBox.count() - 1):
            self.multiDragNextButton.setText('确定')
        else:
            self.multiDragNextButton.setText('确定并输入下次滑动')
    '''
        点击多线滑动的确定按钮
        和多点点击类似
        使左侧不可修改
    '''
    def confirm_m_drag_num(self):
        #a_t_ui.now_drag_num.setText(a_t_ui.v_m_drag_num.text())
        if(self.confirmMultiDragButton.text() == '确定'):
            self.confirmMultiDragButton.setEnabled(True)
            self.v_m_drag_num.setEnabled(False)
            self.confirmMultiDragButton.setText('修改')
            self.dragSelectComboBox.clear()
            drag_num = int(self.v_m_drag_num.text())
            self.points_list_drag = [((-1,-1),(-1,-1)) for p in range(drag_num)]
            for i in range(1,drag_num + 1):
                self.dragSelectComboBox.addItem("待输入滑动%d"%i)
            self.multiDragNextButton.setEnabled(True)
        else:
            self.confirmMultiDragButton.setText('确定')
            self.v_m_drag_num.setEnabled(True)
    def reset_drag_no(self):
        self.dragSelectComboBox.clear()
        self.dragSelectComboBox.addItem('待输入')
        self.multiDragNextButton.setText('确定并输入下一个点')

        self.confirmMultiDragButton.setText('确定')
        self.v_m_drag_num.setEnabled(True)
        self.multiDragNextButton.setEnabled(False)

    def add_new_test_b(self):
        test_w = t_window()
        test_w.InputAssignmentButton.setEnabled(False)
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
            functions_class.multi_drag_test()
            #print("加入多线滑动测试")
        elif (a_t_ui.tabWidget.currentIndex() == 6):
            functions_class.random_drag_test()
            #print("加入随机滑动测试")
        elif (a_t_ui.tabWidget.currentIndex() == 7):
            functions_class.long_touch_drag_test()
            #print("加入长按滑动测试")
        elif(self.tabWidget.currentIndex() == 8):
            functions_class.all_random_test()
    def update_queue_lists(self):
        test_window = t_window()
        queue_items = [self.currentQueueList.item(i).text() for i in range(self.currentQueueList.count())]
        #test_window.queueList.setFocus(True)
        test_window.tabWidget.setCurrentIndex(0)
        test_window.queueList.addItems(queue_items)
    def fin_queue_edit(self):
        test_window = t_window()
        #print("队列输入完毕")
        self.update_queue_lists()
        if(test_window.queueList.count() == 0):
            test_window.saveButton.setEnabled(False)
            test_window.loadButton.setEnabled(True)
        else:
            test_window.loadButton.setEnabled(False)
            test_window.saveButton.setEnabled(True)
            test_window.startButton.setEnabled(True)
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
    functions_class.read_exception()
    '''测试用 正式版去掉'''
    t_ui.InputAssignmentButton.setEnabled(True)
    current_test_thread = GetCurrentTestThread(t_ui)
    current_test_thread.start()
    '''以上'''
    ui.show()
    sys.exit(app.exec_())
# queueList
# reportList