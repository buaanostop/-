# -*- coding: utf-8 -*-
"""
MonkeyServer
通过socket接受关于MonkeyRunner的指令并在cmd中执行。
"""
"""
更新日志 2019.04.17
1.在连接上设备后，会在根目录connectlog.txt中写入True,UI可以直接查看该connectlog.txt文档。
  在使用connect操作时触发，所以之前需要UI重写根目录下的connectlog.txt中的内容为False
"""
"""
更新日志 2019.04.14
1.在Test类中增加了 isconnect()方法，返回是否连接设备
    如果连接设备返回 True, 否则返回False

2.加入截图功能ScreenShot类，伴随Test类中方法的调用自动启动，
  图片存在路径 ScreenShot 中的 self.__path
  图片时间Log文件 存在 self.__logpath
  每一行格式为 图片名 秒级时间戳
  例如
  1.png 1555228887
  2.png 1555228889
  3.png 1555228891
  4.png 1555228892
  使用时，可读取秒级时间戳并转换成需要的格式，转换方法如下
    import time
    timeStamp = 1381419600 #秒级时间戳
    timeArray = time.localtime(timeStamp)
    otherStyleTime = time.strftime("%Y--%m--%d %H:%M:%S", timeArray)
    print otherStyleTime   # 2013--10--10 23:40:00

3.cmd信息存入
    具体在Test类 writelog方法中
    设定log文件路径在Test的 __init__方法中
    信息写入Log文件，并同时在cmd中打印
"""
import sys
import time
import socket
import random
import threading
from com.android.monkeyrunner import MonkeyRunner
from com.android.monkeyrunner import MonkeyDevice
from com.android.monkeyrunner import MonkeyImage

#sys.stdout = open("E:/dontstop/example/log.txt")
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
        
