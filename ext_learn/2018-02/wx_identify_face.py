#-*- coding:utf-8 -*-

__author__ = 'wangjf'

import cv2,os
from wxpy import *

bot = Bot(cache_path=True)

def face(pic):
    print('---正在处理---')
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
    count = 0
    img = cv2.imread(pic)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        count += 1
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),4)
        font = cv2.FONT_HERSHEY_SIMPLEX

        roi_gray = gray[y:y+h/2,x:x+w]
        roi_color = img[y:y+h/2,x:x+w]

    cv2.imwrite("face_detected_1.jpg",img)
    print(count)
    return count

@bot.register(Friend,PICTURE)
def face_msg(msg):
    img_name = msg.file_name
    friend = msg.chat
    print(msg.chat)
    print('---接受图片---')
    msg.get_file('' + img_name)
    count = face(img_name)
    img_save = "face_detected_1.jpg"
    if count == 0:
        msg.reply('未检测到人脸')
    else:
        msg.reply_image(img_save)
        msg.reply("检测到{}张人脸".format(count))
    os.remove(img_name)
    os.remove(img_save)

embed()