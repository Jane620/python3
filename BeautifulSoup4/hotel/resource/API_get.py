#-*- coding:utf-8 -*-
import requests,time,re

__author__ = 'wangjf'

def api_get_provinceList(name):

    api_url = 'http://api.shenjian.io/?appid=ed92def577917b6916b034e5da702c57'
    param = {'city':name}
    time.sleep(1)
    req = requests.get(api_url,params=param)
    rep = req.json().get('data')
    if rep:
        out = rep['province']
    else:
        out = 'none'
    return out


def baike_get_provinceList(name,url):

    url = url + name
    rep = requests.get(url)
    html = rep.content.decode('utf-8')
    # 匹配方式 省,自治区，直辖市
    reg = re.compile(u'([\u4e00-\u9fa5]{2}省)|(黑龙江省)|(北京市|上海市|重庆市|天津市)|(广西壮族自治区|内蒙古自治区|西藏自治区|新疆维吾尔自治区|宁夏回族自治区)|(澳门特别行政区|香港特别行政区)')
    provinceList = re.search(reg,html)
    if provinceList:
        provinceList = provinceList.group()
    else:
        provinceList = ''
    #print(provinceList)
    return provinceList