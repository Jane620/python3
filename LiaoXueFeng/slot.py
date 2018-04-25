#-*- coding:utf-8 -*-

__author__ = 'wangjf'

class Students:

    __slots__ = ('name','age')


class Student_2(Students):

    __slots__ = ('score')


class Student_3:

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('score is not a num')
        if value < 0 or value > 100:
            raise ValueError('score must bewteen 0 ~ 100')
        self._score = value


class Screen(object):

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self,value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        return self._width * self._height


if __name__ == '__main__':
    s = Students()
    s.name ='a'
    s.age = '20'
    s2 = Student_2()
    s2.score = '5'

    s3 = Student_3()
    s3.score = 20
    print(s3.score)

    s = Screen()
    s.width = 1024
    s.height = 768
    print(s.resolution)
    assert s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution
