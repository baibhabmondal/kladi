#!/usr/bin/env python3

from flask import Flask, render_template

app = Flask(__name__, 
            static_folder = './vue/dist/static', 
            template_folder = './vue/dist') 

@app.route('/')
def index():
    return render_template('index.html')
