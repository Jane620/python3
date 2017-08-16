#-*- coding:utf-8 -*-

__author__ = 'wangjf'


# 不进行指定则默认按照顺序
def func1(a,b=4,c=5):
    print(a,b,c)

func1(1,2)

# *args作为元祖
def func2(a,*args):
    print(a,args)

func2(1,2,3)

# **kwargs输出字典，将key：value均输出
def func3(a,**kwargs):
    print(a,kwargs)

func3(a=1,b=2,c=3)

# 传入参数为* 的时候，匹配了b,c
def func4(a,b,c=3,d=4,e=5) -> int:
    print(a,b,c,d,e)

func4(4,*(5,6,7,8))

print(func4.__annotations__)