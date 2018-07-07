# -*- coding: utf-8 -*-
# @Time    : 2018/7/5 下午5:04
# @Author  : Jane
# @Site    : 
# @File    : append_wrong.py
# @Software: PyCharm

def do_append(int=0,list=[]):
    list.append(int)
    print(int)
    print(list)

def do_append_fix(int=0,list=None):
    # 仅当传入为空，才进行初始化，否则按照正常来
    if list is None:
        list = []
    list.append(int)
    print(int)
    print(list)

if __name__ == '__main__':
    do_append(1)
    do_append(2)
    do_append(3,[4])
    # 为何出现[1，2]
    # 因为函数本身也是一个对象，append会改变对象的属性，因此会保留对象的改变
    print("---------")
    do_append_fix(1)
    do_append_fix(2)
    do_append_fix(3,[4])