#!/usr/bin/env python3
import os
import shutil
import requests
import redis
import multipart as mp
import json
from multipart import tob
from flask import Flask, render_template, request, abort
from werkzeug.utils import secure_filename
from flask_uploads import *
from pymongo import MongoClient

try:
    from io import BytesIO
except ImportError:
    from StringIO import StringIO as BytesIO

# change the url of redis db
r = redis.Redis('localhost')
app = Flask(__name__, 
            static_folder = '../dist/static', 
            template_folder = '../dist') 
app.config['UPLOADS_DEFAULT_DEST'] = app.root_path
UPLOAD_FOLDER = '../dist/uploads'
files = UploadSet('files', ('txt', 'pdf', 'png', 'jpg', 'gif', 'jpeg', 'mp4', 'mkv', 'webm', 'tex'))
configure_uploads(app, files)


client = MongoClient()
db = client["science"]
data = db["data"]

count = 1692

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')

def catch_all(path):
    return render_template("index.html")

def index():
    return render_template("index.html")

@app.route('/api/upload', methods = ['GET', 'POST'])
def upload():
    # if request.method == 'POST':
    #     files.save(request.files['file'])
    #     shutil.move('kladi/files', 'dist/uploads') 
    #     return 'OK'
    title = request.form['text']
    des = request.form['des']
    tags = request.form['tags']
    f = request.form['myfile']

    global count
    count = count +1

    link = {"_id" : count,
            "title" : title,
            "des": des,
            "tags" : list(tags)}
    data.insert_one(link)


    return 'OK'

# fetches url 
@app.route('/api/nodes/values')
def fetch_vals():
    values = []
    for i in r.keys():
        values.append(r.get(i).decode('utf-8')) 
    return str(values)
        

@app.route('/api/nodes/links')
def fetch_links():
    print('im here')
    a = []
    for i in r.keys():
        a.append(i.decode('utf-8'))
    return str(a)

@app.route('/api/nodes/posts')
def fetch_posts():
    post_list = []
    for i in data.find():
        post_list.append(i)
    return post_list


@app.route('/api/nodes/<postid>')
def fetch_one_post(postid):
    for j in data.find():
        if j["_id"]==postid:
            d = j
    return d

if __name__ == '__main__':
    app.run(debug = True)
