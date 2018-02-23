#-*- coding:utf-8 -*-
import pymysql
import csv
__author__ = 'wangjf'


mysql_config = {
    'host': '10.213.3.232',
    'port': 3306,
    'user': 'test_user',
    'password': 'test_user@123456',
    'db': 'vem',
    'charset': 'utf8',
    'cursorclass': pymysql.cursors.DictCursor,

}
config = {
        'host': '10.212.1.10',
        'port': 3306,
        'user': 'membership',
        'password': 'mem2017test',
        'db': 'membership',
        'charset': 'utf8mb4',
        'cursorclass': pymysql.cursors.DictCursor,
}

connection = pymysql.connect(**config)

condition = 'NFHZ9%'

def write_to_xls(content):
    with open('ipcid.csv','w') as csvfile:
        fieldnames = ['ID','MACHINE_ID']
        writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
        for i in content:
            writer.writerow({'ID':i['ID'],'MACHINE_ID':i['MACHINE_ID']})

try:
    with connection.cursor() as cursor:
        # 执行sql语句，进行查询
        #sql = "select ID,MACHINE_ID from vem_machine_status where MACHINE_ID like 'NFHZ9%';"
        sql = "SELECT * from ms_user_wechat;"
        cursor.execute(sql)
        # 获取查询结果
        result = cursor.fetchall()
        list_1 = []
        for i in result:
            list_1.append(i)
        print(list_1)
        print(len(list_1))
        #write_to_xls(list_1)
    # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
    #connection.commit()
finally:
    connection.close();