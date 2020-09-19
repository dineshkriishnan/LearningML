from flask import Flask, render_template, request
import automl
from automl import heatmap, read_data
from io import StringIO
import pandas as pd
from flask.helpers import send_file

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods = ['GET', 'POST'])
def upload():
    if request.method == 'POST':
      fileStr = request.files['file']
      data = read_data(fileStr)
      return render_template('index.html',head=[data.head().to_html(classes='data')]
      ,describe=[data.describe().to_html(classes='data')]
      ,correlation = heatmap(data.corr())
      )
    return render_template('index.html')