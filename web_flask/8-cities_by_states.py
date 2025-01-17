#!/usr/bin/python3
"""comment"""


from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """comment"""
    states = storage.all('State')
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown(ex):
    """comment"""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_list():
    """comment"""
    states = storage.all('State')
    return render_template('8-cities_by_states.html', states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
