import functools

def inc(x):
    return x +10

counter = [1,2,3,4,5]
counter2 = [[1,4,7],[2,5,8],[3,6,9]]

list2 = list(map(inc,counter))
list3 = list(map(lambda x:x+9,counter))
list4 = list(functools.reduce(lambda x,y:x+y,counter2))


print(list2)
print(list3)
print(list4)

# filter 基于函数过滤元素 过滤负数
list5 = list(filter(lambda x : x >= 0,range(-5,5)))
print(list5)

#reduce

def myreduce(function,sequence):
    first = sequence[0]
    for next in sequence[1:]:
        first = function(sequence,next)
    return first

sequence1 = [1,2,3,4]
print(myreduce(sum,sequence1))

x = sum(sequence1,2)
print(x)
