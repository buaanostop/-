# _*_ coding:utf-8 _*_
"""
Monkey.py
作用为从UI获取具体的操作
通过socket发送消息给MonkeyServer进行具体操作
简化MonkeyServer的功能，仅接受信息并进行简单操作。
功能：
1.创建测试队列
2.保存、读取测试队列
3.控制测试的运行

"""
import sys
import time
import random
import os
from Operation import *
from MonkeySender import *
import threading
import shutil


        
#----------------------
#测试队列所用参数
oplist = []
allrandomlist = []
resolution_ratio = (1080, 1920) #需要获取 分辨率 （x, y)
test = None # 测试线程
#----------------------
#文件路径相关参数
rootpath = os.getcwd() # 当前根目录
logpath = "log.txt" # Log文件名
savepath = rootpath+'\save' # 存档文件夹
shotpath = rootpath+'\screenshot' # 截图文件夹
monkeypath = rootpath+'\MonkeyServer.py' # MonkeyServer.py脚本路径
log_new_path = shotpath + '\log_new.txt' # ScreenShot Log 文件路径
#----------------------
#前期准备
##检测save文件夹是否存在，不存在则创建save文件夹
if not os.path.exists(savepath):
    os.makedirs(savepath)
##检测screenshot文件夹是否存在，不存在则创建screenshot文件夹
if not os.path.exists(shotpath):
    os.makedirs(shotpath)
else:
    shutil.rmtree(shotpath)
    os.makedirs(shotpath)
##清空Log文件
logfile = open(logpath, 'w')
logfile.close()
##清空screenshot文件夹Log文件
#log_new_file = open(log_new_path, 'w') #不要screenshot的log文件
#log_new_file.close()

##启动MonkeyServer
thread_monkey = do_run_monkey(monkeypath)
thread_monkey.start()

def __ifprint(data):
    """写入Log同时打印信息，若不想打印则注释掉下面的print"""
    print(data)
    
def __writelog(data):
    """把信息写入log文件"""
    __ifprint(data)
    logfile = open(logpath, 'a')
    logfile.write(data + '\n')
    logfile.close()
        
def __now():
    """返回当前时间信息"""
    return str(time.strftime("%Y-%m-%d %H:%M:%S "))

##-------------------------------
##针对设备的操作
def connect():
    """连接设备
    返回值
    ----------
    Tuple : (x,y) 连接成功 返回分辨率
    bool :  False 连接失败
    """
    __writelog(__now() + "connect...")
    return do_connect()

def open_app(package_name, activity_name):
    """打开应用
    参数
    ----------
    package_name : string 
                    包名 例如 com.Jelly.JellyFish
    activity_name : string
                    活动名 例如 com.unity3d.player.UnityPlayerActivity
    返回值
    ---------

    """
    __writelog(__now() + "open app")
    do_open_app(package_name, activity_name)
    return True

def set_resolution_ratio(width, height):
    """设定分辨率 （用于手动修改）
    参数
    ------------
    width : int
            宽度
    height : int
            高度
    """
    resolution_ratio = (width, height)
    return resolution_ratio

##----------------------------------------
##针对测试列表的操作
def refresh():
    """刷新屏幕"""
    do_refresh()
    
def clear():
    """清空测试列表"""
    oplist.clear()
    return oplist

def now_running():
    """返回当前正在进行的测试
    返回值
    -----------
    int : 测试的序号，0开始，在没有开始或已经结束的情况下返回-1

    """
    return do_now_running()

def delete(index):
    """删除列表中第index个测试
    参数
    -------------
    index : int
            要删除的位置（从1开始）

    """
    oplist.pop(index - 1)
    return oplist

def change(index1, index2):
    """将原来在Index1的测试调到位置Index2
    参数
    -----------
    index1: int
            原来的位置（从1开始）
    index2: int
            改变后的位置（从1开始）
    
    """
    op = oplist.pop(index1 - 1)
    oplist.insert(index2 - 1, op)
    return oplist
    
def save(save_name):
    """将oplist保存
    参数
    -------------
    save_name : string
                存档的路径
    返回值
    -------------
    bool : True 保存成功
            False 保存失败
    """
    try:
        f = open(save_name,'w')
        for op in oplist:
            f.write(str(op.todict())+'\n')
        f.close()
        __writelog(__now() + save_name + " save success")
        return True
    except:
        f.close()
        __writelog(__now() + save_name + " save fail")
        return False

