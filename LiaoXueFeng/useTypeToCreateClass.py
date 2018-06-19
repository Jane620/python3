# -*- coding: utf-8 -*-
# @Time    : 2018/4/25 下午5:21
# @Author  : Jane
# @Site    : 
# @File    : useTypeToCreateClass.py
# @Software: PyCharm


def fn(self,name='world'):
    print('hello',name)

if __name__ == '__main__':
    # type for 3 args
    # class name = Hello
    # extends object
    # method hello = fn
    Hello = type('Hello',(object,),dict(hello=fn))
    h = Hello()
    h.hello()