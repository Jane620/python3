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

# 替换replace ，但是注意不是真正的修改，而是生成一个新的对象
str1 = 'spamxxxxspam'
print(str1.replace('am','amp'))
where = str1.find('am')
print(str1[:where] + 'good' + str1[where:])

# str转换成list 通过'.join重新将list转换为str  ,str则无此用途
str2 = str1
list2 = list(str2)
print(list2)
str3 = ''.join(list2)
list2.append(1)
str4 = str(list2)
print('str3:',str3)
print('str4:',str4)

#split根据配置分割
str5 = "this is my way."
list5 = str5.split(' ')
print(list5)


# %06d表示用0补齐前面的位数
i = 50000
print('%04d' %i)