#-*- coding:utf-8 -*-
import numpy
__author__ = 'wangjf'

# 贝叶斯算法
class Bayes:

    def __init__(self):
        self.length = -1
        self.labelcount = dict()
        self.vectorcount = dict()

    def fit(self,dataSet:list,labels:list):
        if(len(dataSet) != len(labels)):
            raise ValueError("你输入的测试数组和类别数组长度不一致")
        # 测试数据特征值的长度
        self.length = len(dataSet[0])
        #所有类别的数量
        labelnum = len(labels)
        #不重复类别的数量
        norlables = set(labels)
        for item in norlables:
            thislabel = item
            # 求当前类型占总类型的比值
            self.labelcount[thislabel] = labels.count(thislabel) / labelnum
        for vector, label in zip(dataSet,labels):
            if labels not in self.vectorcount:
                self.vectorcount[label] = []
            self.vectorcount[label].append(vector)
        print("训练结束")
        return self

    def btest(self,TestData, labelsSet):
        if self.length == -1:
            raise ValueError("还未开始训练，请先训练")
        #计算TestData分别各个类别的概率
        lbDict = dict()
        for thislb in labelsSet:
            p = 1
            alllabel = self.labelcount[thislb]
            allvector = self.vectorcount[thislb]
            vnum = len(allvector)
            # 等同zip函数，将多个列表进行行列转换
            allvector = numpy.array(allvector).T
            for index in range(len(TestData)):
                vector = list(allvector[index])
                p *= vector.count(TestData[index])/vnum
                print(p)
            lbDict[thislb] = p * alllabel
        thislabel = sorted(lbDict,key=lambda x:lbDict[x],reverse=True)[0]
        return thislabel



