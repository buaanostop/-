# _*_ coding:utf-8 _*_
from tkinter import *
import tkinter as tk
from tkinter import *
import threading
import time
# entry1 = "000"
#def test_UI(root):
root = Tk()
root.title("hello world")
root.geometry('900x600')

menubar = tk.Menu(root)  # 菜单选项
start_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label = '开始',menu = start_menu)

test_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label = '编辑测试',menu = test_menu)

report_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label = '编辑报告',menu = report_menu)

pause_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label = '暂停',menu = pause_menu)

stop_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label = '终止',menu = stop_menu)

save_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label = '保存',menu = save_menu)

delete_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label = '删除',menu = delete_menu)

clean_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label = '清屏',menu = clean_menu)

clean_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label = '帮助',menu = clean_menu)

root.config(menu=menubar)

##左侧frame##
frame_left=Frame(root,bg = 'white',width = 500,height = 1200)
frame_left.pack(side = 'left')

log_name = "log.txt"
content_initialize = "开始测试后，测试报告会显示在这"
label_2=Label(frame_left,text = content_initialize,bg = 'white',justify='left')
label_2.place(x = 0,y = 0)
#label_test = Lab

#采用timer实时监测文件变化
def log_monitor():
    global log_name
    try:
            file_log = open(log_name,'r')
            content = file_log.read()
            global label_2
            label_2.config(text = content)
            file_log.close()
            global log_timer
            log_timer = threading.Timer(1,log_monitor)
            log_timer.start()
    except IOError:
            content = "暂时未读取到日志文件"
            label_2.config(text = content)
        
        
log_timer = threading.Timer(1,log_monitor)
log_timer.start()
##左侧frame##


# 连接手机或模拟器的按钮

judge_con = 0 # 判断输入信息按钮是否展开
judge_choose_test = 0 # 判断是否弹测试选择按钮是否展开

def click_b_con():
    global judge_choose_test
    global judge_con
    if judge_choose_test == 0 and judge_con == 0:
        b_choose.forget()
        fm_con.pack()
        b_choose.pack(fill = 'x')
        judge_con = 1

        fm_touch.forget()
        fm_r_touch.forget()
        fm_drag.forget()
        fm_r_drag.forget()

    elif judge_choose_test == 0 and judge_con == 1:
        fm_con.forget()
        judge_con = 0
    elif judge_choose_test == 1 and judge_con == 0:
        b_choose.forget()
        fm_con.pack()
        b_choose.pack(fill = 'x')
        judge_con = 1
        fm_choose.forget()
        judge_choose_test = 0

        fm_touch.forget()
        fm_r_touch.forget()
        fm_drag.forget()
        fm_r_drag.forget()
        
    elif judge_choose_test == 1 and judge_con == 1:
        fm_con.forget()
        judge_con = 0
        fm_choose.forget()
        judge_choose_test = 0
    
b_con = Button(root, text = '请先点击输入设备信息', font = ('黑体',12), height = 2, command = click_b_con)
b_con.pack(fill = 'x')

# 应用信息

fm_con = Frame(root) # 连接手机或模拟器的块

v_con_x = 0 # 分辨率x值，初值为0
v_con_y = 0 # 分辨率y值，初值为0
v_p_name = '' # 应用的包名
v_a_name = '' # 应用的活动名

con_x = Label(fm_con, text = '分辨率x值:')
con_x.pack(side = 'top')
con_x_text = StringVar()
con_x_entry = Entry(fm_con, textvariable = con_x_text)
con_x_text.set("")
con_x_entry.pack(side = 'top')

con_y = Label(fm_con, text = '分辨率y值:')
con_y.pack(side = 'top')
con_y_text = StringVar()
con_y_entry = Entry(fm_con, textvariable = con_y_text)
con_y_text.set("")
con_y_entry.pack(side = 'top')


