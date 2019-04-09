# _*_ coding:utf-8 _*_
from tkinter import *
import tkinter as tk
from tkinter import *
# entry1 = "000"
def test_UI(root):
    # root = Tk()
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

    root.config(menu=menubar)

    label_1=Label(root, text = '显示结果:',bg = 'white',width = 80)
    label_1.pack(side = 'left',fill ='y')
    '''x
    entry_text1 = StringVar()
    entry_1 = Entry(root, textvariable = entry_text1)
    entry_text1.set("")
    entry_1.pack()


    def on_click():
        # print("asddd:%s"%(entry_1.get()))
        entry1 = entry_1.get()
    Button(root, text="press", command = on_click).pack()
    '''

    v_con_x = 0 # 分辨率x值，初值为0
    v_con_y = 0 # 分辨率y值，初值为0
    v_p_name = '' # 应用的包名
    v_a_name = '' # 应用的活动名

    con_x = Label(root, text = '分辨率x值:')
    con_x.pack(side = 'top')
    con_x_text = StringVar()
    con_x_entry = Entry(root, textvariable = con_x_text)
    con_x_text.set("")
    con_x_entry.pack(side = 'top')

    con_y = Label(root, text = '分辨率y值:')
    con_y.pack(side = 'top')
    con_y_text = StringVar()
    con_y_entry = Entry(root, textvariable = con_y_text)
    con_y_text.set("")
    con_y_entry.pack(side = 'top')


    p_name = Label(root, text = '应用的包名(Package Name):')
    p_name.pack(side = 'top')
    p_name_text = StringVar()
    p_name_entry = Entry(root, textvariable = p_name_text)
    p_name_text.set("")
    p_name_entry.pack(side = 'top')

    a_name = Label(root, text = '应用的活动名(Activity Name):')
    a_name.pack(side = 'top')
    a_name_text = StringVar()
    a_name_entry = Entry(root, textvariable = a_name_text)
    a_name_text.set("")
    a_name_entry.pack(side = 'top')

    def click_1():
        v_con_x = con_x_entry.get()
        v_con_y = con_y_entry.get()
        v_p_name = p_name_entry.get()
        v_a_name = a_name_entry.get()
    Button(root, text="确定",command = click_1).pack(pady = 5)

    label_1=Label(root, text = ' ')
    label_1.pack(fill ='x',pady = '5')

    # 点击屏幕测试

    v_pos_x = 0 # 点击的位置x
    v_pos_y = 0 # 点击的位置y
    v_touch_n = 0 # 点击的次数
    v_i_time = 1 # 多次点击时间隔时间,默认为1秒

    
    fm1 = Frame(root,bg = 'coral')
    fm1.pack(side = 'left',fill = 'y')
    label_fm1=Label(fm1,bg = 'linen', text = '                     点击屏幕测试                    ')
    label_fm1.pack(fill ='x',pady = '5')

    pos_x = Label(fm1, text = '点击的位置x:',pady=5,bg = 'coral')
    pos_x.pack(side = 'top')
    pos_x_text = StringVar()
    pos_x_entry = Entry(fm1, textvariable = pos_x_text)
    pos_x_text.set("")
    pos_x_entry.pack(side = 'top',pady=5)

    pos_y = Label(fm1, text = '点击的位置y:',pady=5,bg = 'coral')
    pos_y.pack(side = 'top')
    pos_y_text = StringVar()
    pos_y_entry = Entry(fm1, textvariable = pos_y_text)
    pos_y_text.set("")
    pos_y_entry.pack(side = 'top',pady=5)

    touch_n = Label(fm1, text = '点击的次数:',pady=5,bg = 'coral')
    touch_n.pack(side = 'top')
    touch_n_text = StringVar()
    touch_n_entry = Entry(fm1, textvariable = touch_n_text)
    touch_n_text.set("")
    touch_n_entry.pack(side = 'top',pady=5)

    i_time = Label(fm1, text = '多次点击时间隔时间,默认为1秒:',pady=5,bg = 'coral')
    i_time.pack(side = 'top')
    i_time_text = StringVar()
    i_time_entry = Entry(fm1, textvariable = i_time_text)
    i_time_text.set("")
    i_time_entry.pack(side = 'top',pady=5)

    def click_2():
        v_pos_x = pos_x_entry.get()
        v_pos_y = pos_y_entry.get()
        v_touch_n = touch_n_entry.get()
        v_i_time = i_time_entry.get()
        
    Button(fm1, text="开始",command = click_2).pack(pady = 5)

    # 随机点屏幕

    v_touch_n = 0 # 点击的次数
    v_i_time = 0 # 每两次点击间隔的时间，秒为单位

    fm2 = Frame(root,bg = 'azure')
    fm2.pack(side = 'left',fill = 'y')
    label_fm2=Label(fm2,bg = 'pink', text = '                       随机点屏幕                      ')
    label_fm2.pack(fill ='x',pady = '5')

    touch_n2 = Label(fm2, text = '点击的次数:',pady=5,bg = 'azure')
    touch_n2.pack(side = 'top')
    touch_n2_text = StringVar()
    touch_n2_entry = Entry(fm2, textvariable = touch_n2_text)
    touch_n2_text.set("")
    touch_n2_entry.pack(side = 'top',pady=5)

    i_time2 = Label(fm2, text = '每两次点击间隔的时间，秒为单位:',pady=5,bg = 'azure')
    i_time2.pack(side = 'top')
    i_time2_text = StringVar()
    i_time2_entry = Entry(fm2, textvariable = i_time2_text)
    i_time2_text.set("")
    i_time2_entry.pack(side = 'top',pady=5)

    def click_3():
        v_touch_n2 = touch_n2_entry.get()
        v_i_time2 = i_time2_entry.get()
        
    Button(fm2, text="开始",command = click_3).pack(pady = 5)



    #滑动屏幕测试

    v_start_x = 0 # 滑动起始位置x
    v_start_y = 0 # 滑动起始位置y
    v_end_x = 0 # 滑动结束位置x
    v_end_y = 0 # 滑动结束位置y
    v_d_time = 1 # 滑动持续时间,默认为1秒
    v_d_num = 1 # 滑动次数，默认为1次
    v_i_time3 = 1 # 多次点击时间隔时间,默认为1秒

    fm3 = Frame(root,bg = 'lightgreen')
    fm3.pack(side = 'left',fill = 'y')
    label_fm3=Label(fm3,bg = 'gold', text = '                      滑动屏幕测试                      ')
    label_fm3.pack(fill ='x',pady = '5')

    start_x = Label(fm3, text = '滑动起始位置x:',pady=5,bg = 'lightgreen')
    start_x.pack(side = 'top')
    start_x_text = StringVar()
    start_x_entry = Entry(fm3, textvariable = start_x_text)
    start_x_text.set("")
    start_x_entry.pack(side = 'top',pady=5)

    start_y = Label(fm3, text = '滑动起始位置y:',pady=5,bg = 'lightgreen')
    start_y.pack(side = 'top')
    start_y_text = StringVar()
    start_y_entry = Entry(fm3, textvariable = start_y_text)
    start_y_text.set("")
    start_y_entry.pack(side = 'top',pady=5)

    end_x = Label(fm3, text = '滑动结束位置x:',pady=5,bg = 'lightgreen')
    end_x.pack(side = 'top')
    end_x_text = StringVar()
    end_x_entry = Entry(fm3, textvariable = end_x_text)
    end_x_text.set("")
    end_x_entry.pack(side = 'top',pady=5)

    end_y = Label(fm3, text = '滑动结束位置y:',pady=5,bg = 'lightgreen')
    end_y.pack(side = 'top')
    end_y_text = StringVar()
    end_y_entry = Entry(fm3, textvariable = end_y_text)
    end_y_text.set("")
    end_y_entry.pack(side = 'top',pady=5)

    d_time = Label(fm3, text = '滑动持续时间,默认为1秒:',pady=5,bg = 'lightgreen')
    d_time.pack(side = 'top')
    d_time_text = StringVar()
    d_time_entry = Entry(fm3, textvariable = d_time_text)
    d_time_text.set("")
    d_time_entry.pack(side = 'top',pady=5)

    d_num = Label(fm3, text = '滑动次数，默认为1次:',pady=5,bg = 'lightgreen')
    d_num.pack(side = 'top')
    d_num_text = StringVar()
    d_num_entry = Entry(fm3, textvariable = d_num_text)
    d_num_text.set("")
    d_num_entry.pack(side = 'top',pady=5)

    i_time3 = Label(fm3, text = '多次点击时间隔时间,默认为1秒:',pady=5,bg = 'lightgreen')
    i_time3.pack(side = 'top')
    i_time3_text = StringVar()
    i_time3_entry = Entry(fm3, textvariable = i_time3_text)
    i_time3_text.set("")
    i_time3_entry.pack(side = 'top',pady=5)

    def click_4():
        v_start_x = start_x_entry.get()
        v_start_y = start_y_entry.get()
        v_end_x = end_x_entry.get()
        v_end_y = end_y_entry.get()
        v_d_time = d_time_entry.get()
        v_d_num = d_num_entry.get()
        v_i_time3 = i_time3_entry.get()

    Button(fm3, text="开始",command = click_4).pack(pady = 5)

    #随机滑动屏幕测试
    v_d_num2 = 0
    v_i_time4 = 1

    fm4 = Frame(root,bg = 'salmon')
    fm4.pack(side = 'left',fill = 'y')
    label_fm4=Label(fm4,bg = 'sienna', text = '                     随机滑动屏幕测试                       ')
    label_fm4.pack(fill ='x',pady = '5')

    d_num2 = Label(fm4, text = '滑动的次数:',pady=5,bg = 'salmon')
    d_num2.pack(side = 'top')
    d_num2_text = StringVar()
    d_num2_entry = Entry(fm4, textvariable = d_num2_text)
    d_num2_text.set("")
    d_num2_entry.pack(side = 'top',pady=5)

    i_time4 = Label(fm4, text = '每两次滑动间隔的时间，秒为单位:',pady=5,bg = 'salmon')
    i_time4.pack(side = 'top')
    i_time4_text = StringVar()
    i_time4_entry = Entry(fm4, textvariable = i_time4_text)
    i_time4_text.set("")
    i_time4_entry.pack(side = 'top',pady=5)

    def click_5():
        v_d_num2 = d_num2_entry.get()
        v_i_time4 = i_time4_entry.get()
        print(v_d_num2,v_i_time4)
    Button(fm4, text="开始",command = click_5).pack(pady = 5)

    root.mainloop()

