# -*- coding: utf-8 -*-  
__author__ = 'wangyang'
from Tkinter import *   #引入Tkinter工具包
import tkMessageBox
import os
import random
import time,sched
import threading
import tkFileDialog


def hello():
    print('hello world!')

class Lottery:

    def __init__(self):

        self.user_list = []
        self.is_stop = threading.Event() #是否停止
        self.is_stop.clear() #设置停止标志符

        self.t = threading.Thread(target = self.show_random_user_thread,args = ())
        self.t.start() #启动循环线程

        # self.read_from_file('test.txt')
        self.draw()
    def __del__( self ):  
        self.t.stop()
    def draw(self):
        self.win = Tk()  #定义一个窗体
        self.win.title('Hello World')    #定义窗体标题
        self.win.geometry('600x400')     #定义窗体的大小，是400X200像素

        bottonframe = Frame(self.win, height = 30)
        bottonframe.pack(fill=X, side = BOTTOM )


        buttonframe = Frame(self.win)
        buttonframe.pack( side = BOTTOM )

        #开始按钮
        self.begin_btn = Button(buttonframe, text='开始' ,height = 4, width = 10,  padx = 5, command=self.begin)
        self.begin_btn.pack(expand=NO, fill=X, side=LEFT) #将按钮pack，充满整个窗体(只有pack的组件实例才能显示)

        #结束按钮
        self.end_btn = Button(buttonframe, text='结束' ,height = 4, width = 10, padx = 5, command=self.end)
        self.end_btn.pack(expand=NO, fill=X, side=LEFT) #将按钮pack，充满整个窗体(只有pack的组件实例才能显示)


        #显示窗口
        self.v = StringVar() 

        self.ans_label = Label(self.win,textvariable = self.v , font = (NONE,40), height = 10 , width = 10 );
        self.v.set("hello world")
        self.ans_label.pack();
        self.v.set("hello")

        #菜单
        menubar = Menu(self.win)

        #创建下拉菜单File，然后将其加入到顶级的菜单栏中
        filemenu = Menu(menubar,tearoff=0)
        filemenu.add_command(label="Open", command=self.open_file)
        # filemenu.add_command(label="Save", command=hello)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.win.destroy)
        menubar.add_cascade(label="File", menu=filemenu)

        #创建下拉菜单Help
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="About", command=self.hello)
        menubar.add_cascade(label="Help", menu=helpmenu)


        #显示菜单
        self.win.config(menu=menubar)

        self.win.mainloop() #进入主循环，程序运行
        self.is_stop = True

    def begin(self):
        self.is_stop.set()
        

    def end(self):
        self.is_stop.clear()

    def show_random_user_thread(self):
        cur_user = - 1;
        while True:
            if not self.is_stop.isSet():
                if cur_user != -1:
                    self.select_one(cur_user)
                self.is_stop.wait()
            else:
                cur_user = self.choose_next();
                self.v.set(cur_user)
                time.sleep(0.1)

    def read_from_file(self, filename):
        file_handle = open(filename)
        # if file_handle == null:
        #   return;
        self.user_list =[]
        line = file_handle.readline()

        while len(line) > 0 :
            line = line.rstrip('\r\n')
            line = line.replace('\n','')
            line = line.replace('\r','')
            self.user_list.append(line)
            print line
            line = file_handle.readline()
        file_handle.close()
        self.v.set(len(self.user_list))

    def select_one(self, select_user):
        self.user_list.remove(select_user)

    def choose_next(self):
        num = len(self.user_list)
        rand = random.randint(0, num - 1)
        chosen_user = self.user_list[rand]
        # del user_list[rand]
        return chosen_user

    def open_file(self):
        filename = tkFileDialog.askopenfilename(initialdir = __file__)
        if filename != '':
            self.read_from_file(filename)
    def hello(self):
        tkMessageBox.showinfo("Hello World!","千千世界 静静倾听 天外之音")

def main():
    # read_from_file('test.txt')
    # print user_list

    # print choose_next();
    
    app = Lottery()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
