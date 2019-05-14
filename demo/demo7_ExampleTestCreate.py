# _*_ coding:utf-8 _*_
"""
demo7 生成示例测试
分辨率：
540x960
720x1280
900x1600
1080x1920
"""
import random
ratio_x = 1080
ratio_y = 1920
max_x = ratio_x - 1
max_y = ratio_y - 1
fp = open("Example "+str(ratio_x)+"x"+str(ratio_y)+".py",'w')
fp.write("# _*_ coding:utf-8 _*_\n")
fp.write("from Monkey import *\n")

# 单击20个点各5次 20*5=100
num = 0
while num < 20:
    x1 = random.randint(0, max_x)
    y1 = random.randint(0, max_y)
    data = "touch("+str(x1)+","+str(y1)+",5,0.5)"
    fp.write(data+'\n')
    num += 1
# 长按20个点各5次 20*5=100
num = 0
while num < 20:
    x1 = random.randint(0, max_x)
    y1 = random.randint(0, max_y)
    data = "long_touch("+str(x1)+","+str(y1)+",1.0,5,0.5)"
    fp.write(data+'\n')
    num += 1
# 随机单击 300 次 300
num = 0
while num < 300:
    x1 = random.randint(0, max_x)
    y1 = random.randint(0, max_y)
    data = "touch("+str(x1)+","+str(y1)+")"
    fp.write(data+'\n')
    num += 1
# 滑动20条线路各5次 20*5=100
num = 0
while num < 20:
    x1 = random.randint(0, max_x)
    y1 = random.randint(0, max_y)
    x2 = random.randint(0, max_x)
    y2 = random.randint(0, max_y)
    data = "drag((("+str(x1)+","+str(y1)+"),("+str(x2)+","+str(y2)+")),1.0,5,0.5)"
    fp.write(data+'\n')
    num += 1
#随机滑动 300
num = 0
while num < 300:
    x1 = random.randint(0, max_x)
    y1 = random.randint(0, max_y)
    x2 = random.randint(0, max_x)
    y2 = random.randint(0, max_y)
    data = "drag((("+str(x1)+","+str(y1)+"),("+str(x2)+","+str(y2)+")))"
    fp.write(data+'\n')
    num += 1
#长按滑动 100
num = 0
while num < 100:
    x1 = random.randint(0, max_x)
    y1 = random.randint(0, max_y)
    x2 = random.randint(0, max_x)
    y2 = random.randint(0, max_y)
    data = "touch_drag((("+str(x1)+","+str(y1)+"),("+str(x2)+","+str(y2)+")))"
    fp.write(data+'\n')
    num += 1

#保存
data = "save(\"示例测试 "+str(ratio_x)+"x"+str(ratio_y)+"\")"
fp.write(data+'\n')
fp.close()
    

