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

@app.route('/api/upload')
def index():
    return render_template('index.html')

app.run()
