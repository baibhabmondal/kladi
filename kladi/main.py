#!/usr/bin/env python3
import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from flask_uploads import *


app = Flask(__name__, 
            static_folder = '../dist/static', 
            template_folder = '../dist') 
app.config['UPLOADS_DEFAULT_DEST'] = app.root_path
files = UploadSet('files', ('txt', 'pdf', 'png', 'jpg', 'gif', 'jpeg', 'mp4', 'mkv', 'webm', 'tex'))
configure_uploads(app, files)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')

def catch_all(path):
    return render_template("index.html")

def index():
    return render_template("index.html")

def allowed_file(filename):
    return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/api/upload', methods = ['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        return 'OK'

if __name__ == '__main__':
    app.run(debug = True)
