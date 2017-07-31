#-*- coding:utf-8 -*-

B = '1101'
I = 0
while B != '':
    # 计算方式为当前值*2+下一位的值
    I = I*2 + (ord(B[0])-ord('0'))
    B = B[1:]

print(I)
#等价于 int 或者  <<
I2 = int('1101',2)
print(I2)

B2 = list(reversed('1101'))
I3 = 0
while B2 != 

print(B2)

