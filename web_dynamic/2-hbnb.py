#!/usr/bin/python3
""" start flask web app """

from uuid import uuid4
from flask import *
from models import storage
from os import *
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place

#flask setup
app = Flask(__name__)
app.url_map.strict_slashes = False
port = 5000
host = '0.0.0.0'

#flask page rendering
@app.teardown_appcontext
def close_db(error):
    """ clear current SQLAlchemy session """
    storage.close()

@app.route('/2-hbnb/')
def hbnb():
    """ handle template requests """
    states = storage.all(State).values()
    states = sorted(states, key=lambda k: k.name)
    st_ct = []

    for state in states:
        st_ct.append([state, key=lambda k: k.name])

    places = storage.all(Place).values()
    places = sorted(places, key=lambda k: k.name)
    amenities = storage.all(Amenity).values()
    amenities = sorted(amenities, key=lambda k: k.name)
    cache_id = str(uuid.uuid4())

    return render_template('2-hbnb.html',
                           states=st_ct,
                           places=places,
                           amenities=amenitites,
                           cache_id=cache_id)

if __name__ == "__main__":
    """ main function """
    app.run(host=host, port=port)
