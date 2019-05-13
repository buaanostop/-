import socket
import time
import sys
import traceback
import os

from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
device = None
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(("", 12345))
except:
    traceback.print_exc()
    os.system("pause")    
try:
    sendsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    port = 12346
    host = '127.0.0.1'
    print("server start")
    recnum = 1
    while True:
        data, addr = s.recvfrom(1024)
        (optype, x1, y1, x2, y2, hold_time, keyorstring) = data.split(':')
        x1 = int(x1)
        y1 = int(y1)
        x2 = int(x2)
        y2 = int(y2)
        hold_time = float(hold_time)
        print(optype,keyorstring,recnum)
        recnum += 1
        if optype == "close":
            #s.close()
            break
        elif optype == "connect":
            print("rec connect")
            device = MonkeyRunner.waitForConnection(5)
            try:
                name = device.getProperty("build.device")
                data = "connect true".encode("utf-8")
                sendsocket.sendto(data, (host, port))
            except:
                data = "connect false".encode("utf-8")
                sendsocket.sendto(data, (host, port))
        elif optype == "touch":
            device.touch(x1,y1,MonkeyDevice.DOWN_AND_UP)
            print("dotouch",x1,y1)

        elif optype == "drag":
            device.drag((x1,y1),(x2,y2),hold_time,10)
    print("server close")
#    os.system("pause")
except :
    traceback.print_exc()
    os.system("pause")

