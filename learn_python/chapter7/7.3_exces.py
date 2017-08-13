
#-*- coding:utf-8 -*-

# find(self,sub)，返回最小匹配的那个index
# Return the lowest index in S where substring sub is found,
str1 = 'listA'
print(str.find(str1,'is'))


# 取中间的值

str5 = 's,pa,m'
str_tmp = str5.split(',')
print(str_tmp[len(str_tmp)//2])
