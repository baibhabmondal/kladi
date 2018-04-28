#!/usr/bin/env python3
import os
import shutil
import requests
import redis
from flask import Flask, render_template, request, abort
from werkzeug.utils import secure_filename
from flask_uploads import *

# change the url of redis db
r = redis.Redis('localhost')
app = Flask(__name__, 
            static_folder = '../dist/static', 
            template_folder = '../dist') 
app.config['UPLOADS_DEFAULT_DEST'] = app.root_path
UPLOAD_FOLDER = '../dist/uploads'
files = UploadSet('files', ('txt', 'pdf', 'png', 'jpg', 'gif', 'jpeg', 'mp4', 'mkv', 'webm', 'tex'))
configure_uploads(app, files)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')

def catch_all(path):
    return render_template("index.html")

def index():
    return render_template("index.html")

@app.route('/api/upload', methods = ['GET', 'POST'])
def upload():
    if request.method == 'POST':
        files.save(request.files['file'])
        print(os.getcwd())
        shutil.move('kladi/files', 'dist/uploads') 
        return 'OK'


@app.route('/api/nodes/<node_name>')
def is_node(node_name):
    if r.get(node_name):
        return r.get(node_name)
    else:
        abort(404)


if __name__ == '__main__':
    app.run(debug = True)
