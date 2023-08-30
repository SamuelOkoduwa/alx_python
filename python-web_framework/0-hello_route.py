# !/usr/bin/python3

from flask import Flask

'''Initialization of the Flask Module'''

app = Flask(__name__)

"""Route"""
@app.route("/", strict_slashes= False)
def Home():
    return "Hello HBNB!"

""""running the flask application"""
if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")