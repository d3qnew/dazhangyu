# -*- coding: utf-8 -*-

# 串口通讯模块,读取16进制数字转换成字符串

#import time
import serial                                                                   #串口通讯库
import binascii                                                                 #ASCII码库


ser = serial.Serial( #下面这些参数根据情况修改
    port='/dev/ttyUSB0',                                                        #串口端口号,linux用的是设备名
    baudrate=9600                                                               #波特率
)


def read_serial():                                                             #读取串口数据函数
    serial_data = ''                                                            #要返回的串口数据字符串
    d = str(binascii.b2a_hex(ser.read()))[2:-1]                                 #读取一次串口返回值,去除头尾留下一个2位的16进制数字并转换成字符串
   
    while(d!='aa'):                                                             #如果取值非AA,向后取值
        d = str(binascii.b2a_hex(ser.read()))[2:-1]                             
    if(d == 'aa'):                                                              #如果取值为aa,开始构建返回字符串
        for i in range(15):                                                     #数据一共16组
            if(i>2):                                                            #抛掉前3组
                serial_data = serial_data+d                                     #累加字符串
            d = str(binascii.b2a_hex(ser.read()))[2:-1]                         #对下一组数据取值
        print(serial_data)
        return serial_data                                                      #返回整理好的16进制字符串


class show_serial_data:                                                       #对整串16进制字符串进行分割并转换为10进制,按照规则计算出6组数据
    
    def __init__(self,data):
        self.data = data

    def pm25(self):                                                             #pm2.5
        return str(int(self.data[0:2],16)*256+int(self.data[2:4],16))
    
    def pm10(self):                                                             #pm10
        return str(int(self.data[4:6],16)*256+int(self.data[6:8],16))
    
    def tvoc(self):                                                             #有机物
        return str((int(self.data[8:10],16)*256+int(self.data[10:12],16))/100)
    
    def humi(self):                                                             #湿度
        return str(int(self.data[12:14],16)*256+int(self.data[14:16],16)/10)
    
    def temp(self):                                                             #温度
        return str(int(self.data[16:18],16)*256+int(self.data[18:20],16)/10)
    
    def hcho(self):                                                             #甲醛
        return str(int(self.data[20:22],16)*256+int(self.data[22:24],16)/100)
    
'''测试读取 
def loop_show():
    s = show_serial_data(read_serial())    
    print('pm2.5:'+s.pm25())
    print('pm10:'+s.pm10())
    print('有机物:'+s.tvoc())
    print('湿度:'+s.humi())
    print('温度:'+s.temp())
    print('甲醛:'+s.hcho())
'''


