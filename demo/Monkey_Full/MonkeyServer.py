# -*- coding: utf-8 -*-
"""
monkey server
在cmd中运行的脚本文件
由Monkey.py中的代码在cmd中打开Monkeyrunner + 此脚本文件
通过socket接收来自Monkey.py发送的信息，根据信息进行操作
"""
import socket
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage
import traceback
import os
import threading
import time
device = None
resolution_ratio = (540, 960)
rootpath = ""
class ScreenShot(threading.Thread):
    """截图"""
    def __init__(self):
        threading.Thread.__init__(self)
        self.device = None
        self.count = 1
        self.path = None
        #self.logpath = None
        self.flag = threading.Event() # 运行标志
        self.flag.clear()
    def connect(self, device):
        self.device = device
        
    def addpath(self, path):
        global rootpath
        rootpath = path
        self.path = path + '/screenshot/shot'
        #self.logpath = path + '/log_new.txt'

    def pause(self):
        self.flag.clear()

    def resume(self):
        self.flag.set()

    def clear(self):
        self.count = 1
        
    def run(self):

        while True:
            try:
                self.flag.wait()
                time.sleep(1.0)
                result = device.takeSnapshot()
                shottime = int(time.time())
                filename = self.path + str(self.count) + '.png'
                result.writeToFile(filename, 'png')

                #logfile = open(self.logpath, 'a')
                #logfile.write('shot'+str(self.count)+'.png '+str(shottime) + '\n')
                #logfile.close()
                self.count += 1
            except:
                traceback.print_exc()
                #os.system("pause")
            
def __connect():
    global device
    print("connect")
    sendsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sendport = 12346
    sendhost = '127.0.0.1'
    
    device = MonkeyRunner.waitForConnection(5)
    try:
        name = device.getProperty("build.device")
        ratio_x = device.getProperty("display.width")
        ratio_y = device.getProperty("display.height")
        ratio = str(ratio_x)+'x'+str(ratio_y)
        data = ratio.encode("utf-8")
        print(data)
        shot.connect(device)
        sendsocket.sendto(data, (sendhost, sendport))
    except:
        data = data = "connect false".encode("utf-8")
        sendsocket.sendto(data, (sendhost, sendport))
   
def __open_app(package_name, activity_name):
    print("open_app",package_name,activity_name)
    device.startActivity(package_name+'/'+activity_name)
    
def __touch(pos_x, pos_y):
    global device
    print("touch ",pos_x,pos_y)
    device.touch(pos_x, pos_y, MonkeyDevice.DOWN_AND_UP)
    
def __down(pos_x, pos_y):
    print("down ",pos_x,pos_y)
    device.touch(pos_x, pos_y, MonkeyDevice.DOWN)

def __move(pos_x, pos_y):
    print("move",pos_x, pos_y)
    device.touch(pos_x, pos_y, MonkeyDevice.MOVE)

def __up(pos_x, pos_y):
    print('up',pos_x, pos_y)
    device.touch(pos_x, pos_y, MonkeyDevice.UP)
    
def __drag(x1, y1, x2, y2, hold_time):
    print("drag", x1, y1, x2, y2, hold_time)
    device.drag((x1,y1),(x2,y2), hold_time, 10)

def __press(button):
    print("press",button)
    device.press(button, MonkeyDevice.DOWN_AND_UP)
    
def __typestr(typestring):
    print("typestr",typestring)
    device.type(typestring)

def __refresh():
    print("refresh")
    shotfile = device.takeSnapshot()
    filename = rootpath + "/refreshshot.png"
    shotfile.writeToFile(filename, 'png')
    print("refreshshot.png save to "+filename)

def __close():
    print("close")
    s.close()
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(("", 12345))
    print("Monkey Server Start")
    shot = ScreenShot()
    shot.setDaemon(True)
    shot.start()
except:
    traceback.print_exc()
    os.system("pause")
try:
    while True:
        shot.pause()
        data, addr = s.recvfrom(1024)
        print(data)
        (optype, x1, y1, x2, y2, hold_time, keyorstring) = data.split(':')
        x1 = int(x1)
        y1 = int(y1)
        x2 = int(x2)
        y2 = int(y2)
        hold_time = float(hold_time)
        
        if optype == "connect":
            shot.addpath(keyorstring.replace('&',':'))
            __connect()
            continue
        elif optype == "open_app":
            (package_name, activity_name) = keyorstring.split('&')
            __open_app(package_name, activity_name)
            continue
        elif optype == "clearshot":
            shot.clear()
            continue
        elif optype == "refresh":
            __refresh()
            continue
            
        else:
            shot.resume()
        
        if optype == "touch":
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
            shot.pause()
            __close()
            break
        else:
            print("don't have this oder")
            print(optype,x1,y1,x2,y2,hold_time,keyorstring)
except:
    traceback.print_exc()
    #os.system("pause")
        
