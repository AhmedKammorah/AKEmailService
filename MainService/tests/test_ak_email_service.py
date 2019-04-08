# -*- coding: utf-8 -*-
# @Author: Ahmed kammorah
# @Date:   2019-04-06 11:30:47
# @Last Modified by:   Ahmed kammorah
# @Last Modified time: 2019-04-06 14:23:49
import unittest
from MainService.main.ak_main_email_service import AKMainEmailService, EmailMessage


MOCK_MESSAGE = {
            'from_email':'ahmedkammorah@xyz.com',
            'to_emails':['ahmedkammorah@gmail.com'],
            'subject':'First Email subject',
            'body':'<strong>First Email body as html</strong>'
        }

class TESTAKEmailService(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('Setup class')

    @classmethod
    def tearDownClass(cls):
        print('Tear down class')

    def setUp(self):
        print('setup')
        self.ak_eamil_ser = AKMainEmailService()
        self.msg = EmailMessage(to_emails=MOCK_MESSAGE['to_emails'],from_email=MOCK_MESSAGE['from_email'],body=MOCK_MESSAGE['body'],subject=MOCK_MESSAGE['subject'])
        self.ser_sendgrid = self.ak_eamil_ser.services['sendgrid']
        self.ser_sparkpost = self.ak_eamil_ser.services['sparkpost']
    def tearDown(self):
        print('teardown')

    def test_main_instance(self):
        self.assertIsNotNone(self.ak_eamil_ser)
        self.assertTrue(len(self.ak_eamil_ser.services)>1)

        self.assertEqual(self.ser_sendgrid.name, 'sendgrid')
        self.assertEqual(self.ser_sendgrid.status, 'up')
        self.assertIsNotNone(self.ser_sendgrid.connector)
        
        self.assertEqual(self.ser_sparkpost.name, 'sparkpost')
        self.assertEqual(self.ser_sparkpost.status, 'up')
        self.assertIsNotNone(self.ser_sparkpost.connector)

    def test_send_eamil(self):
        res_status, response = self.ak_eamil_ser.send_email(self.msg)

if __name__== "__main__":
    unittest.main()