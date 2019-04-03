import time
import sys
from com.android.monkeyrunner import MonkeyRunner,MonkeyDevice,MonkeyImage
device = MonkeyRunner.waitForConnection()
sleepTime = 3
now = time.strftime("%Y-%m-%d-%H-%M-%S ")
if not device:
    print("Please connect a device to start!")
else:
    print("Test start!")
print(now+"Try to open app.")
device.startActivity(component='com.Jelly.JellyFish/com.unity3d.player.UnityPlayerActivity')
MonkeyRunner.sleep(10)
print(now+"App open success.")
print(now+"Start press test.")
device.touch(280, 540, 'DOWN_AND_UP')
MonkeyRunner.sleep(sleepTime)
device.touch(435, 850, 'DOWN_AND_UP')
MonkeyRunner.sleep(sleepTime)
device.touch(280, 640, 'DOWN_AND_UP')
MonkeyRunner.sleep(sleepTime)
device.touch(435, 850, 'DOWN_AND_UP')
MonkeyRunner.sleep(sleepTime)
device.touch(280, 720, 'DOWN_AND_UP')
MonkeyRunner.sleep(sleepTime)
device.touch(435, 850, 'DOWN_AND_UP')
