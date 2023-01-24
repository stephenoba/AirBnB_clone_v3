#!/usr/bin/python3
"""index.py to connect to API"""
from flask import jsonify

from api.v1.views import app_views


@app_views.route('/status', strict_slashes=False)
def getStatus():
    """Get status"""
    return jsonify({"status": "OK"})
