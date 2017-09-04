#-*- coding:utf-8 -*-

__author__ = 'wangjf'

'''
根据页面爬取每个公司的员工人数
'''

url_sample ='http://www.maigoo.com/news/467451.html'

import requests

url_list = []
part1 = 'http://www.fortunechina.com/china500/'
part2 = '/2016'
for count in range(1,501):
    context_url = part1 + str(count) + part2
    url_list.append(context_url)

