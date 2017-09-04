#-*- coding:utf-8 -*-

__author__ = 'wangjf'

class BySubjectGradeBook(object):
    def __init__(self):
        self._grades = {}
    def add_student(self,name):
        self._grades[name] = {}
        print('grade:',self._grades)

    def report_grade(self,name,subject,score):
        by_subject = self._grades[name]
        grade_list = by_subject.setdefault(subject,[])
        grade_list.append(score)
        print('grade_list:',self._grades)

    def average_grade(self,name):
        by_subject = self._grades[name]
        total,count=0,0
        for grade in by_subject.values():
            total += sum(grade)
            count += len(grade)
        return total/count

book = BySubjectGradeBook()
book.add_student('tom')
book.report_grade('tom','math',60)
book.report_grade('tom','class',80)
book.report_grade('tom','magic',40)
num = book.average_grade('tom')
print(num)
