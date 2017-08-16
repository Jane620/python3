#-*- coding:utf-8 -*-

__author__ = 'wangjf'


D = {'a':1,'b':2}
iter1 = iter(D)
# 仅输出key
#print(next(iter1))

for value in iter1:
    print(value,D[value])

G = ((x, x * x) for x in range(5))
print(next(G))