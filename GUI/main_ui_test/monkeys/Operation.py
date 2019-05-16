# _*_ coding:utf-8 _*_

class Operation():
    """操作类，记录各种操作"""

    def __init__(self, optype, pointlist, number, interval_time, hold_time, keyorstring, wait_time):
        self.optype = optype
        self.pointlist = pointlist
        self.number = int(number)
        self.interval_time = float(interval_time)
        self.hold_time = float(hold_time)
        self.keyorstring = str(keyorstring)
        self.wait_time = float(wait_time)

    def todict(self):
        data = {'optype': self.optype,
                'pointlist': self.pointlist,
                'number': self.number,
                'interval_time': self.interval_time,
                'hold_time': self.hold_time,
                'keyorstring': self.keyorstring,
                'wait_time': self.wait_time}
        return data
        
    def display(self): # 测试用
        print(self.optype, self.pointlist, self.number, self.interval_time, self.hold_time, self.keyorstring, self.wait_time)