def load(save_name):
    """读取存档
    参数
    -----------
    save_name : string
                存档的路径
    返回值
    -----------
    List(Operation) : 读取成功，返回列表
    bool : False 读取失败
    """
    try:       
        clear() # 清空当前oplist
        f = open(save_name,'r')
        data = f.readline()
        while data:
            data = eval(data)
            op = Operation(data['optype'],data['pointlist'],data['number'],data['interval_time'],
                            data['hold_time'],data['keyorstring'],data['wait_time'])
            oplist.append(op)
            data = f.readline()
        f.close()
        __writelog(__now() + save_name + " load success")
        return oplist
    except:
        f.close()
        __writelog(_now() + save_name + " load fail")
        return False

def all_random(test_number=100):
    """生成完全随机测试
    参数
    -----------
    test_number : int
                生成的测试项个数，默认为100
    返回值
    list[Operation]
    随机操作的队列

    """
    num = 0
    testtype = ['touch','long_touch','drag','touch_drag']
    testtime = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0]
    max_x = resolution_ratio[0] - 1
    max_y = resolution_ratio[1] - 1
    allrandomlist.clear()
    while num < test_number:
        index = random.randint(0,3)
        if index == 0: # touch
            x1 = random.randint(0, max_x)
            y1 = random.randint(0, max_y)
            touch(x1, y1)
        elif index == 1: # long_touch
            x1 = random.randint(0, max_x)
            y1 = random.randint(0, max_y)
            t1 = random.randint(0, 3)
            long_touch(x1, y1, testtime[t1])
        elif index == 2: # drag
            x1 = random.randint(0, max_x)
            y1 = random.randint(0, max_y)
            x2 = random.randint(0, max_x)
            y2 = random.randint(0, max_y)
            t1 = random.randint(0, 5)
            drag(((x1,y1),(x2,y2)), testtime[t1])
        elif index == 3: # touch_drag
            x1 = random.randint(0, max_x)
            y1 = random.randint(0, max_y)
            x2 = random.randint(0, max_x)
            y2 = random.randint(0, max_y)
            t1 = random.randint(0, 3)
            t2 = random.randint(0, 5)
            touch_drag(((x1,y1),(x2,y2)), testtime[t1], testtime[t2])         
        num += 1
    __writelog(__now() + "all_random test add success")
    return allrandomlist

def close():
    __writelog(__now() + "close")
    do_close()
    return True
##-------------------------------
##添加各种测试项
def touch(pos_x, pos_y, touch_number=1, interval_time=1.0):
    """单击
    参数
    -------------
    pos_x : int
            点击的位置横坐标
    pos_y : int
            点击的位置纵坐标
    touch_numbere : int
            点击的次数，默认为1
    interval_time : float
            多次点击间隔时间,默认为1秒

    """
    op = Operation('touch', ((pos_x, pos_y),), touch_number, interval_time, 0, 0, 0)
    oplist.append(op)
    allrandomlist.append(op)
    __writelog(__now() + "touch test add success")
    return op

def long_touch(pos_x, pos_y, touch_time=1.0, touch_number=1, interval_time=1.0):
    """长按测试
    参数
    -----------
    pos_x : int
            点击的位置x
    pos_y : int
            点击的位置y
    touch_time: float
            按住的时间，默认为1秒
    touch_number : int
            长按的次数
    interval_time : float
            每次长按间隔的时间
    
    """
    op = Operation('long_touch', ((pos_x, pos_y),), touch_number, interval_time, touch_time, 0, 0)
    oplist.append(op)
    allrandomlist.append(op)
    __writelog(__now() + "long_touch test add success")
    return op
    
def multi_touch(pointlist, loop_number=1, interval_time = 1.0, loop_time = 1.0):
    """多位置顺序单击
    参数
    ---------------
    pointlist : ((x1,y1),(x2,y2),...(x10,y10)),x,y均为int
                多个位置的坐标
                当前限定为10个点
    loop_number : int
                循环的遍数，默认为1
    interval_time : float
                两次点击的间隔时间,默认为1秒
    loop_time : float
                两遍循环的间隔时间，默认为1秒

    """
    op = Operation('multi_touch', pointlist, loop_number, interval_time, 0, 0, loop_time)
    oplist.append(op)
    __writelog(__now() + "multi_touch add success")
    return op
    
def random_touch(pointlist, touch_number=1, interval_time=1.0):
    """随机点击屏幕测试
    参数
    -----------
    pointlist : ((x1,y1),(x2,y2)) x,y均为int 或 None
                由两个点围成的矩形为随机的范围
                如果传入None 则没有范围，在全屏内随机
    touch_number : int
                点击的次数
    interval_time : float
                每两次点击间隔的时间，默认为1秒
    """
    op = Operation('random_touch', pointlist, touch_number, interval_time, 0, 0, 0)
    oplist.append(op)
    __writelog(__now() + "random_touch test add success")
    return op

