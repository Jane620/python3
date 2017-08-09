#-*- coding:utf-8 -*-

__author__ = 'wangjf'


# 返回多个参数的方式
def multiple(x,y):
    x = 2
    y = [3,4]
    return x,y

x = 1
L = [1,2]
x,L = multiple(x,L)
print(x,L)

#任意参数的实例

def f(*args):
    print(args)

f(1)
f(1,2,3,4)


#
def tracker(func,*args,**kargs):
    print('call func',func.__name__)
    return func(*args,**kargs)

def func3(a,b,c,d):
    return a + b + c + d

print(tracker(func3,1,2,c=3,d=4))


# *args 和 **kwargs用法

def func_var_args(fargs,*args):
    print('args:',fargs)
    for value in args:
        print('another args:',value)

def func_var_kwarg(fargs,**kwargs):
    print('args:',fargs)
    for key in kwargs:
        print('another keyword args:{0}:{1}'.format(key,kwargs[key]))

func_var_args(1, 'two', 3)
func_var_kwarg(fargs=1, arg2='two', arg3=3)
