# -*- coding: utf-8 -*-
# @Author: ahmedkammorah
# @Date:   2019-04-04 11:23:35
# @Last Modified by:   Ahmed kammorah
# @Last Modified time: 2019-04-05 19:10:58

SENDGRID_API_KEY = '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'
SERVICE_STATUS_URL = "http://status.sendgrid.com/api/v2/summary.json"

EMAIL_SERVICE_COMPONENT_NAME = "Mail Sending" #"API v3"

import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from email_provider_connector import EmailProviderConnector, RESPONSE_STATE

import requests
from pprint import pprint


class EPSendGridConnector(EmailProviderConnector):

    def __init__(self):
        self.sg = SendGridAPIClient(SENDGRID_API_KEY)

    def send_email(self, message):
        """ Sending Email message by sendgrid service 

        Args:
            message: Full message 
        """
        try:
            response = self.sg.send(message)
            print(response.status_code)
            if response.status_code == 200 or response.status_code == 202:
                return RESPONSE_STATE.OK, response
            elif response.status_code >= 500:
                return RESPONSE_STATE.SERVICE_ERROR, response
            elif response.status_code == 429:
                return RESPONSE_STATE.OVERRATE_ERROR, response
            elif response.status_code >= 400 and response.status_code < 500:
                return RESPONSE_STATE.USER_ERROR, response
        except Exception as e:
            print(e.message)
        return RESPONSE_STATE.OTHER_ERROR, response
    
    def health_check(self):
        """ Checking the health of the email conponent in sendgrid service 
        """
        url = SERVICE_STATUS_URL
        response = requests.request("GET", url)
        if response.status_code >= 200 and response.status_code < 300:
            ser_components = response.json().get('components', [])
            comps = list(filter(lambda e: e.get('name', None) == EMAIL_SERVICE_COMPONENT_NAME, ser_components))
            if len(comps) > 1
                pprint(comps)
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
