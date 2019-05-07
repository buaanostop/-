# _*_ coding:utf-8 _*_
"""
test monkey
"""
from Monkey import *
import time

connect()

time.sleep(1)

start()

time.sleep(1)

pause()

time.sleep(1)

resume()

time.sleep(1)

stop()

time.sleep(1)

touch(2,3,1,1)

time.sleep(1)

random_touch(10,2)

time.sleep(1)

press("KEYCODE_HOME")

time.sleep(1)

typestr("hello world")

time.sleep(1)

drag(20,30,70,70, 1, 10, 2)

time.sleep(1)

random_drag(10,1)

print_oplist()

time.sleep(3)

closeMonkeyServer()
