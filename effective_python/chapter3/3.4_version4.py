#-*- coding:utf-8 -*-

__author__ = 'wangjf'

import collections

Grade = collections.namedtuple('Grade',('score','weight'))

class Subject(object):

    def __init__(self):
        self._grades = []

    def report_grade(self,score,weight):
        self._grades.append(Grade(score,weight))

    def average_grade(self):
        total,total_weight = 0,0
        for grade in self._grades:
            print('grade:',grade)
            total += grade.score * grade.weight
            total_weight += grade.weight
        return total / total_weight

class Student(object):
    def __init__(self):
        self._subjects = {}
    def subject(self,name):
        if name not in self._subjects:
            self._subjects[name] = Subject()
        return self._subjects[name]

    def average(self):
        total,count=0,0
        for subject in self._subjects.values():
            total += subject.average_grade()
            count += 1
        return total / count

class GradeBook(object):
    def __init__(self):
        self._students = {}

    def student(self,name):
        if name not in self._students:
            self._students[name] = Student()
            print('studentname:',self._students[name])
        return self._students[name]

book = GradeBook()
tom = book.student('tom')
math = tom.subject('math')
math.report_grade(80,0.1)
magic = tom.subject('magic')
magic.report_grade(60,0.3)
print(tom.average())