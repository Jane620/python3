# -*- coding:utf-8 -*-
'''
@author: jwang
@license: (C) Copyright 2018-2019, Nokia Sbell Tech Corporation Limited.
@contact: jianfeng.2.wang@nokia-sbell.com
@software: Pycharm
@file: 0_algorithms.py
@time: 2019/1/2 13:49
@desc:
'''

from algorithms.sort import merge_sort


if __name__ == '__main__':
    my_list = [1,9,3,6,10,5,4,22,7]
    my_list = merge_sort(my_list)
    print(my_list)