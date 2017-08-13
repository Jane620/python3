#-*- coding:utf-8 -*-


# or 仅当一个为真返回，and必须为全部为真返回
tuple1 = 2 or 3 , 3 or 2
print(tuple1)

tuple2 = 2 and 3 , 3 and 2
print(tuple2)

tuple3 = 0 and 0 ,2 or 0
print(tuple3)

# 三元运算符  if 满足为 =后面部分，否则为else
value = 't' if 0 else 'f'
print(value)