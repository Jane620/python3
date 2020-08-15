# -*- coding:utf-8 -*-
'''
@author: jwang
@license: (C) Copyright 2018-2019, Nokia Sbell Tech Corporation Limited.
@contact: jianfeng.2.wang@nokia-sbell.com
@software: Pycharm
@file: 2_Flatten.py
@time: 2019/1/2 14:41
@desc:
'''

from algorithms.arrays import flatten,flatten_iter
from collections import Iterable


def flatten_list(iterator):
    for ele in iterator:
        if isinstance(ele, Iterable):
            # yield from 返回迭代器的值，而yield则返回迭代器本身
            yield from flatten_iter(ele)
        else:
            yield ele


if __name__ == '__main__':
    my_list = [[7,8],[6,5,4],[3,2,1]]

    result_list = flatten(my_list)
    iter_list = flatten_list(my_list)
    #print(result_list)
    try:
        for i in range(81):
            print(iter_list.__next__())
    except StopIteration:
        pass
        #print("StopIteration")
