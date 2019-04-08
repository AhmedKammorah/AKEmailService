# -*- coding: utf-8 -*-
# @Author: ahmedkammorah
# @Date:   2019-04-04 17:53:13
# @Last Modified by:   Ahmed kammorah
# @Last Modified time: 2019-04-08 21:07:19
import unittest
from MainService.main.ak_main_email_service import EmailMessage
from MainService.main.ep_sendgrid_connector import EPSendGridConnector

MOCK_MESSAGE = {
            'from_email':'ahmedkammorah@xyz.com',
            'to_emails':['ahmedkammorah@gmail.com'],
            'subject':'First Email subject',
            'body':'<strong>First Email body as html</strong>'
        }

class TestEPSparkSpotConnector(unittest.TestCase):
    def setUp(self):
        self.ep_sg = EPSendGridConnector()
        self.msg1 = EmailMessage(to_emails=MOCK_MESSAGE['to_emails'], from_email=MOCK_MESSAGE['from_email'], subject=MOCK_MESSAGE['subject'], body=MOCK_MESSAGE['body'])
    
    def test_send_email(self):
        self.ep_sg.send_email(self.msg1)

    def test_health_check(self):
        self.assertTrue(self.ep_sg.health_check())

if __name__ == "__main__":
    unittest.main()