#!/usr/bin/python3
from flask import Flask

app = Flask(__name__)
@app.route('/', strict_slashes=False)
def hello():
    return ('Hello HBNB!')
@app.route('/hbnb', strict_slashes=False)
def ello():
    return ('HBNB')
@app.route('/c/<text>', strict_slashes=False)
def get_text(text):
    text = text.replace("_", " ")
    return "C " + str(text)
@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def get_python(text='is cool'):
    text = text.replace("_", " ")
    return "Python " + str(text)
if __name__ == '__main__':
      app.run(host='0.0.0.0', port=5000)
