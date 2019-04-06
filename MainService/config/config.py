# -*- coding: utf-8 -*-
# @Author: ahmedkammorah
# @Date:   2019-04-05 13:06:43
# @Last Modified by:   Ahmed kammorah
# @Last Modified time: 2019-04-06 14:09:07

import os

# AUTH
AK_API_JWT_SECRET_KEY = ''
AK_JWT_ALGORITHM = 'HS256'

# RPC Service
AK_RPC_URI = ''
TSCORE_USERNAME = ''
TSCORE_PASSWORD = ''


REDIS_HOST = "ak-redis"
REDIS_PORT = 6379

# print os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
print (__file__)
print(os.path.realpath(__file__))
print()
import yaml
current_dir = os.path.dirname(__file__)
connector_config_file_name = 'conectors_conf.yaml'
connector_config_path = os.path.join(current_dir, connector_config_file_name)
def load_config(config_file):
    with open(config_file, 'r') as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
conector_config = load_config(connector_config_path)

print(conector_config)