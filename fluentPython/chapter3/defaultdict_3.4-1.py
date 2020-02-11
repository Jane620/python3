#-*- coding:utf-8 -*-
from collections import defaultdict

dd = defaultdict(list)
#运行的原理
'''
1. 调用list()生成一个新列表
2. 把这个新列表作为值，new-key作为他的键，放入dd中
3. 返回这个列表的引用
'''
dd[7] = 9

for key,value in dd.items():
    print(key,value)
