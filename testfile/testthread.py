# -*- coding: utf-8 -*-
"""Test类
调用Test类中的各种方法来对模拟器或手机界面进行操作。
"""
import random
import sys
import time
import threading
from com.android.monkeyrunner import MonkeyRunner,MonkeyDevice,MonkeyImage


class Operation():
    """操作类，给Test类记录各种操作"""
    def __init__(self, optype, x1, y1, x2, y2, number, interval_time, drag_time, keyorstring ):
        self.optype = optype
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.number = number
        self.interval_time = interval_time
        self.drag_time = drag_time
        self.keyorstring = keyorstring
        
        
class Test(threading.Thread):
    
    def __init__(self):
        """初始化"""
        threading.Thread.__init__(self)
        self.__flag = threading.Event() # 暂停标志
        self.__flag.set() # 设为True
        self.__running = threading.Event() # 运行标志
        self.__running.set() # 设为True
        self.__resolution_x = 0 # 分辨率x
        self.__resolution_y = 0 # 分辨率y
        self.__device = None # 设备
        self.__oplist = [] # 模拟操作的列表
        
    def connect(self, resolution_x=540, resolution_y=960):
        """连接模拟器或手机
        参数
        ----------
        resolution_x : int
                       分辨率x值
        resolution_y : int
                       分辨率y值
                       
        返回值
        ----------
        int
            返回 1 : 成功连接设备
            返回 0 : 连接设备失败

        示例
        ----------
        >>> a.connect(540, 960)
        """
        self.__resolution_x = resolution_x
        self.__resolution_y = resolution_y
        print(time.strftime("%Y-%m-%d %H:%M:%S ") + "Connect ...")
        self.__device = MonkeyRunner.waitForConnection() # 连接设备或模拟器
        if not self.__device:
            print("Please connect a device to start.")
            return 0
        else:
            print(time.strftime("%Y-%m-%d %H:%M:%S ") + "Connection succeeded.")
            return 1
            
    def open_app(self, package_name, activity_name):
        """打开设备上的应用
        参数
        ----------
        package_name : string
                    应用的Package Name 包名
        activity_name: string
                    应用的Activity Name 活动名
        示例
        ----------
        >>> a.open_app('com.Jelly.JellyFish','com.unity3d.player.UnityPlayerActivity')        
        """
        print(time.strftime("%Y-%m-%d %H:%M:%S ") + "Oppen application ...")
        self.__device.startActivity(component = package_name + "/" + activity_name)
        MonkeyRunner.sleep(10)
        print(time.strftime("%Y-%m-%d %H:%M:%S ") + "Open application succeeded.")

    def pause(self):
        print("pause")
        self.__flag.clear()

    def resume(self):
        print("resume")
        self.__flag.set()

    def stop(self):
        print("stop")
        self.__flag.set()
        self.__running.clear()
    

    def touch(self,pos_x, pos_y, touch_number=1, interval_time=1):
        """点击屏幕测试
        参数
        -------------
        pos_x : int
                点击的位置x
        pos_y : int
                点击的位置y
        touch_numbere : int
                点击的次数，默认为1
        interval_time : float
                多次点击时间隔时间,默认为1秒
        
        """
        #optype, x1, y1, x2, y2, number, interval_time, drag_time, keyorstring
        op = Operation('touch',pos_x,pos_y,0,0,touch_number,interval_time,0,0)
        self.__oplist.append(op)

    def random_touch(self, touch_number, interval_time):
        """随机点击屏幕测试
        参数
        -----------
        touch_number : int
                    点击的次数
        interval_time : float
                    每两次点击间隔的时间，秒为单位
        示例
        -----------
        >>> a.random_touch(200, 1)
        """
        op = Operation('random_touch',0,0,0,0,touch_number,interval_time,0,0)
        self.__oplist.append(op)

    def press(self, key_name):
        """按键测试
        参数
        -----------
        key_name : string
                按键的名字

        """
        op = Operation('press',0,0,0,0,0,0,0,key_name)
        self.__oplist.append(op)

    def type(self, typestring):
        """键盘输入测试
        参数
        -------
        typestring : string
                    要输入的字符串
        """
        op = Operation('type',0,0,0,0,0,0,0,typestring)
        self.__oplist.append(op)
              
    def drag(self,start_x, start_y, end_x, end_y, drag_time=1, drag_number=1, interval_time=1):
        """滑动屏幕测试
        参数
        ---------------
        start_x : int
                滑动起始位置x
        start_y : int
                滑动起始位置y
        end_x : int
                滑动结束位置x
        end_y : int
                滑动结束位置y
        drag_time : float
                滑动持续时间,默认为1秒
        drag_number : int
                滑动次数，默认为1次
        interval_time : float
                滑动间隔时间，默认为1秒
        """
        #optype, x1, y1, x2, y2, number, interval_time, drag_time, keyorstring
        op = Operation('drag',start_x,start_y,end_x,end_y,drag_number,interval_time,drag_time,0)
        self.__oplist.append(op)

            
    def random_drag(self, drag_number, interval_time):
        """随机滑动屏幕测试
        参数
        -----------
        drag_number : int
                    滑动的次数
        interval_time : float
                    每两次滑动间隔的时间，秒为单位
        示例
        ------------
        >>> a.random_drag(200, 3)
        """
        op = Operation('random_drag',0,0,0,0,drag_number,interval_time,1,0)
        self.__oplist.append(op)


        
    def run(self):
        opnum = len(self.__oplist)
        if(opnum <= 0):
            return
        for op in self.__oplist:
