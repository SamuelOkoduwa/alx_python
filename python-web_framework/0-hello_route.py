# !/usr/bin/python3

from flask import Flask

'''
Initialization of the Flask Module

'''

app = Flask(__name__)
app.url_map.strict_slashes = False

"""
Route

"""
@app.route("/")
def Home():
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")