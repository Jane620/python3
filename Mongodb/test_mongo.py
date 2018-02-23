#-*- coding:utf-8 -*-
from pymongo import MongoClient
import pprint
from math import sin, asin, cos,degrees
__author__ = 'wangjf'

def conn():
    conn = MongoClient('mongodb://nos:nosproject@10.5.0.40:27017/nos')
    db = conn.nos
    return db

def Calc_Round(lat,lng,distance):

    latlng_list = []
    # 地球平均半径，6371km
    EARTH_RADIUS = 6371

    #
    dlng = 2 * asin(sin(distance / (2 * EARTH_RADIUS)) / cos(lat))
    dlng = degrees(dlng)  # 弧度转换成角度

    dlat = distance / EARTH_RADIUS
    dlng = degrees(dlat)  # 弧度转换成角度

    left_top = lng - dlng
    right_top = lat + dlat
    left_bottom = lat - dlat
    right_bottom = lng + dlng

    latlng_list = [left_top,right_top,left_bottom,right_bottom]

    return latlng_list

def query(left_top,left_bottom,right_top,right_bottom):
    '''
        按照传入4个边角，left_top,left_bottom,right_top,right_bottom
        SQL范围
            bottom.lat < lat < top.lat
            left.lng < lng < right.lng
    '''
    db = conn()
    pipeline = [
        {'$match': {"address.Latitude": {'$gt': left_bottom, '$lt': right_top}}},
        {'$match': {"address.Longitude": {'$gt': left_top, '$lt': right_bottom}}}
    ]
    my_set = db.zfjinfos.aggregate(pipeline)

    result_list = []
    count = 0
    for i in list(my_set):
        result = {}
        result['id'] = count
        result['name'] = i['address']['POI']
        result['latitude'] = i['address']['Latitude']
        result['longitude'] = i['address']['Longitude']
        result['address'] = i['address']['Desc']
        count += 1
        result_list.append(result)
        #pprint.pprint(i)
    pprint.pprint(result_list)

if __name__ == '__main__':
    #conn()
    lat = 45.7276012  #
    lng = 122.6681158
    distance = 500 # 千米
    condition = Calc_Round(lat,lng,distance)
    query(condition[0],condition[2],condition[1],condition[3])