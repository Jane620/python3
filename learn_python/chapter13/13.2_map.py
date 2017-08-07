#-*- coding:utf-8 -*-

import dis


# map(func,args) 通常args为可迭代对象，将func适用于遍历的args每个对象


# for ,map,list推导式检查调用底层代码的资源，比较三种方式的效率

#增加函数add_func ?
def dis_for(array):
    a = []
    add_func = a.append
    for i in array:
        add_func(i+1)
    return a

def dis_for2(array):
    for x in range(len(array)):
        array[x] += 10
    return array

def dis_map(array):
    return map(lambda x:x+1,array)
    #return map(int.__add__ , array)

def dis_list(array):
    return [x+1 for x in array]

num = [1,2,3,4]
dis.dis(dis_for2)
#print(dis_for(num))