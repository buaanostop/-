# -*- coding: utf-8 -*-
"""Read Me
1.！！运行之前调整 runMonkeyServer()中的文件位置
2.直接在python shell中运行此文件 或按F5
3.等待cmd窗口显示 MonkeyServer start
4.按连接手机
5.cmd中显示 Connection success 即为连接成功
6.输入点击次数和间隔时间
7.点击添加测试
8.点击开始测试
"""

"""
简化测试UI

"""
from tkinter import *
import os
import socket
import time
import _thread as thread
"""
Test测试方法集
UI的按钮调用以下方法来创建测试条目，开始、暂停、继续、停止测试
再使用socket发送要执行的MonkeyRunner指令给MonkeyServer
"""
uisocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = 8081
host = '127.0.0.1'
def runMonkeyServer(lock):
    ##!!!!!!!!!!!!!!!!!!!!!!!!!!!!此位置改成MonkeyServer.py所在位置
    os.system("monkeyrunner E:\dontstop\example\MonkeyServer.py")
    lock.release()

lock = thread.allocate_lock()
lock.acquire()
thread.start_new(runMonkeyServer,(lock,))

def connect():
    print("TestMethod: connection")
    send('connect',0,0,0,0,0,0,0,0)

def pause():
    print("TestMethod: pause")
    send('pause',0,0,0,0,0,0,0,0)

def resume():
    print("TestMethod: resume")
    send('resume',0,0,0,0,0,0,0,0)

def stop():
    print("TestMethod: stop")
    send('stop',0,0,0,0,0,0,0,0)

def start():
    print("TestMethod: start")
    send('start',0,0,0,0,0,0,0,0)


def random_touch():
    touch_number = int(e_touch_number.get()) # 通过输入框获取参数 点击次数
    interval_time = float(e_interval_time.get()) # 通过输入框获取参数 间隔时间
    print("TestMethod: random_touch 点击次数:%d 间隔时间:%f"%(touch_number, interval_time))
    send('random_touch',0,0,0,0,touch_number,interval_time,0,0)
##def open_app():
##    """打开app
##    需要参数
##    --------------
##    package_name:string
##                应用的package name 包名
##    activity_name: string
##                应用的activity name 活动名
##
##    """
##    package_name =
##    activity_name = 
##    print("TestMethod: open_app")
##    send('open_app',0,0,0,0,0,0,0,package_name + '&' + activity_name)
##
##def touch():
##        """点击屏幕测试
##        参数
##        -------------
##        pos_x : int
##                点击的位置x
##        pos_y : int
##                点击的位置y
##        touch_number : int
##                点击的次数，默认为1
##        interval_time : float
##                多次点击时间隔时间,默认为1秒
##        
##        """
##    pos_x = int()
##    pos_y = int()
##    touch_number = int()
##    interval_time = float()
##    print("TestMethod: touch 点击位置:(%d,%d) 点击次数:%d 间隔时间:%f"%(pos_x,pos_y,touch_number,interval_time))
##    send('touch',pos_x,pos_y,0,0,touch_number,interval_time,0,0)



##def press():
##        """按键测试
##        参数
##        -----------
##        key_name : string
##                按键的名字
##
##        """
##    key_name =
##    print("TestMethod: press %s"%key_name)
##    send('press',0,0,0,0,0,0,0,key_name)
##
##def typestr():
##        """键盘输入测试
##        参数
##        -------
##        typestring : string
##                    要输入的字符串
##        """
##    typestring =
##    print("TestMethod: typestr %s",typestring)
##    send('typestr',0,0,0,0,0,0,0,typestring)
##
##def drag():
##        """滑动屏幕测试
##        参数
##        ---------------
##        start_x : int
##                滑动起始位置x
##        start_y : int
##                滑动起始位置y
##        end_x : int
##                滑动结束位置x
##        end_y : int
##                滑动结束位置y
##        drag_time : float
##                滑动持续时间,默认为1秒
##        drag_number : int
##                滑动次数，默认为1次
##        interval_time : float
##                滑动间隔时间，默认为1秒
##        """
##    start_x = int()
##    start_y = int()
##    end_x = int()
##    end_y = int()
##    drag_time = float()
##    drag_number = int()
##    interval_time = float()
##    print("TestMethod: drag")
##    send('drag', start_x, start_y, end_x, end_y, drag_number, interval_time, drag_time, 0)
##    
##def random_drag()
##        """随机滑动屏幕测试
##        参数
##        -----------
##        drag_number : int
##                    滑动的次数
##        interval_time : float
##                    每两次滑动间隔的时间，秒为单位
##        """
##    drag_number = int()
##    interval_time = float()
##    print("TestMethod: random_drag")
##    send('random_drag',0,0,0,0,drag_number, interval_time, 1, 0)
    
def send(optype, x1, y1, x2, y2, number, interval_time, drag_time, keyorstring):
    data = bytes("%s:%d:%d:%d:%d:%d:%f:%f:%s"%(optype,x1,y1,x2,y2,number,interval_time,drag_time,keyorstring),encoding="utf8")
    uisocket.sendto(data, (host, port))




root = Tk()

l_touch_number = Label(root, text='随机点击次数')
l_touch_number.grid(row=0, sticky=W)

e_touch_number = Entry(root)
e_touch_number.grid(row=0, column=1, sticky=E)


l_interval_time = Label(root, text='点击间隔时间')
l_interval_time.grid(row=1, sticky=W)

e_interval_time = Entry(root)
e_interval_time.grid(row=1, column=1, sticky=E)

b_connection = Button(root, text='连接手机', command=connect)
b_connection.grid(row=2,column=0)

b_random_touch = Button(root, text='添加随机点击测试', command=random_touch)
b_random_touch.grid(row=2,column=1)

b_start = Button(root, text='开始测试', command=start)
b_start.grid(row=3, column=0)

b_pause = Button(root, text='暂停测试', command=pause)
b_pause.grid(row=3, column=1)

b_resume = Button(root, text='继续测试', command=resume)
b_resume.grid(row=4, column=1)

b_stop = Button(root, text='停止测试', command=stop)
b_stop.grid(row=4, column=0)

mainloop()
