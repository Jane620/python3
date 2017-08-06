#-*- coding:utf-8 -*-

# zip函数返回的是一个可迭代对象，因此需要通过list调用显性显示
# 返回的对象为tuple
# Return a zip object whose .__next__() method returns a tuple

L1 = [1,2,3,4]
L2 = [5,6,7,8]

L3 = zip(L1,L2)
print(list(L3))

#直接用L3存在问题，目测为3.4.4的bug，3.6的版本上无此问题
for x,y in zip(L1,L2):
    print(x,'+',y,'=',x+y)