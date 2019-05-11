import socket
import time
import sys
import traceback
import os
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("", 12345))

try:
    sendsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    port = 12346
    host = '127.0.0.1'
    print("server start")
    while True:
        data, addr = s.recvfrom(1024)
        (optype, x1, y1, x2, y2, hold_time, keyorstring) = data.split(':')
        print(optype,keyorstring)
        if optype == "close":
            s.close()
            break
        elif optype == "connect":
            print("rec connect")
            time.sleep(3)
            data = "connect true".encode("utf-8")
            sendsocket.sendto(data, (host, port))
    print("server close")
except :
    traceback.print_exc()
    os.system("pause")
    
