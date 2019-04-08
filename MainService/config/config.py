# -*- coding: utf-8 -*-
# @Author: ahmedkammorah
# @Date:   2019-04-05 13:06:43
# @Last Modified by:   Ahmed kammorah
# @Last Modified time: 2019-04-08 02:52:54

import os


REDIS_HOST = "ak-redis"
REDIS_PORT = 6379

RPC_SERVER = 'localhost'
RPC_PORT = 50051
 
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