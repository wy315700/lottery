# -*- coding: utf-8 -*-  
__author__ = 'wangyang'
from Tkinter import *   #引入Tkinter工具包
import os
import random
import time,sched
import threading

this_file_path = os.path.split(os.path.realpath(__file__))[0] + '\\';


def hello():
    print('hello world!')

class Lottery:

    def __init__(self):

        self.user_list = []
        self.is_stop = True #是否停止
        self.read_from_file('test.txt')
        self.draw()
    def __del__( self ):  
        self.is_stop = True 
    def draw(self):
        self.win = Tk()  #定义一个窗体
        self.win.title('Hello World')    #定义窗体标题
        self.win.geometry('600x400')     #定义窗体的大小，是400X200像素

        bottonframe = Frame(self.win, height = 30)
        bottonframe.pack(fill=X, side = BOTTOM )


        buttonframe = Frame(self.win)
        buttonframe.pack( side = BOTTOM )


        self.begin_btn = Button(buttonframe, text='开始' ,height = 4, width = 10,  padx = 5, command=self.begin)
        #注意这个地方，不要写成hello(),如果是hello()的话，
        #会在mainloop中调用hello函数，
        # 而不是单击button按钮时出发事件
        self.begin_btn.pack(expand=NO, fill=X, side=LEFT) #将按钮pack，充满整个窗体(只有pack的组件实例才能显示)
        self.end_btn = Button(buttonframe, text='结束' ,height = 4, width = 10, padx = 5, command=self.end)
        #注意这个地方，不要写成hello(),如果是hello()的话，
        #会在mainloop中调用hello函数，
        # 而不是单击button按钮时出发事件
        self.end_btn.pack(expand=NO, fill=X, side=LEFT) #将按钮pack，充满整个窗体(只有pack的组件实例才能显示)
        self.v = StringVar() 

        self.ans_label = Label(self.win,textvariable = self.v , font = (NONE,40), height = 10 , width = 10 );
        self.v.set("hello world")
        self.ans_label.pack();
        self.v.set("hello")


        self.win.mainloop() #进入主循环，程序运行
        self.is_stop = True

    def begin(self):
        self.is_stop = False
        self.t = threading.Thread(target = self.show_random_user_thread,args = ())
        self.t.start()

    def end(self):
        self.is_stop = True

    def show_random_user_thread(self):
        while self.is_stop == False:
            cur_user = self.choose_next();
            self.v.set(cur_user)
            time.sleep(0.1)

    def read_from_file(self, filename):
        file_handle = open(this_file_path + filename)
        # if file_handle == null:
        #   return;
        line = file_handle.readline()

        while len(line) > 0 :
            line = line.rstrip('\r\n')
            line = line.replace('\n','')
            line = line.replace('\r','')
            self.user_list.append(line)
            print line
            line = file_handle.readline()
        file_handle.close()

    def choose_next(self):
        num = len(self.user_list)
        rand = random.randint(0, num - 1)
        chosen_user = self.user_list[rand]
        # del user_list[rand]
        return chosen_user

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
