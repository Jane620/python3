#-*- coding:utf-8 -*-

# 检测某个类型的类型 有三种方式
list_a = [1,2,3]

print(type(list_a))

if type(list_a) == type([]):
    print('yes1')

if type(list_a) == list:
    print('yes2')

if isinstance(list_a,list):
    print('yes3')

#需要注意，在函数或者后续的类中使用这类判断，会破坏整体的结构，因此只限制一类类型的使用，不能做到通用