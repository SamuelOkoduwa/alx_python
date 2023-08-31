
"""Starting a web application using flask with a route displaying C followed by the value of the text variable
"""


from flask import Flask, render_template

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

@app.route("number_template/<n>")
def display_html(n):
    return render_template("5-number.html, n=n")
        
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')