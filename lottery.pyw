# -*- coding: utf-8 -*-  
__author__ = 'wangyang'
from Tkinter import *   #引入Tkinter工具包
import tkMessageBox
import os,sys
import random
import time,sched
import threading
import tkFileDialog
import xlrd
import pyglet


def hello():
    print('hello world!')

class Lottery:

    def __init__(self):

        self.user_list = []
        self.event = threading.Event() #消息
        self.event.clear() #设置消息

        self.is_stop = False #由于最后关闭线程

        self.t = threading.Thread(target = self.show_random_user_thread,args = ())
        self.t.start() #启动循环线程

        # self.read_from_file('test.txt')
        self.draw()
    def __del__( self ): 
        pass
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
        self.event.set()
        self.is_stop =True

    def begin(self):
        self.event.set()
        

    def end(self):
        self.event.clear()

    def show_random_user_thread(self):
        cur_user = None;
        while self.is_stop == False:
            if not self.event.isSet():
                if cur_user != None:
                    self.select_one(cur_user)
                self.event.wait()
            else:
                cur_user = self.choose_next();
                if not cur_user == None:
                    self.v.set(cur_user)
                time.sleep(0.1)

    def read_from_file(self, filename):
        '''从excel读取'''
        file_handle = xlrd.open_workbook(filename)
        sheet = file_handle.sheet_by_index(0)
        lines = (sheet.col_values(0,1)) # 假设第一列是姓名,可调整
        # if file_handle == null:
        #   return;
        # self.user_list =[]

        for line in lines:
            self.user_list.append(line)
            print line
            
        self.v.set(len(self.user_list))

    def select_one(self, select_user):
        self.user_list.remove(select_user)

    def choose_next(self):
        num = len(self.user_list)
        if num > 0 :
            rand = random.randint(0, num - 1)
            chosen_user = self.user_list[rand]
            # del user_list[rand]
            return chosen_user
        return None

    def open_file(self):
        filename = tkFileDialog.askopenfilename(initialdir = "./")
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
        def musicplay():
            song = pyglet.media.load('music.mp3')
            song.play()
            pyglet.app.run()
                
        musicplay_thread = threading.Thread(target=musicplay)
        musicplay_thread.daemon = True
        musicplay_thread.start()
        main()
    except KeyboardInterrupt:
        pass
