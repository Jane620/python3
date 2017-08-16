#-*- coding:utf-8 -*-

__author__ = 'wangjf'

'''
python2.6将长度不同的用None补齐
list1 = list(map(None,[1,2,3],[4,5,6,7]))
print(list1)
'''

# 将多余部分直接舍弃
def myzip(*args):
    seqs = [list(S) for S in args]
    res = []
    while all(seqs):
        # 遍历seqs对象，返回pop(0) 的对象，多个列组合成一个元祖
        tuple1 = tuple(s.pop(0) for s in seqs)
        res.append(tuple1)
    return res

s1,s2,s3 = 'abc','xyz1','jqka2'
print(myzip(s1,s2))

''' python3的处理
seqs = [list(s) for s in [s1,s2]]
print(seqs)
tuple1 = tuple(s.pop(0) for s in seqs)
print(seqs)
print(tuple1)
'''

def myzipPad(*args,pad=None):
    seqs = [list(s) for s in args]
    res = []
    while any(seqs):
        # 同上，不同部分为判断s的值如果为空则将pad填充
        res.append(tuple((S.pop(0) if S else pad) for S in seqs))
    return res

print(myzipPad(s1,s2))
print(myzipPad(s1,s2,pad='o'))

# 改造，通过生成器返回
# 最大区别为不用append，因为一个为输出整体结果，一个为输出本次的计算，因此无需append
def myzip2(*args):
    seqs = [list(s) for s in args]
    while all(seqs):
        yield tuple(s.pop(0) for s in seqs)

def myzipPad2(*args,pad=None):
    seqs = [list(s) for s in args]
    while any(seqs):
        yield tuple((s.pop(0) if s else pad) for s in seqs)

print('---')
print(list(myzip2(s1,s2)))
print(list(myzipPad2(s1,s2)))

# 改造2 ，不再通过pop方法进行删除元素，而是通过最短最长参数来进行判断
#
def myzip3(*args):
    # 返回args参数中较短一个的长度
    minlen = min(len(s) for s in args)
    return (tuple(s[i] for s in args) for i in range(minlen))


def myzipPad3(*args,pad=None):
    maxlen = max(len(s) for s in args)
    index = range(maxlen)
    return tuple([(s[i] if len(s) > i else pad) for s in args] for i in index)

print('----3-----')
print(myzip3(s1,s2))
print(myzipPad3(s1,s2))

print('---test---')
len1 = min([len(s) for s in [s1,s2]])
print(len1)

# 改造3
def myzip4(*args):
    iters = map(iter,args)
    while iters:
        res =  [next(s) for s in iters]
        yield tuple(res)

print('---4---')
print(list(myzip4(s1,s2)))
