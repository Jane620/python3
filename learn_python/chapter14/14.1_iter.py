#-*- coding:utf-8 -*-

# iter() 可以将序列转换为迭代器, 其中字典的迭代器为key
L = [1,2,3]
D = {'a':1, 'b':2, 'c':3}
iter_L = iter(L)
iter_D = iter(D)

while True:
    try:
        #这里可能存在问题,如果两个迭代器元素个数不同，则可能先结束的迭代器会抛出异常
        iter_enum_L = next(iter_L)
        iter_enum_D = next(iter_D)
    except StopIteration:
        break
    print(iter_enum_D + ':', iter_enum_L)


