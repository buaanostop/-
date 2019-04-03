import time
import sys
import random
from com.android.monkeyrunner import MonkeyRunner,MonkeyDevice,MonkeyImage
device = MonkeyRunner.waitForConnection()
sleepTime = 3
now = time.strftime("%Y-%m-%d-%H-%M-%S ")
if not device:
    print("Please connect a device to start!")
else:
    print("Test start!")
print(now + "Try to open app.")
device.startActivity(component='com.Jelly.JellyFish/com.unity3d.player.UnityPlayerActivity')
MonkeyRunner.sleep(10)
print(now + "App open success.")
print(now + "Start play test.")
device.touch(280, 460, 'DOWN_AND_UP')
MonkeyRunner.sleep(10)
num = 1
while(num <= 20):
    x = random.randint(70,470)
    print('%sdrag %d (270,520), (%d,630).'%(now,num,x))
    device.drag((270, 520), (x, 630), 1, 10)
    MonkeyRunner.sleep(sleepTime)
    num += 1
print(now+"Test finish.")
