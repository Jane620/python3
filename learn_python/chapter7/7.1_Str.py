#-*- coding:utf-8 -*-

B = '1101'
O = '7377'
I = 0
IO = 0
while O != '':
    # 计算方式为当前值*2+下一位的值
    #I = I*2 + (ord(B[0])-ord('0'))
    IO = IO * 8 + (ord(O[0])-ord('0'))
    print(ord(O[0])-ord('0'))
    #B = B[1:]
    O = O[1:]

print('二进制:',I)
print('八进制:',IO)
#等价于 int 或者  <<
I2 = int('1101',2)
print(I2)
print(int('7377',8))



