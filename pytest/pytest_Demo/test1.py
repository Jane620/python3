# -*- coding:utf-8 -*-
'''
@author: jwang
@license: (C) Copyright 2018-2019, Nokia Sbell Tech Corporation Limited.
@contact: jianfeng.2.wang@nokia-sbell.com
@software: Pycharm
@file: test1.py
@time: 2019/8/26 14:13
@desc:
'''

def test_passing():
    assert (1,2,3) == (1,2,3)


def inc(x):
    return x + 1

def test_answer():
    assert inc(4) == 5