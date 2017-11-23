#-*- coding:utf-8 -*-
import scrapy,pickle,os
__author__ = 'wangjf'


class HotelScrapy(scrapy.Spider):
    name = 'hotels'
    base_path = '/Users/wangjianfeng/Code/github/python3/scrapy_demo/scrapy_demo/'

    def read_data(self):
        data_list = None
        with open(self.base_path + 'spiders/date_list.pkl','rb') as fr:
            data_list = pickle.load(fr)
        addrs = []
        for _, v in data_list.items():
            for x in v:
                values = [y[1] for y in x.values()]
                addrs.append(''.join(values))
        return addrs

    def start_requests(self):
        urls = self.read_data()
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)

    def parse(self, response):
        page = response.url.split('/')[-1]
        filename = 'hotel_%s' %page
        path = self.base_path +'storage/'
        with open(path + filename,'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' %filename)