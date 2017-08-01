#-*- coding:utf-8 -*-


# 2种方式创建a:0,b:0的字典
dict_t2 = dict.fromkeys([x for x in 'ab'],0)
dict_t2_2 = {x:0 for x in 'ab'}

# 在原处修改对象的方法 append,sorted,extend,pop list[x] = x
