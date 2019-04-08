# -*- coding: utf-8 -*-
# @Author: ahmedkammorah
# @Date:   2019-04-04 11:23:35
# @Last Modified by:   Ahmed kammorah
# @Last Modified time: 2019-04-07 00:55:15

import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

import requests
from pprint import pprint

from MainService.main.email_provider_connector import EmailProviderConnector, RESPONSE_STATE

from MainService.config.config import conector_config
class EPSendGridConnector(EmailProviderConnector):
    """SendGrid Email service Connector 
       
       Attributes:
           config: The config and settings related to SendGrid provider
           sparky: instance of SendGrid client
    """

    def __init__(self):
       """Initalize the connector class with config and client instance"""
       self.config = conector_config.get('sendgrid', {})
       self.sg = SendGridAPIClient(self.config['API_KEY'])

    def send_email(self, email_message):
        """ Sending Email message by sendgrid service 

        Args:
            message: Full message 
        """
        message = Mail(
                from_email=email_message.from_email,
                to_emails=email_message.to_emails,
                subject=email_message.subject,
                html_content=email_message.body)
        try:
            response = self.sg.send(message)
            print(response.status_code)
            if response.status_code == 200 or response.status_code == 202:
                return RESPONSE_STATE.OK, response
            elif response.status_code >= 500:
                return RESPONSE_STATE.SERVICE_ERROR, response
            elif response.status_code == 429:
                return RESPONSE_STATE.OVERRATE_ERROR, response
            elif response.status_code in [413, 415]:
                return RESPONSE_STATE.USER_ERROR, response
            elif response.status_code >= 400 and response.status_code < 500:
                return RESPONSE_STATE.REQUEST_ERRORs, response
        except Exception as e:
            print(e.message)
        return RESPONSE_STATE.OTHER_ERROR, response
    
    def health_check(self):
        """ Checking the health of the email conponent in sendgrid service """
        url = self.config['STATUS_URL']
        EMAIL_SERVICE_COMPONENT_NAME = self.config['COMPONENT_NAME']
        response = requests.get(url)
        if response.status_code >= 200 and response.status_code < 300:
            ser_components = response.json().get('components', [])
            comps = list(filter(lambda e: e.get('name', None) == EMAIL_SERVICE_COMPONENT_NAME, ser_components))
            if len(comps) >= 1:
                # pprint(comps)
                comp = comps[0]
                if comp.get('status', None) == 'operational':
                    return True
        return False
if __name__ == "__main__":

    message = Mail(
        from_email='ahmedkammorah@trendy.com',
        to_emails='ahmedkammorah@gmail.com',
        subject='Sending with SendGrid is Fun',
        html_content='<strong>and easy to do anywhere, even with Python</strong>')
    ep = EPSendGridConnector()
    # ep.send_email(message)
    print(ep.health_check())
