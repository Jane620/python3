#-*- coding:utf-8 -*-

__author__ = 'wangjf'

'''
创建一个字典将所有用户的名字和分数保存下来
'''

class SimpleGradeBook(object):

    def __init__(self):
        self._grades={}

    def add_student(self,name):
        self._grades[name] = []

    def report_grade(self,name,score):
        self._grades[name].append(score)

    def average_grade(self,name):
        grades = self._grades[name]
        return sum(grades)/len(grades)

book = SimpleGradeBook()
book.add_student('tom')
book.report_grade('tom',90)
book.report_grade('tom',60)
book.add_student('kate')
book.report_grade('kate',60)
avage = book.average_grade('tom')
print(avage)