#!/usr/bin/python3
"""index.py to connect to API"""
from flask import jsonify

from models import storage
from api.v1.views import app_views


entities = ["Amenity", "City", "Place", "Review", "State", "User"]


@app_views.route('/status', strict_slashes=False)
def getStatus():
    """Get status"""
    return jsonify({"status": "OK"})


@app_views.route('/stats', strict_slashes=False)
def getStats():
    """Get stats"""
    res = {}
    for e in entities:
        res[e.lower()] = storage.count(e)
    return jsonify(res)


if __name__ == "__main__":
    pass