p_name = Label(fm_con, text = '应用的包名(Package Name):')
p_name.pack(side = 'top')
p_name_text = StringVar()
p_name_entry = Entry(fm_con, textvariable = p_name_text)
p_name_text.set("")
p_name_entry.pack(side = 'top')

a_name = Label(fm_con, text = '应用的活动名(Activity Name):')
a_name.pack(side = 'top')
a_name_text = StringVar()
a_name_entry = Entry(fm_con, textvariable = a_name_text)
a_name_text.set("")
a_name_entry.pack(side = 'top')

def click_b_con_confirm():
    global judge_con
    v_con_x = con_x_entry.get()
    v_con_y = con_y_entry.get()
    v_p_name = p_name_entry.get()
    v_a_name = a_name_entry.get()
    fm_con.forget() # 点击设备信息的确定按钮之后，会暂时消除填入信息的行，再次点击‘请先点击输入设备信息’按钮之后会重新出现
    judge_con = 0
Button(fm_con, text="确定",command = click_b_con_confirm).pack(pady = 5)

# label_1=Label(fm_con, text = ' ')
# label_1.pack(fill ='x',pady = '5')

def click_b_choose():
    global judge_choose_test
    global judge_con
    if judge_choose_test == 0 and judge_con == 0:
        fm_choose.pack()
        judge_choose_test = 1

        fm_touch.forget()
        fm_r_touch.forget()
        fm_drag.forget()
        fm_r_drag.forget()

    elif judge_choose_test == 0 and judge_con == 1:
        fm_con.forget()
        judge_con = 0
        fm_choose.pack()
        judge_choose_test = 1

        fm_touch.forget()
        fm_r_touch.forget()
        fm_drag.forget()
        fm_r_drag.forget()

    elif judge_choose_test == 1 and judge_con == 0:
        fm_choose.forget()
        judge_choose_test = 0
    elif judge_choose_test == 1 and judge_con == 1:
        fm_con.forget()
        judge_con = 0
        fm_choose.forget()
        judge_choose_test = 0

def click_b_touch():
    fm_choose.forget()
    fm_touch.pack()
def click_b_r_touch():
    fm_choose.forget()
    fm_r_touch.pack()
def click_b_drag():
    fm_choose.forget()
    fm_drag.pack()
def click_b_r_drag():
    fm_choose.forget()
    fm_r_drag.pack()

    
fm_choose = Frame(root)    

b_choose = Button(root, text = '选择测试类型', font = ('黑体',12), height = 2, command = click_b_choose)
b_choose.pack(fill = 'x')

b_touch_test = Button(fm_choose, text = '点击屏幕测试', font = ('黑体',10), height = 3, command = click_b_touch)
b_touch_test.pack(side = 'left')

b_r_touch_test = Button(fm_choose, text = '随机点击屏幕测试', font = ('黑体',10), height = 3, command = click_b_r_touch)
b_r_touch_test.pack(side = 'left')

b_drag_test = Button(fm_choose, text = '滑动屏幕测试', font = ('黑体',10), height = 3, command = click_b_drag)
b_drag_test.pack(side = 'left')

b_r_drag_test = Button(fm_choose, text = '随机屏幕测试', font = ('黑体',10), height = 3, command = click_b_r_drag)
b_r_drag_test.pack(side = 'left')



# 点击屏幕测试

v_pos_x = 0 # 点击的位置x
v_pos_y = 0 # 点击的位置y
v_touch_n = 0 # 点击的次数
v_i_time = 1 # 多次点击时间隔时间,默认为1秒


fm_touch = Frame(root)
# fm1.pack(side = 'left',fill = 'y')
label_fm_touch=Label(fm_touch,bg = 'white', text = '点击屏幕测试', font = ('黑体',12))
label_fm_touch.pack(fill ='x',pady = '5')

pos_x = Label(fm_touch, text = '点击的位置x:',pady=5)
pos_x.pack(side = 'top')
pos_x_text = StringVar()
pos_x_entry = Entry(fm_touch, textvariable = pos_x_text)
pos_x_text.set("")
pos_x_entry.pack(side = 'top',pady=5)

