# -*- coding: utf-8 -*-
"""浮光游戏试玩测试
点击第一个按键后，随机向下滑动，让水母向上游动
"""
import time
import sys
import random
from com.android.monkeyrunner import MonkeyRunner,MonkeyDevice,MonkeyImage
device = MonkeyRunner.waitForConnection() #连接设备
sleepTime = 3 #滑动间隔时间

if not device:
    print("Please connect a device to start!")
else:
    print("Test start!")
print(time.strftime("%Y-%m-%d-%H-%M-%S ") + "Try to open app.")
device.startActivity(component='com.Jelly.JellyFish/com.unity3d.player.UnityPlayerActivity') #打开应用
MonkeyRunner.sleep(10)
print(time.strftime("%Y-%m-%d-%H-%M-%S ") + "App open success.")
print(time.strftime("%Y-%m-%d-%H-%M-%S ") + "Start play test.")
device.touch(280, 460, 'DOWN_AND_UP') # 按第一个键
MonkeyRunner.sleep(10)
num = 1
while(num <= 20): # 20次滑动
    x = random.randint(70,470) # 随机生成范围内的x值，x与水母左右运动方向相关
    print('%sdrag %d (270,520), (%d,630).'%(time.strftime("%Y-%m-%d-%H-%M-%S "),num,x))
    device.drag((270, 520), (x, 630), 1, 10) # 滑动屏幕从 (270,520) 到 (x,630),持续时间1秒
    MonkeyRunner.sleep(sleepTime)
    num += 1
print(time.strftime("%Y-%m-%d-%H-%M-%S ")+"Test finish.")
