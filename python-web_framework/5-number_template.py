"""
This is to start Flask web application including route
"""

from flask import Flask
from flask import render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def Hello_HBNB():
    return 'Hello HBNB!'

@app.route('/hbnb')
def HBNB():
    return 'HBNB'

@app.route('/c/<text>')
def cisfun(text):
    return 'C ' + text.replace('_', ' ')

@app.route('/python/<text>')
def pythoniscool(text='is cool'):
    return 'Python ' + text.replace('_', ' ')

@app.route('/number/<int:n>')
def nisinteger(n):
    return "{:d} is a number".format(n)

@app.route('/number_template/<int:n>')
def numberstemplates(n):
    """display a HTML page only if n is an integer"""
    return render_template('5-number.html', n=n)
        
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')