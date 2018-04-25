#-*- coding:utf-8 -*-

__author__ = 'wangjf'

from  tensorflow.examples.tutorials.mnist import input_data
# 引入训练数据,one_hot=True则表明每个张量中只有一个为1,其他元素为0
mnist = input_data.read_data_sets("MNIST_data/",one_hot=True)

print(mnist)

import tensorflow as tf
# tensorflow 依赖高效的c++后端进行计算，因此与后端链接需要session
sess = tf.InteractiveSession()

# 为输入图像和目标输出类别创建节点,实为类似函数参数，运行时必须传入
# why 784?  28*28 = 784, 在mnist数据集中，数字以28*28的灰度像素图呈现
# y为输出,2维张量，每一行为10维的one_hot相量
x = tf.placeholder("float",shape=[None,784])
y_ = tf.placeholder("float",shape=[None,10])

#权重W和偏置b

W = tf.Variable(tf.zeros([784,10]))
b = tf.Variable(tf.zeros([10]))