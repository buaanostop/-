# -*- coding: utf-8 -*-
from guide_UI import guide
from test_UI import test_UI
from tkinter import *
import tkinter as tk  # 使用Tkinter前需要先导入
import threading
import time
import os
import socket
import _thread as thread
import webbrowser


class main_UI:
    window = tk.Tk()  # 实例化object，建立窗口window
    window.title('主界面')  # 给窗口的可视化起名字
    window.geometry('900x600')  # 设定窗口的大小(长 * 宽) 这里的乘是小x
    window.resizable(0, 0)

    l = tk.Label(window, text='手机APP异常检测', bg='lightskyblue', font=('黑体', 40), width=20, height=3)  # 在图形界面上设定标签
    # 说明： bg为背景，font为字体，width为长，height为高，这里的长和高是字符的长和高，比如height=2,就是标签有2个字符这么高

    l.pack(pady='110')  # 放置标签Label内容content区域放置位置，自动调节尺寸

    # top = Toplevel()
    def guide2():
        top = Toplevel()
        guide(top)

    def test2():
        root = Toplevel()
        test_UI(root)

    def click_sur():
        webbrowser.open("https://link.jiandaoyun.com/f/5cb910d6c221e541e8fb3a17")

    def click_fb():
        webbrowser.open("https://link.jiandaoyun.com/f/5cb9215b196c2d1d50253635")

    survey = tk.Button(window, text='用户调查', font=('黑体', 12), width=15, height=2, command=click_sur)
    survey.pack(side='bottom', expand='yes')

    feedback = tk.Button(window, text='问题反馈', font=('黑体', 12), width=15, height=2, command=click_fb)
    feedback.pack(side='bottom', expand='yes')

    c = tk.Button(window, text='测试', font=('黑体', 12), width=15, height=2, command=test2)
    c.pack(side='bottom', expand='yes')

    d = tk.Button(window, text='引导', font=('黑体', 12), width=15, height=2, command=guide2)
    d.pack(side='bottom', expand='yes')

    window.mainloop()
    # 注意，loop因为是循环的意思，window.mainloop就会让window不断的刷新，如果没有mainloop,就是一个静态的window,传入进去的值就不会有循环，mainloop就相当于一个很大的while循环，有个while，每点击一次就会更新一次，所以我们必须要有循环
    # 所有的窗口文件都必须有类似的mainloop函数，mainloop是窗口文件的关键的关键。
