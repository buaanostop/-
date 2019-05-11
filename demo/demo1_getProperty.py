# -*- coding: utf-8 -*-
"""
自动获取设备的分辨率

"""

"""
此种方法有一定的问题需要进一步讨论
在获取分辨率时不带设备下部的虚拟按键部分
例如一台实际显示屏幕分辨率 1920 * 1080的设备
在通过monkeyrunner获取到的分辨率就是 1812*1080
如果需要获取到包含虚拟按键的部分，可以用demo2中先截图再获取截图信息的方法

"""
from com.android.monkeyrunner import MonkeyRunner
from com.android.monkeyrunner import MonkeyDevice

device = MonkeyRunner.waitForConnection(5) #等待时间5秒
if not device:
    print("Please connect your device.")
else:
    print("Connect success.")

x = device.getProperty("display.height")
y = device.getProperty("display.width")

print(x,y)
