# !/usr/bin/python3

"""Starting a web application using flask"""
from flask import Flask

'''Initialization of the Flask Module'''

app = Flask(__name__)
app.url_map.strict_slashes = False

"""Route"""
@app.route("/")
def Home():
    return "Hello HBNB!"

@app.route("/hbnb")
def about():
    return "HBNB"

"""running the flask application"""
if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")