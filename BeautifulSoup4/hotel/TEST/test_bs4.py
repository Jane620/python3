#-*- coding:utf-8 -*-

__author__ = 'wangjf'

import requests,math,re,xlwt
from bs4 import BeautifulSoup

def get_single_info(city_id,stars='',pages=1):

    url = 'http://hotels.ctrip.com/Domestic/Tool/AjaxHotelList.aspx'
    headers = {'Cookie':'Session=SmartLinkCode=U877868&SmartLinkKeyWord=&SmartLinkQuary=&SmartLinkHost=&SmartLinkLanguage=zh; ASP.NET_SessionId=klnrdjd3qekf33emrf4zbkbb; _abtest_userid=8e94d37f-ba6a-43a0-80f3-ee5dfb3aa245; appFloatCnt=1; manualclose=1; adscityen=Hangzhou; HotelCityID=1split%E5%8C%97%E4%BA%ACsplitBeijingsplit2017-09-29split2017-09-30split0; page_time=1505519900324%2C1505519912333%2C1505519917322%2C1505519942331%2C1505519968347%2C1505608370754%2C1505608371042%2C1505608374517%2C1505609168924%2C1505627494759%2C1505627496809%2C1505990910744%2C1505991057293%2C1506674923019%2C1506675274786%2C1506675275847%2C1506675286785%2C1506675293856%2C1506675399852%2C1506675825109%2C1506675833233%2C1506675834148%2C1506675835043%2C1506675843229%2C1506734789280; _RF1=60.12.11.28; _RSG=LkqpV4lI.KArfIL2iRJ2rB; _RGUID=a53e4af1-1fcf-4b95-bd42-4dbb02552a75; __zpspc=9.2.1506734791.1506734791.1%234%7C%7C%7C%7C%7C%23; _jzqco=%7C%7C%7C%7C1506674924204%7C1.1020905377.1506674923836.1506675845726.1506734791198.1506675845726.1506734791198.undefined.0.0.9.9; _ga=GA1.2.1727429083.1506674924; _gid=GA1.2.2051130117.1506674924; MKT_Pagesource=PC; _bfa=1.1503063039794.4226bb.1.1506674921494.1506734788787.13.89; _bfs=1.17; _bfi=p1%3D102002%26p2%3D102002%26v1%3D89%26v2%3D88',
           'Cache-Control':'max-age=0',
           'Referer':'http://hotels.ctrip.com/hotel/macau59',
           'Connection':'keep-alive',
           'Origin':'http://hotels.ctrip.com',
           'Accept-Encoding':'gzip, deflate',
           'Accept-Language':'zh-CN,zh;q=0.8',
           'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
           'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
           'Accept':'*/*'}
    '''
    type 区分品牌类型 0-经济连锁，1-高端连锁
    group 区分其他品牌 1-首旅如家，359-都市118
    '''
    data = {
    'cityId': str(city_id),
    'star':str(stars),
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
    #time.sleep(3) #无效果，最终在4000+的时候依旧无法使用，因此可以判定为按照一个IP一次请求的数量来限制
    re = requests.post(url,headers=headers,data=data).text
    #print('原始re:',re)
    return re

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
        hotel_style = '无星级'
        if span:
            hotel_stars = re.search(r'[\d](.5){0,1}',span[0]['title']).group()
            hotel_style = ''.join(re.findall(r'(.*)（',span[0]['title']))
        hotel_detail[hotel_name] = [hotel_stars,hotel_style]
    return hotel_detail


def wirte_to_xls(name,content):

    file_path = '../resource/hotel_%s.xls' % name
    workbook = xlwt.Workbook(encoding='ascii')
    worksheet = workbook.add_sheet(name,cell_overwrite_ok=True)
    row0 = [u'省份', u'酒店名', u'星级', u'类型']
    worksheet.write(0, 0, row0[0])
    worksheet.write(0, 1, row0[1])
    worksheet.write(0, 2, row0[2])
    worksheet.write(0, 3, row0[3])

    row1 = []
    for key,value in content.items():
        province = '广州'
        hotel_name = key
        hotel_star = value[0]
        hotel_type = value[1]
        row1.append([province,hotel_name,hotel_star,hotel_type])

    for i in range(len(row1)):
        worksheet.write(i + 1, 0, row1[i][0])
        worksheet.write(i + 1, 1, row1[i][1])
        worksheet.write(i + 1, 2, row1[i][2])
        worksheet.write(i + 1, 3, row1[i][3])

    workbook.save(file_path)

if __name__ == '__main__':
    city_code = '750'
    city_name = '广汉'
    total_query = eval(get_single_info(city_code,pages=1))
    total_count = total_query.get('hotelAmount')
    #print('酒店总数：',total_count)
    page_count = math.ceil(total_count / 25)
    '''
    hotelList 酒店详细信息
    HotelMaiDianData 酒店详细起步卖价
    '''
    dict_info = {}
    for i in range(1,int(page_count)+1):
        result = eval(get_single_info(city_code,pages=i))
        content = result.get('hotelList')
        #print('未处理前：',content)
        single_dict = anaysis_info(content)
        dict_info.update(single_dict)
        #print('目前处理进度：{0}，数量为:{1}'.format(i,len(dict_info)))
    print(dict_info)
    wirte_to_xls(city_name,dict_info)