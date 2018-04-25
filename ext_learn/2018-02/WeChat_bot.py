#-*- coding:utf-8 -*-

__author__ = 'wangjf'

from wxpy import *
import json,requests

bot = Bot(console_qr=True,cache_path=True)
my_friend = ensure_one(bot.search("全栈攻城狮小分队"))
tuling = Tuling(api_key="b436f834ce2f4c2489b6732559d0ab1c")

# 调用图灵机器人API ,收发信息
def auto_reply(text):

    url = "http://www.tuling123.com/openapi/api"
    api_key = "b436f834ce2f4c2489b6732559d0ab1c"

    payload = {
        "key":api_key,
        "info":text,
        "userid":123456
    }
    r = requests.post(url,data=json.dumps(payload))
    result = json.loads(r.content)
    print(result)
    return "[reply]" + result["text"]

'''
@bot.register(msg_types=FRIENDS)
def forward_message(mp):u 347890
return auto_reply(mp)   Q1~#!                                                                           
'''

@bot.register(my_friend)
def reply_my_friend(msg):
    tuling.do_reply(msg,at_member=True)

embed()
