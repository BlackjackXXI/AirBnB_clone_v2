#!/usr/bin/python3
"""
Sa script that starts a Flask web application:
Your web application must be listening on 0.0.0.0, port 5000
Routes:
/: display “Hello HBNB!”
"""

from flask import Flask
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_route():
    """ Displays 'Hello HBNB!' """
    return 'Hello HBNB!'
@app.route('/hbnb', strict_slashes=False)
def hbnb_route():
    """ Displays 'HBNB' """
    return 'HBNB'
@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """ Displays C followed by text"""
    text = text.replace("_", " ")
    return 'C ' + text
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
