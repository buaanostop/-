import os
import subprocess
import signal

class LogCat():

    def __init__(self):
        self.logpath = os.getcwd() + "/logcat.txt"
        self.packageName = " "
        self.pid = 0
        self.flag = False
        self.fderr = open(os.getcwd()+"/pipe.err", 'w')
        self.logfile = open(self.logpath, 'w')
        self.log = None
        
    def __getPackageName(self):
#        print("getPackageName")
        root = os.popen("adb root")
        print("already root")
        data = os.popen("adb shell dumpsys window | findstr mCurrentFocus")
        mCurrentFocus = data.read()
        list1 = mCurrentFocus.split(' ')
        print(list1)
        errtime = 0
        while len(list1) != 5:
            data = os.popen("adb shell dumpsys window | findstr mCurrentFocus")
            mCurrentFocus = data.read()
            list1 = mCurrentFocus.split(' ')
            print(list1)
            errtime += 1
            print(errtime)
            if errtime >=5:
                return False
        list2 = list1[4].split('/')
        self.packageName = list2[0] # 包名
        print(self.packageName)
        return True
    def start(self, level = 'W'):
        if not self.__getPackageName():
            return False
        os.popen("adb logcat -c") # 清空缓存
        print("adb logcat clear")
        command = "adb shell logcat *:" + level + " --pid=$(pidof -s " + self.packageName + ")"
#        print("command ready",command)
        st = subprocess.STARTUPINFO
        st.dwFlags = subprocess.STARTF_USESHOWWINDOW
        st.wShowWindow=subprocess.SW_HIDE
#        print("next is self.log")
        self.log = subprocess.Popen(command,stdout = self.logfile, stderr = self.fderr, shell=True, startupinfo=st)
##        print(command)
##        print("readytopopen")
##        log = subprocess.Popen(command, shell = True)
        self.flag = True
        self.pid = self.log.pid
        print(self.log.pid)
        
    def close(self):
        if self.flag and self.pid != 0:
            try:
                self.log.terminate()
                os.popen("adb kill-server")
            except :
                pass
            return True
        else:
            return False
