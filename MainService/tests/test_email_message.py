# -*- coding: utf-8 -*-
# @Author: Ahmed kammorah
# @Date:   2019-04-06 00:45:19
# @Last Modified by:   Ahmed kammorah
# @Last Modified time: 2019-04-06 14:14:27
import unittest
from MainService.main.ak_main_email_service import EmailMessage

MOCK_MESSAGE = {
            'from_email':'ahmedkammorah@xyz.com',
            'to_emails':['ahmedkammorah@gmail.com'],
            'subject':'First Email subject',
            'body':'<strong>First Email body as html</strong>'
        }

class TestEamilMessage(unittest.TestCase):
    def setUp(self):
        self.msg1 = EmailMessage(to_emails=MOCK_MESSAGE['to_emails'], from_email=MOCK_MESSAGE['from_email'], subject=MOCK_MESSAGE['subject'], body=MOCK_MESSAGE['body'])

    def tearDown(slef):
        pass

    def test_to_emails(self):
        self.assertEqual(self.msg1.to_emails, MOCK_MESSAGE['to_emails'])
        self.assertGreater(len(self.msg1.to_emails), 0)
        self.assertListEqual(self.msg1.to_emails, MOCK_MESSAGE['to_emails'])