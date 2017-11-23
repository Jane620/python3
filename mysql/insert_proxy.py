#-*- coding:utf-8 -*-
import requests,time
from bs4 import BeautifulSoup
import pymysql

__author__ = 'wangjf'


def IPpool(ips,protols):

    error = 1
    proxies = {protols:''.join(ips)}

    headers = {'Cache-Control': 'max-age=0',
                       'Referer': 'http://hotels.ctrip.com/hotel/macau59',
                       'Connection': 'keep-alive',
                       'Origin': 'http://hotels.ctrip.com',
                       'Accept-Encoding': 'gzip, deflate',
                       'Accept-Language': 'zh-CN,zh;q=0.8',
                       'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
                       'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                       'Accept': '*/*'}
    data = {
                'cityId': '010',
                'star': '',
                'page': '1',
                '__VIEWSTATEGENERATOR': 'DB1FBB6D',
                'cityName': '%25E6%25BE%25B3%25E9%2597%25A',
                'contyped': '0',
                'attachDistance': '0',
                'a': '0',
                'markType': '0',
                'htlFrom': 'hotellist',
                'isHuaZhu': 'False',
                'ubt_price_key': 'htl_search_result_promotion',
                'isfromlist': 'T',
                'HideIsNoneLogin': 'T',
                'OrderBy': '99',
                'IsCanReserve': 'F',
                'prepay': 'F',
                'promotion': 'F',
                'priceRange': '-2',
                'useFG': 'F',
                'isusergiftcard': 'F',
                'requestTravelMoney': 'F',
                'hasPKGHotel': 'F',
                'hotelType': 'T',
                'htlPageView': '0',
                'IsOnlyAirHotel': 'F',
                'operationtype': 'NEWHOTELORDER'
            }
    try:
        html=requests.get('http://hotels.ctrip.com/Domestic/Tool/AjaxHotelList.aspx',headers=headers,data=data,proxies=proxies,timeout=1)
    except Exception:
        error = 0
    return error


def IPspider(numpage):

    url = 'http://www.xicidaili.com/nn/'
    for num in range(1, numpage + 1):
        ipurl = url + str(num)
        header = {'User-Agent':'IP',}
        print('Now downloading the ' + str(num * 100) + ' ips')
        content = requests.get(ipurl,headers=header).text
        bs = BeautifulSoup(content, 'html.parser')
        res = bs.find_all('tr')
        temp = []
        for item in res:
            try:
                tds = item.find_all('td')
                protols = str.lower(tds[5].text)
                ip =  tds[1].text
                port = tds[2].text
                ips = protols + '//:' + ip + ':' + port
                is_valid = IPpool(ips,protols)
                temp.append([ip,port,protols,is_valid])
            except IndexError:
                continue
        write_to_mysql(temp)
    print('插入数据结束')

def write_to_mysql(data):

    conn = mysql_con()
    cur = conn.cursor()
    now = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    for x in data:
        cur.execute('insert into proxy(ip,port,type,is_valid,test_date) values (%s,%s,%s,%s,%s)',[x[0],x[1],x[2],x[3],now])
    conn.commit()
    cur.close()
    conn.close()



def mysql_con():

    return pymysql.connect('localhost', 'root', 'root', 'scrapy')


if __name__ == '__main__':
    IPspider(100)