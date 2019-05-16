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
##    time.sleep(5)
##    sendsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
##    sendport = 12346
##    sendhost = '127.0.0.1'
##    data = bytes("connect true",encoding="utf8")
##    sendsocket.sendto(data, (host, port))
    
def __open_app(package_name, activity_name):
    print("open_app",package_name,activity_name)

def __touch(pos_x, pos_y):
    print("touch ",pos_x,pos_y)

def __down(pos_x, pos_y):
    print("down ",pos_x,pos_y)

def __move(pos_x, pos_y):
    print("move",pos_x, pos_y)

def __up(pos_x, pos_y):
    print('up',pos_x, pos_y)
    
def __drag(x1, y1, x2, y2, hold_time):
    print("drag", x1, y1, x2, y2, hold_time)

def __press(button):
    print("press",button)

def __typestr(typestring):
    print("typestr",typestring)


def __close():
    print("close")
    
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("", 12345))
print("Monkey Server Start")

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
    elif optype == "down":
        __down(x1, y1)
    elif optype == "move":
        __move(x1, y1)
    elif optype == "up":
        __up(x1, y1)
    elif optype == "drag":
        __drag(x1, y1, x2, y2, hold_time)
    elif optype == "press":
        __press(keyorstring)
    elif optype == "typestr":
        __typestr(keyorstring)
    elif optype == "close":
        __close()
        break
    else:
        print("don't have this oder")
        print(optype,x1,y1,x2,y2,hold_time,keyorstring)
        
        
