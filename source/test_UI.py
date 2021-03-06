# _*_ coding:utf-8 _*_
from tkinter import *
from NewModel import SimpleModel
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
import threading
import time

import os
import socket
import _thread as thread


# entry1 = "000"
def test_UI(root):
    # 一些常数和错误处理#
    bool_ever_click_connect_button = 0
    bool_is_device_connected_successful = 0
    min_click_times = 1
    max_click_times = 9999
    min_interval_time = 0.1
    max_interval_time = 99.9
    min_drag_times_number = 1
    max_drag_times_number = 9999
    min_drag_during_time = 0.1
    max_drag_during_time = 9.9
    min_drag_interval_time = 0.1
    max_drag_interval_time = 99.9
    max_pos_x = 1000
    max_pos_y = 1000

    exception_count = 0
    while (1):
        try:
            open('exception_' + str(exception_count) + '.txt')
            exception_count += 1
        except IOError:
            break
    empty_error_code = 0
    number_error_code = 1
    logic_error_code = 2
    resolution_ration_error_code = 3
    something_else_error_code = 4
    have_not_connect_error_code = 5
    not_successful_connected_error_code = 6

    def error_message_prompt(error_code):
        if (error_code == 0):  # 错误信息:空输入
            tk.messagebox.showinfo('输入错误', '输入不能为空或非半角阿拉伯数字，具体输入规范可参考顶部菜单栏的“帮助”按钮')
        elif (error_code == 1):  # 错误信息：输入的应该是数字却不是
            tk.messagebox.showinfo('输入错误', '请输入半角阿拉伯正数，具体输入规范可参考顶部菜单栏的“帮助”按钮')
        elif (error_code == 2):
            tk.messagebox.showinfo('输入错误', '请输入不要超过限定范围，具体输入范围可参考顶部菜单栏的“帮助”按钮')
        elif (error_code == 3):
            tk.messagebox.showinfo('输入错误', '请正确输入手机分辨率，以半角阿拉伯正数形式输入')
        elif (error_code == something_else_error_code):
            tk.messagebox.showinfo('未知错误', '发生了一些未知的错误，程序将退出')
        elif (error_code == have_not_connect_error_code):
            tk.messagebox.showinfo('提示', '请先连接设备！')
        elif (error_code == not_successful_connected_error_code):
            tk.messagebox.showinfo('连接错误', '还未成功连接设备')

    # 常数和错误处理结束#

    # root = Tk()
    root.title("测试界面")
    root.geometry('1250x650')

    root.resizable(0, 0)  # 禁止调整窗口大小

    uisocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    port = 8081
    host = '127.0.0.1'

    def runMonkeyServer(lock):
        str = 'monkeyrunner ' + os.path.join(os.getcwd(), 'MonkeyServer.py')
        # str = 'r"' + str + '"'
        # print(str)
        ##!!!!!!!!!!!!!!!!!!!!!!!!!!!!此位置改成MonkeyServer.py所在位置
        ret = os.system(str)
        '''if(ret == 0):
            tk.messagebox.showinfo('运行错误','无法打开monkeyrunner，请检查路径设置是否正确')
        '''
        lock.release()

    lock = thread.allocate_lock()
    lock.acquire()
    thread.start_new(runMonkeyServer, (lock,))

    def connect_waiting():
        nonlocal bool_is_device_connected_successful
        connect_log = open(os.getcwd() + '\\connectlog.txt', 'r')
        content = connect_log.read()
        nonlocal connect_waiting_timer
        if (content == 'True'):
            bool_is_device_connected_successful = 1
            print_text.insert('end', 'connection successful!')
            connect_waiting_timer.cancel()
            connect_log.close()
        else:
            connect_log.close()
            connect_waiting_timer = threading.Timer(0.5, connect_waiting)
            connect_waiting_timer.start()

    def connect():
        nonlocal bool_ever_click_connect_button
        bool_ever_click_connect_button = 1
        path = os.getcwd()
        print_text.insert('end', "TestMethod: waiting for connection..")
        send('connect', ord(path[0]), 0, 0, 0, 0, 0, 0, path[2:])
        nonlocal connect_waiting_timer
        connect_waiting_timer = threading.Timer(0.5, connect_waiting)
        connect_waiting_timer.start()
        # send('connect',0,0,0,0,0,0,0,0)

    connect_waiting_timer = threading.Timer(0.5, connect_waiting)

    def pause():
        print_text.insert('end', "TestMethod: pause")
        send('pause', 0, 0, 0, 0, 0, 0, 0, 0)

    def resume():
        print_text.insert('end', "TestMethod: resume")
        send('resume', 0, 0, 0, 0, 0, 0, 0, 0)

    def stop():
        print_text.insert('end', "TestMethod: stop")
        send('stop', 0, 0, 0, 0, 0, 0, 0, 0)

    def start():
        picture_file = os.path.join(os.getcwd(), 'screenshot')
        log_timer = threading.Timer(1, log_monitor)
        log_timer.start()
        model_thread = SimpleModel(picture_collection_path=picture_file, step_length=5, limit_range=100, time_interval=3)
        model_thread.start()
        print_text.insert('end', "Calculate model thread start")
        print_text.insert('end', "TestMethod: start")
        send('start', 0, 0, 0, 0, 0, 0, 0, 0)

    def send(optype, x1, y1, x2, y2, number, interval_time, drag_time, keyorstring):
        data = bytes(
            "%s:%d:%d:%d:%d:%d:%f:%f:%s" % (optype, x1, y1, x2, y2, number, interval_time, drag_time, keyorstring),
            encoding="utf8")
        uisocket.sendto(data, (host, port))

    '''
    def random_touch():
        touch_number = int(e_touch_number.get()) # 通过输入框获取参数 点击次数
        interval_time = float(e_interval_time.get()) # 通过输入框获取参数 间隔时间
        print("TestMethod: random_touch 点击次数:%d 间隔时间:%f"%(touch_number, interval_time))
        send('random_touch',0,0,0,0,touch_number,interval_time,0,0)
    def delete_print():
        nonlocal print_text
        print_text.delete(0,'end')
    '''
    menubar = tk.Menu(root)  # 菜单选项

    def help_func():
        tk.messagebox.showinfo('帮助',
                               '输入请输入半角阿拉伯数字，每一个输入文本框都输入完毕以后再点击确认按钮。\n\
                            输入范围限制如下：\n\
                                  点击次数：1-9999次\n\
                                  间隔时间：0.1-99.9s\n\
                                  滑动次数：1-9999次\n\
                                  滑动时间：0.1-9.9s\n\
                                  滑动间隔时间：0.1-99.9s\n\
                                  点击位置不可超出app分辨率\n\
                                  若希望软件自动启动需要测试的游戏，请正确输入游戏的包名和活动名，留空则默认对当前运行的应用进行测试\n\
                                  需要修改分辨率参数，输入并再次确认即可\n\
                                  使用遇到问题，可发送邮件到buaanostop@163.com')

    # help_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_command(label='帮助', command=help_func)

    root.config(menu=menubar)

    ## 最左边文本框输出测试队列信息
    print_text = Listbox(root, bg='white', width='45', height='80')

    def delete_text():
        nonlocal print_text
        print_text.delete(0, 'end')

    b_delete = Button(root, text='清屏', width='3', command=delete_text).pack(side='left', fill='y')
    print_text.pack(side='left')
    ## 最左边文本框输出测试队列信息

    ##左侧frame##
    frame_left = Frame(root, bg='white', width=459, height=1200)
    frame_left.pack(side='left')

    log_name = "log.txt"
    exception_raw_name = 'exception.txt'
    exception_name = 'exception_' + str(exception_count) + '.txt'
    content_initialize = "开始测试后，测试报告会显示在这"
    scr = scrolledtext.ScrolledText(frame_left, width=65, height=1200)
    scr.insert('end', content_initialize)
    scr.pack()
    # label_2=Label(scr,text = content_initialize,bg = 'white',justify='left')
    # label_2.place(x = 0,y = 0)
    # os.remove(os.getcwd() + '\\' + exception_raw_name)
    connect_status_flag = open(os.getcwd() + '\\connectlog.txt', 'w+')  # 初始化connectlog.txt
    connect_status_flag.write("False")
    connect_status_flag.close()
    # label_test = Lab
    # print(os.getcwd())
    # 采用timer实时监测文件变化
    read_log = 0
    log_lines = []
    bool_successful_read_log = 0
    file_log = open('connectlog.txt', 'r')
    try:
        os.remove(os.getcwd() + '\\' + exception_raw_name)
    except:
        do_nothing = 0
    def log_monitor():
        nonlocal log_name
        nonlocal read_log
        nonlocal log_lines
        nonlocal file_log
        nonlocal scr
        nonlocal bool_successful_read_log
        try:
            read_log = 1
            if (not bool_successful_read_log):
                file_log = open(log_name, 'r')
                bool_successful_read_log = 1
            final_line = file_log.readline()
            if (final_line != '' and len(final_line.strip() )!= 0):
                log_lines.append(final_line)
                scr.insert('end', final_line)
            # print(log_lines)
            # nonlocal label_2
            # label_2.config(text = content)
            # file_log.close()
            try:
                file_exception = open(exception_raw_name, 'r')
                file_exception_log = open(exception_name, 'a+')
                lines_count = len(log_lines)
                if (len(log_lines) == 0):
                    # print('no log file')
                    log_timer = threading.Timer(0.5, log_monitor)
                    log_timer.start()
                    return
                lines_to_be_written = []
                min_lines_error_log = min(10, lines_count)
                for i in range(lines_count - 1, lines_count - min_lines_error_log, -1):
                    lines_to_be_written.append(log_lines[i])
                file_exception_log.writelines(lines_to_be_written)
                scr.insert('end', '\n出现异常！相关内容已经保存到根目录下' + exception_name + '\n测试已停止')
                # content = content + '\n出现异常！相关内容已经保存到根目录下' + exception_name + '\n测试已停止'
                # label_2.config(text = content)
                print_text.insert('end', '出现异常！相关内容已经保存到' + exception_name)
                print_text.insert('end', '测试已停止')
                nonlocal exception_count
                exception_count += 1
                file_exception.close()
                os.remove(os.getcwd() + '\\' + exception_raw_name)
                stop()
                file_log.close()
                file_exception_log.close()
            except IOError:
                log_timer = threading.Timer(0.5, log_monitor)
                log_timer.start()
        except IOError:
            if (read_log == 0):
                scr.insert('end', '暂未读取到日志文件')
            # label_2.config(text = content)

    '''log_timer = threading.Timer(1,log_monitor)
    log_timer.start()'''
    ##左侧frame##

    # 连接手机按钮
    b_con_phone = Button(root, text='连接设备', font=('黑体', 12), height=2, command=connect)
    b_con_phone.pack(fill='x', side='top')

    # 打开app按钮

    judge_con = 0  # 判断输入信息按钮是否展开
    judge_choose_test = 0  # 判断是否弹测试选择按钮是否展开

    def click_b_con():  # 开始命名成了连接。。实际上此函数时展开输入app选项的按钮
        nonlocal judge_choose_test
        nonlocal judge_con
        if (bool_ever_click_connect_button == 0):
            error_message_prompt(have_not_connect_error_code)
            return
        if (bool_is_device_connected_successful == 0):
            error_message_prompt(not_successful_connected_error_code)
            return
        if judge_choose_test == 0 and judge_con == 0:
            b_choose.forget()
            fm_con.pack()
            b_choose.pack(fill='x')
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
            b_choose.pack(fill='x')
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

    b_con = Button(root, text='输入需要测试的app参数', font=('黑体', 12), height=2, command=click_b_con)
    b_con.pack(fill='x')

    # 应用信息

    fm_con = Frame(root)  # 连接手机或模拟器的块

    v_con_x = 0  # 分辨率x值，初值为0
    v_con_y = 0  # 分辨率y值，初值为0
    v_p_name = ''  # 应用的包名
    v_a_name = ''  # 应用的活动名

    con_x = Label(fm_con, text='分辨率x值:')
    con_x.pack(side='top')
    con_x_text = StringVar()
    con_x_entry = Entry(fm_con, textvariable=con_x_text)
    con_x_text.set("")
    con_x_entry.pack(side='top')

    con_y = Label(fm_con, text='分辨率y值:')
    con_y.pack(side='top')
    con_y_text = StringVar()
    con_y_entry = Entry(fm_con, textvariable=con_y_text)
    con_y_text.set("")
    con_y_entry.pack(side='top')

    p_name = Label(fm_con, text='应用的包名(Package Name):')
    p_name.pack(side='top')
    p_name_text = StringVar()
    p_name_entry = Entry(fm_con, textvariable=p_name_text)
    p_name_text.set("")
    p_name_entry.pack(side='top')

    a_name = Label(fm_con, text='应用的活动名(Activity Name):')
    a_name.pack(side='top')
    a_name_text = StringVar()
    a_name_entry = Entry(fm_con, textvariable=a_name_text)
    a_name_text.set("")
    a_name_entry.pack(side='top')

    def click_b_con_confirm():
        nonlocal judge_con
        v_con_x = con_x_entry.get()
        v_con_y = con_y_entry.get()
        try:
            nonlocal max_pos_x
            nonlocal max_pos_y
            v_con_x = int(con_x_entry.get())
            v_con_y = int(con_y_entry.get())
            max_pos_x = v_con_x
            max_pos_y = v_con_y
        except ValueError:
            error_message_prompt(resolution_ration_error_code)
        v_p_name = p_name_entry.get()
        v_a_name = a_name_entry.get()
        fm_con.forget()  # 点击设备信息的确定按钮之后，会暂时消除填入信息的行，再次点击‘请先点击输入设备信息’按钮之后会重新出现
        judge_con = 0
        # print("TestMethod: open_app")
        send('open_app', 0, 0, 0, 0, 0, 0, 0, v_p_name + '&' + v_a_name)
        nonlocal print_text
        print_text.delete(0, 'end')

    Button(fm_con, text="确定", command=click_b_con_confirm).pack(pady=5)

    def click_b_choose():
        nonlocal judge_choose_test
        nonlocal judge_con
        if (bool_ever_click_connect_button == 0):
            error_message_prompt(have_not_connect_error_code)
            return
        if (bool_is_device_connected_successful == 0):
            error_message_prompt(not_successful_connected_error_code)
            return
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
        # fm_ctrl.forget()
        fm_choose.forget()
        fm_touch.pack()

    def click_b_r_touch():
        # fm_ctrl.forget()
        fm_choose.forget()
        fm_r_touch.pack()

    def click_b_drag():
        # fm_ctrl.forget()
        fm_choose.forget()
        fm_drag.pack()

    def click_b_r_drag():
        # fm_ctrl.forget()
        fm_choose.forget()
        fm_r_drag.pack()

    fm_choose = Frame(root)

    b_choose = Button(root, text='选择测试类型', font=('黑体', 12), height=2, command=click_b_choose)
    b_choose.pack(fill='x')

    b_touch_test = Button(fm_choose, text='点击屏幕测试', font=('黑体', 10), height=3, command=click_b_touch)
    b_touch_test.pack(side='left')

    b_r_touch_test = Button(fm_choose, text='随机点击屏幕测试', font=('黑体', 10), height=3, command=click_b_r_touch)
    b_r_touch_test.pack(side='left')

    b_drag_test = Button(fm_choose, text='滑动屏幕测试', font=('黑体', 10), height=3, command=click_b_drag)
    b_drag_test.pack(side='left')

    b_r_drag_test = Button(fm_choose, text='随机屏幕测试', font=('黑体', 10), height=3, command=click_b_r_drag)
    b_r_drag_test.pack(side='left')

    # 点击屏幕测试

    v_pos_x = 0  # 点击的位置x
    v_pos_y = 0  # 点击的位置y
    v_touch_n = 0  # 点击的次数
    v_i_time = 1.00  # 多次点击时间隔时间,默认为1.00秒

    fm_touch = Frame(root)
    # fm1.pack(side = 'left',fill = 'y')
    label_fm_touch = Label(fm_touch, bg='white', text='点击屏幕测试', font=('黑体', 12))
    label_fm_touch.pack(fill='x', pady='5')

    pos_x = Label(fm_touch, text='点击的位置x:', pady=5)
    pos_x.pack(side='top')
    pos_x_text = StringVar()
    pos_x_entry = Entry(fm_touch, textvariable=pos_x_text)
    pos_x_text.set("")
    pos_x_entry.pack(side='top', pady=5)

    pos_y = Label(fm_touch, text='点击的位置y:', pady=5)
    pos_y.pack(side='top')
    pos_y_text = StringVar()
    pos_y_entry = Entry(fm_touch, textvariable=pos_y_text)
    pos_y_text.set("")
    pos_y_entry.pack(side='top', pady=5)

    touch_n = Label(fm_touch, text='点击的次数:', pady=5)
    touch_n.pack(side='top')
    touch_n_text = StringVar()
    touch_n_entry = Entry(fm_touch, textvariable=touch_n_text)
    touch_n_text.set("")
    touch_n_entry.pack(side='top', pady=5)

    i_time = Label(fm_touch, text='多次点击时间隔时间,默认为1秒:', pady=5)
    i_time.pack(side='top')
    i_time_text = StringVar()
    i_time_entry = Entry(fm_touch, textvariable=i_time_text)
    i_time_text.set("")
    i_time_entry.pack(side='top', pady=5)

    def click_b_confirm_touch():
        nonlocal print_text
        try:
            v_pos_x = int(pos_x_entry.get())
            v_pos_y = int(pos_y_entry.get())
            v_touch_n = int(touch_n_entry.get())
            v_i_time = float(i_time_entry.get())
            fm_touch.forget()
            fm_choose.pack()
            logic_error = 0
            if (v_pos_x < 0 or v_pos_x > max_pos_x):
                logic_error = 1
            if (v_pos_y < 0 or v_pos_y > max_pos_y):
                logic_error = 1
            if (v_touch_n < min_click_times or v_touch_n > max_click_times):
                logic_error = 1
            if (v_i_time < min_interval_time or v_i_time > max_interval_time):
                logic_error = 1
            if (logic_error == 1):
                error_message_prompt(logic_error_code)
            else:
                print_text.insert('end', "TestMethod: touch")
                print_text.insert('end', "点击位置:(%d,%d) 点击次数:%d 间隔时间:%f" % (v_pos_x, v_pos_y, v_touch_n, v_i_time))
                send('touch', v_pos_x, v_pos_y, 0, 0, v_touch_n, v_i_time, 0, 0)
        except ValueError:
            if (
                    pos_x_entry.get() == '' or pos_y_entry.get() == '' or touch_n_entry.get() == '' or i_time_entry.get() == ''):
                error_message_prompt(empty_error_code)
            else:
                error_message_prompt(number_error_code)

    Button(fm_touch, text="加入测试队列", command=click_b_confirm_touch).pack(pady=5)

    # 随机点屏幕

    v_r_touch_n = 0  # 点击的次数
    v_r_touch_time = 1.0  # 每两次点击间隔的时间，秒为单位

    fm_r_touch = Frame(root)
    label_fm_r_touch = Label(fm_r_touch, bg='white', text='随机点屏幕', font=('黑体', 12))
    label_fm_r_touch.pack(fill='x', pady='5')

    r_touch_n = Label(fm_r_touch, text='点击的次数:', pady=5)
    r_touch_n.pack(side='top')
    r_touch_n_text = StringVar()
    r_touch_n_entry = Entry(fm_r_touch, textvariable=r_touch_n_text)
    r_touch_n_text.set("")
    r_touch_n_entry.pack(side='top', pady=5)

    r_touch_time = Label(fm_r_touch, text='每两次点击间隔的时间，秒为单位:', pady=5)
    r_touch_time.pack(side='top')
    r_touch_time_text = StringVar()
    r_touch_time_entry = Entry(fm_r_touch, textvariable=r_touch_time_text)
    r_touch_time_text.set("")
    r_touch_time_entry.pack(side='top', pady=5)

    def click_b_r_touch_confirm():
        nonlocal print_text
        try:
            v_r_touch_n = int(r_touch_n_entry.get())
            v_r_touch_time = float(r_touch_time_entry.get())  # 间隔时间 对应interval time
            fm_r_touch.forget()
            fm_choose.pack()
            logic_error = 0
            if (v_r_touch_n < 0 or v_r_touch_n > max_click_times):
                logic_error = 1
            if (v_r_touch_time < min_interval_time or v_r_touch_time > max_interval_time):
                logic_error = 1
            if (logic_error == 1):
                error_message_prompt(logic_error_code)
            else:
                print_text.insert('end', "TestMethod: random_touch")
                print_text.insert('end', "点击次数:%d 间隔时间:%fs" % (v_r_touch_n, v_r_touch_time))
                send('random_touch', 0, 0, 0, 0, v_r_touch_n, v_r_touch_time, 0, 0)
        except ValueError:
            if (r_touch_n_entry.get() == '' or r_touch_time_entry.get() == ''):
                error_message_prompt(empty_error_code)
            else:
                error_message_prompt(number_error_code)

    Button(fm_r_touch, text="加入测试队列", command=click_b_r_touch_confirm).pack(pady=5)

    # 滑动屏幕测试

    v_start_x = 0  # 滑动起始位置x
    v_start_y = 0  # 滑动起始位置y
    v_end_x = 0  # 滑动结束位置x
    v_end_y = 0  # 滑动结束位置y
    v_d_time = 1  # 滑动持续时间,默认为1秒
    v_d_num = 1  # 滑动次数，默认为1次
    v_d_i_time = 1.0  # 多次点击时间隔时间,默认为1秒

    fm_drag = Frame(root)
    # fm3.pack(side = 'left',fill = 'y')
    label_fm_drag = Label(fm_drag, bg='white', text='滑动屏幕测试', font=('黑体', 12))
    label_fm_drag.pack(fill='x', pady='2')

    start_x = Label(fm_drag, text='滑动起始位置x:', pady=2)
    start_x.pack(side='top')
    start_x_text = StringVar()
    start_x_entry = Entry(fm_drag, textvariable=start_x_text)
    start_x_text.set("")
    start_x_entry.pack(side='top', pady=5)

    start_y = Label(fm_drag, text='滑动起始位置y:', pady=2)
    start_y.pack(side='top')
    start_y_text = StringVar()
    start_y_entry = Entry(fm_drag, textvariable=start_y_text)
    start_y_text.set("")
    start_y_entry.pack(side='top', pady=5)

    end_x = Label(fm_drag, text='滑动结束位置x:', pady=2)
    end_x.pack(side='top')
    end_x_text = StringVar()
    end_x_entry = Entry(fm_drag, textvariable=end_x_text)
    end_x_text.set("")
    end_x_entry.pack(side='top', pady=5)

    end_y = Label(fm_drag, text='滑动结束位置y:', pady=2)
    end_y.pack(side='top')
    end_y_text = StringVar()
    end_y_entry = Entry(fm_drag, textvariable=end_y_text)
    end_y_text.set("")
    end_y_entry.pack(side='top', pady=5)

    d_time = Label(fm_drag, text='滑动持续时间,默认为1秒:', pady=2)
    d_time.pack(side='top')
    d_time_text = StringVar()
    d_time_entry = Entry(fm_drag, textvariable=d_time_text)
    d_time_text.set("")
    d_time_entry.pack(side='top', pady=5)

    d_num = Label(fm_drag, text='滑动次数，默认为1次:', pady=2)
    d_num.pack(side='top')
    d_num_text = StringVar()
    d_num_entry = Entry(fm_drag, textvariable=d_num_text)
    d_num_text.set("")
    d_num_entry.pack(side='top', pady=5)

    d_i_time = Label(fm_drag, text='多次点击时间隔时间,默认为1秒:', pady=2)
    d_i_time.pack(side='top')
    d_i_time_text = StringVar()
    d_i_time_entry = Entry(fm_drag, textvariable=d_i_time_text)
    d_i_time_text.set("")
    d_i_time_entry.pack(side='top', pady=5)

    def click_b_drag_confirm():
        nonlocal print_text
        try:
            v_start_x = int(start_x_entry.get())
            v_start_y = int(start_y_entry.get())
            v_end_x = int(end_x_entry.get())
            v_end_y = int(end_y_entry.get())
            v_d_time = int(d_time_entry.get())
            v_d_num = int(d_num_entry.get())
            v_d_i_time = float(d_i_time_entry.get())
            fm_drag.forget()
            fm_choose.pack()
            logic_error = 0
            if (v_start_x < 0 or v_start_x > max_pos_x):
                logic_error = 1
            if (v_start_y < 0 or v_start_y > max_pos_y):
                logic_error = 1
            if (v_end_x < 0 or v_end_x > max_pos_x):
                logic_error = 1
            if (v_end_y < 0 or v_end_y > max_pos_y):
                logic_error = 1
            if (v_start_x == v_end_x or v_start_y == v_end_y):
                logic_error = 1
            if (v_d_time < min_drag_during_time or v_d_time > max_drag_during_time):
                logic_error = 1
            if (v_d_num < min_drag_times_number or v_d_num > max_drag_times_number):
                logic_error = 1
            if (v_d_i_time < min_drag_interval_time or v_d_i_time > max_drag_interval_time):
                logic_error = 1
            if (logic_error == 1):
                error_message_prompt(logic_error_code)
            else:
                print_text.insert('end', "TestMethod: drag")
                print_text.insert('end', "滑动起始位置:(%d,%d) 滑动结束位置:(%d,%d)" % (v_start_x, v_start_y, v_end_x, v_end_y))
                print_text.insert('end', "滑动持续时间: %f 滑动次数: %d 滑动间隔时间: %d" % (v_d_time, v_d_num, v_d_i_time))
                send('drag', v_start_x, v_start_y, v_end_x, v_end_y, v_d_num, v_d_i_time, v_d_time, 0)
        except ValueError:
            if (start_x_entry.get() == '' or start_y_entry.get() == '' or end_x_entry.get() == '' or \
                    end_y_entry.get() == '' or d_time_entry.get() == '' or d_num_entry.get() == '' or \
                    d_i_time_entry.get() == ''):
                error_message_prompt(empty_error_code)
            else:
                error_message_prompt(number_error_code)
        # print("TestMethod: drag )

    Button(fm_drag, text="加入测试队列", command=click_b_drag_confirm).pack(pady=5)

    # 随机滑动屏幕测试
    v_r_d_num = 0  # 滑动的次数，默认为0
    v_r_d_i_time = 1.0  # 每两次滑动间隔的时间，秒为单位

    fm_r_drag = Frame(root)
    label_fm_r_drag = Label(fm_r_drag, bg='white', text='随机滑动屏幕测试', font=('黑体', 12))
    label_fm_r_drag.pack(fill='x', pady='5')

    r_d_num = Label(fm_r_drag, text='滑动的次数:', pady=5)
    r_d_num.pack(side='top')
    r_d_num_text = StringVar()
    r_d_num_entry = Entry(fm_r_drag, textvariable=r_d_num_text)
    r_d_num_text.set("")
    r_d_num_entry.pack(side='top', pady=5)

    r_d_i_time = Label(fm_r_drag, text='每两次滑动间隔的时间，秒为单位:', pady=5)
    r_d_i_time.pack(side='top')
    r_d_i_time_text = StringVar()
    r_d_i_time_entry = Entry(fm_r_drag, textvariable=r_d_i_time_text)
    r_d_i_time_text.set("")
    r_d_i_time_entry.pack(side='top', pady=5)

    def click_b_r_drag_confirm():
        try:
            v_r_d_num = int(r_d_num_entry.get())
            v_r_d_i_time = float(r_d_i_time_entry.get())
            fm_r_drag.forget()
            fm_choose.pack()
            logic_error = 0
            if (v_r_d_num < min_drag_times_number or v_r_d_num > max_drag_times_number):
                logic_error = 1
            if (v_r_d_i_time < min_drag_interval_time or v_r_d_i_time > max_drag_interval_time):
                logic_error = 1
            if (logic_error == 1):
                error_message_prompt(logic_error_code)
            print_text.insert('end', "TestMethod: random_drag")
            print_text.insert('end', "滑动次数: %d 滑动间隔时间: %f" % (v_r_d_num, v_r_d_i_time))
            # print("TestMethod: random_drag 滑动次数: %d 滑动间隔时间: %f"%(v_r_d_num, v_r_d_i_time))
            send('random_drag', 0, 0, 0, 0, v_r_d_num, v_r_d_i_time, 1, 0)
        except ValueError:
            if (r_d_num_entry.get() == '' or r_d_i_time_entry.get() == ''):
                error_message_prompt(empty_error_code)
            else:
                error_message_prompt(number_error_code)

    Button(fm_r_drag, text="加入测试队列", command=click_b_r_drag_confirm).pack(pady=5)

    def click_start_b():
        nonlocal fin_in_b
        nonlocal b_con_phone
        nonlocal b_con
        nonlocal fm_con
        nonlocal b_choose
        nonlocal fm_choose
        nonlocal fm_touch
        nonlocal fm_r_touch
        nonlocal fm_drag
        nonlocal fm_r_drag

        if (bool_ever_click_connect_button == 0):
            error_message_prompt(have_not_connect_error_code)
            return
        if (bool_is_device_connected_successful == 0):
            error_message_prompt(not_successful_connected_error_code)
            return
        fin_in_b.forget()
        b_con_phone.forget()
        fm_con.forget()
        b_con.forget()
        fm_choose.forget()
        b_choose.forget()
        fm_touch.forget()
        fm_r_touch.forget()
        fm_drag.forget()
        fm_r_drag.forget()

        start_b.pack(side='top', fill='x')
        pause_b.pack(side='top', fill='x')
        resume_b.pack(side='top', fill='x')
        stop_b.pack(side='top', fill='x')
        return_in_b.pack(side='bottom', fill='x')

    def click_return_in_b():
        nonlocal b_con
        nonlocal b_choose
        nonlocal fin_in_b
        nonlocal start_b
        nonlocal pause_b
        nonlocal resume_b
        nonlocal stop_b
        nonlocal return_in_b

        start_b.forget()
        pause_b.forget()
        resume_b.forget()
        stop_b.forget()
        return_in_b.forget()

        b_con_phone.pack(fill='x')
        b_con.pack(fill='x')
        b_choose.pack(fill='x')
        fin_in_b.pack(fill='x', side='bottom')

    fin_in_b = Button(root, text='队列输入完毕', font=('黑体', 12), height=2, command=click_start_b)
    fin_in_b.pack(side='bottom', fill='x')

    start_b = Button(root, text='开始测试', font=('黑体', 12), height=2, command=start)  # 开始按钮
    pause_b = Button(root, text='暂停测试', font=('黑体', 12), height=2, command=pause)  # 暂停按钮
    resume_b = Button(root, text='继续测试', font=('黑体', 12), height=2, command=resume)  # 继续按钮
    stop_b = Button(root, text='终止测试', font=('黑体', 12), height=2, command=stop)  # 终止按钮
    return_in_b = Button(root, text='返回队列输入界面', font=('黑体', 12), height=2, command=click_return_in_b)  # 继续输入按钮

    root.mainloop()
    '''except:
        error_message_prompt(something_else_error_code)'''
# root = tk.Tk()
# test_UI(root)
