#-*- coding:utf-8 -*-
import pymysql
__author__ = 'wangjf'


db = pymysql.connect('localhost','root','root','scrapy',charset='utf8')
cursor = db.cursor()
sql = ''
with open('db_oper/insert_area.sql','r') as f:
    for line in f.readlines():
        sql = line.encode('utf-8')
        cursor.execute(sql)
        db.commit()
cursor.close()
db.close()