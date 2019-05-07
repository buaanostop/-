# -*- coding: utf-8 -*-
"""
monkey server
在cmd中运行的脚本文件
由Monkey.py中的代码在cmd中打开Monkeyrunner + 此脚本文件
通过socket接收来自Monkey.py发送的信息，根据信息进行操作
"""
import socket

def __connect():
    print("connect")

def __open_app(package_name, activity_name):
    pass

def __touch(pos_x, pos_y):
    print("touch ",pos_x,pos_y)

def __drag(x1, y1, x2, y2, hold_time):
    pass

def __press(button):
    pass

def __typestr(typestring):
    pass

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("", 8081))

while True:
    data, addr = s.recvfrom(1024)
    (optype, x1, y1, x2, y2, hold_time, keyorstring) = data.split(':')
    x1 = int(x1)
    y1 = int(y1)
    x2 = int(x2)
    y2 = int(y2)
    hold_time = float(hold_time)

    if optype == "connect":
        __connect()
    elif optype == "open_app":
        (package_name, activity_name) = keyorstring.split('&')
        __open_app(package_name, activity_name)
    elif optype == "touch":
        __touch(x1, y1)
    elif optype == "drag":
        __drag(x1, y1, x2, y2, hold_time)
    elif optype == "press":
        __press(keyorstring)
    elif optype == "typestr":
        __typestr(keyorstring)
    else:
        print("close")
        break
        
