#-*- coding:utf-8 -*-
import xlwt,xlrd
import os
from xlutils.copy import copy

def create_file(province,file_path):

    workbook = xlwt.Workbook(encoding='ascii')
    worksheet = workbook.add_sheet(province, cell_overwrite_ok=True)
    workbook.save(file_path)


def wirte_to_xls(province,city,content):

    file_path = 'hotel_%s.xls' % province
    if not os.path.exists(file_path):
        create_file(province,file_path)

    rb = xlrd.open_workbook(file_path)
    wb = copy(rb)
    ws = wb.get_sheet(0)

    #workbook = xlwt.Workbook(encoding='ascii')
    worksheet = wb.add_sheet(city,cell_overwrite_ok=True)
    row0 = [u'省份',u'市' , u'酒店名', u'星级', u'类型']
    worksheet.write(0, 0, row0[0])
    worksheet.write(0, 1, row0[1])
    worksheet.write(0, 2, row0[2])
    worksheet.write(0, 3, row0[3])
    worksheet.write(0, 4, row0[4])

    row1 = []
    for key,value in content.items():
        province_name = province
        city_name = city
        hotel_name = key
        hotel_star = value[0]
        hotel_type = value[1]
        row1.append([province_name,city_name,hotel_name,hotel_star,hotel_type])

    for i in range(len(row1)):
        worksheet.write(i + 1, 0, row1[i][0])
        worksheet.write(i + 1, 1, row1[i][1])
        worksheet.write(i + 1, 2, row1[i][2])
        worksheet.write(i + 1, 3, row1[i][3])
        worksheet.write(i + 1, 4, row1[i][4])

    wb.save(file_path)

if __name__ == '__main__':

    province_name = '北京市'
    city_name = '北京1'
    city_id = '1'
    dict_info = {'欧杰西假日酒店（西安钟楼店）': ['3', '舒适型'], '西安钟楼丽晶庭院酒店': ['3', '舒适型'], '西安东方大酒店': ['4', '国家旅游局评定为四星级'], '西安大雁塔和颐酒店': ['4', '高档型'], '陕西世纪金源大饭店': ['5.5', '国家旅游局评定为五星级'], '西安金莎国际酒店': ['3.5', '高档型'], '美豪丽致酒店（西安鼓楼店）': ['4.5', '高档型'], '西安中心戴斯酒店（钟楼店）': ['4', '高档型'], '西安天域凯莱大饭店': ['5', '国家旅游局评定为五星级'], '西安富凯禧玥酒店': ['4.5', '豪华型'], '左艺术时尚精品酒店（西安钟楼店）': ['3', '舒适型'], '美豪酒店（西安钟楼东大街店）': ['4.5', '高档型'], '璞隐酒店（西安大雁塔店）': ['4.5', '高档型'], '西安王子星月（精品）酒店': ['4', '高档型'], '西安曲江银座酒店': ['4', '高档型'], '西安古都文化大酒店（原古都新世界大酒店）': ['4', '高档型'], '美豪丽致酒店（西安高新店）': ['4.5', '高档型'], '西安天朗时代大酒店': ['4.5', '豪华型'], '美丽豪酒店（西安曲江大雁塔会展中心店）': ['4.5', '高档型'], '景玉商旅酒店（西安北大街地铁口店）': ['3.5', '国家旅游局评定为三星级'], '秦唐一号酒店（西安钟楼店）': ['4', '高档型'], '西安途家斯维登度假公寓（钟楼火车站）': ['3', '舒适型'], '西安名都国际酒店': ['3.5', '高档型'], '西安骊苑大酒店': ['4', '国家旅游局评定为四星级'], '西安君诚国际酒店': ['4', '高档型']}

    wirte_to_xls(province_name,city_name,dict_info)