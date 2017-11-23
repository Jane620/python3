#-*- coding:utf-8 -*-

__author__ = 'wangjf'

import requests,math,re,csv,random,os,time
import xlwt,xlrd
from xlutils.copy import copy
from bs4 import BeautifulSoup

def change_proxy():

    reader = csv.reader(open('ips-enable2.csv'))
    IPpool = []
    for row in reader:
        IPpool.append(row)
    return random.choice(IPpool)

def change_agent():

    uas = [
        "Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
        "MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
        "JUC (Linux; U; 2.3.7; zh-cn; MB200; 320*480) UCWEB7.9.3.103/139/999",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0a1) Gecko/20110623 Firefox/7.0a1 Fennec/7.0a1",
        "Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10",
        "Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13",
        "Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_0 like Mac OS X; en-us) AppleWebKit/420.1 (KHTML, like Gecko) Version/3.0 Mobile/1A542a Safari/419.3",
        "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_0 like Mac OS X; en-us) AppleWebKit/532.9 (KHTML, like Gecko) Version/4.0.5 Mobile/8A293 Safari/6531.22.7",
        "Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10",
        "Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+",
        "Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.0; U; en-US) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/233.70 Safari/534.6 TouchPad/1.0",
        "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
        "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
        "Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER) ",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 UBrowser/4.0.3214.0 Safari/537.36",
        "Mozilla/5.0 (Linux; U; Android 2.2.1; zh-cn; HTC_Wildfire_A3333 Build/FRG83D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
        "Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)",
        "Mozilla/4.0 (compatible; MSIE 6.0; ) Opera/UCWEB7.0.2.37/28/999",
        "Openwave/ UCWEB7.0.2.37/28/999",
        "NOKIA5700/ UCWEB7.0.2.37/28/999",
        "UCWEB7.0.2.37/28/999",
        "Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.0; U; en-US) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/233.70 Safari/534.6 TouchPad/1.0",
        "Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13",
        "Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10",
        "Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    ]
    return  random.choice(uas)

def get_single_info(city_id, pages=1):

    proxies_tmp = change_proxy()
    agent = change_agent()

    proxies = {proxies_tmp[0]:proxies_tmp[1]}

    url = 'http://hotels.ctrip.com/Domestic/Tool/AjaxHotelList.aspx'
    # 'Cookie':'Session=SmartLinkCode=U877868&SmartLinkKeyWord=&SmartLinkQuary=&SmartLinkHost=&SmartLinkLanguage=zh; ASP.NET_SessionId=klnrdjd3qekf33emrf4zbkbb; _abtest_userid=8e94d37f-ba6a-43a0-80f3-ee5dfb3aa245; appFloatCnt=1; manualclose=1; adscityen=Hangzhou; HotelCityID=1split%E5%8C%97%E4%BA%ACsplitBeijingsplit2017-09-29split2017-09-30split0; page_time=1505519900324%2C1505519912333%2C1505519917322%2C1505519942331%2C1505519968347%2C1505608370754%2C1505608371042%2C1505608374517%2C1505609168924%2C1505627494759%2C1505627496809%2C1505990910744%2C1505991057293%2C1506674923019%2C1506675274786%2C1506675275847%2C1506675286785%2C1506675293856%2C1506675399852%2C1506675825109%2C1506675833233%2C1506675834148%2C1506675835043%2C1506675843229%2C1506734789280; _RF1=60.12.11.28; _RSG=LkqpV4lI.KArfIL2iRJ2rB; _RGUID=a53e4af1-1fcf-4b95-bd42-4dbb02552a75; __zpspc=9.2.1506734791.1506734791.1%234%7C%7C%7C%7C%7C%23; _jzqco=%7C%7C%7C%7C1506674924204%7C1.1020905377.1506674923836.1506675845726.1506734791198.1506675845726.1506734791198.undefined.0.0.9.9; _ga=GA1.2.1727429083.1506674924; _gid=GA1.2.2051130117.1506674924; MKT_Pagesource=PC; _bfa=1.1503063039794.4226bb.1.1506674921494.1506734788787.13.89; _bfs=1.17; _bfi=p1%3D102002%26p2%3D102002%26v1%3D89%26v2%3D88',
    headers = {'Cache-Control':'max-age=0',
           'Referer':'http://hotels.ctrip.com/hotel/macau59',
           'Connection':'keep-alive',
           'Origin':'http://hotels.ctrip.com',
           'Accept-Encoding':'gzip, deflate',
           'Accept-Language':'zh-CN,zh;q=0.8',
           'User-Agent':agent,
           'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
           'Accept':'*/*',
           'Host':'hotels.ctrip.com'}
    '''
    type 区分品牌类型 0-经济连锁，1-高端连锁
    group 区分其他品牌 1-首旅如家，359-都市118
    '''
    data = {
    'cityId': str(city_id),
    'star':'',
    'page': str(pages),
    '__VIEWSTATEGENERATOR':'DB1FBB6D',
    'cityName':'%25E6%25BE%25B3%25E9%2597%25A',
    'contyped':'0',
    'attachDistance':'0',
    'a':'0',
    'markType':'0',
    'htlFrom':'hotellist',
    'isHuaZhu':'False',
    'ubt_price_key':'htl_search_result_promotion',
    'isfromlist':'T',
    'HideIsNoneLogin':'T',
    'OrderBy':'99',
    'IsCanReserve':'F',
    'prepay':'F',
    'promotion':'F',
    'priceRange':'-2',
    'useFG':'F',
    'isusergiftcard':'F',
    'requestTravelMoney':'F',
    'hasPKGHotel':'F',
    'hotelType':'T',
    'htlPageView':'0',
    'IsOnlyAirHotel':'F',
    'operationtype':'NEWHOTELORDER'
}
    time.sleep(random.choice([1,2,3,4,5]))
    try:
        re = requests.post(url,headers=headers,data=data,proxies=proxies,timeout=5).text
        return re
    except requests.exceptions.ProxyError as e:
        pass
    #print('原始re:',re)

