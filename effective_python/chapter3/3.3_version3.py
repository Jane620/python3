#-*- coding:utf-8 -*-

__author__ = 'wangjf'

class WeightedGradeBook(object):
    def __init__(self):
        self._grades = {}
    def add_student(self,name):
        self._grades[name] = {}
        print('grade:',self._grades)

    def report_grade(self,name,subject,score,weight):
        by_subject = self._grades[name]
        grade_list = by_subject.setdefault(subject,[])
        grade_list.append((score,weight))
        print('grade_list:',self._grades)

    def average_grade(self,name):
        by_subject = self._grades[name]
        total,count=0,0
        for grade in by_subject.values():
            # 已经开始过于复杂了，因此需要考虑增加辅助类
            pass

book = WeightedGradeBook()
book.add_student('tom')
book.report_grade('tom','math',60,0.2)
book.report_grade('tom','magic',40,0.4)