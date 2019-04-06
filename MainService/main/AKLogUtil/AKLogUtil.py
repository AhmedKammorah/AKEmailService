# -*- coding: utf-8 -*-
# @Author: Ahmed kammorah
# @Date:   2019-04-05 13:45:24
# @Last Modified by:   Ahmed kammorah
# @Last Modified time: 2019-04-06 14:09:32


import os
import json
import logging.config
import logging
import errno


BASE_LOG_PATH = "/ak/logs/"
def mkdir_p(path):
    try:
        os.makedirs(path, exist_ok=True)  # Python>3.2
    except TypeError:
        try:
            os.makedirs(path)
        except OSError as exc: # Python >2.5
            if exc.errno == errno.EEXIST and os.path.isdir(path):
                pass
            else: raise

def setup_logging(default_path='logging.json', default_level=logging.INFO,env_key='LOG_CFG', service_name="AKService"):

	"""Setup logging configuration

	"""
	print('Start config logging default_path : ',default_path)
	log_dir = "{}{}/".format(BASE_LOG_PATH, service_name)
	
	mkdir_p(log_dir)
	print("Log logs path {}".format(log_dir))

	current_path = os.path.dirname(__file__)
	path = default_path
	value = os.getenv(env_key, None)
	if value:
		path = value
	else:
		path = os.path.join(current_path,default_path)

	if os.path.exists(path):
		print(path)
		
		with open(path, 'rt') as f:
			config = json.load(f)
		# append new logger with the service name with the template 
		# change the location of the files
		config["handlers"]["info_file_handler"]["filename"] = "{}info.log".format(log_dir)
		config["handlers"]["error_file_handler"]["filename"]= "{}error.log".format(log_dir)
		config["handlers"]["debug_file_handler"]["filename"]= "{}debug.log".format(log_dir)
		logging.config.dictConfig(config)
		print('----------------------- START LOGGING for  {}  service------------------'.format(service_name))
	else:
		print('----------------------- START LOGGING  basicConfig------------------')
		logging.basicConfig(level=default_level)

def getLogger(service_name="AKService"):
	SERVICE_NAME = service_name 
	setup_logging(default_path='logging.json', default_level=logging.DEBUG, service_name=service_name)
	logger = logging.getLogger(SERVICE_NAME)
	logger.info('start working service {}'.format(service_name))
	return logger

if __name__ == "__main__":
	"""
		For test only
	"""
	getLogger("Ahmed")