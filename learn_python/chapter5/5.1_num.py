#-*- coding:utf-8 -*-

#二进制 ， 八进制 ，十六进制
print(0b1010101)
print(0o123)
print(0x32)

int_10 = 10
#hex() , oct() , bin()
print(hex(int_10))
print(oct(int_10))
print(bin(int_10))

# slice最后一位为步长
list_test = [x for x in range(10)]
list_test2 = list_test[1:7:2]
list_test3 = list_test[slice(1, 7, 2)]
print(list_test2)
print(list_test3)

# 多项比较
x = 1
y = 2
z = 3
print(x < y < z )

print(0.1*3-0.3)