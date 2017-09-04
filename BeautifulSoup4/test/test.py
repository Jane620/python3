#-*- coding:utf-8 -*-

__author__ = 'wangjf'

import requests,re
from bs4 import BeautifulSoup


def get_html(url):
    rep = requests.get(url)
    return rep.text

def get_soap(html):
    soap = BeautifulSoup(html,'html.parser')
    return soap

# 需要适应单栏以及双栏
def get_soap_info(content,limit=50):

    soap = get_soap(content)
    tr = soap.find_all('tr', attrs={'class': 'md_tr font14 bgcolor'}, limit=limit)
    tr2 = soap.find_all('tr', attrs={'class': 'md_tr font14 bgcolor-s'}, limit=limit)
    tr3 = []
    minlen = min(len(tr), len(tr2))
    for i in range(minlen):
        tr3.append(tr[i])
        tr3.append(tr2[i])
    dict_info = {}
    for i in tr3:
        td = i.find_all('td')
        # 表明为双排列
        if len(td) < 4:
            key,value = get_depth_two(td)
            if value:
                html = value[1]
                num = get_depth_three(html)
                value[1] = num
            dict_info[key] = value
        else:
            get_depth_two_two(td)
            #dict_info[key] = value

    print(dict_info)


def get_depth_two(content):

    list_info = []
    rank = ''.join(content[0].contents).strip()
    for i in content:
        length = len(i.contents)
        if length > 1:
            href = i.contents[1].get('href')
            text = ''.join(i.contents[1].contents)
            list_info.append(text)
            list_info.append(href)

    return (rank,list_info)

def get_depth_two_two(content):
    # 1,3列为序号，2，4列为内容
    dict_info = {}
    list_info = []
    count = 0
    for content in content:
        count += 1
        #print('content:',content)
        if count % 2 == 0:
            list_info = []
            continue
        else:
            rank = ''.join(content.contents).strip()
            href_tmp = content.find_next('td')
            if href_tmp.find('a'):
                href = href_tmp.find_next('a').get('href')
                text = ''.join(content.find_next('a').contents)
            else:
                href = ''
                text = ''.join(content.find_next('td').contents)
            list_info.append(href)
            list_info.append(text)
        dict_info[rank] = list_info

    # 将结果重新组装成一个新的dict按照1-100的顺序
    print(dict_info)


def get_depth_three(url):
    if not url:
        return ''
    content = get_html(url)
    soap = get_soap(content)

    div = soap.find_all('div', attrs={'class': 'desc'})
    # 部分页面会出现重复
    p = div[0].find_all_next('p')
    list_info = []
    for i in p:
        desc = str(i.contents)
        list_info.append(''.join(desc))

    desc_info = ''.join(list_info)
    # 调整正则，适应更多情况
    target_reg = re.compile(r'职工[\d]+万?|员工.?[\d]+万?')
    match = re.findall(target_reg, desc_info)
    return match[0] if match else '0'

if __name__ == '__main__':
    url = 'http://www.maigoo.com/news/467715.html'
    url2 = 'http://www.maigoo.com/news/467546.html'
    html = rep = requests.get(url).text
    content = get_soap_info(html,limit=50)
