from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route('/greet', methods=['POST'])
def greet():
  name = request.form['name']
  return f'Hello, {name}!'


@app.route('/')
def hello():
    return render_template('index.html', message='Hello, World!')


