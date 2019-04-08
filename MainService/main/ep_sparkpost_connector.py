# -*- coding: utf-8 -*-
# @Author: ahmedkammorah
# @Date:   2019-04-04 11:24:11
# @Last Modified by:   Ahmed kammorah
# @Last Modified time: 2019-04-08 23:02:04
from MainService.main.email_provider_connector import EmailProviderConnector,RESPONSE_STATE, logger
from sparkpost import SparkPost
import requests
from MainService.config.config import conector_config
from pprint import pprint
API_URL = 'https://api.sparkpost.com/api/v1/transmissions'
class EPSparkPostConnector(EmailProviderConnector):
    """SparkPost Email service Connector 
       
       Attributes:
           config: The config and settings related to sparkpost provider
           sparky: instance of sparkspot client
    """
    # https://api.sparkpost.com/api/v1
    
    def __init__(self):
        """Initalize the connector class with config and client instance"""
        self.config = conector_config.get('sparkpost', {})
        # self.sparky = SparkPost(self.config['API_KEY'])
        self.API_KEY = self.config['API_KEY']
        self.headers = {
            'Content-Type': "application/json",
            'Accept': "application/json",
            'Authorization': self.API_KEY,
            }

    def send_email(self, message):
        """ Sending Email message by SparkPost service 

        Args:
            message: Full message 
        """
        logger.info('Start Sending Email using SparkPost')
        try:
            
            msgData = message.build_sparkpost_msg()
            querystring = {"num_rcpt_errors":"3"}
            response = requests.post(API_URL, data=msgData,headers=self.headers, params=querystring)            
            logger.info('Response form sending email using SparkPost with status_code: {} and text: {}'.format(response.status_code, response.text))
            
            if response.status_code == 200 or response.status_code == 202:
                return RESPONSE_STATE.OK, response.text
            elif response.status_code >= 500:
                return RESPONSE_STATE.SERVICE_ERROR, response.text
            elif response.status_code == 429:
                return RESPONSE_STATE.OVERRATE_ERROR, response.text
            elif response.status_code in [401, 403, 404, 405]:
                # service error
                # request problem
                return RESPONSE_STATE.REQUEST_ERROR, response.text 
            elif response.status_code >= 400 and response.status_code < 500:
                return RESPONSE_STATE.USER_ERROR, response.text
        except Exception as e:
            # print(e.message)
            logger.error("Error in sending Email with SparkPost error:{}".format(e))
        return RESPONSE_STATE.OTHER_ERROR, None

    def health_check(self):
        """ Checking the health of the email conponent in sparkpost service """
        url = self.config['STATUS_URL']
        logger.info('Start heartbeat sparkpost service')
        EMAIL_SERVICE_COMPONENT_NAME = self.config['COMPONENT_NAME']
        print(EMAIL_SERVICE_COMPONENT_NAME)
        response = requests.get(url)
        if response.status_code >= 200 and response.status_code < 300:
            ser_components = response.json().get('components', [])
            comps = list(filter(lambda e: e.get('name', None) == EMAIL_SERVICE_COMPONENT_NAME, ser_components))
            if len(comps) > 0:
                comp = comps[0]
                if comp.get('status', None) == 'operational':
                    logger.info('heartbeat sparkpost service is Up and running')
                    return True
        return False


if __name__ == "__main__":
    pass
