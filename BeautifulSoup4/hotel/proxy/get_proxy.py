import requests
from bs4 import BeautifulSoup
import csv

def IPpool():

    reader=csv.reader(open('ip-list.csv'))

    csvfile = open('ips-enable2.csv', 'w')
    writer = csv.writer(csvfile)

    count = 0
    for row in reader:
        rows = row[0].split('://')
        proxies = {rows[0]:rows[1]}
        count += 1
        print('进度:', count)
        try:
            html=requests.get('http://www.baidu.com',proxies=proxies,timeout=0.5)
            writer.writerow(row)
        except Exception as e:
            continue

def IPspider(numpage):

    csvfile = open('ip-list.csv','w')
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
                temp.append(protols+'://'+ips)
                #temp.append(ips)
                writer.writerow(temp)
            except IndexError:
                continue

# 假设爬取前十页所有的IP和端口
if __name__ == '__main__':
    #IPspider(100)
    IPpool()