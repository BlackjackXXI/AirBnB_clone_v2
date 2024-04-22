#!/usr/bin/python3
"""
Sa script that starts a Flask web application:
Your web application must be listening on 0.0.0.0, port 5000
Routes:
/: display “Hello HBNB!”
"""

from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)

@app.route('/states_list', strict_slashes=False)
def states_list():
    """ state objects"""
    
    return render_template('7-states_list.html',
                           states=storage.all('State').values())
@app.teardown_appcontext
def teardown(self):
    """SQLAlchemy"""
    storage.close()
if __name__ == '__main__':
    app.run(host='0.0.0.0')
