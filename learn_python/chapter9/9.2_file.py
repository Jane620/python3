#-*- coding:utf-8 -*-

'''
open 打开一个文件

'''

file_stream = open(r'..\resource\textfile','r')
for line in file_stream:
    print(line)

#eval  将字符串当做可执行程序代码
