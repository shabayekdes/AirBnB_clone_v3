#!/usr/bin/python3
'''api status'''
import models
from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status', strict_slashes=False)
def ok():
    '''return stuff'''
    return jsonify(status='OK')
