#-*- coding:utf-8 -*-
from flask import Flask,url_for,request,render_template,make_response,redirect,abort
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/cookies')
def index_cookies():
    username = request.cookies.get('username')

@app.route('/store_cookies')
def index_store():
    resp = make_response(render_template('response.html'))
    resp.set_cookies('username','the username')
    return resp

@app.route('/')
def index_page():
    return redirect(url_for('abort'))

@app.route('/abort')
def abort():
    abort(401)
    print('it can not be print')

@app.route('/hello')
@app.route('/hello/<name>')
def hello_world(name=None):
    return render_template('hello.html',name=name)

@app.route('/user/<username>')
def show_user_name(username):
    return 'hello,%s' % username

@app.route('/port/<int:post_id>')
def show_port(post_id):
    return 'Post %d' % post_id

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/abouts')
def abouts():
    return 'The abouts page'

if __name__ == '__main__':
    #with app.test_request_context():
        #print(url_for('index_page'))
        #print(url_for('show_user_name', username='jfwang'))
    app.run(host='0.0.0.0',debug=True)





