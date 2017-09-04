#-*- coding:utf-8 -*-

__author__ = 'wangjf'

import functools

# reduce函数接受2个参数，并循环调用func，计算最终结果
# 也可以提供初始值，计算方式则为
# f(1,2) -> f(f(1,2),3) ....
# f(100,1) -> f(f(100,1),2)...

def f(x,y):
    return x+y

list1 = [1,2,3,4,5]
res1 = functools.reduce(f,list1)
print(res1)
res2 = functools.reduce(f,list1,100)
print(res2)

