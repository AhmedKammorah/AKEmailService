# -*- coding: utf-8 -*-
# @Author: Ahmed kammorah
# @Date:   2019-04-05 19:09:42
# @Last Modified by:   Ahmed kammorah
# @Last Modified time: 2019-04-08 21:19:18
import unittest
from MainService.main.ak_main_email_service import EmailMessage
from MainService.main.ep_sparkpost_connector import EPSparkPostConnector


MOCK_MESSAGE = {
            'from_email':'ahmedkammorah@kamayalabs.com',
            'to_emails':['ahmedkammorah@gmail.com'],
            'subject':'First Email subject',
            'body':'<strong>First Email body as html</strong>'
        }

class TestEPSendGridConnector(unittest.TestCase):
    def setUp(self):
        self.ep_spost = EPSparkPostConnector()
        self.msg1 = EmailMessage(to_emails=MOCK_MESSAGE['to_emails'], from_email=MOCK_MESSAGE['from_email'], subject=MOCK_MESSAGE['subject'], body=MOCK_MESSAGE['body'])
    def test_send_email(self):
        self.ep_spost.send_email(self.msg1)

    def test_health_check(self):
        self.assertTrue(self.ep_spost.health_check())


if __name__ == "__main__":
    unittest.main()

