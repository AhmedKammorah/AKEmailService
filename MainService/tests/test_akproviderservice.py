# -*- coding: utf-8 -*-
# @Author: Ahmed kammorah
# @Date:   2019-04-05 23:37:23
# @Last Modified by:   Ahmed kammorah
# @Last Modified time: 2019-04-06 14:14:46
import unittest
from MainService.main.ak_main_email_service import AKProviderService

class TESTAKProviderService(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('Setup class')

    @classmethod
    def tearDownClass(cls):
        print('Tear down class')

    def setUp(self):
        print('setup')
        self.ser1 = AKProviderService('sendgrid')
    def tearDown(self):
        print('teardown')

    def test_name(self):
        self.assertEqual(self.ser1.name , 'sendgrid')
        self.assertIsNotNone(self.ser1.connector)
        

    def test_connector(self):
        pass



if __name__== "__main__":
    unittest.main()