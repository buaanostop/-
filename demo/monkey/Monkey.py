# _*_ coding:utf-8 _*_
"""
Monkey.py
作用为从UI获取具体的操作
通过socket发送消息给MonkeyServer进行具体操作
简化MonkeyServer的功能，仅接受信息并进行简单操作。
功能：
1.创建测试队列
2.控制测试的运行

"""
import sys
import socket
import random
import time

class Operation():
    """操作类，记录各种操作"""

    def __init__(self, optype, pointlist, number, interval_time, hold_time, keyorstring, wait_time):
        self.optype = optype
        self.pointlist = pointlist
        self.number = int(number)
        self.interval_time = float(interval_time)
        self.hold_time = float(hold_time)
        self.keyorstring = str(keyorstring)
        self.wait_time = float(wait_time)

    def display(self):
        print(self.optype, self.pointlist, self.number, self.interval_time, self.hold_time, self.keyorstring, self.wait_time)
                           
logpath = "log.txt"
oplist = []
uisocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = 8081
host = '127.0.0.1'

def __ifprint(data):
    print(data)
    
def __writelog(data):
    __ifprint(data)
    logfile = open(logpath, 'a')
    logfile.write(data + '\n')
    logfile.close()

def __send(optype, x1=0, y1=0, x2=0, y2=0, hold_time=1.0, keyorstring="none"):
    data = bytes("%s:%d:%d:%d:%d:%f:%s"%(optype,x1,y1,x2,y2,hold_time,keyorstring),encoding="utf8")
    uisocket.sendto(data, (host, port))
    print("send: "+ optype)
    
def __now():
    return str(time.strftime("%Y-%m-%d %H:%M:%S "))

##-------------------------------
def connect():
    __writelog(__now() + "connect...")
    __send("connect")

def open_app():
    __writelog(__now() + "open app")
    __send("connect")

##-------------------------------
def touch(pos_x, pos_y, touch_number=1, interval_time=1.0):
    """单击
    参数
    -------------
    pos_x : int
            点击的位置横坐标
    pos_y : int
            点击的位置纵坐标
    touch_numbere : int
            点击的次数，默认为1
    interval_time : float
            多次点击间隔时间,默认为1秒

    """
    op = Operation('touch', ((pos_x, pos_y),), touch_number, interval_time, 0, 0, 0)
    oplist.append(op)
    __writelog(__now() + "touch test add success")

def long_touch(pos_x, pos_y, touch_time=1.0, touch_number=1, interval_time=1.0):
    """长按测试
    参数
    -----------
    pos_x : int
            点击的位置x
    pos_y : int
            点击的位置y
    touch_time: float
            按住的时间，默认为1秒
    touch_number : int
            长按的次数
    interval_time : float
            每次长按间隔的时间
    
    """
    op = Operation('long_touch', ((pos_x, pos_y),), touch_number, interval_time, touch_time, 0, 0)
    oplist.append(op)
    __writelog(__now() + "long_touch test add success")
    
def multi_touch(pointlist, loop_number=1, interval_time = 1.0, loop_time = 1.0):
    """多位置顺序单击
    参数
    ---------------
    pointlist : ((x1,y1),(x2,y2),...(x10,y10)),x,y均为int
                多个位置的坐标
                当前限定为10个点
    loop_number : int
                循环的遍数，默认为1
    interval_time : float
                两次点击的间隔时间,默认为1秒
    loop_time : float
                两遍循环的间隔时间，默认为1秒

    """
    op = Operation('multi_touch', pointlist, loop_number, interval_time, 0, 0, loop_time)
    oplist.append(op)
    __writelog(__now() + "multi_touch add success")
    
def random_touch(pointlist, touch_number=1, interval_time=1.0):
    """随机点击屏幕测试
    参数
    -----------
    pointlist : ((x1,y1),(x2,y2)) x,y均为int 或 None
                由两个点围成的矩形为随机的范围
                如果传入None 则没有范围，在全屏内随机
    touch_number : int
                点击的次数
    interval_time : float
                每两次点击间隔的时间，默认为1秒
    """
    op = Operation('random_touch', pointlist, touch_number, interval_time, 0, 0, 0)
    oplist.append(op)
    __writelog(__now() + "random_touch test add success")

