import sys
import os
import socket
import threading
import os
import _thread as thread
import Monkey
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QDockWidget, QListWidget
from PyQt5.QtGui import *
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
    max_pos_x = 1000
    max_pos_y = 1000
    path = os.getcwd()
    exception_count = 0
    #connect_waiting_timer = None
    add_test_form = None
    test_form = None
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
    def read_exception():
        '''while(1):
            try:
                open('exception_' + str(exception_count) + '.txt')
                exception_count += 1
            except IOError:
                break'''
    def error_message_prompt(self,error_code):
        empty_error_code = 0
        number_error_code = 1
        logic_error_code = 2
        resolution_ration_error_code = 3
        something_else_error_code = 4
        have_not_connect_error_code = 5
        not_successful_connected_error_code = 6
        #if(error_code == 0):#错误信息:空输入

    #常数和错误处理结束#
    def runMonkeyServer(self,lock):
    ##!!!!!!!!!!!!!!!!!!!!!!!!!!!!此位置改成MonkeyServer.py所在位置
        ret = os.system(r"monkeyrunner C:\Users\Lenovo\Desktop\Autotest-master\example\MonkeyServer.py")
        lock.release(self)
    def monkey_runner_initial(self):
        lock = thread.allocate_lock()
        lock.acquire()
        thread.start_new(runMonkeyServer,(lock,))

    def connect(self):
        print("ok")
        #print_text.insert('end',"TestMethod: waiting for connection..")
        self.add_text('waiting for connection',self.test_window.reportList)
        connect_successful = Monkey.connect()
        if(connect_successful):
            self.add_text('connection successful!',self.test_window.reportList)
        else:
            self.add_text('fail to connect your device,please check that if your device connect to computer successfully',self.test_window.reportList)
        '''connect_waiting_timer = threading.Timer(0.5,connect_waiting)
        connect_waiting_timer.start()'''

    def pause(self):
        self.add_text('pausing...',self.test_window.reportList)
        Monkey.pause()

    def resume(self):
        self.add_text('now resume',self.test_window.reportList)
        Monkey.resume()

    def stop(self):
        #print_text.insert('end',"TestMethod: stop")
        #send('stop',0,0,0,0,0,0,0,0)
        Monkey.stop()

    def start(self):
        #log_timer = threading.Timer(1,log_monitor)
        #log_timer.start()
        self.add_text('start!',self.test_window.reportList)
        #send('start',0,0,0,0,0,0,0,0)
        Monkey.start()