def drag(pointlist, drag_time=1.0, drag_number=1, interval_time=1.0):
    """滑动屏幕测试
    参数
    ---------------
    pointlist : ((x1,y1),(x2,y2)) x,y均为int
                滑动的起点和终点
    drag_time : float
            滑动持续时间,默认为1秒
    drag_number : int
            滑动次数，默认为1次
    interval_time : float
            滑动间隔时间，默认为1秒
    """
    op = Operation('drag', pointlist, drag_number, interval_time, drag_time, 0, 0)
    oplist.append(op)
    allrandomlist.append(op)
    __writelog(__now() + "drag test add success")
    return op

def multi_drag(pointlist, loop_number=1, interval_time = 1.0, drag_time=1.0, loop_time = 1.0):
    """多位置滑动测试
    参数
    ---------------
    pointlist : ((startx1,starty1,endx1,endy1),(startx2,starty2,endx2,endy2)...),均为int
                多个(起点，终点)位置的坐标
    loop_number : int
                滑动的遍数，默认为1
    interval_time : float
                两次滑动的间隔时间,默认为1秒
    drag_time : float
                每次滑动的持续时间，默认为1秒
    loop_time : float
                两遍滑动的间隔时间，默认为1秒

    """
    op = Operation('multi_drag', pointlist, loop_number, interval_time, drag_time, 0, loop_time)   
    oplist.append(op)
    __writelog(__now() + "multi_drag add success")
    return op
    
def random_drag(pointlist, drag_number=1, interval_time=1.0, drag_time=1.0):
    """随机滑动屏幕测试
    参数
    -----------
    pointlist : ((x1,y1),(x2,y2)) x,y均为int 或 None
                由两个点围成的矩形为随机的范围
                如果传入None 则没有范围，在全屏内随机
    drag_number : int
                随机滑动次数
    interval_time : float
                每两次滑动间隔的时间，默认为1秒
    drag_time : float
                滑动时间，默认为1秒

    """
    op = Operation('random_drag', pointlist, drag_number, interval_time, drag_time, 0, 0)
    oplist.append(op)
    __writelog(__now() + "random_drag test add success")
    return op

def touch_drag(pointlist, touch_time=1.0, drag_time=1.0, touch_number=1, interval_time=1.0):
    """长按滑动测试
    参数
    -----------
    pointlist : ((x1,y1),(x2,y2)) x,y均为int
                按住的点和滑动的终点的坐标
    touch_time : float
                长按的时间，默认为1秒
    drag_time : float
                滑动的时间， 默认为1秒
    touch_number : int
                长按滑动的次数
    interval_time : float
                两次动作的间隔时间

    """
    op = Operation('touch_drag', pointlist, touch_number, interval_time, drag_time, 0, touch_time)
    oplist.append(op)
    allrandomlist.append(op)
    __writelog(__now() + "touch_drag test add success")
    return op
   
def press(key_name):
    """按键测试
    参数
    -----------
    key_name : string
            按键的名字

    """
    op = Operation('press', None, 0, 0, 0, key_name, 0)
    oplist.append(op)
    __writelog(__now() + "press test add success")
    return op

def typestr(typestring):
    """键盘输入测试
    参数
    -------
    typestring : string
                要输入的字符串
    """
    op = Operation('typestr', None, 0, 0, 0, typestring, 0)
    oplist.append(op)
    __writelog(__now() + "typestr test add success")
    return op

def wait(wait_time):
    """等待
    参数
    ------
    wait_time : float
                要等待的时间

    """
    op = Operation('wait', None, 0, 0, 0, 0, wait_time)
    oplist.append(op)
    __writelog(__now() + "wait test add success")
    return op

def print_oplist(): #测试用
    for op in oplist:
        op.display()
        

##-------------------------------
##针对测试线程的操作
def start():
    global test
    __writelog(__now() + "start")
    test = DoTest(oplist)
    test.start()
#    __send("start")
    return True
    
def pause():
    global test
    __writelog(__now() + "pause")
#    __send("pause")
    test.pause()
    return True

def resume():
    global test
    __writelog(__now() + "resume")
#    __send("resume")
    test.resume()
    return True

def stop():
    global test
    __writelog(__now() + "stop")
#    __send("stop")
    test.stop()
    return True

##-------------------------------




