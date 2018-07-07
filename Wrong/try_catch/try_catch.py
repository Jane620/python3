# -*- coding: utf-8 -*-
# @Time    : 2018/7/5 下午5:15
# @Author  : Jane
# @Site    : 
# @File    : try_catch.py
# @Software: PyCharm


def divide(int):
    base = 100
    try:
        result = base / int
    except Exception as e:
        print("exception: ",e)


def divide_fix(int):
    base = 100
    try:
        result = base / int
    except ZeroDivisionError as e:
        print("exception: ", e)


if __name__ == '__main__':
    import time as tm
    t1 = tm.time()
    divide(0)
    t2 = tm.time()
    divide_fix(0)
    t3 = tm.time()
    print("第一个{0}，第二个{1}".format(t2-t1,t3-t2))
    print(2 and 3)