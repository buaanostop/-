import Monkey
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
import socket
import threading
import os
import _thread as thread
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
    connect_waiting_timer = None
    def __init__(self):
        self.thread_start()
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
  
    while(1):
        try:
            open('exception_' + str(exception_count) + '.txt')
            exception_count += 1
        except IOError:
            break
    def runMonkeyServer(self,lock):
    ##!!!!!!!!!!!!!!!!!!!!!!!!!!!!此位置改成MonkeyServer.py所在位置
        ret = os.system(r"monkeyrunner C:\Users\Lenovo\Desktop\Autotest-master\example\MonkeyServer.py")
        lock.release(self)
    def monkey_runner_initial(self):
        lock = thread.allocate_lock()
        lock.acquire()
        thread.start_new(runMonkeyServer,(lock,))
    def connect_waiting(self):
        #nonlocal bool_is_device_connected_successful
        connect_log = open(os.getcwd() + '\\connectlog.txt','r')
        content = connect_log.read()
        if(content == 'True'):
            bool_is_device_connected_successful = 1
            #print_text.insert('end','connection successful!')
            self.connect_waiting_timer.cancel()
            connect_log.close()
        else:
            connect_log.close()
            self.connect_waiting_timer = threading.Timer(0.5,self.connect_waiting)
            self.connect_waiting_timer.start()  
    def thread_start(self):
        self.connect_waiting_timer = threading.Timer(0.5,self.connect_waiting)
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
      
    def connect(self):
        
        #print_text.insert('end',"TestMethod: waiting for connection..")
        
        #send('connect',ord(path[0]),0,0,0,0,0,0,path[2:])
        Monkey.connect()
        connect_waiting_timer = threading.Timer(0.5,connect_waiting)
        connect_waiting_timer.start()
        #send('connect',0,0,0,0,0,0,0,0)
    connect_waiting_timer = threading.Timer(0.5,connect_waiting)
    def pause(self):
        #print_text.insert('end',"TestMethod: pause")
        #send('pause',0,0,0,0,0,0,0,0)
        Monkey.pause()

    def resume(self):
        #print_text.insert('end',"TestMethod: resume")
        #send('resume',0,0,0,0,0,0,0,0)
        Monkey.resume()

    def stop(self):
        #print_text.insert('end',"TestMethod: stop")
        #send('stop',0,0,0,0,0,0,0,0)
        Monkey.stop()

    def start(self):
        #log_timer = threading.Timer(1,log_monitor)
        #log_timer.start()
        #print_text.insert('end',"TestMethod: start")
        #send('start',0,0,0,0,0,0,0,0)
        Monkey.start()