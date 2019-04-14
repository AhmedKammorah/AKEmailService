# -*- coding: utf-8 -*-
# @Author: ahmedkammorah
# @Date:   2019-04-04 11:23:35
# @Last Modified by:   Ahmed kammorah
# @Last Modified time: 2019-04-15 00:17:01

import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


from pprint import pprint

from MainService.main.email_provider_connector import EmailProviderConnector, RESPONSE_STATE, logger, requests
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
       logger.info("Initalize EPSendGridConnector Connector")

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
        logger.info('Start Sending Email using SendGrid')
        try:
            response = self.sg.send(message)
            logger.info('Response form sending email using sendgrid with status_code:{}'.format(response.status_code))
            print(response)
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
            # print(e.message)
            logger.error("Error in sending Email with sendgrid error:{}".format(e))
        return RESPONSE_STATE.OTHER_ERROR, None
    
if __name__ == "__main__":

    message = Mail(
        from_email='ahmedkammorah@trendy.com',
        to_emails='ahmedkammorah@gmail.com',
        subject='Sending with SendGrid is Fun',
        html_content='<strong>and easy to do anywhere, even with Python</strong>')
    ep = EPSendGridConnector()
    ep.send_email(message)
    print(ep.health_check())
