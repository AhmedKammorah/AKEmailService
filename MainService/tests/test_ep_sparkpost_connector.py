# -*- coding: utf-8 -*-
# @Author: Ahmed kammorah
# @Date:   2019-04-05 19:09:42
# @Last Modified by:   Ahmed kammorah
# @Last Modified time: 2019-04-06 14:04:39
import unittest
from MainService.main.ep_sparkpost_connector import EPSparkPostConnector


MOCK_MESSAGE = {
            'from_email':'ahmedkammorah@trendy.com',
            'to_emails':'ahmedkammorah@gmail.com',
            'subject':'Sending with SendGrid is Fun',
            'html_content':'<strong>and easy to do anywhere, even with Python</strong>'
        }

class TestEPSendGridConnector(unittest.TestCase):
    def setUp(self):
        self.ep_spost = EPSparkPostConnector()
    def test_send_email(self):
        pass

    def test_health_check(self):
        self.assertTrue(self.ep_spost.health_check())


if __name__ == "__main__":
    unittest.main()

