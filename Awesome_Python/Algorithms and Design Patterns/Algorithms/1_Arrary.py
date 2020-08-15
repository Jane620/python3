# -*- coding:utf-8 -*-
'''
@author: jwang
@license: (C) Copyright 2018-2019, Nokia Sbell Tech Corporation Limited.
@contact: jianfeng.2.wang@nokia-sbell.com
@software: Pycharm
@file: 1_Arrary.py
@time: 2019/1/2 13:53
@desc:
'''\


from algorithms.arrays import delete_nth
import collections


def delte_nth_list(array,n):
    result = []
    # 将array的值作为key, 出现的次数进行累计
    count = collections.defaultdict(int)

    for i in array:
        # 判断出现次数与我实际要求的次数进行对比，不足部分进行append
        if count[i] < n:
            result.append(i)
            print("count[i]:",count[i])
            # key出现次数进行累计
            count[i] += 1
            print("count:",count)

    return result


if __name__ == '__main__':
    native_array = [1, 2, 3, 1, 2, 4, 1, 1, 2, 5]

    # list.count(value)也可以计算列表某个数字的出现次数，总体time complex O(n^2)
    # 删除列表中出现次数少于2的数字
    # result_array = delete_nth(native_array,1)    time complex O(n)
    # print(result_array)
    result = delte_nth_list(native_array,1)