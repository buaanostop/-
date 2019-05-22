import cv2 as cv
import numpy as np
import os
import threading
import time
import queue

class SimpleModel(threading.Thread):
    q = queue.Queue()
    found_exception = False
    quit_flag = 0
    def __init__(self, picture_collection_path, step_length, limit_range, time_interval):
        threading.Thread.__init__(self)
        self.picture_collection_path = picture_collection_path
        self.step_length = step_length
        self.limit_range = limit_range
        self.time_interval = time_interval
        self.quit_flag = 0

    def run(self):
        print('Model thread begin')
        # 先把存储图片的文件夹清空
        del_file(self.picture_collection_path)
        while 1:
            time.sleep(self.time_interval)
            exception_order = picture_classification(self.picture_collection_path, self.step_length, self.limit_range)
            # print(exception_order)
            print_check(exception_order)
            if exception_order != -1:
                self.q.put('found')
                print('found exception')
                self.found_exception = True
                break
            if self.quit_flag == 1:
                print("stop model")
                break
       # if(exception_order != -1):
            #print_exception(exception_order, self.picture_collection_path)



'''
    picture_classification 用来对一组图片进行分类，目的是要找到与整体有差异的若干张图片
                           根据相邻图片的相似程度来区分正常和异常图片
                           通过计算两张图片的欧式距离来判断其相似程度
                           直到若干张图片都相似才判断它们都为异常
    picture_collection_path：储存图片的文件夹的路径
    step_length：参数，表示分组的步长，即判断相邻的step_length张图片为异常还是正常
    limit_range：参数，表示接受的相似程度，即当欧式距离小于limit_range时判断两张图片为相似
    i：返回值，返回这组图片第一张的序号
 '''


def picture_classification(picture_collection_path, step_length, limit_range):
    txt_path = os.path.join(os.getcwd(), 'picture_status.txt')
    data = open(txt_path, 'a')
    path = picture_collection_path
    # picture_num为图片的总数量
    picture_num = len([lists for lists in os.listdir(path) if os.path.isfile(os.path.join(path, lists))])
    print('the picture_num is %s' % picture_num, file=data)
    if picture_num < step_length:
        return -1
    # 遍历一组内的所有图片
    for i in range(picture_num - step_length + 1, picture_num + 1):
        # print(i)
        print('this order is: %s' % i, file=data)
        # 取第i张图片和组内的所有图片计算距离
        for j in range(picture_num - step_length + 1, picture_num + 1):
            if j == i:
                continue
            # print(j)
            # 得到每次比较的两张图片的名字
            picture1_name = path + '\shot' + str(i) + '.png'
            picture2_name = path + '\shot' + str(j) + '.png'
            print('pictures name are %s %s' % (picture1_name, picture2_name), file=data)
            # 将要比较的两张图片转换为数组
            first_array = np.array(cv.imread(picture1_name))
            second_array = np.array(cv.imread(picture2_name))
            # 计算两张图片之间的欧氏距离
            euclidean_distance = np.sqrt(np.sum((second_array - first_array) * (second_array - first_array)))
            print('the distance is %s' % euclidean_distance, file=data)
            # 若两张图片的距离不满足要求，直接return -1
            if euclidean_distance > limit_range:
                return -1
    # 如果所有图片都满足要求，就返回这组图片第一张的序号
    return i - step_length + 1


# 用来清空一个文件夹下的所有图片
# path: 要删除的文件夹的绝对路径
def del_file(path):
    file_list = os.listdir(path)
    for i in file_list:
        # 先将要删除的文件的名字处理为绝对路径
        file_path = os.path.join(path, i)
        os.remove(file_path)


# 将捕获到的异常信息输出到 exception.txt 中
# order 为异常图片的序号，path为存储图片的文件夹的绝对路径
def print_exception(order, path):
    # 获得要输出信息的图片的绝对路径
    picture1_path = path + '\shot' + str(order) + '.png'
    # 获得输出信息文本的绝对路径
    txt_path = os.path.join(os.getcwd(), 'exception.txt')
    # print(txt_path)
    data = open(txt_path, 'w')
    print('exception appeared!', file=data)
    # 输出异常图片的序号到txt中
    print('the picture order is: %s' % order, file=data)
    # 输出异常图片的得到时间到txt中
    print('the picture got in: %s' % os.stat(picture1_path).st_ctime, file=data)


def print_check(order):
    txt_path = os.path.join(os.getcwd(), 'check.txt')
    data = open(txt_path, 'a')
    print('this order is: %s' % order, file=data)


# picture_file 为储存截图的文件夹
'''picture_file = os.path.join(os.getcwd(), 'screenshot')
# print(picture_file)
model_thread = SimpleModel(picture_collection_path=picture_file, step_length=5, limit_range=100, time_interval=3)
model_thread.start()'''

