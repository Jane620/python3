#-*- coding:utf-8 -*-

__author__ = 'wangjf'

import tensorflow as tf
import numpy as np

input1 = tf.placeholder("float")
input2 = tf.placeholder("float")

output = tf.multiply(input1,input2)

with tf.Session() as sess:
    print(sess.run(output,feed_dict={input1:[7.],input2:[2.]}))