# -*- coding: utf-8 -*-
"""点击浮光游戏中的按键测试
"""
import time
import sys
from com.android.monkeyrunner import MonkeyRunner,MonkeyDevice,MonkeyImage
device = MonkeyRunner.waitForConnection() # 连接设备
sleepTime = 3 # 按键的间隔时间
if not device:
    print("Please connect a device to start!")
else:
    print("Test start!")
print(time.strftime("%Y-%m-%d-%H-%M-%S ")+"Try to open app.")
device.startActivity(component='com.Jelly.JellyFish/com.unity3d.player.UnityPlayerActivity') # 打开应用
MonkeyRunner.sleep(10)
print(time.strftime("%Y-%m-%d-%H-%M-%S ")+"App open success.")
print(time.strftime("%Y-%m-%d-%H-%M-%S ")+"Start press test.")
device.touch(280, 540, 'DOWN_AND_UP') # 按第二个键
MonkeyRunner.sleep(sleepTime)
device.touch(435, 850, 'DOWN_AND_UP') # 按返回键
MonkeyRunner.sleep(sleepTime)
device.touch(280, 640, 'DOWN_AND_UP') # 按第三个键
MonkeyRunner.sleep(sleepTime)
device.touch(435, 850, 'DOWN_AND_UP') # 按返回键
MonkeyRunner.sleep(sleepTime)
device.touch(280, 720, 'DOWN_AND_UP') # 按第四个键
MonkeyRunner.sleep(sleepTime)
device.touch(435, 850, 'DOWN_AND_UP') # 按返回键
