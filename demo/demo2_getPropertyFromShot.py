# -*- coding: utf-8 -*-
"""
自动获取设备的分辨率

"""

"""
先截图再获取截图信息的方法
缺点：需要使用PIL模块 cmd中执行的脚本文件不能import PIL 使用起来比较麻烦

"""

from com.android.monkeyrunner import MonkeyRunner
from com.android.monkeyrunner import MonkeyDevice
from com.android.monkeyrunner import MonkeyImage

#from PIL import Image

filename = "E:/dontstop/shotforproperty.png"
device = MonkeyRunner.waitForConnection(5) #等待时间5秒
if not device:
    print("Please connect your device.")
else:
    print("Connect success.")

shot = device.takeSnapshot()
shot.writeToFile(filename,"png")
#im = Image.open(filename)
#height = im.size[1]
#width = im.size[0]

#print(height,width)