class ScreenShot(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.__device = None
        self.__flag = threading.Event()
        self.__flag.clear()
        self.__running = threading.Event()
        self.__running.set()
        self.__isstart = False
        self.__count = 0
        self.__path = None
        self.__logpath = None

    def addpath(self,path):
        self.__path = path + '/screenshot/'
        self.__logpath = self.__path + 'log.txt'

        logfile = open(self.__logpath,'w')
        logfile.close()
        
    def connect(self,device):
        self.__device = device
        
    def pause(self):
        self.__flag.clear()

    def resume(self):
        self.__flag.set()

    def stop(self):
        self.__flag.set()
        self.__running.clear()

    def runstart(self):
        self.__running.set()
        
    def isstart(self):
        return self.__isstart

    def run(self):
        self.__isstart = True
        
        while True:
            self.__running.wait()
            self.__flag.wait()
            self.__count += 1
            result = self.__device.takeSnapshot()
            shottime = time.time()
            shottime = int(shottime) # 秒级时间戳
            filename = self.__path + str(self.__count) + '.png'
            result.writeToFile(filename,'png')

            #写入log
            logfile = open(self.__logpath,'a')
            logfile.write(str(self.__count)+'.png '+str(shottime)+'\n')
            logfile.close()
#            print("ScreenShot"+str(self.__count))
            time.sleep(0.5)
        
class Test(threading.Thread):
    
    def __init__(self):
        """初始化"""
        threading.Thread.__init__(self)
        self.__flag = threading.Event() # 暂停标志
        self.__flag.set() # 设为True
        self.__running = threading.Event() # 运行标志
        self.__running.clear() # 设为False
        self.__resolution_x = 0 # 分辨率x
        self.__resolution_y = 0 # 分辨率y
        self.__device = None # 设备
        self.__oplist = [] # 模拟操作的列表
        self.__isstart = False
        self.__shot = ScreenShot()
        self.__logpath = None #log文件地址
        self.__connectlogpath = None

    def addpath(self,path): #添加log文件地址
        self.__logpath = path+"/log.txt"
        self.__connectlogpath = path+"/connectlog.txt"
        self.__shot.addpath(path)
#        print(self.__logpath)
        logfile = open(self.__logpath,'w')
        logfile.close()
        
    def writelog(self,data):
        print(data)
        logfile = open(self.__logpath,'a')
        logfile.write(data+'\n')
        logfile.close()

    def writeconnectlog(self):
        connectlog = open(self.__connectlogpath,'w')
        connectlog.write("True")
        connectlog.close()
        
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
        self.writelog(time.strftime("%Y-%m-%d %H:%M:%S ") + "Connect ...")
#        print(data)
#        print(data)
#        print(time.strftime("%Y-%m-%d %H:%M:%S ") + "Connect ...")
        self.__device = MonkeyRunner.waitForConnection() # 连接设备或模拟器
        if not self.__device:
            self.writelog("Please connect a device to start.")

            return 0
        else:
            self.__shot.connect(self.__device)
            self.writelog(time.strftime("%Y-%m-%d %H:%M:%S ") + "Connection success")
            self.writelog("Connect to : %s"%self.__device)
            
            
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
        self.writelog(time.strftime("%Y-%m-%d %H:%M:%S ") + "Oppen application ...")
        self.__device.startActivity(component = package_name + "/" + activity_name)
        MonkeyRunner.sleep(10)
        self.writelog(time.strftime("%Y-%m-%d %H:%M:%S ") + "Open application succeeded.")

    def pause(self):
        self.writelog("pause")
        self.__shot.pause()
        self.__flag.clear()

    def resume(self):
        self.writelog("resume")
        self.__shot.resume()
        self.__flag.set()

    def stop(self):
        self.writelog("stop")
        self.__shot.stop()
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
        self.writelog("touch test add success")

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
        self.writelog("random_touch test add success")

    def press(self, key_name):
        """按键测试
        参数
        -----------
        key_name : string
                按键的名字

        """
        op = Operation('press',0,0,0,0,0,0,0,key_name)
        self.__oplist.append(op)
        self.writelog("press test add success")

    def typestr(self, typestring):
        """键盘输入测试
        参数
        -------
        typestring : string
                    要输入的字符串
        """
        op = Operation('typestr',0,0,0,0,0,0,0,typestring)
        self.__oplist.append(op)
        self.writelog("typestr test add success")
              
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
        self.writelog("drag test add success")
            
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
        self.writelog("random_drag test add success")

    def runstart(self):
        self.__shot.runstart()
        self.__running.set()

    def isstart(self):
        """判断是否启动线程"""
        return self.__isstart

    def isconnect(self):
        """判断是否连接设备"""
        if self.__device:
            return True
        else:
            return False
    def run(self):
        self.__shot.start()
        self.__isstart = True
        
        while True:
            self.__running.wait()
            opnum = len(self.__oplist)
            if(opnum <= 0):
                self.writelog("no test")
            else:
                self.__shot.resume()
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
                            self.writelog("%stouch %d (%d,%d)."%(time.strftime("%Y-%m-%d %H:%M:%S "), num, pos_x, pos_y))
                            self.__device.touch(pos_x, pos_y, 'DOWN_AND_UP')
                            num += 1
                            MonkeyRunner.sleep(interval_time)
                        else:
                            self.__oplist[:] = []
                            break
                            
    # random_touch
                elif op.optype == 'random_touch':
                    touch_number = op.number
                    interval_time = op.interval_time
                    self.writelog(time.strftime("%Y-%m-%d %H:%M:%S ") + "Random touch test start.")
                    num = 1
                    while(num <= touch_number):
                        if self.__running.isSet():
                            self.__flag.wait()
                            x = random.randint(0, self.__resolution_x) # 随机生成位置x
                            y = random.randint(0, self.__resolution_y) # 随机生成位置y
                            self.writelog("%srandom_touch %d (%d,%d)."%(time.strftime("%Y-%m-%d %H:%M:%S "),num,x,y))
                            self.__device.touch(x, y, 'DOWN_AND_UP') # 点击(x,y)
                            MonkeyRunner.sleep(interval_time)
                            num += 1
                        else:
                            self.__oplist[:] = []
                            break
                    if self.__running.isSet():
                        self.writelog(time.strftime("%Y-%m-%d %H:%M:%S ") + "Random touch test finished.")
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
                            self.writelog("%sdrag %d (%d,%d) to (%d,%d)."%(time.strftime("%Y-%m-%d %H:%M:%S "),num,start_x,start_y,end_x,end_y))
                            self.__device.drag((start_x, start_y), (end_x, end_y), drag_time, 10)
                            MonkeyRunner.sleep(interval_time)
                            num += 1
                        else:
                            self.__oplist[:] = []
                            break

    #random_drag
                elif op.optype == 'random_drag':
                    drag_number = op.number
                    interval_time = op.interval_time
                    self.writelog(time.strftime("%Y-%m-%d %H:%M:%S ") + "Random drag test start.")
                    num = 1
                    while(num <= drag_number):
                        if self.__running.isSet():
                            self.__flag.wait()
                            x_start = random.randint(0, self.__resolution_x)
                            y_start = random.randint(0, self.__resolution_y)
                            x_end = random.randint(0,self.__resolution_x)
                            y_end = random.randint(0,self.__resolution_y)
                            self.writelog("%srandom_drag %d (%d,%d) to (%d,%d)."%(time.strftime("%Y-%m-%d %H:%M:%S "),num,x_start,y_start,x_end,y_end))
                            self.__device.drag((x_start, y_start), (x_end, y_end), 1, 10)
                            MonkeyRunner.sleep(interval_time)
                            num += 1
                        else:
                            self.__oplist[:] = []
                            break
                    if self.__running.isSet():
                        self.writelog(time.strftime("%Y-%m-%d %H:%M:%S ") + "Random drag test finished.")                

    #press
                elif op.optype == 'press':
                    key_name = op.keyorstring
                    if self.__running.isSet():
                        self.__flag.wait()
                        self.writelog("%spress %s."%(time.strftime("%Y-%m-%d %H:%M:%S "),key_name))
                        self.__device.press(key_name, 'DOWN_AND_UP')
                    else:
                        self.__oplist[:] = []
                        break
    #typestr
                elif op.optype == 'typestr':
                    typestring = op.keyorstring
                    if self.__running.isSet():
                        self.writelog("%stype %s."%(time.strftime("%Y-%m-%d %H:%M:%S "),typestring))
                        self.__device.type(typestring)
                    else:
                        self.__oplist[:] = []
                        break
                else:
                    self.writelog("optype error")
                    
            self.__shot.pause()
            self.__oplist[:] = []
            self.__running.clear()
            
            
##
##Socket相关
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("", 8081))

