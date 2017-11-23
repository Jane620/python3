# -*- coding: utf-8 -*-
import json
from os.path import dirname,join
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class HotelScrapyPipeline(object):

    def __init__(self):
        self.filename = open(join(dirname(__file__),'hotel_detail.json'),'wb')

    def process_item(self, item, spider):
        jsontext = json.dumps(dict(item),ensure_ascii=False) + ',\n'
        self.filename.write(jsontext.encode('utf-8'))
        return item

    def close_spider(self,spider):
        self.filename.close()
