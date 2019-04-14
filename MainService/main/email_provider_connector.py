# -*- coding: utf-8 -*-
# @Author: ahmedkammorah
# @Date:   2019-04-04 11:25:23
# @Last Modified by:   Ahmed kammorah
# @Last Modified time: 2019-04-14 20:42:09
from enum import Enum
from MainService.main.AKLogUtil.AKLogUtil import getLogger
logger = getLogger("EmailConnectors")
import requests
class RESPONSE_STATE(Enum):
    OK=1
    USER_ERROR=2
    SERVICE_ERROR=3
    OVERRATE_ERROR=4
    REQUEST_ERROR=5
    OTHER_ERROR=6


class EmailProviderConnector(object):
    def __init__(self):
        """Initalize the connector class with config and client instance"""
        self.config = {}

    def send_email(self, message):
        """ Sending Email message by provider service 

        Args:
            message: Full message 
        """
        pass
        
    def health_check(self):
        """ Checking the health of the email conponent in sendgrid service """
        url = self.config['STATUS_URL']
        logger.info('Start heartbeat {} service'.format(self.config['NAME']))
        EMAIL_SERVICE_COMPONENT_NAME = self.config['COMPONENT_NAME']
        response = requests.get(url)
        if response.status_code >= 200 and response.status_code < 300:
            ser_components = response.json().get('components', [])
            comps = list(filter(lambda e: e.get('name', None) == EMAIL_SERVICE_COMPONENT_NAME, ser_components))
            if len(comps) >= 1:
                comp = comps[0]
                if comp.get('status', None) == 'operational':
                    logger.info('heartbeat {} service is Up and running'.format(self.config['NAME']))
                    return True
                else:
                    logger.info('heartbeat {} sub-service {} is not operational'.format(self.config['NAME'], EMAIL_SERVICE_COMPONENT_NAME))
        logger.info('heartbeat {} service is Down'.format(self.config['NAME']))
        return False