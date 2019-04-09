# -*- coding: utf-8 -*-
from guide_UI import guide
from test_UI2 import test_UI
from tkinter import *
import tkinter as tk  # 使用Tkinter前需要先导入
class main_UI:
    window = tk.Tk()  # 实例化object，建立窗口window
    window.title('My Window')  # 给窗口的可视化起名字
    window.geometry('900x600')  # 设定窗口的大小(长 * 宽) 这里的乘是小x
    l = tk.Label(window, text='LOGO', bg='lightskyblue', font=('Arial', 40), width=15, height=3)  # 在图形界面上设定标签
    # 说明： bg为背景，font为字体，width为长，height为高，这里的长和高是字符的长和高，比如height=2,就是标签有2个字符这么高
     
    l.pack(pady='110')  # 放置标签Label内容content区域放置位置，自动调节尺寸
    
    # top = Toplevel()
    def guide2():
        top = Toplevel()
        guide(top)
    def test2():
        root = Toplevel()
        test_UI(root)
    # 在窗口界面设置放置Button按键
    b = tk.Button(window, text='报告', font=('黑体', 12), width=8, height=2)
    b.pack(side='bottom',expand='yes')
    # b.place(relx = 0.5, rely = 0.5)

    c = tk.Button(window, text='测试', font=('黑体', 12), width=8, height=2,command = test2)
    c.pack(side='bottom',expand='yes')

    d = tk.Button(window, text='引导', font=('黑体', 12), width=8, height=2, command = guide2)
    d.pack(side='bottom',expand='yes')

    menubar = tk.Menu(window)  # 菜单选项

    filemenu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label = '文件',menu = filemenu)

    filemenu.add_command(label='新建')
    filemenu.add_command(label='打开')
    filemenu.add_command(label='保存')
    # filemenu.add_separator() 添加一条分隔线
    filemenu.add_command(label='退出', command=window.destroy)

    editmenu = tk.Menu(menubar,tearoff=0)
    menubar.add_cascade(label = '编辑',menu = editmenu)

    editmenu.add_command(label='剪切')
    editmenu.add_command(label='复制')
    editmenu.add_command(label='粘贴')

    viewmenu = tk.Menu(menubar,tearoff=0)
    menubar.add_cascade(label = '视图',menu = viewmenu)

    helpmenu = tk.Menu(menubar,tearoff=0)
    menubar.add_cascade(label = '帮助',menu = helpmenu)

    window.config(menu=menubar)

    d.pack_forget()
    d.pack(side='bottom',expand='yes')

    window.mainloop()
    # 注意，loop因为是循环的意思，window.mainloop就会让window不断的刷新，如果没有mainloop,就是一个静态的window,传入进去的值就不会有循环，mainloop就相当于一个很大的while循环，有个while，每点击一次就会更新一次，所以我们必须要有循环
    # 所有的窗口文件都必须有类似的mainloop函数，mainloop是窗口文件的关键的关键。
