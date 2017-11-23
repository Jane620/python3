#-*- coding:utf-8 -*-
import os
import flaskr
import unittest
import tempfile

__author__ = 'wangjf'


class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        database = flaskr.read_config('DATABASE')
        self.db_fd,database = tempfile.mkstemp()
        flaskr.app.config['TESTING'] = True
        self.app = flaskr.app.test_client()
        flaskr.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(flaskr.read_config('DATABASE'))

    def login(self, username, password):
        return self.app.post('/login', data=dict(username=username, password=password), follow_redirects=True)

    def logout(self):
        return self.app.get('/logout', follow_redirects=True)


    def test_empty_db(self):
        rv = self.app.get('/')
        assert b'No entries here so far' in rv.data

    def test_login_logout(self):
        rv = self.login('admin','admin')
        assert b'You are successful login.' in rv.data
        rv = self.logout()
        assert b'You are not login.' in rv.data
        rv = self.login('adminx','default')
        assert b'Invalid username' in rv.data
        rv = self.login('admin','defaultx')
        assert b'Invalid password' in rv.data

    def test_message(self):
        self.login('admin','admin')
        rv = self.app.post('/add',data=dict(title='<hello>',text='<strong>HTML</strong> allowed here'),follow_redirects=True)
        assert b'No entries here so far' not in rv.data
        assert b'hello' in rv.data
        assert b'<strong>HTML</strong> allowed here' in rv.data

if __name__ == '__main__':
    unittest.main()

