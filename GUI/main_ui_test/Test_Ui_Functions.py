import sys
import os
import socket
import threading
import os
import _thread as thread
import Monkey
from test_queue import test_thread
from NewModel import SimpleModel
from functools import wraps
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QDockWidget, QListWidget
from PyQt5.QtGui import *
def disp_func_msg(func):
    @wraps(func)
    def print_name(*args,**kw):
        print("running test_ui_function:{}".format(func.__name__))
        return func(*args,**kw)
    return print_name
class rangeErrorException(Exception):
    def __init__(self):
        pass
class pointNotEnoughException(Exception):
    index = -1
    def __init__(self,index):
        self.index = index
class TestUiFunctionsClass(object):
    path = os.path.split(os.path.realpath(sys.argv[0]))[0]
    bool_ever_click_connect_button = 0
    bool_is_device_connected_successful = 0
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
    max_long_touch_during_time = 9.9
    max_loop_times = 100
    min_loop_times = 1
    max_pos_x = 1000
    max_pos_y = 1000
    empty_error_code = 0
    number_error_code = 0
    logic_error_code = 2
    not_enough_code = 3
    load_error_code = 4
    have_not_connect_error_code = 5
    not_successful_connected_error_code = 6
    exception_count = 0
    #connect_waiting_timer = None
    add_test_form = None
    test_form = None
    exception_raw_name = path + '\\exception.txt'
    exception_name = ''
    log_name = path + '\\log.txt'
    log_lines = []
    log_timer = None
    bool_successful_read_log = 0
    end_log_monitor = 0
    model_thread = None
    def __init__(self,test_form,add_test_form):
        #self.thread_start()
        self.test_form = test_form
        self.add_test_form = add_test_form
    def add_text(self,text,widget):
        widget.addItem(text)
    def close_monkeyrunner(self):
        Monkey.close()
    def close_model(self):
        if(self.model_thread != None):
            self.model_thread.quit_flag = 1
    #一些常数和错误处理#
    def read_exception(self):
        while(1):
            try:
                new_e_path = self.path + '\\log\\'+ 'exception_' + str(self.exception_count) + '.txt'

                #print(new_e_path)
                f_t = open( new_e_path)
                self.exception_count += 1
                f_t.close()
            except IOError:
                break
    def error_message_prompt(self,widget,error_code,extra_msg = ""):
        empty_error_code = 0
        number_error_code = 0
        logic_error_code = 2
        resolution_ration_error_code = 3
        something_else_error_code = 4
        have_not_connect_error_code = 5
        not_successful_connected_error_code = 6
        if(error_code == 0):#错误信息:空输入
           QMessageBox.about(widget,'输入错误',extra_msg + '输入不能为空或其他非法字符，请输入半角阿拉伯正数，具体输入规范可参考“帮助”按钮')
        elif(error_code == 1):#错误信息：输入的应该是数字却不是
           QMessageBox.about(widget,'输入错误','请输入半角阿拉伯正数，具体输入规范可参考“帮助”按钮')
        elif(error_code == 2):
           QMessageBox.about(widget,'输入错误',extra_msg + '请输入不要超过限定范围，具体输入范围可参考“帮助”按钮')
        elif(error_code == 3):
           QMessageBox.about(widget,'输入错误','缺少第%s个点的数据，请补充' %extra_msg)
        elif(error_code == 4):
           QMessageBox.about(widget,'读档错误','读取存档失败，请稍后重试')
        elif(error_code == have_not_connect_error_code):
           QMessageBox.about(widget,'提示','请先连接设备！')
        elif(error_code == not_successful_connected_error_code):
           QMessageBox.about(widget,'连接错误','还未成功连接设备')
    #常数和错误处理结束#
    def runMonkeyServer(self,lock):
    ##!!!!!!!!!!!!!!!!!!!!!!!!!!!!此位置改成MonkeyServer.py所在位置
        ret = os.system(r"monkeyrunner C:\Users\Lenovo\Desktop\Autotest-master\example\MonkeyServer.py")
        lock.release(self)
    def monkey_runner_initial(self):
        lock = thread.allocate_lock()
        lock.acquire()
        thread.start_new(runMonkeyServer,(lock,))
    @disp_func_msg
    def connect(self):
        self.add_text('waiting for connection\n',self.test_form.reportList)
        connect_successful = Monkey.connect()
        if(connect_successful != False):
            self.add_text('connection successful!\n',self.test_form.reportList)
        else:
            self.add_text('fail to connect your device,please check that if your device connect to computer successfully\n',self.test_form.reportList)
        return connect_successful
    @disp_func_msg
    def pause(self):
        #self.add_text('pausing...',self.test_form.reportList)
        Monkey.pause()
    @disp_func_msg
    def resume(self):
        #self.add_text('now resume',self.test_form.reportList)
        Monkey.resume()
    @disp_func_msg
    def stop(self):
        self.end_log_monitor = 1
        self.model_thread.quit_flag = 1
        Monkey.stop()
    @disp_func_msg
    def start(self):
        picture_file = os.path.join(os.getcwd(), 'screenshot')
        self.add_text('start!',self.test_form.reportList)

        self.model_thread = SimpleModel(picture_collection_path=picture_file, step_length=5, limit_range=100, time_interval=3)
        self.model_thread.start()

        self.log_timer = threading.Timer(0.01,self.log_monitor)
        self.log_timer.start()


        '''self.test_thread = test_thread()
        self.test_thread.start()'''
        '''if debug'''
        #self.read_exception()s
        Monkey.start()

    def range_inside(self,**arg):
        if(arg.get('x',1) > self.test_form.max_x) :
            return False,'坐标x(' + str(arg['x']) +'):'
        if  arg.get('y',1) > self.test_form.max_y :
            return False,'坐标y('+ str(arg['y']) +'):'
        if(arg.get('click_times',1)> self.max_click_times or arg.get('click_times',1) < self.min_click_times ):
            return False,'点击次数('+ str(arg['click_times']) +'):'
        if(arg.get('interval_time',1) > self.max_interval_time or arg.get('interval_time',1) < self.min_interval_time):
            return False,'间隔时间('+ str(arg['interval_time']) +'):'
        if(arg.get('loop_interval_time',1) > self.max_interval_time or arg.get('loop_interval_time',1) < self.min_interval_time):
            return False,'循环间隔时间('+ str(arg['loop_interval_time']) +'):'
        if(arg.get('during_time',1) > self.max_long_touch_during_time or arg.get('during_time',1) < self.min_drag_during_time):
            return False,'持续时间('+ str(arg['during_time']) +'):'
        if(arg.get('loop_times',1) > self.max_loop_times or arg.get('loop_times',1) < self.min_loop_times):
            return False,'循环遍数('+ str(arg['loop_time']) +'):'
        if(arg.get('drag_times',1) > self.max_drag_times_number or arg.get('drag_times',1) < self.min_drag_times_number):
            return False,'滑动次数('+ str(arg['drag_times']) +'):'
        return True,""
    def placeholder_to_text(self,*arg):
        if(isinstance(arg[0],list)):
            list_con = arg[0]
            for item in list_con:
                if(item.text() == ""):
                    item.setText(item.placeholderText())
        else:
            for item in arg:
                if(item.text() == ""):
                    item.setText(item.placeholderText())
    def add_single_point_test(self):
        extra_msg = ""
        try:
            x = int(self.add_test_form.v_touch_pos_x.text())
            y = int(self.add_test_form.v_touch_pos_y.text())
            self.placeholder_to_text(self.add_test_form.v_touch_num,self.add_test_form.v_touch_i_time)
            touch_number = int(self.add_test_form.v_touch_num.text())
            interval_time = float(self.add_test_form.v_touch_i_time.text())
            #print(self.test_form.max_x)
            in_range,extra_msg = self.range_inside(x = x,y = y,click_times = touch_number,interval_time = interval_time)
            if(not in_range):
                raise rangeErrorException()
            Monkey.touch(x,y,touch_number,interval_time)
            self.add_test_form.currentQueueList.addItem('单点点击测试: %s,%d次,间隔%fs' % (str((x,y)),touch_number,interval_time))
        except ValueError:
            self.error_message_prompt(self.add_test_form,self.empty_error_code,extra_msg)
        except rangeErrorException:
            self.error_message_prompt(self.add_test_form,self.logic_error_code,extra_msg)
    def add_single_long_touch_test(self):
        extra_msg = ""
        try:
            x = int(self.add_test_form.v_press_pos_x.text())
            y = int(self.add_test_form.v_press_pos_y.text())
            self.placeholder_to_text(self.add_test_form.v_press_time,self.add_test_form.v_press_num,self.add_test_form.v_press_i_time)
            during_time = float(self.add_test_form.v_press_time.text())
            touch_number = int(self.add_test_form.v_press_num.text())
            interval_time = float(self.add_test_form.v_press_i_time.text())
            #print(self.test_form.max_x)
            in_range,extra_msg = self.range_inside(x = x,y = y,during_time = during_time,click_times = touch_number,interval_time = interval_time)
            if(not in_range):
                raise rangeErrorException()
            Monkey.long_touch(x,y,touch_number,interval_time)
            self.add_test_form.currentQueueList.addItem('单点长按测试: %s,持续%ds,%d次,间隔%fs' %(str((x,y)),during_time,touch_number,interval_time))
        except ValueError:
            self.error_message_prompt(self.add_test_form,self.empty_error_code,extra_msg)
        except rangeErrorException:
            self.error_message_prompt(self.add_test_form,self.logic_error_code,extra_msg)
    def multi_touch_test(self):
        extra_msg = ""
        try:
            point_tuple = tuple(self.add_test_form.points_list_touch)
            if((-1,-1) in point_tuple):
                id = point_tuple.index((-1,-1))
                p_e = pointNotEnoughException(id+1)
                raise p_e
            self.placeholder_to_text(self.add_test_form.v_m_touch_i_time,self.add_test_form.v_m_touch_loop_num)
            #during_time = float(self.add_test_form.v_press_time.text())
            loop_number = int(self.add_test_form.v_m_touch_loop_num.text())
            interval_time = float(self.add_test_form.v_m_touch_i_time.text())
            loop_interval_time = float(self.add_test_form.v_m_touch_loop_i_time.text())
            in_range,extra_msg = self.range_inside(loop_times = loop_number,interval_time = interval_time,loop_interval_time = loop_interval_time)
            if(not in_range):
                raise rangeErrorException()
            Monkey.multi_touch(point_tuple,loop_number,interval_time,loop_interval_time)
            self.add_test_form.currentQueueList.addItem('多点顺序点击: 循环%d次,循环内点击间隔%f秒，循环间隔%f秒' %(loop_number,interval_time,loop_interval_time))
        except ValueError:
            self.error_message_prompt(self.add_test_form,self.empty_error_code,extra_msg)
        except rangeErrorException:
            self.error_message_prompt(self.add_test_form,self.logic_error_code,extra_msg)
        except pointNotEnoughException:
            self.error_message_prompt(self.add_test_form,self.not_enough_code,str(p_e.index))
    def set_monkey_ration(self,x,y):
        Monkey.set_resolution_ratio(x,y)
    def random_touch_test(self):
        extra_msg = ""
        point_list = None
        try:
            self.placeholder_to_text(self.add_test_form.v_r_touch_num,self.add_test_form.v_r_touch_i_time)
            if(self.add_test_form.v_r_touch_p1_x.text() == '' and self.add_test_form.v_r_touch_p1_x.text() == ''\
                and self.add_test_form.v_r_touch_p1_x.text() == '' and self.add_test_form.v_r_touch_p1_x.text() == ''):
                touch_number = int(self.add_test_form.v_r_touch_num.text())
                interval_time = float(self.add_test_form.v_r_touch_i_time.text())
                #没有x1y1 和x2y2的情况
                in_range,extra_msg = self.range_inside(click_times = touch_number,interval_time = interval_time)
                if(not in_range):
                    raise rangeErrorException()
            else:
                x1 = int(self.add_test_form.v_r_touch_p1_x.text())
                y1 = int(self.add_test_form.v_r_touch_p1_y.text())
                x2 = int(self.add_test_form.v_r_touch_p2_x.text())
                y2 = int(self.add_test_form.v_r_touch_p2_y.text())
                touch_number = int(self.add_test_form.v_r_touch_num.text())
                interval_time = float(self.add_test_form.v_r_touch_i_time.text())
                #有两个点坐标的情况
                in_range,extra_msg = self.range_inside(x = x1,y = y1,click_times = touch_number,interval_time = interval_time)
                if(not in_range):
                    raise rangeErrorException()
                in_range2,extra_msg =self.range_inside(x = x2,y = y2)
                if(not in_range2):
                    raise rangeErrorException()
                point_list = ((x1,y1),(x2,y2))
            Monkey.random_touch(point_list,touch_number,interval_time)
            self.add_test_form.currentQueueList.addItem('随机点击测试: 点击%d次,间隔%fs' %(touch_number,interval_time))
        except ValueError:
            self.error_message_prompt(self.add_test_form,self.empty_error_code,extra_msg)
        except rangeErrorException:
            self.error_message_prompt(self.add_test_form,self.logic_error_code,extra_msg)
    def drag_test(self):
        extra_msg = ""
        point_list = None
        try:
            self.placeholder_to_text(self.add_test_form.v_drag_num,self.add_test_form.v_drag_i_time)
            x1 = int(self.add_test_form.v_drag_p1_x.text())
            y1 = int(self.add_test_form.v_drag_p1_y.text())
            x2 = int(self.add_test_form.v_drag_p2_x.text())
            y2 = int(self.add_test_form.v_drag_p2_y.text())
            drag_number = int(self.add_test_form.v_drag_num.text())
            interval_time = float(self.add_test_form.v_drag_i_time.text())
            in_range,extra_msg = self.range_inside(x = x1,y = y1,drag_times = drag_number,interval_time = interval_time)
            if(not in_range):
                raise rangeErrorException()
            in_range2,extra_msg =self.range_inside(x = x2,y = y2)
            if(not in_range2):
                raise rangeErrorException()
            point_list = ((x1,y1),(x2,y2))
            Monkey.drag(point_list,drag_number,interval_time)
            self.add_test_form.currentQueueList.addItem('单线滑动测试: (%d,%d)到(%d,%d),点击%d次,间隔%fs' %(x1,y1,x2,y2,drag_number,interval_time))
        except ValueError:
            self.error_message_prompt(self.add_test_form,self.empty_error_code,extra_msg)
        except rangeErrorException:
            self.error_message_prompt(self.add_test_form,self.logic_error_code,extra_msg)
    def multi_drag_test(self):
        line_edits = [self.add_test_form.v_m_drag_loop_num,self.add_test_form.v_m_drag_i_time,\
                self.add_test_form.v_m_drag_time,self.add_test_form.v_m_drag_trip_i_time ]
        extra_msg = ""
        try:
            drag_tuple = tuple(self.add_test_form.points_list_drag)
            if( ((-1,-1),(-1,-1)) in drag_tuple):
                id = drag_tuple.index((-1,-1),(-1,-1))
                p_e = pointNotEnoughException(id + 1)
                raise p_e
            self.placeholder_to_text(line_edits)
            trip_number = int(line_edits[0].text())
            trip_interval_time = float(line_edits[1].text())
            drag_during_time = float(line_edits[2].text())
            drag_interval_time = float(line_edits[3].text())
            in_range,extra_msg = self.range_inside(loop_times = trip_number,interval_time = drag_interval_time,loop_interval_time = trip_interval_time,during_time = drag_during_time)
            if(not in_range):
                raise rangeErrorException()
            Monkey.multi_drag(drag_tuple,trip_number,drag_interval_time,drag_during_time,trip_interval_time)
            self.add_test_form.currentQueueList.addItem('多次顺序滑动: 循环%d次,循环内滑动间隔%f秒，滑动持续时间%f秒，循环间隔%f秒' %(trip_number,drag_interval_time,drag_during_time,trip_interval_time))
        except ValueError:
            self.error_message_prompt(self.add_test_form,self.empty_error_code,extra_msg)
        except rangeErrorException:
            self.error_message_prompt(self.add_test_form,self.logic_error_code,extra_msg)
        except pointNotEnoughException:
            self.error_message_prompt(self.add_test_form,self.not_enough_code,str(p_e.index))
    def random_drag_test(self):
        extra_msg = ""
        point_list = None
        try:
            self.placeholder_to_text(self.add_test_form.v_r_drag_num,self.add_test_form.v_r_drag_i_time,self.add_test_form.v_r_drag_time)
            if(self.add_test_form.v_r_drag_start_p_x.text() == '' and self.add_test_form.v_r_drag_start_p_y.text() == ''\
                and self.add_test_form.v_r_drag_end_p_x.text() == '' and self.add_test_form.v_r_drag_end_p_y.text() == ''):
                drag_number = int(self.add_test_form.v_r_drag_num.text())
                interval_time = float(self.add_test_form.v_r_drag_i_time.text())
                drag_during_time = float(self.add_test_form.v_r_drag_time.text())
                #没有x1y1 和x2y2的情况
                in_range,extra_msg = self.range_inside(drag_times = drag_number,interval_time = interval_time,during_time = drag_during_time)
                if(not in_range):
                    raise rangeErrorException()
            else:
                x1 = int(self.add_test_form.v_r_drag_start_p_x.text())
                y1 = int(self.add_test_form.v_r_drag_start_p_y.text())
                x2 = int(self.add_test_form.v_r_drag_end_p_x.text())
                y2 = int(self.add_test_form.v_r_drag_end_p_y.text())
                drag_number = int(self.add_test_form.v_r_drag_num.text())
                interval_time = float(self.add_test_form.v_r_drag_i_time.text())
                drag_during_time = float(self.add_test_form.v_r_drag_time.text())
                #没有x1y1 和x2y2的情况
                in_range,extra_msg = self.range_inside(x = x1,y = y1,drag_times = drag_number,interval_time = interval_time,during_time = drag_during_time)
                if(not in_range):
                    raise rangeErrorException()
                in_range2,extra_msg =self.range_inside(x = x2,y = y2)
                if(not in_range2):
                    raise rangeErrorException()
                point_list = ((x1,y1),(x2,y2))
            Monkey.random_drag(point_list,drag_number,interval_time,drag_during_time)
            self.add_test_form.currentQueueList.addItem('随机滑动测试: 滑动%d次,间隔%fs,滑动持续%fs' %(drag_number,interval_time,drag_during_time))
        except ValueError:
            self.error_message_prompt(self.add_test_form,self.empty_error_code,extra_msg)
        except rangeErrorException:
            self.error_message_prompt(self.add_test_form,self.logic_error_code,extra_msg)
    def test_found_exception(self):
        self.test_thread.found_exception = True
    def long_touch_drag_test(self):
        extra_msg = ""
        try:
            self.placeholder_to_text(self.add_test_form.v_press_drag_num,self.add_test_form.v_press_drag_p_time,\
                self.add_test_form.v_press_drag_p_time_2,self.add_test_form.v_press_drag_p_time_3)
            x1 = int(self.add_test_form.v_press_drag_start_p_x.text())
            y1 = int(self.add_test_form.v_press_drag_start_p_y.text())
            x2 = int(self.add_test_form.v_press_drag_end_p_x.text())
            y2 = int(self.add_test_form.v_press_drag_end_p_y.text())
            touch_number = int(self.add_test_form.v_press_drag_num.text())
            touch_time = float(self.add_test_form.v_press_drag_p_time.text())
            drag_during_time = float(self.add_test_form.v_press_drag_p_time_2.text())
            interval_time = float(self.add_test_form.v_press_drag_p_time_3.text())
            in_range,extra_msg = self.range_inside(x = x1,y = y1,click_times = touch_number,during_time =drag_during_time, interval_time = interval_time)
            if(not in_range):
                raise rangeErrorException()
            in_range2,extra_msg =self.range_inside(x = x2,y = y2,during_time = touch_time)
            if(not in_range2):
                raise rangeErrorException()
            point_list = ((x1,y1),(x2,y2))
            Monkey.touch_drag(point_list,touch_time,drag_during_time,touch_number,interval_time)
            self.add_test_form.currentQueueList.addItem('长按滑动测试: (%d,%d)到(%d,%d),长按持续%fs,滑动持续%fs,长按滑动点击%d次,两次间隔%fs' %(x1,y1,x2,y2,touch_time,drag_during_time,touch_number,interval_time))
        except ValueError:
            self.error_message_prompt(self.add_test_form,self.empty_error_code,extra_msg)
        except rangeErrorException:
            self.error_message_prompt(self.add_test_form,self.logic_error_code,extra_msg)
    def change_queue(self,src,dst):
        Monkey.change(src+1,dst+1)
    def delete_from_queue(self,index):
        Monkey.delete(index)
    def after_found(self):
        self.test_form.pauseButton.setEnabled(False)
        self.test_form.resumeButton.setEnabled(False)
        self.test_form.stopButton.setText('退出')
    def disp_report_information(self,nop,context):
        self.test_form.reportList.addItem(context)
    def log_monitor(self):
        if(self.end_log_monitor == 1):
            return
        log_name = self.log_name
        #read_log = self.read_log
        log_lines = self.log_lines
        self.exception_name = self.path + '\\log\\exception_' + str(self.exception_count)+'.txt'
        try:
            self.read_log = 1
            if(not self.bool_successful_read_log):
                self.file_log = open(log_name,'r')
                self.bool_successful_read_log = 1
            final_line = self.file_log.readline()
            if(final_line != '' ):
                if(len(log_lines) == 0 or  final_line != log_lines[-1]):
                    log_lines.append(final_line)
                    self.disp_report_information('end',final_line)
            #print(log_lines)
            #nonlocal label_2
            #label_2.config(text = content)
            #file_log.close()
            try:
                #print(self.exception_raw_name)
                if(self.model_thread.q.empty()):
                    raise IOError
                else:
                    print(self.model_thread.q.get())
                #if(self.model_thread.q.get() != 'found'):
                   # raise IOError

                #file_exception = open(self.exception_raw_name,'r')
                file_exception_log = open(self.exception_name,'a+')
                lines_count = len(log_lines)
                if(len(log_lines) == 0):
                    #print('no log file')
                    self.log_timer = threading.Timer(0.01,self.log_monitor)
                    self.log_timer.start()
                    return
                lines_to_be_written = []
                min_lines_error_log = min(10,lines_count)
                for i in range(lines_count - 1,lines_count - min_lines_error_log,-1):
                    lines_to_be_written.insert(0,log_lines[i])
                file_exception_log.writelines(lines_to_be_written)
                self.disp_report_information('end','\n出现异常！相关内容已经保存到log目录下' + self.exception_name + '\n测试已停止')
                self.exception_count += 1
                #self.test_form.click_stop_b()
                self.after_found()
                self.stop()
                self.file_log.close()
                file_exception_log.close()
            except IOError:
                self.log_timer = threading.Timer(0.01,self.log_monitor)
                self.log_timer.start()
        except IOError:
            if(self.read_log == 0):
                self.disp_report_information('end','暂未读取到日志文件')
                self.log_timer = threading.Timer(0.01, self.log_monitor)
                self.log_timer.start()

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
            this_x = int(self.add_test_form.v_m_touch_pos_x.text())
            this_y = int(self.add_test_form.v_m_touch_pos_y.text())
            in_range,error_msg = self.range_inside(x = this_x,y = this_y)
            if(not in_range):
                raise rangeErrorException()
            new_point = (this_x,this_y)
            point_index = self.add_test_form.pointSelectComboBox.currentIndex() 
            self.add_test_form.points_list_touch[point_index] = new_point
            current_point = self.add_test_form.pointSelectComboBox.currentText()
            if('（未设置）' in current_point):
                current_point_text = current_point.replace('（未设置）',str(new_point))
                self.add_test_form.pointSelectComboBox.setItemText(point_index,current_point_text)
            else:
                current_point_text = '第%d点'%(point_index+1) + str(new_point)
                self.add_test_form.pointSelectComboBox.setItemText(point_index,current_point_text)
            if(point_index != self.add_test_form.pointSelectComboBox.count() - 1):
                self.add_test_form.pointSelectComboBox.setCurrentIndex(point_index + 1)
            self.add_test_form.v_m_touch_pos_x.clear()
            self.add_test_form.v_m_touch_pos_y.clear()
        except ValueError:
            self.error_message_prompt(self.add_test_form,self.empty_error_code)
        except rangeErrorException:
            self.error_message_prompt(self.add_test_form,self.logic_error_code,error_msg)
    def mul_drag_next_P(self):
        line_edits = [self.add_test_form.v_m_drag_start_p_x,self.add_test_form.v_m_drag_start_p_y,\
            self.add_test_form.v_m_drag_end_p_x,self.add_test_form.v_m_drag_end_p_y]
        try:
            x1 = int(line_edits[0].text())
            y1 = int(line_edits[1].text())
            x2 = int(line_edits[2].text())
            y2 = int(line_edits[3].text())
            in_range1,error_msg = self.range_inside(x = x1,y = y1)
            if(not in_range1):
                raise rangeErrorException()
            in_range2,error_msg = self.range_inside(x = x2,y = y2)
            if(not in_range2):
                raise rangeErrorException()
            drag_two_point = ((x1,y1),(x2,y2))
            point_index = self.add_test_form.dragSelectComboBox.currentIndex() 
            self.add_test_form.points_list_drag[point_index] = drag_two_point
            #current_two_point = self.add_test_form.drag_two_point.currentText()
            current_point_text = '滑动%d'%(point_index+1)
            self.add_test_form.dragSelectComboBox.setItemText(point_index,current_point_text)
            if(point_index != self.add_test_form.dragSelectComboBox.count() - 1):
                for i in range(4):
                    line_edits[i].clear()
                self.add_test_form.dragSelectComboBox.setCurrentIndex(point_index + 1)
            else:
                QMessageBox.about(self.add_test_form,'提示','成功输入最后一次滑动信息')
       

        except ValueError:
            self.error_message_prompt(self.add_test_form,self.empty_error_code)
        except rangeErrorException:
            self.error_message_prompt(self.add_test_form,self.logic_error_code,error_msg)
    def all_random_test(self):
        value = int(self.add_test_form.randomTestNumValue.text())
        if(value  == 0):
            return
        else:
            ops = Monkey.all_random(value)
            items = self.operations_to_str(ops)
            self.add_test_form.currentQueueList.addItems(items)
    def save(self):
        Monkey.save('only')
    def load(self):
        try:
            item_list = Monkey.load('only')
            if(item_list == False):
                self.error_message_prompt(self.test_form,4)
                return
            else:
                strs = self.operations_to_str(item_list)
                self.test_form.queueList.addItems(strs)
        except:
            self.error_message_prompt(self.test_form,4)
    def open_app(self,p,a):
        Monkey.open_app(p,a)
    def judge_input_ration(self,x,y):
       #print(self.test_form.max_x)
        if(x > self.test_form.max_x or y > self.test_form.max_y):
            return False
        else:
            return True
    def operations_to_str(self,ops):  
        strs = []
        for op in ops:
            item_str = ""
            if(op.optype == 'touch'):
                item_str = '单点点击测试: %s,%d次,间隔%fs'%(str(op.pointlist),op.number,op.interval_time)
            elif(op.optype == 'long_touch'):
                item_str = '单点长按测试: %s,持续%ds,%d次,间隔%fs'%(str(op.pointlist),op.hold_time,op.number,op.interval_time)
            elif(op.optype == 'multi_touch'):
                item_str = '多点顺序点击: 循环%d次,循环内点击间隔%f秒，循环间隔%f秒'%(op.number,op.interval_time,op.wait_time)
            elif(op.optype == 'random_touch'):
                item_str = '随机点击测试: 点击%d次,间隔%fs'%(op.number,op.interval_time)
            elif(op.optype == 'drag'):
                item_str = '单线滑动测试: (%d,%d)到(%d,%d),点击%d次,间隔%fs'%(op.pointlist[0][0],op.pointlist[0][1],op.pointlist[1][0],op.pointlist[1][1],op.number,op.interval_time)
            elif(op.optype == 'multi_drag'):
                item_str = '多次顺序滑动: 循环%d次,循环内滑动间隔%f秒，滑动持续时间%f秒，循环间隔%f秒'%(op.number,op.interval_time,op.hold_time,op.wait_time)
            elif(op.optype == 'random_drag'):
                item_str = '随机滑动测试: 滑动%d次,间隔%fs,滑动持续%fs'%(op.number,op.interval_time,op.hold_time)
            elif(op.optype == 'touch_drag'):
                item_str = '长按滑动测试: (%d,%d)到(%d,%d),长按持续%fs,滑动持续%fs,长按滑动点击%d次,两次间隔%fs'%(op.pointlist[0][0],op.pointlist[0][1],op.pointlist[1][0],op.pointlist[1][1],\
                    op.wait_time,op.hold_time,op.number,op.interval_time)
            strs.append(item_str)
        return strs