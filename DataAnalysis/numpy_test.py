import numpy


def numpy_calc(n):
    data1 = numpy.arange(n) ** 2
    data2 = numpy.arange(n) ** 3
    data3 = data1 + data2
    return data3

def nomal_calc(n):
    data1 = range(n)
    data2 = range(n)
    data3 = [];
    for i in range(n):

        data3 = data1[i] + data2[i]