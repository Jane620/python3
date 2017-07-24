#-*- coding:utf-8 -*-

'''读取一个html页面，
1. 打印html结构
2. 匹配一个特定正则式的字符串
3. 统计出现的次数

试例页面
http://blog.sina.com.cn/s/blog_5016ee390102e5qv.html
匹配内容
两位数字且仅为2位数字

过程遇到问题
1. 部分网页进行压缩，可以用urlopen(url).info() 查看content-encoding，需要借助zlib进行解压
'''

import urllib.request
import re

re_str = re.compile(r'\d{2,2}')
count = 0
test_url = 'http://blog.sina.com.cn/s/blog_5016ee390102e5qv.html'
url_open = urllib.request.urlopen(test_url)
url_text = url_open.read().decode('utf-8')

for match in re_str.finditer(url_text):
    count += 1
print(count)