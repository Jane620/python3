#-*- coding:utf-8 -*-

__author__ = 'wangjf'

# 将传参进行转换 然后传入对应的func中
# 其中有一点不明了，因为zip后的结果为tuple ，实际调用的func(*args) 应该为 abs((-1,))类似，为何能出结果？
def mymap(func,*seqs):
    res = []
    for args in zip(*seqs):
        res.append(func(*args))
    return res

# 等同上面，采用列表推导式，性能更佳
def mymap2(func,*seqs):
    return [func(*args) for args in zip(*seqs)]

print(list(mymap(abs,[-1,-2,-5,-3,0,1])))
print(list(mymap(pow,[1,2,3],[4,5,6])))