t = Test()

print("MonkeyServer start")

while True:
    data, addr = s.recvfrom(1024)
    # print(data)
    (optype,x1,y1,x2,y2,number,interval_time,drag_time,keyorstring) = data.split(':')
    # 类型转换，从data中的str类型转换成各自的类型
    x1 = int(x1)
    y1 = int(y1)
    x2 = int(x2)
    y2 = int(y2)
    number = int(number)
    interval_time = float(interval_time)
    drag_time = float(drag_time)
    # 判断命令类型并执行
    if optype == 'connect':
        t.addpath(chr(x1)+':'+keyorstring)
        t.connect()
    elif optype == 'start':
        if not t.isstart():
            t.start()
        t.runstart()
    elif optype == 'pause':
        t.pause()
    elif optype == 'resume':
        t.resume()
    elif optype == 'stop':
        t.stop()
    elif optype == 'open_app':
        (package_name, activity_name) = keyorstring.split('&')
        t.open_app(package_name, activity_name)
    elif optype == 'touch':
        t.touch(x1, y1, number, interval_time)
    elif optype == 'random_touch':
        t.random_touch(number, interval_time)
    elif optype == 'press':
        t.press(keyorstring)
    elif optype == 'typestr':
        t.typestr(keyorstring)
    elif optype == 'drag':
        t.drag(x1, y1, x2, y2, drag_time, number, interval_time)
    elif optype == 'random_drag':
        t.random_drag(number, interval_time)
    else:
        print("no such optype")
        
    # print("%s:%d:%d:%d:%d:%d:%f:%f:%s"%(optype,x1,y1,x2,y2,number,interval_time,drag_time,keyorstring))
    
    
