import requests
from bs4 import BeautifulSoup
import csv

def IPpool():

    reader=csv.reader(open('ip-list2.csv'))
    csvfile = open('ips-enable2.csv', 'w')
    writer = csv.writer(csvfile)

    count = 0
    for row in reader:
        rows = row[0].split('://')
        proxies = {rows[0]:rows[1]}
        count += 1
        ip = [str(x) for x in rows[1].split()]
        print('进度:', count)
        try:
            # proxies
            test_url = 'https://m.dianping.com/tuan/ajax/dealShop?dealGroupId=29511665&lat=&lng=&userCityId=3'
            html=requests.get(test_url,proxies=proxies,timeout=0.05)
            writer.writerow([rows[0],row[0]])
        except Exception as e:
            continue

def IPpool2():

    #reader=csv.reader(open('ip-list2.csv'))
    reader = csv.reader(open('ips-enable2.csv'))
    csvfile = open('ips-enable3.csv', 'w')
    writer = csv.writer(csvfile)

    count = 0
    for _,row in reader:
        rows = row.split('://')
        proxies = {rows[0]:rows[1]}
        count += 1
        ip = [str(x) for x in rows[1].split()]
        print('进度:', count)
        content = "{'ipaddr':'"+ row +  "'}"
        writer.writerow([content])

def IPspider(numpage):

    csvfile = open('ip-list2.csv','w')
    writer = csv.writer(csvfile)
    url = 'http://www.xicidaili.com/nn/'
    for num in range(1, numpage + 1):
        ipurl = url + str(num)
        header = {'User-Agent':'IP',}
        print('Now downloading the ' + str(num * 100) + ' ips')
        content = requests.get(ipurl,headers=header).text
        bs = BeautifulSoup(content, 'html.parser')
        res = bs.find_all('tr')
        for item in res:
            try:
                temp = []
                tds = item.find_all('td')
                protols = str.lower(tds[5].text)
                ips = tds[1].text + ':' + tds[2].text
                temp.append(protols + '://' +ips)
                #temp.append(ips)
                writer.writerow(temp)
            except IndexError:
                continue

# 假设爬取前十页所有的IP和端口
if __name__ == '__main__':
    #IPspider(30)
    #IPpool()
    IPpool2()