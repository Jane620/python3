#!/bin/env python
# encoding:utf8
#
# 抓取58的城市
# author songmw
#
from pinyin import pinyin
import requests,re


def getHtml():

    urlItem = requests.get('http://www.58.com/chuzu/changecity/')
    html = urlItem.text
    html = html.encode('utf8')
    return html

if __name__ == '__main__':

    html = getHtml()

    # print(html)
    # 获取所有的省份
    prov_list = re.findall(b'<dt.*?>(.*)</dt>',html)

    # 获取所有的市
    rc = re.compile(b'<dd.*?>(.*?)</dd>')
    city_list = rc.findall(html)

    # data
    data = []
    data.append({"en": "beijing", "cn": "北京"})
    data.append({"en": "tianjin", "cn": "天津"})
    data.append({"en": "shanghai", "cn": "上海"})
    data.append({"en": "chongqing", "cn": "重庆"})

    for k in range(len(prov_list)):
        prov_dict = {}
        prov_dict['en'] = pinyin.get(prov_list[k])
        prov_dict['cn'] = prov_list[k]

        if k == 0 or k == len(prov_list) - 1:
            continue

        # 获取该省下的所有市
        rc = re.compile('\<a.*?\>(.*?)\<\/a\>')
        item_city = rc.findall(city_list[k])

        prov_dict['city'] = item_city
        data.append(prov_dict)

    for v in data:
        print('*' * 10)
        print("该省%s（%s）" % (v['cn'], v['en']))

        if v.has_key('city'):

            print("旗下有的城市:")
            for city_name in v['city']:
                print(city_name)