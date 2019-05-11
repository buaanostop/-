# -*- coding: utf-8 -*-
"""判断是否连接"""
from com.android.monkeyrunner import MonkeyRunner,MonkeyDevice,MonkeyImage

device = MonkeyRunner.waitForConnection(3)

try:
    a = device.getProperty("build.device")
    print(str(a))
except :
    print("no device")

    
#java.lang.NullPointerException
