#-*- coding:utf-8 -*-
import pymysql
__author__ = 'wangjf'

config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': 'root',
    'db': 'scrapy',
    'charset': 'utf8',
    'cursorclass': pymysql.cursors.DictCursor,
}

# Connect to the database
connection = pymysql.connect(**config)

condition = '浙江'

# 执行sql语句
try:
    with connection.cursor() as cursor:
        # 执行sql语句，进行查询
        sql = "select city_url from city_to_province;"
        cursor.execute(sql)
        # 获取查询结果
        result = cursor.fetchall()
        list_1 = []
        for i in result:
            list_1.append(i['city_url'])
        print(list_1)
    # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
    #connection.commit()

finally:
    connection.close();



