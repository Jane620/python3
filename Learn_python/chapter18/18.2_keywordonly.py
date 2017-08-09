#-*- coding:utf-8 -*-

__author__ = 'wangjf'

# 如果传参存在* ，则*后面的参数必须进行指定为keyword，否则会出TypeError
def func1(a, *, b, c):
    print(a,b,c)

#func1(1,2,3)
#func1(1)
func1(1,b=2,c=3,)

# **后面不能再跟其他参数,但是前面可以进行指定
#def func2(a,**kwargs,b,c):
def func2(a,b=2,c=3,**kwargs):
    print(a,b,c)
    for key in kwargs:
        print('another args:{0},{1}'.format(key,kwargs[key]))

func2(1,b=3,c=4,key=6,value=7)



