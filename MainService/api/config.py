# -*- coding: utf-8 -*-
# @Author: ahmedkammorah
# @Date:   2017-01-22 02:45:44
# @Last Modified by:   Ahmed kammorah
# @Last Modified time: 2019-04-15 00:48:27

import os
from MainService.config.config import BASE_HOST, BASE_REST_PORT,AK_API_JWT_SECRET_KEY,AK_JWT_ALGORITHM

DOCS_HOST = '{}:{}'.format(BASE_HOST,BASE_REST_PORT)

MAIN_DEFAULT_USER = {
  'username':'demo',
  'password':'f82fa358a6a100de1815fa0d57f876fda078d9e136494f1589d9d894'
}

