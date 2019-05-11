# _*_ coding:utf-8 _*_
"""字典保存并读取"""

data = {'optype':"touch",'pointlist':((1,1),(2,2)),'number':5}
data2 = {'optype':'drag','pointlist':None,'number':3}
f = open('demo4save.save','w')
f.write(str(data)+'\n')
f.write(str(data2)+'\n')
f.close()

f = open('demo4save.save','r')
a = f.readline()
dict1 = eval(a)
b = f.readline()
dict2 = eval(b)
f.close()
print(dict1['number'])
print(dict2['optype'])
