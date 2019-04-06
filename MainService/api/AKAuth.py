# -*- coding: utf-8 -*-
# @Author: ahmedkammorah
# @Date:   2017-01-21 23:51:34
# @Last Modified by:   Ahmed kammorah
# @Last Modified time: 2019-04-06 18:49:24

'''
    TS Custom JWT Auth 
    This work by JWT Config
    and API secrit  
'''

from flask_jwt import JWT, jwt_required, current_identity
from werkzeug.security import safe_str_cmp

from AKAPP import app

def authenticate(username, password):
    '''
        Not used here because there is no login in this service 
        just authoriation 
    '''
    print('authenticate')
    return 'user'

def identity(payload):
    '''
        For Payload and jwt token retrive 
    '''
    print('identity')
    print(payload)
    user_id = payload['id']
    return payload

jwt = JWT(app, authenticate, identity)