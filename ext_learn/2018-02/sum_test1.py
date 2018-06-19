# -*- coding: utf-8 -*-
# @Time    : 2018/5/21 下午2:44
# @Author  : Jane
# @Site    : 
# @File    : sum_test1.py
# @Software: PyCharm

def getinfo():
    list_1 = []
    for i in range(1,100):
        if i%3 ==0 or i%5 == 0:
            list_1.append(i)

    value = map(sum,list_1)
    #value = ''.join(value)
    return value

if __name__ == '__main__':
    s = getinfo()
    print(type(s))