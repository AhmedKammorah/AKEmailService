# -*- coding: utf-8 -*-
# @Author: ahmedkammorah
# @Date:   2017-01-21 23:51:34
# @Last Modified by:   Ahmed kammorah
# @Last Modified time: 2019-04-08 02:22:03

'''
    TS Custom JWT Auth 
    This work by JWT Config
    and API secrit  
'''

from flask_jwt import JWT, jwt_required, current_identity
from werkzeug.security import safe_str_cmp

from MainService.api.AKAPP import app, MAIN_DEFAULT_USER

class User(object):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password
MainUser = User(1, MAIN_DEFAULT_USER['username'], MAIN_DEFAULT_USER['password'])
   

def authenticate(username, password):
    '''
        TODO: make user and auth service to create the user and generate tokens for users
        just authoriation 
    '''
    print('authenticate')
    user = MainUser
    if user and safe_str_cmp(user.password.encode('utf-8'), password.encode('utf-8')):
        return user
    return 'No User matches'

def identity(payload):
    '''
        For Payload and jwt token retrive 
    '''
    print('identity')
    print(payload)
    # user_id = payload['id']
    return payload

jwt = JWT(app, authenticate, identity)

