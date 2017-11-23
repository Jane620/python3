#-*- coding:utf-8 -*-
import scrapy,random
from hotel_scrapy.items import HotelScrapyItem
__author__ = 'wangjf'

class XCSpider(scrapy.Spider):

    name = 'xchotel'
    start_urls = ['http://hotels.ctrip.com/domestic/domestic-city-hotel.html']

    def parse(self, response):
        for dd in response.xpath('//dl[@class="pinyin_filter_detail layoutfix"]/dd'):
            for a in dd.css('a'):
                item = HotelScrapyItem()
                item['cityId'] = ''.join(filter(str.isdigit, a.xpath('@href').extract_first()))
                item['cityName'] = a.css('::text').extract_first()
                src = 'http://hotels.ctrip.com' + a.xpath('@href').extract_first()
                yield scrapy.Request(src, meta={'item': item}, callback=self.parse_pagenum)

    def parse_pagenum(self,response):
        item = response.meta['item']
        #item['city_code'] = response.meta['city_code']
        item['cityUrl'] = response.url
        item['provinceId'] = response.xpath('//meta[@name="location"]').xpath('@content').extract()[0].split(';')[0].split('province=')[-1]
        page_num  = response.xpath('//div[@class="c_page_list layoutfix"]/a[@rel="nofollow"]').xpath('@data-value').extract_first()
        if page_num:
            item['pageNum'] = page_num
        else:
            item['pageNum'] = '1'

        base_url = response.url + '/p0'

        yield scrapy.Request(url=base_url, meta={'item':item}, callback=self.parse_detail)


    def parse_detail(self,response):

        item = response.meta['item']
        page_num = int(item['pageNum'])
        #from scrapy.shell import inspect_response
        #inspect_response(response,self)
        for hotel_detail in  response.css('li.hotel_item_name'):
            hotels = {}
            hotels['hotel_name'] = hotel_detail.css('h2.hotel_name a').xpath('@title').extract_first()
            hotels['hotel_addr'] = hotel_detail.css('p.hotel_item_htladdress::text').extract()[-1].strip('】')
            hotels['hotel_star'] = ''.join(filter(str.isdigit,hotel_detail.css('h2.hotel_name').xpath('following-sibling::span').xpath('@class').extract()[-1])).strip('0') or '0'
            item['hotels'] = hotels
            yield item

        if page_num > 1:
            for i in range(2,page_num):
                next_page = '/'.join(response.url.split('/')[:-1]) + '/p' + str(i)
                yield scrapy.Request(url=next_page, meta={'item':item}, callback=self.parse_detail)







