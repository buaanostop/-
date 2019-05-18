# -*- coding: utf-8 -*-

"""
简化测试UI

"""
from tkinter import *
from tkinter.ttk import *
import os
import time
import _thread as thread
import Monkey
import tkinter.messagebox

    
def connect():
    print("UI: connection")
    connectflag = Monkey.connect()
    if connectflag:
        tkinter.messagebox.showinfo('提示','连接成功')
    else:
        tkinter.messagebox.showerror('错误','连接失败')
        
def pause():
    print("UI: pause")
    Monkey.pause()

def resume():
    print("UI: resume")
    Monkey.resume()

def stop():
    print("UI: stop")
    Monkey.stop()

def start():
    print("UI: start")
    Monkey.start()

def drag():
    print("UI: drag add")
    x1 = int(e_x1.get())
    y1 = int(e_y1.get())
    x2 = int(e_x2.get())
    y2 = int(e_y2.get())
    pointlist = ((x1,y1),(x2,y2))
    Monkey.drag(pointlist)

def on_closing():
    Monkey.close()
    root.destroy()
    
root = Tk()

e_x1 = Entry(root)
e_x1.grid(row=0, column=1, sticky=E)

e_y1 = Entry(root)
e_y1.grid(row=0, column=2, sticky=E)

e_x2 = Entry(root)
e_x2.grid(row=1, column=1, sticky=E)

e_y2 = Entry(root)
e_y2.grid(row=1, column=2, sticky=E)

b_connection = Button(root, text='连接手机', command=connect)
b_connection.grid(row=2,column=0)

b_random_touch = Button(root, text='滑动测试', command=drag)
b_random_touch.grid(row=2,column=1)

b_start = Button(root, text='开始测试', command=start)
b_start.grid(row=3, column=0)

b_pause = Button(root, text='暂停测试', command=pause)
b_pause.grid(row=3, column=1)

b_resume = Button(root, text='继续测试', command=resume)
b_resume.grid(row=4, column=1)

b_stop = Button(root, text='停止测试', command=stop)
b_stop.grid(row=4, column=0)

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
