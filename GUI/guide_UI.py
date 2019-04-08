from tkinter import *
import tkinter as tk  # 使用Tkinter前需要先导入

def guide(top):
        top.title('guide')
        top.geometry('900x600')
        leftb = tk.Button(top, text='上一张', font=('黑体', 12), width=8, height=2)
        leftb.pack(side = 'left')
        rightb = tk.Button(top, text='下一张', font=('黑体', 12), width=8, height=2)
        rightb.pack(side = 'right')

        # label = Label(top, text = '当前步骤示意图')
        bm = PhotoImage(file = '1.png')
        label2 = Label(top, image = bm)
        label2.bm = bm
        label2.pack()
        helpb = tk.Button(top,text = '帮助', font=('Arial', 10), width=6, height=2)
        helpb.pack(side = 'bottom',expand = 'yes')

        label3 = Label(top,text = '图片信息',bg='grey', font=('Arial', 40), width=15, height=3)
        label3.pack(side = 'bottom',expand = 'yes')
        