pos_y = Label(fm_touch, text = '点击的位置y:',pady=5)
pos_y.pack(side = 'top')
pos_y_text = StringVar()
pos_y_entry = Entry(fm_touch, textvariable = pos_y_text)
pos_y_text.set("")
pos_y_entry.pack(side = 'top',pady=5)

touch_n = Label(fm_touch, text = '点击的次数:',pady=5)
touch_n.pack(side = 'top')
touch_n_text = StringVar()
touch_n_entry = Entry(fm_touch, textvariable = touch_n_text)
touch_n_text.set("")
touch_n_entry.pack(side = 'top',pady=5)

i_time = Label(fm_touch, text = '多次点击时间隔时间,默认为1秒:',pady=5)
i_time.pack(side = 'top')
i_time_text = StringVar()
i_time_entry = Entry(fm_touch, textvariable = i_time_text)
i_time_text.set("")
i_time_entry.pack(side = 'top',pady=5)

def click_b_confirm_touch():
    v_pos_x = pos_x_entry.get()
    v_pos_y = pos_y_entry.get()
    v_touch_n = touch_n_entry.get()
    v_i_time = i_time_entry.get()
    fm_touch.forget()
    fm_choose.pack()
Button(fm_touch, text="加入测试队列",command = click_b_confirm_touch).pack(pady = 5)

# 随机点屏幕

v_r_touch_n = 0 # 点击的次数
v_r_touch_time = 0 # 每两次点击间隔的时间，秒为单位

fm_r_touch = Frame(root)
label_fm_r_touch=Label(fm_r_touch,bg = 'white', text = '随机点屏幕', font = ('黑体',12))
label_fm_r_touch.pack(fill ='x',pady = '5')

r_touch_n = Label(fm_r_touch, text = '点击的次数:',pady=5)
r_touch_n.pack(side = 'top')
r_touch_n_text = StringVar()
r_touch_n_entry = Entry(fm_r_touch, textvariable = r_touch_n_text)
r_touch_n_text.set("")
r_touch_n_entry.pack(side = 'top',pady=5)

r_touch_time = Label(fm_r_touch, text = '每两次点击间隔的时间，秒为单位:',pady=5)
r_touch_time.pack(side = 'top')
r_touch_time_text = StringVar()
r_touch_time_entry = Entry(fm_r_touch, textvariable = r_touch_time_text)
r_touch_time_text.set("")
r_touch_time_entry.pack(side = 'top',pady=5)

def click_b_r_touch_confirm():
    v_r_touch_n = r_touch_n_entry.get()
    v_r_touch_time = r_touch_time_entry.get()
    fm_r_touch.forget()
    fm_choose.pack()
Button(fm_r_touch, text="加入测试队列",command = click_b_r_touch_confirm).pack(pady = 5)



#滑动屏幕测试

v_start_x = 0 # 滑动起始位置x
v_start_y = 0 # 滑动起始位置y
v_end_x = 0 # 滑动结束位置x
v_end_y = 0 # 滑动结束位置y
v_d_time = 1 # 滑动持续时间,默认为1秒
v_d_num = 1 # 滑动次数，默认为1次
v_d_i_time = 1 # 多次点击时间隔时间,默认为1秒

fm_drag = Frame(root)
# fm3.pack(side = 'left',fill = 'y')
label_fm_drag=Label(fm_drag,bg = 'white', text = '滑动屏幕测试', font = ('黑体',12))
label_fm_drag.pack(fill ='x',pady = '2')

start_x = Label(fm_drag, text = '滑动起始位置x:',pady=2)
start_x.pack(side = 'top')
start_x_text = StringVar()
start_x_entry = Entry(fm_drag, textvariable = start_x_text)
start_x_text.set("")
start_x_entry.pack(side = 'top',pady=5)

