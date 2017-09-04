#-*- coding:utf-8 -*-

__author__ = 'wangjf'
"""
documentation
"""
s1,s2 = 'abc','defg'

list1 = [s for s in [s1,s2]]
list2 = max([len(s) for s in [s1,s2]])
list3 = tuple([s[i] for s in [s1,s2]] for i in range(3))
list4 = tuple([s[i] if len(s) > i else None for s in [s1,s2]] for i in range(4))
print(list1)
print(list2)
print(list3)
print(list4)



