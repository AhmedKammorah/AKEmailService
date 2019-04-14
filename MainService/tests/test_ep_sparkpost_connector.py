# -*- coding: utf-8 -*-
# @Author: Ahmed kammorah
# @Date:   2019-04-05 19:09:42
# @Last Modified by:   Ahmed kammorah
# @Last Modified time: 2019-04-14 23:58:51
import unittest
from unittest.mock import patch, Mock
from nose.tools import assert_is_not_none, assert_true
import json
from unittest import skipIf

from MainService.main.ak_main_email_service import EmailMessage
from MainService.main.ep_sparkpost_connector import EPSparkPostConnector

from MainService.config.config import PROD_REAL_API_SKIP

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


    @patch('MainService.main.ep_sparkpost_connector.requests.get')
    def test_health_check(self, mock_get):
        mock_get.return_value.ok = True
        mock_get.return_value.status_code = 200
        print(mock_get)
        res = self.ep_spost.health_check()
        assert_is_not_none(res)
        # self.assertTrue(res)
        
    def test_health_check_down(self):
        with patch('MainService.main.ep_sparkpost_connector.requests.get') as mock_get:
            mock_get.return_value.ok = False
            mock_get.return_value.status_code = 404
            res = self.ep_spost.health_check()
        assert_is_not_none(res)
        self.assertFalse(res)

    def test_health_check_up(self):
        with patch('MainService.main.ep_sparkpost_connector.requests.get') as mock_get:
            mock_get.return_value = Mock(ok=True)
            mock_get.return_value.status_code = 202
            with open('/app/MainService/tests/data_mocks/sparkpost_status.json') as f:
                status_json = json.loads(f.read())
            mock_get.return_value.json.return_value =  status_json
            res = self.ep_spost.health_check()
        assert_is_not_none(res)
        self.assertTrue(res)

if __name__ == "__main__":
    unittest.main()

