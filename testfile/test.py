# -*- coding: utf-8 -*-
"""Test类
调用Test类中的各种方法来对模拟器或手机界面进行操作。
"""
import random
import sys
import time
from com.android.monkeyrunner import MonkeyRunner,MonkeyDevice,MonkeyImage

class Test():
    
    __device = None # 设备
    __resolution_x = 0 # 分辨率x
    __resolution_y = 0 # 分辨率y
    
    def __init__(self):
        """初始化"""
        pass

    def connect(self, resolution_x, resolution_y):
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
        num = 1
        while(num <= touch_number):            
            print("%stouch %d (%d,%d)."%(time.strftime("%Y-%m-%d %H:%M:%S "), num, pos_x, pos_y))
            self.__device.touch(pos_x, pos_y, 'DOWN_AND_UP')
            num += 1
            MonkeyRunner.sleep(interval_time)

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
        print(time.strftime("%Y-%m-%d %H:%M:%S ") + "Random touch test start.")
        num = 1
        while(num <= touch_number):
            x = random.randint(0, self.__resolution_x) # 随机生成位置x
            y = random.randint(0, self.__resolution_y) # 随机生成位置y
            print("%srandom_touch %d (%d,%d)."%(time.strftime("%Y-%m-%d %H:%M:%S "),num,x,y))
            self.__device.touch(x, y, 'DOWN_AND_UP') # 点击(x,y)
            MonkeyRunner.sleep(interval_time)
            num += 1
        print(time.strftime("%Y-%m-%d %H:%M:%S ") + "Random touch test finished.")

    def press(self, key_name):
        print("%spress %s."%(time.strftime("%Y-%m-%d %H:%M:%S "),key_name))
        self.__device.press(key_name, 'DOWN_AND_UP')

    def type(self, typestring):
        print("%stype %s."%(time.strftime("%Y-%m-%d %H:%M:%S "),typestring))
        self.__device.type(typestring)
              
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
        num = 1
        while(num <= drag_number):
            print("%sdrag %d (%d,%d) to (%d,%d)."%(time.strftime("%Y-%m-%d %H:%M:%S "),num,start_x,start_y,end_x,end_y))
            self.__device.drag((start_x, start_y), (end_x, end_y), drag_time, 10)
            MonkeyRunner.sleep(interval_time)
            num += 1
            
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
        print(time.strftime("%Y-%m-%d %H:%M:%S ") + "Random drag test start.")
        num = 1
        while(num <= drag_number):
            x_start = random.randint(0, self.__resolution_x)
            y_start = random.randint(0, self.__resolution_y)
            x_end = random.randint(0,self.__resolution_x)
            y_end = random.randint(0,self.__resolution_y)
            print("%srandom_drag %d (%d,%d) to (%d,%d)."%(time.strftime("%Y-%m-%d %H:%M:%S "),num,x_start,y_start,x_end,y_end))
            self.__device.drag((x_start, y_start), (x_end, y_end), 1, 10)
            MonkeyRunner.sleep(interval_time)
            num += 1
        print(time.strftime("%Y-%m-%d %H:%M:%S ") + "Random drag test finished.")

    def play_test(self):
        """玩游戏测试
        """
        print(time.strftime("%Y-%m-%d %H:%M:%S ") + "Play test start.")
        interval_time = 3
        self.__device.touch(280, 460, 'DOWN_AND_UP') # 按第一个键
        MonkeyRunner.sleep(10)
        num = 1
        while(num <= 20): # 20次滑动
            x = random.randint(70,470) # 随机生成范围内的x值，x与水母左右运动方向相关
            print('%sdrag %d (270,520) to (%d,630).'%(time.strftime("%Y-%m-%d %H:%M:%S "),num,x))
            device.drag((270, 520), (x, 630), 1, 10) # 滑动屏幕从 (270,520) 到 (x,630),持续时间1秒
            MonkeyRunner.sleep(interval_time)
            num += 1
        print(time.strftime("%Y-%m-%d %H:%M:%S ") + "Play test finished.")