# touch
            if op.optype == 'touch':
                touch_number = op.number
                pos_x = op.x1
                pos_y = op.y1
                interval_time = op.interval_time
                num = 1
                while(num <= touch_number):
                    if self.__running.isSet():
                        self.__flag.wait()
                        print("%stouch %d (%d,%d)."%(time.strftime("%Y-%m-%d %H:%M:%S "), num, pos_x, pos_y))
                        self.__device.touch(pos_x, pos_y, 'DOWN_AND_UP')
                        num += 1
                        MonkeyRunner.sleep(interval_time)
                    else:
                        self.__oplist[:] = []
                        return
                        
# random_touch
            elif op.optype == 'random_touch':
                touch_number = op.number
                interval_time = op.interval_time
                print(time.strftime("%Y-%m-%d %H:%M:%S ") + "Random touch test start.")
                num = 1
                while(num <= touch_number):
                    if self.__running.isSet():
                        self.__flag.wait()
                        x = random.randint(0, self.__resolution_x) # 随机生成位置x
                        y = random.randint(0, self.__resolution_y) # 随机生成位置y
                        print("%srandom_touch %d (%d,%d)."%(time.strftime("%Y-%m-%d %H:%M:%S "),num,x,y))
                        self.__device.touch(x, y, 'DOWN_AND_UP') # 点击(x,y)
                        MonkeyRunner.sleep(interval_time)
                        num += 1
                    else:
                        self.__oplist[:] = []
                        return
                print(time.strftime("%Y-%m-%d %H:%M:%S ") + "Random touch test finished.")
# drag
            elif op.optype == 'drag':
                start_x = op.x1
                start_y = op.y1
                end_x = op.x2
                end_y = op.y2
                drag_time = op.drag_time
                drag_number = op.number
                interval_time = op.interval_time
                num = 1
                while(num <= drag_number):
                    if self.__running.isSet():
                        self.__flag.wait()
                        print("%sdrag %d (%d,%d) to (%d,%d)."%(time.strftime("%Y-%m-%d %H:%M:%S "),num,start_x,start_y,end_x,end_y))
                        self.__device.drag((start_x, start_y), (end_x, end_y), drag_time, 10)
                        MonkeyRunner.sleep(interval_time)
                        num += 1
                    else:
                        self.__oplist[:] = []
                        return

#random_drag
            elif op.optype == 'random_drag':
                drag_number = op.number
                interval_time = op.interval_time
                print(time.strftime("%Y-%m-%d %H:%M:%S ") + "Random drag test start.")
                num = 1
                while(num <= drag_number):
                    if self.__running.isSet():
                        self.__flag.wait()
                        x_start = random.randint(0, self.__resolution_x)
                        y_start = random.randint(0, self.__resolution_y)
                        x_end = random.randint(0,self.__resolution_x)
                        y_end = random.randint(0,self.__resolution_y)
                        print("%srandom_drag %d (%d,%d) to (%d,%d)."%(time.strftime("%Y-%m-%d %H:%M:%S "),num,x_start,y_start,x_end,y_end))
                        self.__device.drag((x_start, y_start), (x_end, y_end), 1, 10)
                        MonkeyRunner.sleep(interval_time)
                        num += 1
                    else:
                        self.__oplist[:] = []
                        return
                print(time.strftime("%Y-%m-%d %H:%M:%S ") + "Random drag test finished.")                

#press
            elif op.optype == 'press':
                key_name = op.keyorstring
                if self.__running.isSet():
                    self.__flag.wait()
                    print("%spress %s."%(time.strftime("%Y-%m-%d %H:%M:%S "),key_name))
                    self.__device.press(key_name, 'DOWN_AND_UP')
                else:
                    self.__oplist[:] = []
                    return
#type
            elif op.optype == 'type':
                typestring = op.keyorstring
                if self.__running.isSet():
                    print("%stype %s."%(time.strftime("%Y-%m-%d %H:%M:%S "),typestring))
                    self.__device.type(typestring)
                else:
                    self.__oplist[:] = []
                    return

            else:
                print("optype error")
        
##例子
##t1 = Test()
##t1.connect()
##t1.random_touch(5,5)
##t1.start()
##time.sleep(6)
##t1.pause()
##time.sleep(6)
##t1.resume()
##time.sleep(6)
##t1.stop()
##
##t1.join()
