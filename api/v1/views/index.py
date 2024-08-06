#!/usr/bin/python3
"""
Module for index
"""

import flask.jsonify
from api.v1.views import app_views
from models import storage


@app_views.route("/status", methods=['GET'], strict_slashes=False)
def status():
    """Method for status route"""
    data = {
        "status": "OK"
    }
    resp = flask.jsonify(data)
    resp.status_code = 200

    return resp


@app_views.route("/stats", methods=['GET'], strict_slashes=False)
def stats():
    """Method of all objects route"""
    data = {
        "amenities": storage.count("Amenity"),
        "cities": storage.count("City"),
        "places": storage.count("Place"),
        "reviews": storage.count("Review"),
        "states": storage.count("State"),
        "users": storage.count("User"),
    }
    resp = flask.jsonify(data)
    resp.status_code = 200

    return resp
