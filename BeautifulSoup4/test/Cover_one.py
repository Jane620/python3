#-*- coding:utf-8 -*-

__author__ = 'wangjf'

import requests,re
from bs4 import BeautifulSoup

root_url = 'http://www.maigoo.com/search/?v=&f=&q=完整榜单'

def has_class_but_no_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')

rep = requests.get(root_url)

soup = BeautifulSoup(rep.text,'html.parser')

print(soup)
# 获取二层页面id号  暂时未解决，部分范围为百度接口

dt = soup.find_all(href=re.compile(r'news'),attrs={'class':'blue b'})
for i in dt:
    pass
    #print(i,end='\n')
