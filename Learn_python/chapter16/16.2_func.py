#-*- coding:utf-8 -*-

__author__ = 'wangjf'

# global声明一个全局命名空间
x = 88
def call_num():
    global x
    x = 99
    #return x

print(x)
call_num()
print(x)