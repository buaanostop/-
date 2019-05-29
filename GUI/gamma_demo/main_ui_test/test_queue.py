import queue
import threading
class test_thread(threading.Thread):
    q = queue.Queue()
    found_exception = False
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        print('Model thread begin')
        # 先把存储图片的文件夹清空
        while 1:
            if(self.found_exception == True):
                print("found")
                self.q.put('found')
                break
