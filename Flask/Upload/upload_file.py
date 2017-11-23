#-*- coding:utf-8 -*-
import os
from flask import Flask,request,redirect,url_for,send_from_directory
from werkzeug.utils import secure_filename
__author__ = 'wangjf'

UPLOAD_FOLDER = '/Users/wangjianfeng/Code/flask/uploads'
ALLOWED_EXTENSIONs = set(['txt','pdf','jpg','png','git'])

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# 定义文件上传大小
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


def allowed_file(filename):

    return '.' in filename and filename.split('.')[-1] in ALLOWED_EXTENSIONs

@app.route('/',methods=['POST'])
def upload_file():
    print('111')
    if request.method == 'POST':
        print('2222')
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            return redirect(url_for('uploaded_file',filename=filename))
    print('3333')
    # 这里的作用是因为，第一次启动的时候因为进不到if，所以界面直接渲染，第二次则跳转了
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
