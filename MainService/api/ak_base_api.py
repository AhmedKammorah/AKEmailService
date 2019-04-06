# -*- coding: utf-8 -*-
# @Author: Ahmed kammorah
# @Date:   2019-04-06 18:18:53
# @Last Modified by:   Ahmed kammorah
# @Last Modified time: 2019-04-06 19:31:58

from flask import Flask
from flask import request
from flask import jsonify
from AKAPP import app, swag_from
from AKAuth import jwt, JWT, jwt_required, current_identity, safe_str_cmp
from flask_cors import CORS, cross_origin

def _getUserId():
    if current_identity:
        return current_identity['id']
    return None


@app.route('/protected')
# @jwt_required()
def protected():
    print ('protected')
    return 'Welcome %s to AKEmailServices API' % current_identity

@app.route("/")
def helloworld():
    '''Welcome API Test'''
    return "Welcome to AKEmailServices API"