#-*- coding:utf-8 -*-

__author__ = 'wangjf'

# all(iterable)
# Return True if all elements of the iterable are true (or if the iterable is empty)

def all1(iterable):
    for element in iterable:
        if not element:
            return False
    return True

list1 = []
print(all(list1))


# all(iterable)
# Return True if any elements of the iterable are true (return False if the iterable is empty)

def any1(iterable):
    for element in iterable:
        if element:
            return True
    return False

list2 = ['',None,1]
print(any1(list2))

# callable(object) 返回对象是否为可调用对象，需要实现__call__才行

class A(object):
    def __init__(self):
        super.__call__()
    def __call__(self, *args, **kwargs):
        pass

a = A()
flag = callable(A)
flag2 = callable(a)
print('A:{0},\na:{1}'.format(flag,flag2))

# divmod(a,b) 等同a//b
quo,rem = divmod(5,2)
print(quo,rem)

# enumerate(iterable,start=0)
def enumerate1(iterable,start=0):
    n = start
    for element in iterable:
        # 每次循环生成
        yield n, element
        n += 1

list3 = ['spring','summer','fall','winter']
enum1 = enumerate1(list3,1)
print(list(enum1))

# filter(function,iterable)
list4 = [1,2,3,4,5,6]
print(list(filter(lambda x: x > 2, list4)))

# property(fget=None,fset=None,fdel=None,doc=None)
#
class B:
    def __init__(self):
        self._x = None

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self,value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x

b = B()
print(b.x)
b.x = '2'
print(b.x)
