#-*- coding:utf-8 -*-

__author__ = 'wangjf'

'''
1. from xx import xx 会将其中的变量名全部复制出来，对命名空间造成破坏，也可能让导入者获得超过所需的变量，通过其他方式变更变量
2. 对于需要进行导入的变量通过__all__=['error'，'encode']的方式，在模块顶层进行复制展示，通过此让人知道
3. 对于不想展示的部分，通过_x的方式进行隐藏
'''

class Person:

    __all__ = [""]

    _addrs = None

    def __init__(self):
        pass

