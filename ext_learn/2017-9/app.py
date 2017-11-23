#-*- coding:utf-8 -*-
from flask import Flask
from redis import Redis,RedisError
import os,socket

redis = Redis(host="redis",db=0,socket_connect_timeout=2,socket_timeout=2)

app = Flask(__name__)

def hello():
    try:
        visits = redis.incr("counter")
    except RedisError:
        visits = "no connnect"

    html = "<h3>Hello {name}!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>" \
           "<b>Visits:</b> {visits}"
    return html.format(name=os.getenv("NAME","world"),hostname=socket.gethostname(),visits=visits)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=801)