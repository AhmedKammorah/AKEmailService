# -*- coding: utf-8 -*-
# @Author: ahmedkammorah
# @Date:   2017-01-22 02:45:44
# @Last Modified by:   Ahmed kammorah
# @Last Modified time: 2019-04-08 02:21:14

import os

# AUTH
AK_API_JWT_SECRET_KEY = 'b11c9f7a37ead9e819c9ea09dff158f6'
AK_JWT_ALGORITHM = 'HS256'

# RPC Service
AK_RPC_URI = ''
AK_USERNAME = ''
AK_PASSWORD = ''
BASE_HOST = 'localhost'

MAIN_DEFAULT_USER = {
  'username':'ahmed',
  'password':'ak_mock_p@ssword'
}
Swagger_template = {
  "swagger": "2.0",
  "info": {
    "title": "AKEmailService API",
    "description": "API for AKEmailService for sending email",
    "contact": {
      "responsibleOrganization": "Ahmed Kammorah",
      "responsibleDeveloper": "Ahmed Kammorah",
      "email": "Ahmedkammorah@gmail.com",
      "url": "www.kammorah.com",
    },
    "termsOfService": "http://kammorah.com/terms",
    "version": "0.0.1"
  },
  "host": BASE_HOST+":5000",  # overrides localhost:5000
  "basePath": "/",  # base bash for blueprint registration
  "schemes": [
    "http",
    "https"
  ],
  "operationId": "getmyData"  
}
