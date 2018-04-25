#-*- coding:utf-8 -*-

__author__ = 'wangjf'

class Student:
    def __init__(self,name):
        self._name = name

    def __str__(self):
        return "Student is {}".format(self._name)

    __repr__ = __str__


class Fib:

    def __init__(self):
        self.a , self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a , self.b = self.b , self.a + self.b
        if self.a > 10:
            raise StopIteration('a is too big')
        return self.a

    def __getitem__(self, n):
        if isinstance(n,int):
            a, b = 0, 1
            for x in range(n):
                a,b = b,a+b
            return a

        if isinstance(n,slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a,b = 0,1
            L = []
            for x in range(stop):
                if x >= start: #因为slice是左闭右开
                    L.append(a)
                a,b =b,a+b
            return L


if __name__ == '__main__':
    s = Student("jane")
    f = Fib()
    for i in f:
        print(i)
    print(f[1:3])