from com.android.monkeyrunner import MonkeyRunner,MonkeyDevice
device = MonkeyRunner.waitForConnection()
if not device:
    print("Please connect a device to start!")
else:
    print("Install package test start!")
device.installPackage("E:/dontstop/JellyFishBig.apk")
print("Install Finish.")
