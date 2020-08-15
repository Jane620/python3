# -*- coding:utf-8 -*-
'''
@author: jwang
@license: (C) Copyright 2018-2019, Nokia Sbell Tech Corporation Limited.
@contact: jianfeng.2.wang@nokia-sbell.com
@software: Pycharm
@file: 5_max_one_index.py
@time: 2019/1/7 16:27
@desc:
repalce 1 num e.g 0 to let the array with the max length

let input array = [1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1]
If we replace 0 at index 3 with 1, we get the longest continuous
sequence of 1s in the array.
So the function return => 3
'''


def max_ones_index(arr):

    n = len(arr)
    max_count = 0
    max_index = 0
    prev_zero = -1
    prev_prev_zero = -1

    for curr in range(n):

        # If current element is 0,
        # then calculate the difference
        # between curr and prev_prev_zero
        if arr[curr] == 0:
            # 第一道保障，确保当只有计算出来的比上一次的最长还长才进行下去，因此只要记录一次上一次和上上次即可
            if curr - prev_prev_zero > max_count:
                max_count = curr - prev_prev_zero
                max_index = prev_zero

            prev_prev_zero = prev_zero
            prev_zero = curr
    # 意图不明？ 整长 - 上上次的索引位置 > 最大长度
    if n - prev_prev_zero > max_count:
        #  则最长索引去上次
        max_index = prev_zero

    return max_index


if __name__ == '__main__':
    input_array = [1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1]
    max_array = max_ones_index(input_array)
    print(max_array)