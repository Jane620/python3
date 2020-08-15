# -*- coding:utf-8 -*-
'''
@author: jwang
@license: (C) Copyright 2018-2019, Nokia Sbell Tech Corporation Limited.
@contact: jianfeng.2.wang@nokia-sbell.com
@software: Pycharm
@file: 4_josephus.py
@time: 2019/1/7 15:41
@desc:
'''



def josephus(int_list,skip):
    skip = skip - 1  # list start with 0 ，so if you want skip the 3rd ,it means the 2nd in list
    idx = 0
    len_list = len(int_list)
    while len_list > 0:
        # 将步长 + 当前位置 余 整个列表的长度来确定需要移除的索引
        idx = (skip + idx) % len_list
        yield int_list.pop(idx)
        len_list -= 1


if __name__ == '__main__':
    list_t = [1,2,3,4,5,6,7,8,9,10,11]
    result = josephus(list_t,3)
    for i in range(10):
        print(next(result))