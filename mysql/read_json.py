#-*- coding:utf-8 -*-
import json,xlwt,xlrd,pymysql,os
from xlutils.copy import copy
__author__ = 'wangjf'


def get_db():
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
    return connection

def get_cityName(cityid):

    conn = get_db()
    try:
        with conn.cursor() as cursor:
            # 执行sql语句，进行查询
            sql = "select city_name from city_to_province where city_code = %s;"
            cursor.execute(sql, (cityid))
            # 获取查询结果
            result = cursor.fetchone()
            return result
            # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
            # connection.commit()
    finally:
        conn.close();

def create_file(province,file_path):

    workbook = xlwt.Workbook(encoding='ascii')
    worksheet = workbook.add_sheet(province, cell_overwrite_ok=True)
    row0 = [u'省份', u'市', u'酒店名', u'地址', u'星级',u'类型']
    worksheet.write(0, 0, row0[0])
    worksheet.write(0, 1, row0[1])
    worksheet.write(0, 2, row0[2])
    worksheet.write(0, 3, row0[3])
    worksheet.write(0, 4, row0[4])
    worksheet.write(0, 5, row0[5])

    workbook.save(file_path)

def wirte_to_xls(province,city,content):

    file_path = 'xls/hotel_%s.xls' % province

    if not os.path.exists(file_path):
        create_file(province,file_path)

    rb = xlrd.open_workbook(file_path)
    wb = copy(rb)
    ws = wb.get_sheet(0)
    # 获取现在已有的行数
    rows = rb.sheets()[0].nrows
    #print('base rows:',rows)

    #workbook = xlwt.Workbook(encoding='ascii')
    #worksheet = wb.add_sheet(city,cell_overwrite_ok=True)
    worksheet = wb.get_sheet(0)
    '''row0 = [u'省份',u'市' , u'酒店名', u'星级', u'类型']
    '''
    row1 = []
    province_name = province
    for j in content:
        city_name = get_cityName(city)['city_name']
        hotel_name = j['hotel_name']
        hotel_star = j['hotel_addr']
        hotel_addr = j['hotel_star']
        hotel_type = j['hotel_type']
        row1.append([province_name,city_name,hotel_name,hotel_star,hotel_addr,hotel_type])

    for i in range(len(row1)):
        worksheet.write(rows + i, 0, row1[i][0])
        worksheet.write(rows + i, 1, row1[i][1])
        worksheet.write(rows + i, 2, row1[i][2])
        worksheet.write(rows + i, 3, row1[i][3])
        worksheet.write(rows + i, 4, row1[i][4])
        worksheet.write(rows + i, 5, row1[i][5])
    wb.save(file_path)



if __name__ == '__main__':

    # 如何将多个json数据合并到一起？
    with open('HOTEL2.json',encoding='utf-8') as fr:
        for line in fr.readlines():
            single = json.loads(line)
            #print(single)
            wirte_to_xls('吉林省',single['cityId'],single['hotels'])




