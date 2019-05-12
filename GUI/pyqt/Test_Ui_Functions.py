import Monkey
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QDockWidget, QListWidget
from PyQt5.QtGui import *
class TestUiFunctions():
    def __init__(self):
        a = 0
    def close_monkeyrunner():
        Monkey.close()
    def close_model():
        sendsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        port = 9999
        host = '127.0.0.1'
        sendsocket.sendto(1,(port,host))
    #一些常数和错误处理#
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

    exception_count = 0
    while(1):
        try:
            open('exception_' + str(exception_count) + '.txt')
            exception_count += 1
        except IOError:
            break

    def monkey_runner_initial():
        lock = thread.allocate_lock()
        lock.acquire()
        thread.start_new(runMonkeyServer,(lock,))
    def runMonkeyServer(lock):
    ##!!!!!!!!!!!!!!!!!!!!!!!!!!!!此位置改成MonkeyServer.py所在位置
        ret = os.system(r"monkeyrunner C:\Users\Lenovo\Desktop\Autotest-master\example\MonkeyServer.py")
        lock.release()
    def error_message_prompt(error_code):
        empty_error_code = 0
        number_error_code = 1
        logic_error_code = 2
        resolution_ration_error_code = 3
        something_else_error_code = 4
        have_not_connect_error_code = 5
        not_successful_connected_error_code = 6
        if(error_code == 0):#错误信息:空输入
            tk.messagebox.showinfo('输入错误','输入不能为空或非半角阿拉伯数字，具体输入规范可参考顶部菜单栏的“帮助”按钮')
        elif(error_code == 1):#错误信息：输入的应该是数字却不是
            tk.messagebox.showinfo('输入错误','请输入半角阿拉伯正数，具体输入规范可参考顶部菜单栏的“帮助”按钮')
        elif(error_code == 2):
            tk.messagebox.showinfo('输入错误','请输入不要超过限定范围，具体输入范围可参考顶部菜单栏的“帮助”按钮')
        elif(error_code == 3):
            tk.messagebox.showinfo('输入错误','请正确输入手机分辨率，以半角阿拉伯正数形式输入')
        elif(error_code == something_else_error_code):
            tk.messagebox.showinfo('未知错误','发生了一些未知的错误，程序将退出')
        elif(error_code == have_not_connect_error_code):
            tk.messagebox.showinfo('提示','请先连接设备！')
        elif(error_code == not_successful_connected_error_code):
            tk.messagebox.showinfo('连接错误','还未成功连接设备')
    #常数和错误处理结束#
    def connect_waiting():
        nonlocal bool_is_device_connected_successful
        connect_log = open(os.getcwd() + '\\connectlog.txt','r')
        content = connect_log.read()
        nonlocal connect_waiting_timer
        if(content == 'True'):
            bool_is_device_connected_successful = 1
            #print_text.insert('end','connection successful!')
            connect_waiting_timer.cancel()
            connect_log.close()
        else:
            connect_log.close()
            connect_waiting_timer = threading.Timer(0.5,connect_waiting)
            connect_waiting_timer.start()
            
    def connect(self):
        nonlocal bool_ever_click_connect_button
        bool_ever_click_connect_button = 1
        path = os.getcwd()
        #print_text.insert('end',"TestMethod: waiting for connection..")
        
        #send('connect',ord(path[0]),0,0,0,0,0,0,path[2:])
        Monkey.connect()
        nonlocal connect_waiting_timer
        connect_waiting_timer = threading.Timer(0.5,connect_waiting)
        connect_waiting_timer.start()
        #send('connect',0,0,0,0,0,0,0,0)
    connect_waiting_timer = threading.Timer(0.5,connect_waiting)
    def pause():
        #print_text.insert('end',"TestMethod: pause")
        #send('pause',0,0,0,0,0,0,0,0)
        Monkey.pause()

    def resume():
        #print_text.insert('end',"TestMethod: resume")
        #send('resume',0,0,0,0,0,0,0,0)
        Monkey.resume()

    def stop():
        #print_text.insert('end',"TestMethod: stop")
        #send('stop',0,0,0,0,0,0,0,0)
        Monkey.stop()

    def start():
        log_timer = threading.Timer(1,log_monitor)
        log_timer.start()
        #print_text.insert('end',"TestMethod: start")
        #send('start',0,0,0,0,0,0,0,0)
        Monkey.start()