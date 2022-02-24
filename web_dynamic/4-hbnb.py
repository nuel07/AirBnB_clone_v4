#!/usr/bin/python3
""" start web flask application """

from models import storage
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
import uuid
from os import *
from flask import *

#flask setup
app = Flask(__name__)
app.url_map.strict_slashes = False
port = 5000
host = '0.0.0.0'

#flask page rendering
@app.teardown_appcontext
def close_db(error):
    """ Clear current SQLAlchemy session """
    storage.close()

@app.route('/4-hbnb/')
def hbnb():
    """ handle requests to templates """
    states = storage.all(State).values()
    states = sorted(states, key=lambda k: k.name)
    st_ct = []

    for state in states:
        st_ct.append([state, key=lambda k: k.name])

    amenitites = storage.all(Amenity).values()
    amenities = sorted(amenities, key=lambda k: k.name)
    places = storage.all(Place).values()
    places = sorted(amenities, key=lambda k: k.name)
    cache_id = str(uuid.uuid4())

    return render_template('4-hbnb.html',
                           states=st_ct,
                           places=places,
                           amenities=amenities,
                           cache_id=cache_id)

if __name__ == "__main__":
    """ Main function """
    app.run(host=host, port=port)
