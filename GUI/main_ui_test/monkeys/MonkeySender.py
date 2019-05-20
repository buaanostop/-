# -*- coding: utf-8 -*-
"""
Sender
把复杂操作分解成一步一步的简化操作发送给MonkeyServer执行。

"""
import socket
import time
import random
import os
from Operation import *
import threading

sendsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = 12345
host = '127.0.0.1'

recsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
recsocket.bind(("", 12346))

wtime = 1.0
resolution_ratio = (540,960)

root_path = os.getcwd()
shot_path = root_path + '\screenshot'
class do_run_monkey(threading.Thread):
    
    def __init__(self, monkeypath):
        threading.Thread.__init__(self)
        self.monkeypath = monkeypath
    def run(self):
        os.popen("monkeyrunner "+self.monkeypath)
#        os.system("monkeyrunner "+self.monkeypath)
            
def do_connect():
    data = bytes("connect:0:0:0:0:1.0:"+shot_path.replace(':','&'),encoding="utf8")
    sendsocket.sendto(data, (host, port))
    print("connect")

    data, addr = recsocket.recvfrom(1024)
    data = data.decode("utf-8")

    print("recv",data)

    if data == "connect false" or data == "NonexNone":
        return False
    else:
        ratio_x, ratio_y = data.split('x')
        resolution_ratio = (ratio_x, ratio_y)
        print("connect to",resolution_ratio)
        return resolution_ratio
    
def do_open_app(package_name, activity_name):
    data = bytes("open_app:0:0:0:0:1.0:"+package_name+'&'+activity_name,encoding="utf8")
    sendsocket.sendto(data, (host, port))
    print("open_app")
    
def do_close():
    data = bytes("close:0:0:0:0:1.0:",encoding="utf8")
    sendsocket.sendto(data, (host, port))
    recsocket.close()
    print("close")
    
class DoTest(threading.Thread):
    def __init__(self, oplist):
        threading.Thread.__init__(self)
        self.flag = threading.Event() # 运行标志
        self.stopflag = threading.Event() # 结束标志
        self.flag.clear()
        self.oplist = oplist
        self.resolution_ratio = resolution_ratio # 需要获取分辨率 （宽 ， 高）

    def __send(self, optype, x1=0, y1=0, x2=0, y2=0, hold_time=1.0, keyorstring=''):
        while not self.flag.isSet():
            if self.stopflag.isSet():
                return
            else:
                self.flag.wait(5)
        data = bytes("%s:%d:%d:%d:%d:%f:%s"%(optype,x1,y1,x2,y2,hold_time,keyorstring),encoding="utf8")
        sendsocket.sendto(data, (host, port))
        print("send: "+ optype)

    def __touch(self, x1, y1):
        print("touch", x1, y1)
        self.__send('touch', x1, y1)

    def __down(self, x1, y1):
        print("down", x1, y1)
        self.__send('down', x1, y1)
        
    def __move(self, x1, y1):
        print("move", x1, y1)
        self.__send('move', x1, y1)

    def __up(self, x1, y1):
        print("up", x1, y1)
        self.__send('up', x1, y1)
        
    def __drag(self, x1, y1, x2, y2, drag_time):
        print("drag", x1, y1, x2, y2, drag_time)
        self.__send('drag', x1, y1, x2, y2, drag_time)

    def __press(self, keyname):
        print("press", keyname)
        self.__send('press', 0, 0, 0, 0, 1.0, keyname)

    def __typestr(self, typestring):
        print("typestr", typestring)
        self.__send('typestr', 0, 0, 0, 0, 1.0, typestring)
        
    def __wait(self, wait_time):
        print("wait", wait_time)
        time.sleep(wait_time)
        
    def __actOp(self, op):
        """根据op,分解步骤，发送步骤"""
        optype = op.optype
        pointlist =  op.pointlist
        number = op.number
        interval_time = op.interval_time
        hold_time = op.hold_time
        keyorstring = op.keyorstring
        wait_time = op.wait_time
# touch
        if optype == 'touch': # -->touch
            num = 1
            pos_x = pointlist[0][0]
            pos_y = pointlist[0][1]
            while num < number:
                self.__touch(pos_x, pos_y)
                self.__wait(interval_time)
                num += 1
                    
            self.__touch(pos_x, pos_y)
            self.__wait(wtime)
# long_touch
        elif optype == 'long_touch': # --> down wait up
            num = 1
            pos_x = pointlist[0][0]
            pos_y = pointlist[0][1]
            while num < number:
                self.__down(pos_x, pos_y)
                self.__wait(hold_time)
                self.__up(pos_x, pos_y)
                self.__wait(interval_time)
                num += 1

            self.__down(pos_x, pos_y)
            self.__wait(hold_time)
            self.__up(pos_x, pos_y)
            self.__wait(wtime)
# multi_touch
        elif optype == 'multi_touch': # --> touch touch ...
            loop = 1
            while loop <= number:
                num = 1
                for point in pointlist:
                    self.__touch(point[0],point[1])
                    if num < len(pointlist): # 不是最后一个点
                        self.__wait(interval_time)
                        num += 1
                    else:
                        break
                if loop == number: # 循环最后一遍
                    self.__wait(wtime)
                else: # 没到最后一遍
                    self.__wait(wait_time)
                loop += 1
