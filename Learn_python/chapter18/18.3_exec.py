#-*- coding:utf-8 -*-

__author__ = 'wangjf'


# 接受多个参数，并且能对内部的值求最小值

# 方法1需要将参数进行分割，首位后后续对比
def min1(*args):
    res = args[0]
    for value in args[1:]:
        if  res > value:
            res = value
    return res

#方法2对1中进行额外处理，将first独立出来
def min2(first , *args):
    for value in args:
        if first > value:
            first = value
    return first

#方法3将args列表化，然后通过sort进行排序
def min3(*args):
    tmp = list(args)
    tmp.sort()
    return tmp[0]

print(min1(1,3,5,2,5))
print(min2('b','d','a'))
print(min3([2,2],[1,3],[3,4]))


# 方法4 可以将函数作为first入参，通过分别调用其他函数来支持min和max支持
def minmax(func,*args):
    res = args[0]
    for value in args[1:]:
        if func(value,res):
            res = value
    return res

def getmin(x,y):
    return x < y
def getmax(x,y):
    return x > y

print(minmax(getmin,1,3,2,4,5,6))
print(minmax(getmax,1,3,2,4,5,6))


# 尝试编写print
import sys

def print30(*args,**kwargs):
    sep = kwargs.get('sep',' ')
    end = kwargs.get('end', '\n')
    file = kwargs.get('file', sys.stdout)
    output = ''
    first = True
    for arg in args:
        output += ('' if first else sep) +str(arg)
        first = False
    file.write(output + end)

print30(1,2,3)
print30(1,2,3,sep='5')



