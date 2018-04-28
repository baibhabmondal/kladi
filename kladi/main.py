#!/usr/bin/env python3
import os
from flask import Flask, render_template
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/upload'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'gif', 'jpeg', 'mp4', 'mkv', 'webm', 'tex'])

app = Flask(__name__, 
            static_folder = './dist/static', 
            template_folder = './dist') 

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')

def catch_all(path):
    return render_template("index.html")

def index():
    return render_template("index.html")

def allowed_file(filename):
    return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/api/upload')
def upload():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        return 'OK'
    else:
        return 'FAIL'


app.run()
