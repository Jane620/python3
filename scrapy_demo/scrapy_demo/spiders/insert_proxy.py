#-*- coding:utf-8 -*-
import scrapy
__author__ = 'wangjf'


class ProxySpider(scrapy.Spider):

    name = 'proxys'
    base_url = 'http://www.xicidaili.com/nn/'
    max_page = 101

    def start_requests(self):
        urls = []
        for x in range(1,self.max_page):
            url = self.base_url + str(x)
            urls.append(url)
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)

    def parse(self, response):
        pass

    #测试代理有效性
    def test_proxy(self):
        pass

