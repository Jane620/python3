#-*- coding:utf-8 -*-
from flask import Flask,request,g,render_template,session,abort,flash,redirect,url_for
import sqlite3
from contextlib import closing
__author__ = 'wangjf'

# configuration
#DATABASE = 'db/flaskr.db'
SECRET_KEY = '\xa4\xb3\xdb[[g\x12S}\xda\xfe\xdf0\xa8\x99\x0e\xd0\xba?W\xef\x10\xcer'

# flask
app = Flask(__name__)
app.config.from_object(__name__)

# connect db
def connect_db():
    return sqlite3.connect(read_config('DATABASE'))

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql') as f:
            db.cursor().executescript(f.read().decode('utf-8'))
        db.commit()

def read_config(config):
    app.config.from_pyfile('Config.ini')
    return app.config[config]

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    g.db.close()

@app.route('/')
def show_entries():
    #
    cur = g.db.execute('select title, text from entries order by id desc')
    entries = [dict(title=row[0],text=row[1]) for row in cur.fetchall()]
    return render_template('show_entries.html',entries=entries)


@app.route('/add',methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    g.db.execute('insert into entries (title,text) values (?,?)',[request.form['title'],request.form['text']])
    g.db.commit()
    flash('New entry was successfully posted')
    print('good')
    return redirect(url_for('show_entries'))


@app.route('/login',methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != read_config('USERNAME'):
            error = 'Invalid username'
        elif request.form['password'] != read_config('PASSWORD'):
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You are successful login.')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in',None)
    flash('You are not login.')
    return redirect(url_for('show_entries'))


if __name__ == '__main__':
    # 首次创建db文件
    app.run(host='0.0.0.0',debug=True)





