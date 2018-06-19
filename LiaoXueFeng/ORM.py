# -*- coding: utf-8 -*-
# @Time    : 2018/4/26 下午6:34
# @Author  : Jane
# @Site    : 
# @File    : ORM.py
# @Software: PyCharm


class Field(object):
    def __init__(self, name, column_type):
        self.name  = name
        self.column_type = column_type

    def __str__(self):
        return '{0}:{1}'.format(self.__class__.name,self.__class__.column_type)

#String type class
class StringField(Field):

    def __init__(self,name):
        super(StringField,self).__init__(name,'varchar2(100)')

#Integer type class
class IntegerField(Field):

    def __init__(self,name):
        super(IntegerField,self).__init__(name,'Number(10)')

class ModelMetaClass(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls,name,bases,attrs)
        print('Found model ',name)
        mappings = dict()
        for k,v in mappings.items():
            if isinstance(v,Field):
                print('Found mapping ',(k,v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings
        attrs['__tables__'] = name
        return type.__new__(cls,name,bases,attrs)

class Model(dict,metaclass=ModelMetaClass):

    def __init__(self,**kwargs):
        super(Model,self).__init__(**kwargs)

    def __getattr__(self, item):
        try:
            return self[item]
        except KeyError:
            raise AttributeError('Model has no attr ',item)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k ,v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self,k,None))
        sql = 'insert into {0} ({1}) values ({2})'.format(self.__tables__,''.join(fields),''.join(args))
        print('Sql:',sql)
        print('Args:',str(args))


class User(Model):
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    passwd = StringField('passwd')

if __name__ == '__main__':
    u = User(id=1,name='jane',email='11@11.com',passwd='1234')
    u.save()