def drag(pointlist, drag_time=1.0, drag_number=1, interval_time=1.0):
    """滑动屏幕测试
    参数
    ---------------
    pointlist : ((x1,y1),(x2,y2)) x,y均为int
                滑动的起点和终点
    drag_time : float
            滑动持续时间,默认为1秒
    drag_number : int
            滑动次数，默认为1次
    interval_time : float
            滑动间隔时间，默认为1秒
    """
    op = Operation('drag', pointlist, drag_number, interval_time, drag_time, 0, 0)
    oplist.append(op)
    __writelog(__now() + "drag test add success")

def multi_drag(pointlist, loop_number=1, interval_time = 1.0, drag_time=1.0, loop_time = 1.0):
    """多位置滑动测试
    参数
    ---------------
    pointlist : ((startx1,starty1,endx1,endy1),(startx2,starty2,endx2,endy2)...),均为int
                多个(起点，终点)位置的坐标
    loop_number : int
                滑动的遍数，默认为1
    interval_time : float
                两次滑动的间隔时间,默认为1秒
    drag_time : float
                每次滑动的持续时间，默认为1秒
    loop_time : float
                两遍滑动的间隔时间，默认为1秒

    """
    op = Operation('multi_drag', pointlist, loop_number, interval_time, drag_time, 0, loop_time)   
    oplist.append(op)
    __writelog(__now() + "multi_drag add success")
    
def random_drag(pointlist, drag_number=1, interval_time=1.0, drag_time=1.0):
    """随机滑动屏幕测试
    参数
    -----------
    pointlist : ((x1,y1),(x2,y2)) x,y均为int 或 None
                由两个点围成的矩形为随机的范围
                如果传入None 则没有范围，在全屏内随机
    drag_number : int
                随机滑动次数
    interval_time : float
                每两次滑动间隔的时间，默认为1秒
    drag_time : float
                滑动时间，默认为1秒

    """
    op = Operation('random_drag', pointlist, drag_number, interval_time, drag_time, 0, 0)
    oplist.append(op)
    __writelog(__now() + "random_drag test add success")

def touch_drag(pointlist, touch_number=1.0, touch_time=1.0, drag_time=1.0, interval_time=1.0):
    """长按滑动测试
    参数
    -----------
    pointlist : ((x1,y1),(x2,y2)) x,y均为int
                按住的点和滑动的终点的坐标
    touch_number : int
                长按滑动的次数
    touch_time : float
                长按的时间，默认为1秒
    drag_time : float
                滑动的时间， 默认为1秒
    interval_time : float
                两次动作的间隔时间

    """
    op = Operation('touch_drag', pointlist, touch_number, interval_time, drag_time, 0, touch_time)
    oplist.append(op)
    __writelog(__now() + "touch_drag test add success")
   
def press(key_name):
    """按键测试
    参数
    -----------
    key_name : string
            按键的名字

    """
    op = Operation('press', None, 0, 0, 0, key_name, 0)
    oplist.append(op)
    __writelog(__now() + "press test add success")

def typestr(typestring):
    """键盘输入测试
    参数
    -------
    typestring : string
                要输入的字符串
    """
    op = Operation('typestr', None, 0, 0, 0, typestring, 0)
    oplist.append(op)
    __writelog(__now() + "typestr test add success")

  

def print_oplist():
    for op in oplist:
        op.display()
        

##-------------------------------
def start():
    __writelog(__now() + "start")
#    __send("start")
    
def pause():
    __writelog(__now() + "pause")
#    __send("pause")

def resume():
    __writelog(__now() + "resume")
#    __send("resume")

def stop():
    __writelog(__now() + "stop")
#    __send("stop")

##-------------------------------
def closeMonkeyServer():
    __writelog(__now() + "close")
    __send("close")


