# -*- coding: utf-8 -*-

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.


#!/usr/bin/python
# -*- coding: UTF-8 -*-




#引入包

import threading    #线程包
import time         
import tkinter as tk    #ｔｋ包
import m_serial     #自己的串口通讯包


class Application(tk.Frame):
    #构造函数
    def __init__(self, master=None):
        super().__init__(master)        
        self.pack()        #显示主窗体
        self.t0 = threading.Thread(target = self.create_widgets(),name='t0')    #把窗体构建方法作为一个线程启动
        self.t1 = threading.Thread(target = self.loopshow,name='t1')            #修改窗体标签内容作为一个线程启动
        self.t0.start()                                                         #启动窗体部件构建线程
        self.t1.start()                                                         #修改窗体标签内容的线程
       
        
              
        

    def create_widgets(self):                                                 #构建窗体部件方法
        
        #######################################################################
        
        self.label_pm25 = tk.Label()                                            #创建一个标签
        #self.label_pm25['text'] = "pm25:"
        self.label_pm25.pack()                                                  #显示此标签
        
        self.label_pm10 = tk.Label()
        #self.label_pm10['text'] = "pm10:"
        self.label_pm10.pack()
        
        self.label_tvoc = tk.Label()
        #self.label_tvoc['text'] = "有机物:"
        self.label_tvoc.pack()
        
        self.label_humi = tk.Label()
        #self.label_humi['text'] = "湿度:"
        self.label_humi.pack()
        
        self.label_temp = tk.Label()
        #self.label_temp['text'] = "温度:"
        self.label_temp.pack()
        
        self.label_hcho = tk.Label()
        #self.label_hcho['text'] = "甲醛:"
        self.label_hcho.pack()
        
        
        #####################################################################
        
        '''
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")
        

        self.quit = tk.Button(self, text="QUIT", fg="red",command=root.destroy)
        self.quit.pack()
        '''

    def loopshow(self):                                                        #修改标签方法,直接引用了外部函数
        loop_show(1)


    def say_hi(self):
        self.label_pm25['text'] = '改'
    
    
#显示
    
def loop_show(inc):                                                            #修改窗体标签内容的函数,调用了读取串口数据模块
    
    while True:    
        s = m_serial.show_serial_data(m_serial.read_serial())
        '''
        print('pm2.5:'+s.pm25())
        print('pm10:'+s.pm10())
        print('有机物:'+s.tvoc())
        print('湿度:'+s.humi())
        print('温度:'+s.temp())
        print('甲醛:'+s.hcho())
        '''
        app.label_pm25['text'] = 'pm2.5:'+s.pm25()
        app.label_pm10['text'] = 'pm10:'+s.pm10()
        app.label_tvoc['text'] = '有机物:'+s.tvoc()
        app.label_humi['text'] = '湿度:'+s.humi()
        app.label_temp['text'] = '温度:'+s.temp()
        app.label_hcho['text'] = '甲醛:'+s.hcho()

        time.sleep(inc)

        

#启动窗体主函数和窗体的基本属性设置
root = tk.Tk()
app = Application(master=root)
app.master.title('sss')                                                         #标题栏
app.master.overrideredirect(0)                                                  #显示隐藏窗体标题栏开关
app.master.resizable(0,0)                                                       #控制窗体尺寸可否修改
app.master.minsize(500,300)                                                     #窗体最小尺寸


        


app.mainloop()                                                                  #启动tk主函数!







