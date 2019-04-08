# -*- coding: utf-8 -*-
# @Author: Ahmed kammorah
# @Date:   2019-04-06 18:18:53
# @Last Modified by:   Ahmed kammorah
# @Last Modified time: 2019-04-08 14:01:48

from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS, cross_origin

from MainService.api.ak_app import app, swag_from
from MainService.api.ak_auth import jwt, JWT, jwt_required, current_identity, safe_str_cmp,authenticate


def _getUserId():
    if current_identity:
        return current_identity['id']
    return None


@app.route("/api/auth", methods=["POST"])
def auth_user_login():
    """
    User authenticate method.
    ---
    tags:
        - "AKAuth"
    description: Authenticate user with credentials(username and password).
    parameters:
      - name: username
        in: formData
        type: string
        required: true
      - name: password
        in: formData
        type: string
        required: true
 
    responses:
      200:
        description: User successfully logged in and return the JWT Token.
      400:
        description: User login failed.
    """
    try:
        username = request.form.get("username")
        password = request.form.get("password")
        print(username)
        print(password)
        user = authenticate(username, password)
        if not user:
            raise Exception("User not found!")

        resp = jsonify({"message": "User authenticated"})
        resp.status_code = 200

        access_token = jwt.jwt_encode_callback(user)

        # add token to response headers - so SwaggerUI can use it
        resp.headers.extend({'jwt-token': access_token})

    except Exception as e:
        resp = jsonify({"message": "Bad username and/or password"})
        resp.status_code = 401

    return resp

@app.route('/api/protected')
@jwt_required()
def protected():
    """
    protected method.
    ---
    tags:
        - "AKAuth"
    description: test call api with jwt token.
  
    responses:
      200:
        description: successfully authorize method.
      400:
        description: User login failed.
    """
    print ('protected')
    return 'Welcome %s to AKEmailServices API' % current_identity

@app.route("/")
def helloworld():
    '''Welcome API Test'''
    return "Welcome to AKEmailServices API"