#-*- coding:utf-8 -*-
import re

#match(pattern,string) 从首字母开始匹配，匹配成功返回match对象，失败返回None，如果要完全匹配，需要以$结尾
match = re.match('Hello[ \t]*(.*)World','Hello   python World')
match_str = match.group()
print(match_str,match)

match2 = re.match('/(.*)/(.*)/(.*)','/usr/home/test_Re')
match_group = match2.groups()
match_group1 = match2.group(0)
print(match_group,match_group1)