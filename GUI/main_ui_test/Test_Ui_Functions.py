import sys
import os
import socket
import threading
import os
import _thread as thread
import Monkey
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
    something_else_error_code = 4
    have_not_connect_error_code = 5
    not_successful_connected_error_code = 6
    exception_count = 0
    #connect_waiting_timer = None
    add_test_form = None
    test_form = None
    exception_raw_name = 'exception.txt'
    exception_name = 'exception_' + str(exception_count)+'.txt'
    log_name = 'log.txt'
    log_lines = []
    log_timer = None
    bool_successful_read_log = 0
    def __init__(self,test_form,add_test_form):
        #self.thread_start()
        self.test_form = test_form
        self.add_test_form = add_test_form
    def add_text(self,text,widget):
        widget.addItem(text)
    def close_monkeyrunner(self):
        Monkey.close()
    def close_model(self):
        sendsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        port = 9999
        host = '127.0.0.1'
        sendsocket.sendto(1,(port,host))

    #一些常数和错误处理#
    def read_exception(self):
        while(1):
            try:
                f_t = open('exception_' + str(self.exception_count) + '.txt')
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
        elif(error_code == something_else_error_code):
           QMessageBox.about(widget,'未知错误','发生了一些未知的错误，程序将退出')
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
        self.add_text('waiting for connection',self.test_form.reportList)
        connect_successful = Monkey.connect()
        if(connect_successful):
            self.add_text('connection successful!',self.test_form.reportList)
        else:
            self.add_text('fail to connect your device,please check that if your device connect to computer successfully',self.test_form.reportList)
        return connect_successful
    @disp_func_msg
    def pause(self):
        self.add_text('pausing...',self.test_form.reportList)
        Monkey.pause()
    @disp_func_msg
    def resume(self):
        self.add_text('now resume',self.test_form.reportList)
        Monkey.resume()
    @disp_func_msg
    def stop(self):
        Monkey.stop()
    @disp_func_msg
    def start(self):
        self.add_text('start!',self.test_form.reportList)
        self.log_timer = threading.Timer(1,self.log_monitor)
        self.log_timer.start()
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
            point_tuple = tuple(self.add_test_form.points_list)
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
        '''还要改动 先不做了'''
        pass
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
            self.add_test_form.currentQueueList.addItem('单线滑动测试: (%d,%d)到(%d,%d),长按持续%fs,滑动持续%fs,长按滑动点击%d次,两次间隔%fs' %(x1,y1,x2,y2,touch_time,drag_during_time,touch_number,interval_time))
        except ValueError:
            self.error_message_prompt(self.add_test_form,self.empty_error_code,extra_msg)
        except rangeErrorException:
            self.error_message_prompt(self.add_test_form,self.logic_error_code,extra_msg)
    def change_queue(self,src,dst):
        Monkey.change(src+1,dst+1)
    def delete_from_queue(self,index):
        Monkey.delete(index)
    def disp_report_information(self,nop,context):
        self.test_form.reportList.addItem(context)
    def log_monitor(self):
        log_name = self.log_name
        #read_log = self.read_log
        log_lines = self.log_lines
        #file_log = self.file_log
        #nonlocal bool_successful_read_log
        try:
            self.read_log = 1
            if(not self.bool_successful_read_log):
                file_log = open(log_name,'r')
                bool_successful_read_log = 1
            final_line = file_log.readline()
            if(final_line != '' and final_line != log_lines[-1]):
                log_lines.append(final_line)
                self.disp_report_information('end',final_line)
            #print(log_lines)
            #nonlocal label_2
            #label_2.config(text = content)
            #file_log.close()
            try:
                file_exception = open(self.exception_raw_name,'r')
                file_exception_log = open(self.exception_name,'a+')
                lines_count = len(log_lines)
                if(len(log_lines) == 0):
                    #print('no log file')
                    self.log_timer = threading.Timer(0.5,self.log_monitor)
                    self.log_timer.start()
                    return
                lines_to_be_written = []
                min_lines_error_log = min(10,lines_count)
                for i in range(lines_count - 1,lines_count - min_lines_error_log,-1):
                    lines_to_be_written.insert(0,log_lines[i])
                file_exception_log.writelines(lines_to_be_written)
                self.disp_report_information('end','\n出现异常！相关内容已经保存到根目录下' + self.exception_name + '\n测试已停止')
                self.exception_count += 1
                file_exception.close()
                os.remove(os.getcwd() + '\\' + self.exception_raw_name)
                self.stop()
                file_log.close()
                file_exception_log.close()
            except IOError:
                self.log_timer = threading.Timer(0.5,self.log_monitor)
                self.log_timer.start()
        except IOError:
            if(self.read_log == 0):
                self.disp_report_information('end','暂未读取到日志文件')
        def save(self):
            Monkey.save()
        def load(self):
            pass
        '''def operations_to_str(self,ops):  
            strs = []
            for op in ops:
                item_str = ""
                if(op.otype == 'touch'):'''
                    