#-*- coding:utf-8 -*-
import requests,re,os
import xlwt,xlrd,pickle
import Step2,API_get
from bs4 import BeautifulSoup

__author__ = 'wangjf'


def get_city(url):

    rep = requests.get(url).text
    soup = BeautifulSoup(rep,'html.parser')
    dl = soup.find_all('dl',attrs={'class':'pinyin_filter_detail layoutfix'})[0]
    dd = dl.find_all('dd')
    dict_city = {}
    base_url = 'http://hotels.ctrip.com'
    for i in range(len(dd)):
        a = [children for children in dd[i].children]
        link = [a[x].get('href') for x in range(len(a))]
        location = [a[x].text for x in range(len(a))]
        for j in range(len(link)):
            id = re.findall(r'[\d]+',link[j])
            dict_city[location[j]] = [''.join(id), base_url + link[j]]

    return dict_city

def write_file(content):

    file_path = '../resource/province.xls'
    workbook = xlwt.Workbook(encoding='ascii')
    worksheet = workbook.add_sheet('省份', cell_overwrite_ok=True)
    row0 = [u'地区',u'省份']
    worksheet.write(0, 0, row0[0])
    worksheet.write(0, 1, row0[1])

    row1 = []
    for key,value in content.items():
        place = key
        province = value
        row1.append([place,province])

    for i in range(len(row1)):
        worksheet.write(i + 1, 0, row1[i][0])
        worksheet.write(i + 1, 1, row1[i][1])
    workbook.save(file_path)


def call_func(province, * city):

    data_file = 'date_list.pkl'

    with open(data_file, 'rb') as fr:
        print('开始读取文件.....')
        data_list = pickle.load(fr)

    count_2 = 0
    k = province
    h = []
    for x in city:
        h.append(x)
    print(h)
    single_list = data_list[k]
    for i in range(len(single_list)):
        for x, y in single_list[i].items():
            count_2 += 1
            if x not in h:
                continue
            print('{0}:{1},开始处理：{2}'.format(k, x, count_2))
            Step2.xc_hotel(k, x, y[0])

    print('数据处理结束')


if __name__ == '__main__':

    data_file = 'date_list.pkl'
    '''
    url = 'http://hotels.ctrip.com/domestic-city-hotel.html'
    #baike_url = 'https://baike.baidu.com/item/'
    city_list = get_city(url)
    #print(city_list)
    provinceList = []
    #count = 0
    provinceList_file = 'provinceList.pkl'
    if not os.path.exists(provinceList_file):
        #写文件
        for key,value in city_list.items():
            provinceList_tmp = {}
            provinces = API_get.api_get_provinceList(key)
            provinceList_tmp[provinces] = {key:value}
            provinceList.append([provinceList_tmp])
            #count += 1
            #if count > 5:
                #break
        #print('原始provinceList:',provinceList)
        # TypeError: write() argument must be str, not list
        with open(provinceList_file,'wb') as fw:
            print('开始写入文件.....')
            pickle.dump(provinceList,fw)

    data_list = {}
    with open(provinceList_file, 'rb') as fr:
        print('开始读取文件.....')
        #provinceList = f.read()
        provinceList2 = pickle.load(fr)
    #print('读取provinceList:',provinceList2)

    for _ in provinceList2:
        for k, v in _[0].items():
            data_list.setdefault(k, []).append(v)

    # 写文件
    data_file = 'date_list.pkl'
    with open(data_file, 'wb') as fw:
        print('开始写入文件date_list.....')
        pickle.dump(data_list, fw)
    '''
    # 读文件
    with open(data_file, 'rb') as fr:
        print('开始读取文件.....')
        data_list = pickle.load(fr)

    #print('处理前数据:',data_list)
    # data_list 格式为[{'1':[{'2':'2-1'},{'3':'3-1'}]}]
    count_2 = 0
    #for k,v in data_list['安徽省'].items():
    k = '浙江省'
    h = ['余姚', '宁海', '象山', '奉化', '宁波', '北仑', '镇海', '舟山', '台州', '温岭', '临海', '瑞安', '乐清', '永嘉', '温州', '天台', '三门', '仙居']
    # 失败集锦 陕西，吉林，海南
    single_list = data_list[k]
    # 对v进行循环处理
    for i in range(len(single_list)):
        for x,y in single_list[i].items():
            count_2 += 1
            if x not in h:
                continue
            print('{0}:{1},开始处理：{2}'.format(k,x,count_2))
            Step2.xc_hotel(k,x,y[0])

    print('数据处理结束')