start_y = Label(fm_drag, text = '滑动起始位置y:',pady=2)
start_y.pack(side = 'top')
start_y_text = StringVar()
start_y_entry = Entry(fm_drag, textvariable = start_y_text)
start_y_text.set("")
start_y_entry.pack(side = 'top',pady=5)

end_x = Label(fm_drag, text = '滑动结束位置x:',pady=2)
end_x.pack(side = 'top')
end_x_text = StringVar()
end_x_entry = Entry(fm_drag, textvariable = end_x_text)
end_x_text.set("")
end_x_entry.pack(side = 'top',pady=5)

end_y = Label(fm_drag, text = '滑动结束位置y:',pady=2)
end_y.pack(side = 'top')
end_y_text = StringVar()
end_y_entry = Entry(fm_drag, textvariable = end_y_text)
end_y_text.set("")
end_y_entry.pack(side = 'top',pady=5)

d_time = Label(fm_drag, text = '滑动持续时间,默认为1秒:',pady=2)
d_time.pack(side = 'top')
d_time_text = StringVar()
d_time_entry = Entry(fm_drag, textvariable = d_time_text)
d_time_text.set("")
d_time_entry.pack(side = 'top',pady=5)

d_num = Label(fm_drag, text = '滑动次数，默认为1次:',pady=2)
d_num.pack(side = 'top')
d_num_text = StringVar()
d_num_entry = Entry(fm_drag, textvariable = d_num_text)
d_num_text.set("")
d_num_entry.pack(side = 'top',pady=5)

d_i_time = Label(fm_drag, text = '多次点击时间隔时间,默认为1秒:',pady=2)
d_i_time.pack(side = 'top')
d_i_time_text = StringVar()
d_i_time_entry = Entry(fm_drag, textvariable = d_i_time_text)
d_i_time_text.set("")
d_i_time_entry.pack(side = 'top',pady=5)

def click_b_drag_confirm():
    v_start_x = start_x_entry.get()
    v_start_y = start_y_entry.get()
    v_end_x = end_x_entry.get()
    v_end_y = end_y_entry.get()
    v_d_time = d_time_entry.get()
    v_d_num = d_num_entry.get()
    v_d_i_time = d_i_time_entry.get()
    fm_drag.forget()
    fm_choose.pack()
Button(fm_drag, text="加入测试队列",command = click_b_drag_confirm).pack(pady = 5)

#随机滑动屏幕测试
v_r_d_num = 0 # 滑动的次数，默认为0
v_r_d_i_time = 1 #每两次滑动间隔的时间，秒为单位 

fm_r_drag = Frame(root)
label_fm_r_drag=Label(fm_r_drag,bg = 'white', text = '随机滑动屏幕测试', font = ('黑体',12))
label_fm_r_drag.pack(fill ='x',pady = '5')

r_d_num = Label(fm_r_drag, text = '滑动的次数:',pady=5)
r_d_num.pack(side = 'top')
r_d_num_text = StringVar()
r_d_num_entry = Entry(fm_r_drag, textvariable = r_d_num_text)
r_d_num_text.set("")
r_d_num_entry.pack(side = 'top',pady=5)

r_d_i_time = Label(fm_r_drag, text = '每两次滑动间隔的时间，秒为单位:',pady=5)
r_d_i_time.pack(side = 'top')
r_d_i_time_text = StringVar()
r_d_i_time_entry = Entry(fm_r_drag, textvariable = r_d_i_time_text)
r_d_i_time_text.set("")
r_d_i_time_entry.pack(side = 'top',pady=5)

def click_b_r_drag_confirm():
    v_r_d_num = r_d_num_entry.get()
    v_r_d_i_time = r_d_i_time_entry.get()
    fm_r_drag.forget()
    fm_choose.pack()
Button(fm_r_drag, text="加入测试队列",command = click_b_r_drag_confirm).pack(pady = 5)


start_b = Button(root, text = '开始测试', font = ('黑体',12), height = 2).pack(side = 'bottom', fill = 'x')


root.mainloop()
