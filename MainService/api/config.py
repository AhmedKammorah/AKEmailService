# -*- coding: utf-8 -*-
# @Author: ahmedkammorah
# @Date:   2017-01-22 02:45:44
# @Last Modified by:   Ahmed kammorah
# @Last Modified time: 2019-04-08 18:18:05

import os
from MainService.config.config import BASE_HOST, BASE_REST_PORT,AK_API_JWT_SECRET_KEY,AK_JWT_ALGORITHM

host = '{}:{}'.format(BASE_HOST,BASE_REST_PORT)

MAIN_DEFAULT_USER = {
  'username':'ahmed',
  'password':'f82fa358a6a100de1815fa0d57f876fda078d9e136494f1589d9d894'
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
  "host": host,  # overrides localhost:5000
  "basePath": "/",  # base bash for blueprint registration
  "schemes": [
    "http",
    "https"
  ],
  "operationId": "getmyData"  
}
