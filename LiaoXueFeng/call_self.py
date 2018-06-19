# -*- coding: utf-8 -*-
# @Time    : 2018/4/25 上午11:44
# @Author  : Jane
# @Site    : 
# @File    : call_self.py
# @Software: PyCharm


class Student:

    def __init__(self,name):
        self._name = name

    # call object self  ,object = method ,method = object
    def __call__(self, *args, **kwargs):
        print('hello,',self._name)


if __name__ == '__main__':
    s = Student('jane')
    s()
    # callable return the object can be callable or not
    print(callable(s))
    print(callable([]))