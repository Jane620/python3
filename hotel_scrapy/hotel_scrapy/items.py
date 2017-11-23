# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HotelScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    cityName = scrapy.Field()
    cityUrl = scrapy.Field()
    pageNum = scrapy.Field()
    provinceId = scrapy.Field()
    cityId = scrapy.Field()

    hotel_name = scrapy.Field()
    hotel_addr = scrapy.Field()
    hotel_star = scrapy.Field()
    hotel_type = scrapy.Field()
    hotels = scrapy.Field()


