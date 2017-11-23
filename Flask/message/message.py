#-*- coding:utf-8 -*-
from flask import Flask,request,flash,redirect,url_for,render_template
__author__ = 'wangjf'

app = Flask(__name__)
app.secret_key = '\x92\xfes\xd1\x80[14\xdf\xcbu\xc0\xdb\xce%\xc5)\xd5\xd4N\xb2ty\x84'

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login',methods=['GET','POST'])
def login():
    error = None
    app.logger.debug('准备登录')
    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
            request.form['password'] != 'admin':
            app.logger.error('登录失败')
            error = 'Invalid credentials'
        else:
            flash('You are login.')
            return redirect(url_for('index'))
    app.logger.warning('未登录')
    return render_template('login.html',error=error)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)

