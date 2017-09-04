#-*- coding:utf-8 -*-
import requests,re,xlwt
from bs4 import BeautifulSoup

__author__ = 'wangjf'

def get_html(url,flag=1):
    try:
        rep = requests.get(url)
        if flag:
            return rep.text
        else:
            return rep.content
    except Exception as e:
        return ''

def get_soup(html):
    soup = BeautifulSoup(html,'html.parser')
    return soup

def get_limit(soup):
    tr = soup.find_all('tr', attrs={'class': re.compile('md_ttl md_tr font16 bgcolor-s')})
    flag = re.findall(re.compile(r'名称'), tr[0].text.strip())
    limit = 100
    if len(flag) > 1:
        limit = 50

    return limit

# 获取第二层的信息
def get_soup_info(soup,limit=50):

    tr = soup.find_all('tr', attrs={'class': re.compile('md_tr font14 bgcolor')}, limit=limit)
    dict_info = {}
    # tds为单个tr
    #print('TR:',tr)
    for tds in tr:
        # td的list，包含单行的所有信息
        td = tds.find_all('td')
        #print('TD:',td)
        # 判断单行 or 单行四列
        if len(td) < 4 :
            key,value = get_depth_two(td)
            dict_info[key] = value
        else:
            flag = re.findall(re.compile(r'公司|集团'),td[3].text)
            if not flag:
                key, value = get_depth_two(td)
                dict_info[key] = value
            else:
                dict_tmp = get_depth_two2(td)
                dict_info.update(dict_tmp)

    # 重新组装一个员工数量到字典内
    dict_info2 = {}
    for key,value in dict_info.items():
        comp_name = value[0]
        member_url = value[1] if value[1].strip().startswith('http') else ''
        member = get_depth_three(member_url,comp_name)
        value.insert(1,member)
        dict_info2[key] = value

    return dict_info2

# 仅对低于三列的情况
def get_depth_two(content):

    list_info = []
    rank = content[0].text.strip()
    if content[1].find('a'):
        href = content[1].find('a').get('href')
        text = content[1].text.strip()
    else:
        href = '-'
        text = content[1].text.strip()
    list_info.append(text)
    list_info.append(href)
    return (rank,list_info)

# 满足单行四列或多行四列的情况
def get_depth_two2(content):
    '''
    1. 多行处理：1，3为序号，2，4为链接+名字
    :param content:
    :return:
    '''
    dict_info = {}
    count = 0
    for tds in content:
        list_info = []
        # 单号取链接+名字，双号取序号
        if count % 2 == 0:
            rank = tds.text.strip()
        else:
            if tds.find('a'):
                href = tds.find('a').get('href')
                text = tds.text.strip()
            else:
                href = '-'
                text = tds.text.strip()
            list_info.append(text)
            list_info.append(href)
        count += 1
        dict_info[rank] = list_info
    # 将结果重新组装成一个新的dict
    return dict_info

# 获取第三层具体员工信息
def get_depth_three(url,name):

    if not url:
        return 0

    content = get_html(url)
    soap = get_soup(content)

    div = soap.find_all('div', attrs={'class': 'desc'})
    if not div:
        return 0
    # 部分页面会出现重复
    p = div[0].find_all_next('p')
    list_info = []
    for i in p:
        desc = str(i.contents)
        list_info.append(''.join(desc))
    desc_info = ''.join(list_info)
    # 调整正则，适应更多情况
    target_reg = re.compile(r'职工[\d]+万?|员工.?[\d]+.{2}')
    match = re.findall(target_reg, desc_info)
    print('match:{0},{1}'.format(name,match))
    if match:
        return match[0]
    else:
        return get_baike(name)
    #return match[0] if match else '0'

# 来自百度百科的添加内容
def get_baike(name):
    root_url = 'https://baike.baidu.com/item/%s' %name
    html = get_html(root_url,flag=0)
    soup = get_soup(html.decode('utf-8'))
    #dl = soup.find_all('dl', attrs={'class': re.compile(r'basicInfo-block basicInfo')})
    str = soup.find('body').text
    #for i in range(len(dl)):
    #    str += dl[i].text
    staff = re.findall(re.compile(r'[\d]+.?[\d]+人'), str)
    print('staff:',staff)
    return ''.join(staff[0] if staff else '0')

# 将结果写入文件中
def write_file(dict_info,name):
    file_path = 'resource/CompanyInfo_%s.xls' % name
    workbook = xlwt.Workbook(encoding='ascii')
    worksheet = workbook.add_sheet(name,cell_overwrite_ok=True)
    row0 = [u'排名', u'公司名称', u'员工数', u'公司链接']
    worksheet.write(0, 0, row0[0])
    worksheet.write(0, 1, row0[1])
    worksheet.write(0, 2, row0[2])
    worksheet.write(0, 3, row0[3])
    row1 = []
    for key,value in dict_info.items():
        rank = int(key.strip())
        comp_name = value[0]
        staff_count = value[1]
        comp_link = value[2]
        row1.append([rank,comp_name,staff_count,comp_link])

    for i in range(len(row1)):
        worksheet.write(i + 1, 0, row1[i][0])
        worksheet.write(i + 1, 1, row1[i][1])
        worksheet.write(i + 1, 2, row1[i][2])
        worksheet.write(i + 1, 3, row1[i][3])

    workbook.save(file_path)


if __name__ == '__main__':
    import time
    start = time.time()

    ANHUI = 'http://www.maigoo.com/news/467660.html'
    CHENGDU = 'http://www.maigoo.com/news/467913.html'
    CHONGQING = 'http://www.maigoo.com/news/468490.html'
    GUANGDONG = 'http://www.maigoo.com/news/460855.html'
    GUANGXI = 'http://www.maigoo.com/news/468542.html'
    GUIZHOU = 'http://www.maigoo.com/news/489624.html'
    HAINAN = 'http://www.maigoo.com/news/469114.html'
    HENAN = 'http://www.maigoo.com/news/473023.html'
    HUBEI = 'http://www.maigoo.com/news/467810.html'
    HUNAN = 'http://www.maigoo.com/news/469023.html'
    JIANGXI = 'http://www.maigoo.com/news/472939.html'
    JIANGSU = 'http://www.maigoo.com/news/488041.html'
    LIAONING = 'http://www.maigoo.com/news/474009.html'
    #SANYA = 'http://www.maigoo.com/news/486873.html'
    SHANDONG = 'http://www.maigoo.com/news/467715.html'
    SHANGHAI = 'http://www.maigoo.com/news/467546.html'
    SHENZHEN = 'http://www.maigoo.com/news/470667.html'
    TIANJIN = 'http://www.maigoo.com/news/467601.html'
    ZHEJIANG = 'http://www.maigoo.com/news/467451.html'

    html = requests.get(HENAN).text

    soup = get_soup(html)
    limit = get_limit(soup)
    content = get_soup_info(soup,limit)
    write_file(content,'HENAN')

    elasped = time.time()-start
    print('time:',elasped)