def anaysis_info(content):
    '''
    :param content:
    :return:
    '''
    hotel_detail = {}
    soup = BeautifulSoup(content,'html.parser')
    a = soup('li',attrs={'class':'hotel_item_name'})
    for j in range(len(a)):
        hotel_name = a[j].a['title']
        span = a[j]('span',attrs={'class':re.compile('hotel_(di|ha|sta)')})
        hotel_stars = '0'
        hotel_style = '低于3星'
        #if span:
        try:
            hotel_stars = re.search(r'[\d](.5){0,1}',span[0]['title']).group()
            hotel_style = ''.join(re.findall(r'(.*)（',span[0]['title']))
        except IndexError:
            continue
        hotel_detail[hotel_name] = [hotel_stars,hotel_style]
    return hotel_detail

def create_file(province,file_path):

    workbook = xlwt.Workbook(encoding='ascii')
    worksheet = workbook.add_sheet(province, cell_overwrite_ok=True)
    workbook.save(file_path)

def wirte_to_xls(province,city,content):

    file_path = 'xls/hotel_%s.xls' % province

    if not os.path.exists(file_path):
        create_file(province,file_path)

    rb = xlrd.open_workbook(file_path)
    wb = copy(rb)
    ws = wb.get_sheet(0)

    #workbook = xlwt.Workbook(encoding='ascii')
    worksheet = wb.add_sheet(city,cell_overwrite_ok=True)
    row0 = [u'省份',u'市' , u'酒店名', u'星级', u'类型']
    worksheet.write(0, 0, row0[0])
    worksheet.write(0, 1, row0[1])
    worksheet.write(0, 2, row0[2])
    worksheet.write(0, 3, row0[3])
    worksheet.write(0, 4, row0[4])

    row1 = []
    for key,value in content.items():
        province_name = province
        city_name = city
        hotel_name = key
        hotel_star = value[0]
        hotel_type = value[1]
        row1.append([province_name,city_name,hotel_name,hotel_star,hotel_type])

    for i in range(len(row1)):
        worksheet.write(i + 1, 0, row1[i][0])
        worksheet.write(i + 1, 1, row1[i][1])
        worksheet.write(i + 1, 2, row1[i][2])
        worksheet.write(i + 1, 3, row1[i][3])
        worksheet.write(i + 1, 4, row1[i][4])

    wb.save(file_path)


def xc_hotel(province_name,city_name,city_code):

    total_query = eval(get_single_info(city_code, pages=1))
    total_count = total_query.get('hotelAmount')
    print('酒店总数：',total_count)
    page_count = math.ceil(total_count / 25)
    '''
    hotelList 酒店详细信息
    HotelMaiDianData 酒店详细起步卖价
    '''
    global null
    null = ''
    pages = int(page_count) + 1
    if pages > 100:
        pages = 100
    dict_info = {}
    for i in range(1, pages):
        reset = get_single_info(city_code, pages=i)
        if isinstance(reset,str):
            result = eval(reset)
            content = result.get('hotelList')
            # print('未处理前：',content)
            if not content:
                continue
        single_dict = anaysis_info(content)
        dict_info.update(single_dict)
        print('目前处理进度：{0}，数量为:{1}'.format(i,len(dict_info)))
    #print(dict_info)
    wirte_to_xls(province_name,city_name, dict_info)


#if __name__ == '__main__':
#    province_name = '浙江省'
#    city_name = '苍南'
#    city_id = '7666'
#    xc_hotel(province_name,city_name,city_id)