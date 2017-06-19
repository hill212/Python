#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-15 09:41:35
# @Author  : zhangbs


# urllib3需要提前pip install urllib3
import urllib3

'''循环按行读取txt文件，文件中按行存储手机号码'''
for line in open("E:/TestDev/TestCode/test/infobirdtools/areacodehttp/zxno.txt"):
    no = line
    # strip()方法用于移除字符串头尾的指定字符，这里移除换行符，避免输入号码之间有空行
    ygno = no.strip()
    url = 'http://118.178.123.42:8088/index.html?PhoneNum=' + ygno
    # urllib3 方法发送http get消息，r.data数据 r.head为头信息
    http = urllib3.PoolManager()
    r = http.request('GET', url)
    b = r.data
    # get请求返回信息为byte，形如b'123中文' ,需要用str方法转换成string并且用gbk编码因为返回结果含中文
    s = str(b, encoding="gbk")
    res = ygno + ',' + s
    # print(res)
    f = open("E:/TestDev/TestCode/test/infobirdtools/areacodehttp/res.txt", "a")
    # 写入文件时每行后面加上换行符
    f.write(res + '\r\n')
    f.close()
