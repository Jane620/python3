# 计算ascii码，并相加

def asc_sum(str):
    '''
    计算str的ascii码
    :param str:
    :return:
    '''
    sum = 0
    list_n = []
    #func_add = list_n.append
    for x in list(str):
        sum += ord(x)
        #func_add(ord(x))
    print(list(map(ord,str)))
    return sum

asc_sum('abc')