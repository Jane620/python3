# -*- coding:utf-8 -*-
'''
@author: jwang
@license: (C) Copyright 2018-2019, Nokia Sbell Tech Corporation Limited.
@contact: jianfeng.2.wang@nokia-sbell.com
@software: Pycharm
@file: 20_scale.py
@time: 2019/4/25 10:48
@desc:
'''

# n=进制，x=输入值
def f(n,x):
    a = [0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F','G','H','I','J']
    b = []
    while True:
        while True:
            s = x // n  # 商
            y = x % n  # 余数
            b = b + [y]
            if s == 0:
                break
            x = s
        b.reverse()
        for i in b:
            print(a[i], end='')

#f(20, 2012)
print(2012%12)