# random_touch
        elif optype == 'random_touch': # --> touch touch ...
            if pointlist is None: #全屏随机
                min_x = 0
                min_y = 0
                max_x = self.resolution_ratio[0] - 1
                max_y = self.resolution_ratio[1] - 1
            else:
                x1 = pointlist[0][0]
                y1 = pointlist[0][1]
                x2 = pointlist[1][0]
                y2 = pointlist[1][1]
                if x1 < x2:
                    min_x = x1
                    max_x = x2
                else:
                    min_x = x2
                    max_x = x1
                if y1 < y2:
                    min_y = y1
                    max_y = y2
                else:
                    min_y = y2
                    max_y = y1
                    
            num = 1
            while num < number: # 不是最后一次
                pos_x = random.randint(min_x, max_x)
                pos_y = random.randint(min_y, max_y)
                self.__touch(pos_x, pos_y)
                self.__wait(interval_time)
                num += 1

            pos_x = random.randint(min_x, max_x)
            pos_y = random.randint(min_y, max_y)
            self.__touch(pos_x, pos_y)
            self.__wait(wtime) #最后一次
# drag
        elif optype == 'drag': # --> drag
            x1 = pointlist[0][0]
            y1 = pointlist[0][1]
            x2 = pointlist[1][0]
            y2 = pointlist[1][1]
            
            num = 1
            while num < number:
                self.__drag(x1, y1, x2, y2, hold_time)
                self.__wait(hold_time) #等待拖动完毕
                self.__wait(interval_time)
                num += 1
        
            self.__drag(x1, y1, x2, y2, hold_time)
            self.__wait(hold_time)
            self.__wait(wtime)
# multi_drag
        elif optype == 'multi_drag': # --> drag drag ...
            loop = 1
            while loop <= number:
                num = 1
                for point in pointlist:
                    x1 = point[0]
                    y1 = point[1]
                    x2 = point[2]
                    y2 = point[3]
                    self.__drag(x1, y1, x2, y2, hold_time)
                    self.__wait(hold_time)
                    if num < len(pointlist): # 不是最后一个点
                        self.__wait(interval_time)
                        num += 1
                    else:
                        break
                if loop == number: # 循环最后一遍
                    self.__wait(wtime)
                else: # 没到最后一遍
                    self.__wait(wait_time)
                loop += 1
# random_drag
        elif optype == 'random_drag': # drag drag ...
            if pointlist is None: #全屏随机
                min_x = 0
                min_y = 0
                max_x = self.resolution_ratio[0] - 1
                max_y = self.resolution_ratio[1] - 1
            else:
                x1 = pointlist[0][0]
                y1 = pointlist[0][1]
                x2 = pointlist[1][0]
                y2 = pointlist[1][1]
                if x1 < x2:
                    min_x = x1
                    max_x = x2
                else:
                    min_x = x2
                    max_x = x1
                if y1 < y2:
                    min_y = y1
                    max_y = y2
                else:
                    min_y = y2
                    max_y = y1
            num = 1
            while num < number: # 不是最后一次
                start_x = random.randint(min_x, max_x)
                start_y = random.randint(min_y, max_y)
                end_x = random.randint(min_x, max_x)
                end_y = random.randint(min_y, max_y)
                self.__drag(start_x, start_y, end_x, end_y, hold_time)
                self.__wait(hold_time)
                self.__wait(interval_time)
                num += 1

            start_x = random.randint(min_x, max_x)
            start_y = random.randint(min_y, max_y)
            end_x = random.randint(min_x, max_x)
            end_y = random.randint(min_y, max_y)
            self.__drag(start_x, start_y, end_x, end_y, hold_time)
            self.__wait(hold_time)
            self.__wait(wtime) #最后一次            
# touch_drag
        elif optype == 'touch_drag': # down wait move up
            x1 = pointlist[0][0]
            y1 = pointlist[0][1]
            x2 = pointlist[1][0]
            y2 = pointlist[1][1]

            num = 1
            while num < number:
                self.__down(x1, y1)
                self.__wait(wait_time)
                self.__move(x2,y2)
                self.__wait(hold_time)
                self.__up(x2,y2)
                self.__wait(interval_time)
                num += 1

            self.__down(x1, y1) #最后一次
            self.__wait(wait_time)
            self.__move(x2,y2)
            self.__wait(hold_time)
            self.__up(x2,y2)
            self.__wait(wtime)
            num += 1
# press
        elif optype == 'press': # press
            self.__press(keyorstring)
            self.__wait(wtime)
# typestr
        elif optype == 'typestr': # typestr
            self.__typestr(keyorstring)
            self.__wait(wtime)

    def pause(self):
        self.flag.clear()

    def resume(self):
        self.flag.set()

    def stop(self):
        self.flag.clear()
        self.stopflag.set()
        
    def run(self):
        self.flag.set()
        self.stopflag.clear()
        for op in self.oplist:
            if self.stopflag.isSet():
                break
            self.__actOp(op)
