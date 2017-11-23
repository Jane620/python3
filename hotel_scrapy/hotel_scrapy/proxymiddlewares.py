#-*- coding:utf-8 -*-
import random,csv
__author__ = 'wangjf'

class ProxyMiddleware(object):

    def process_request(self,request,spider):

        pro_adr = self.get_proxy()
        request.meta['proxy'] = pro_adr
        return request

    def process_response(self,request,response,spider):

        if response.state != 200:
            proxy = self.get_proxy()
            request.meta['proxy'] = proxy
            return request

        return response

    def get_proxy(self):
        base_path = '/Users/wangjianfeng/Code/github/python3/hotel_scrapy'
        reader = csv.reader(open(base_path + '/hotel_scrapy/ips-enable.csv'))
        IPpool = []
        for row in reader:
            IPpool.append(row)
        proxy = random.choice(IPpool)
        return ''.join(proxy)



