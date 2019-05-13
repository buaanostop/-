import os
"""demo6
开启线程调用demo6
由demo6建立管道打开monkeyrunner和demo5的server
可以不打开cmd窗口实现运行monkeyrunner
"""
def runmonkeyrunner():
    a = os.popen('monkeyrunner E:/dontstop/demo/demo5_testserver.py')

