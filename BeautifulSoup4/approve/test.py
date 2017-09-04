#-*- coding:utf-8 -*-
import re,requests
from bs4 import BeautifulSoup
__author__ = 'wangjf'

url = 'https://baike.baidu.com/search/none'
param = {'word':'金昌金川集团有限公司','pn':'0','rn':'10','enc':'utf8'}

rep = requests.get(url,params=param).content.decode('utf-8')

soup = BeautifulSoup(rep,'html.parser')

p = soup.find_all('dl',attrs={'class':'search-list'})

dd = p[0].find_next('dd')

#a = dd[0].find_next('a')

print(dd.a.get('href'))