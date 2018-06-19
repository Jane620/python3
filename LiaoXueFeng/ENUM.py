# -*- coding: utf-8 -*-
# @Time    : 2018/4/25 下午4:57
# @Author  : Jane
# @Site    : 
# @File    : ENUM.py
# @Software: PyCharm

from enum import Enum,unique

class Mon:
    Month = Enum('Month',('Oct','Jan','Feb','Mar','Apr'))

# it can tell the explain the duplicate value
@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

if __name__ == '__main__':
    # member.value 获取值 ，默认从1开始
    for name, member in Mon.Month._member_map_.items():
        print(name, '=>', member, ',', member.value)

    day1 = Weekday.Wed.value
    print(day1)
    print(Weekday['Tue'])
    print(Weekday(1))

    for name ,value in Weekday.__members__.items():
        print(name ,'=>',value,',',value.value)