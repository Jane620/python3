#-*- coding:utf-8 -*-
import requests
__author__ = 'wangjf'



def get_hotel(cityid,page):

    url = 'http://hotels.ctrip.com/Domestic/Tool/AjaxHotelList.aspx'
    proxy = {'https':'144.123.46.106:8118'}
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Origin': 'http://hotels.ctrip.com',
        'Cache-Control': 'max-age=0',

        'Connection':'keep-alive',
        'Host': 'hotels.ctrip.com',
        'Referer': 'http://hotels.ctrip.com/hotel/shanghai2',
        'User-Agent':'Mozilla/4.0 (compatible; MSIE 6.0; ) Opera/UCWEB7.0.2.37/28/999'
        }
    data = {
        'cityId': str(cityid),
    'star':'',
    'page': str(page),
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
    r = requests.post(url,headers=headers,data=data,proxies=proxy)
    print(r.text)



if __name__ == '__main__':
    get_hotel(1,1)