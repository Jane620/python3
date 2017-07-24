#!/usr/bin/env python3
# -*- coding: utf-8 -*-

a = 2**32
print(a)

print("一个好日子")

#中文到数字
str1 = ord('好')
print(str1)
#数字到中文
str2 = chr(22909)
print(str2)

#string类型
str3 = 'abc'
#bytes类型
str4 = b'abc'
print(type(str3))
print(type(str4))

str5 = b'\xe4\xb8\xad\xe6\x96\x87'.decode('UTF-8')
print(str5)

print('%2d-%02d' %(3,1))