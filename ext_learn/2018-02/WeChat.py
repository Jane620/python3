#-*- coding:utf-8 -*-

__author__ = 'wangjf'


from wxpy import *

#首次登录 需要扫码QR码
bot = Bot(cache_path=True)

friends_stat = bot.friends().stats()

friends_loc = []

print(bot.__dict__)

# 统计性别
for province, count in friends_stat["sex"].items():
    if province != "":
        friends_loc.append([province,count])

friends_loc.sort(key=lambda x : x[1],reverse=True)

for item in friends_loc[:10]:
    print(item[0],item[1])
'''
@bot.register()
def print_message(msg):
    print(msg.text)
    return '我是一个机器人，只会重复你的话'
'''
#embed()