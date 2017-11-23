#-*- coding:utf-8 -*-
from flask import Flask,request,session,escape,redirect,url_for
__author__ = 'wangjf'

app = Flask(__name__)
app.secret_key = '\x92\xfes\xd1\x80[14\xdf\xcbu\xc0\xdb\xce%\xc5)\xd5\xd4N\xb2ty\x84'

@app.route('/')
def index():
    if 'username' in session:
        return 'logging as %s' % escape(session['username'])
    return 'you are not logged in'

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        session['username'] = str(request.form['username'])
        return redirect(url_for('index'))
    return '''
        <form action="" method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    session.pop('username',None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)

