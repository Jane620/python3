#-*- coding:utf-8 -*-
import re
__author__ = 'wangjf'

str = '<p style="text-align:left;">　　1　一汽-大众汽车有限公司　　　　　　　　　　　　　徐平</p>'

list_a = ['94', '中国石油大庆润滑油二厂大庆132126']

match = ''.join(re.findall(re.compile(r'[^\\u4e00-\\u9fa5]+'),list_a[1]))

print(match)