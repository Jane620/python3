#-*- coding:utf-8 -*-
import copy
import sys

y = list([1,2,3])

print(sys.getrefcount(y))
a = y
#浅拷贝，新建引用，指向原对象，但是本身对象也不相同
x = copy.copy(y)

#深拷贝,生成新的对象
z = copy.deepcopy(y)

print(x == z)
print(a is y)
print(x is y)
print(x is z)
print(z is y)