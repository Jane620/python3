# -*- coding:utf-8 -*-
'''
@author: jwang
@license: (C) Copyright 2018-2019, Nokia Sbell Tech Corporation Limited.
@contact: jianfeng.2.wang@nokia-sbell.com
@software: Pycharm
@file: College_QA.py
@time: 2019/7/31 10:54
@desc:
'''


class A:
    def __init__(self):
        self.n = 2

    def add(self, m):
        print('self is {0} @A.add'.format(self))
        self.n += m

class E:
    def __init__(self):
        self.n = 6

    def add(self, m):
        print('self is {0} @E.add'.format(self))
        #super().add(m)
        self.n += 6


class B(E):
    def __init__(self):
        self.n = 3

    def add(self, m):
        print('self is {0} @B.add'.format(self))
        super().add(m)
        self.n += 3

class C(A):
    def __init__(self):
        self.n = 4

    def add(self, m):
        print('self is {0} @C.add'.format(self))
        super().add(m)
        self.n += 4


class D(B, C):
    def __init__(self):
        self.n = 5

    def add(self, m):
        print('self is {0} @D.add'.format(self))
        super().add(m)
        self.n += 5


if __name__ == '__main__':
    d = D()
    #D.mro()
    #print(D.mro())
    d.add(2)
    print(d.n)