# -*- coding: utf-8 -*-
# @Author: ahmedkammorah
# @Date:   2019-04-04 11:24:11
# @Last Modified by:   Ahmed kammorah
# @Last Modified time: 2019-04-06 14:07:53

# SPARTPOST_API_KEY = "45b036dbdb872be184355255c0e81293ecd94a12"
# EMAIL_SERVICE_COMPONENT_NAME = "Transmissions API"
# SERVICE_STATUS_URL =""
from MainService.main.email_provider_connector import EmailProviderConnector
from sparkpost import SparkPost
import requests
from MainService.config.config import conector_config

class EPSparkPostConnector(EmailProviderConnector):
    """SparkPost Email service Connector 
       
       Attributes:
           config: The config and settings related to sparkpost provider
           sparky: instance of sparkspot client
    """

    
    def __init__(self):
        """Initalize the connector class with config and client instance"""
        self.config = conector_config.get('sparkpost', {})
        self.sparky = SparkPost(self.config['API_KEY'])


    def send_email(self, message):
        """ Sending Email message by SparkPost service 

        Args:
            message: Full message 
        """
        try:
            response = self.sparky.transmissions.send(
                                            use_sandbox = True,
                                            recipients = message.to_emails,
                                            html = message.body,
                                            from_email = message.from_email,
                                            subject = message.subject)
            print(response.status_code)
            if response.status_code == 200 or response.status_code == 202:
                return RESPONSE_STATE.OK, response
            elif response.status_code >= 500:
                return RESPONSE_STATE.SERVICE_ERROR, response
            elif response.status_code == 429:
                return RESPONSE_STATE.OVERRATE_ERROR, response
            elif response.status_code in [401, 403, 404, 405]:
                # service error
                # request problem
                return RESPONSE_STATE.REQUEST_ERROR, response 
            elif response.status_code >= 400 and response.status_code < 500:
                return RESPONSE_STATE.USER_ERROR, response
        except Exception as e:
            print(e.message)
        return RESPONSE_STATE.OTHER_ERROR, response

    def health_check(self):
        """ Checking the health of the email conponent in sendgrid service """
        url = self.config['STATUS_URL']
        EMAIL_SERVICE_COMPONENT_NAME = self.config['COMPONENT_NAME']
        print(EMAIL_SERVICE_COMPONENT_NAME)
        response = requests.get(url)
        if response.status_code >= 200 and response.status_code < 300:
            ser_components = response.json().get('components', [])
            comps = list(filter(lambda e: e.get('name', None) == EMAIL_SERVICE_COMPONENT_NAME, ser_components))
            if len(comps) > 0:
                comp = comps[0]
                if comp.get('status', None) == 'operational':
                    return True
        return False


if __name__ == "__main__":
    pass
