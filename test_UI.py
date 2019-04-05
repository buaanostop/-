# -*- coding: UTF-8 -*-
import tkinter as tk
from tkinter import Menu
root = tk.Tk()
root.title("首页")  #设置程序顶部标题文字
root.resizable(width=False,height = False)
root.geometry("640x600")    #设置程序框大小
button_width = 10
distance = 80
axis_x = 0
def _quit():
    root.quit()
    root.destroy()
    exit()
#创建菜单栏功能
start_button= tk.Button(root,text = '开始',width =button_width)
start_button.place(x=axis_x,y=0)
axis_x = axis_x+distance


edit_test_button= tk.Button(root,text = '编辑测试',width = button_width)
edit_test_button.place(x=axis_x,y=0)
axis_x = axis_x+distance

edit_report_button= tk.Button(root,text = '编辑报告',width = button_width)
edit_report_button.place(x=axis_x,y=0)
axis_x = axis_x+distance

pause_button= tk.Button(root,text = '暂停',width = button_width)
pause_button.place(x=axis_x,y=0)
axis_x = axis_x+distance

end_button= tk.Button(root,text = '终止',width = button_width)
end_button.place(x=axis_x,y=0)
axis_x = axis_x+distance

save_button= tk.Button(root,text = '保存',width = button_width)
save_button.place(x=axis_x,y=0)
axis_x = axis_x+distance

remove_button= tk.Button(root,text = '删除',width = button_width)
remove_button.place(x=axis_x,y=0)
axis_x = axis_x+distance

clear_button= tk.Button(root,text = '清屏',width = button_width)
clear_button.place(x=axis_x,y=0)
axis_x = axis_x+distance

#print(axis_x)
root.mainloop()
