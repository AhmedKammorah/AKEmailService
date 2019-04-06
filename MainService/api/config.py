# -*- coding: utf-8 -*-
# @Author: ahmedkammorah
# @Date:   2017-01-22 02:45:44
# @Last Modified by:   Ahmed kammorah
# @Last Modified time: 2019-04-06 19:12:08

import os

# AUTH
AK_API_JWT_SECRET_KEY = ''
AK_JWT_ALGORITHM = 'HS256'

# RPC Service
AK_RPC_URI = ''
TSCORE_USERNAME = ''
TSCORE_PASSWORD = ''

# if os.environ.get('AK_APP_ENV') == 'pro':
#     print 'Prodction environment'
#     # AUTH
#     AK_API_JWT_SECRET_KEY = ''
#     AK_JWT_ALGORITHM = 'HS256'


# elif os.environ.get('AK_APP_ENV') == 'dev':
#     print 'development environment'
#     # AUTH
#     AK_API_JWT_SECRET_KEY = ''
#     AK_JWT_ALGORITHM = 'HS256'



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
  "host": "0.0.0.0",  # overrides localhost:500
  "basePath": "/api",  # base bash for blueprint registration
  "schemes": [
    "http",
    "https"
  ],
  "operationId": "getmyData"
}