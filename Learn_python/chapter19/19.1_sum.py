#-*- coding:utf-8 -*-

__author__ = 'wangjf'


def sum1(L):
    if not L:
        return None
    first , *arg  = L
    return first if not arg else first + sum1(arg)

L = [1,2,3,4,5]
print(sum1(L))
print(sum1([]))