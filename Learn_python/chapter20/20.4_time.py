#-*- coding:utf-8 -*-

__author__ = 'wangjf'

import time

reps = 1000

replist = range(reps)

def timer(func,*args,**kwargs):
    start = time.clock()
    for i in replist:
        ret = func(*args,**kwargs)
    elapsed = time.clock()-start
    return (elapsed,ret)



import sys

reps2 = 10000
replist2 = range(reps2)

def forloop():
    res = []
    for x in replist2:
        res.append(abs(x))
    return res

def listcomp():
    return [abs(x) for x in replist2]
    #return [x+1 for x in replist2]

def mapcall():
    return list(map(lambda x:x+1,replist2))
    #return list(map(abs(x),replist2))

def getexpr():
    return list(abs(x) for x in replist2)

def genfunc():
    def gen():
        for x in replist2:
            yield x
    return list(gen())

print(sys.version)

for test in (forloop,listcomp,mapcall,getexpr,genfunc):
    elapsed , ret = timer(test)
    print('-' * 33)
    print('{0}:{1} => [{2}...{3}]'.format(test.__name__,elapsed,ret[0],ret[-1]))


# 低数量级，可以看出listcomp存在一定优势，如果增大数量级，可见map最优
# 楼上的结论属于，当调用的为内置函数时，如果为一般的自定义函数，例如lambda，则依旧还是列表推导式性能快