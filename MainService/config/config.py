# -*- coding: utf-8 -*-
# @Author: ahmedkammorah
# @Date:   2019-04-05 13:06:43
# @Last Modified by:   Ahmed kammorah
# @Last Modified time: 2019-04-08 18:29:32

import os


REDIS_HOST = "ak-redis"
REDIS_PORT = 6379


BASE_HOST = os.environ.get('BASE_HOST', None)
BASE_REST_PORT = 5000

RPC_SERVER = BASE_HOST
RPC_PORT = 50051

# AUTH
AK_API_JWT_SECRET_KEY = os.environ.get('AK_API_JWT_SECRET_KEY', None)
AK_JWT_ALGORITHM = 'HS256'

SENDGRID_API_KEY = os.environ.get('SENDGRID_API_KEY', None)
SPARKPOST_API_KEY = os.environ.get('SPARKPOST_API_KEY', None)

if os.environ.get('AK_APP_ENV') == 'dev':
    BASE_HOST = 'localhost'

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
conector_config.get('sendgrid')['API_KEY'] = SENDGRID_API_KEY
conector_config.get('sparkpost')['API_KEY'] = SPARKPOST_API_KEY
print(conector_config)