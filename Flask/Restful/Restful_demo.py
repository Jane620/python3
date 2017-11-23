#-*- coding:utf-8 -*-
from flask import Flask,request
from flask_restful import Api,Resource,reqparse,abort
__author__ = 'wangjf'

app = Flask(__name__)
api = Api(app)

USER_LIST = {
    '1':{'name':'John'},
    '2':{'name':'Tom'}
}

parser = reqparse.RequestParser()
parser.add_argument('name',type=str)

def abort_if_not_exist(user_id):
    if user_id not in USER_LIST:
        abort(404,message="User {} doesn't not exist".format(user_id))

class UserList(Resource):

    def get(self,user_id):
        abort_if_not_exist(user_id)
        return USER_LIST[user_id]


    def put(self,user_id):
        args = parser.parse_args(strict=True)
        USER_LIST[user_id] = {'name':args['name']}
        return USER_LIST[user_id]

    def delete(self,user_id):
        del USER_LIST[user_id]
        return 'success'

api.add_resource(UserList,'/users/<user_id>')

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)






