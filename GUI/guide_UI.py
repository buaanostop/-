from tkinter import *
import tkinter as tk  # 使用Tkinter前需要先导入

def guide(top):
        top.title('引导界面')
        top.geometry('900x600')
        top.resizable(0,0)
        ind = 28
        def lastp():
                nonlocal  label2
                nonlocal label3
                nonlocal ind
                if(ind == 1):
                        ind = 28
                        label2.forget()
                        label3.forget()
                        bm = PhotoImage(file = 'guideP/1.png',width = 630, height = 441)
                        label2 = Label(top, image = bm, bg = 'lightyellow')
                        label2.bm = bm
                        label2.pack()

                        bms = PhotoImage(file = 'guideP/1s.png',width = 630, height = 100)
                        label3 = Label(top, image = bms, bg = 'white')
                        label3.bm = bms
                        label3.pack()
                else:
                        ind = ind-1
                        label2.forget()
                        label3.forget()
                        bm = PhotoImage(file = 'guideP/'+str(ind)+'.png',width = 630, height = 441)
                        label2 = Label(top, image = bm, bg = 'lightyellow')
                        label2.bm = bm
                        label2.pack()
                        
                        bms = PhotoImage(file = 'guideP/'+str(ind)+'s.png',width = 630, height = 100)
                        label3 = Label(top, image = bms, bg = 'white')
                        label3.bm = bms
                        label3.pack()
        def nextp():
                nonlocal label2
                nonlocal label3
                nonlocal ind
                if(ind == 28):
                        ind = 1
                        label2.forget()
                        label3.forget()
                        bm = PhotoImage(file = 'guideP/1.png',width = 630, height = 441)
                        label2 = Label(top, image = bm, bg = 'lightyellow')
                        label2.bm = bm
                        label2.pack()

                        bms = PhotoImage(file = 'guideP/1s.png',width = 630, height = 100)
                        label3 = Label(top, image = bms, bg = 'white')
                        label3.bm = bms
                        label3.pack()
                else:
                        ind = ind+1
                        label2.forget()
                        label3.forget()
                        bm = PhotoImage(file = 'guideP/'+str(ind)+'.png',width = 630, height = 441)
                        label2 = Label(top, image = bm, bg = 'lightyellow')
                        label2.bm = bm
                        label2.pack()

                        bms = PhotoImage(file = 'guideP/'+str(ind)+'s.png',width = 630, height = 100)
                        label3 = Label(top, image = bms, bg = 'white')
                        label3.bm = bms
                        label3.pack()
        
        leftb = tk.Button(top, text='上一张', font=('黑体', 12), width=6, height=5, command = lastp)
        leftb.pack(side = 'left')
        rightb = tk.Button(top, text='下一张', font=('黑体', 12), width=6, height=5, command = nextp)
        rightb.pack(side = 'right')

        # label = Label(top, text = '当前步骤示意图')
        bm = PhotoImage(file = 'guideP/28.png',width = 630, height = 441)
        label2 = Label(top, image = bm, bg = 'lightyellow')
        label2.bm = bm
        label2.pack()

        bms = PhotoImage(file = 'guideP/28s.png',width = 630, height = 100)
        label3 = Label(top, image = bms, bg = 'white')
        label3.bm = bms
        label3.pack()
        # label3 = Label(top,text = '主界面\nsss',bg='white', font=('Arial', 12), width=70, height=3)
        # label3.pack(side = 'bottom',expand = 'yes')
        
