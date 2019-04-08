# -*- coding: utf-8 -*-
# @Author: ahmedkammorah
# @Date:   2019-04-04 11:25:23
# @Last Modified by:   Ahmed kammorah
# @Last Modified time: 2019-04-08 21:06:00
from enum import Enum
from MainService.main.AKLogUtil.AKLogUtil import getLogger
logger = getLogger("EmailConnectors")

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
        pass

    def send_email(self, message):
        """ Sending Email message by provider service 

        Args:
            message: Full message 
        """
        pass
        
    def health_check(self):
        """ Checking the health of the email conponent in sendgrid service """
        pass