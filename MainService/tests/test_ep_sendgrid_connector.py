# -*- coding: utf-8 -*-
# @Author: ahmedkammorah
# @Date:   2019-04-04 17:53:13
# @Last Modified by:   Ahmed kammorah
# @Last Modified time: 2019-04-06 13:19:11
import unittest

from MainService.main.ep_sendgrid_connector import EPSendGridConnector



class TestEPSparkSpotConnector(unittest.TestCase):
    def setUp(self):
        self.ep_sg = EPSendGridConnector()
    def test_send_email(self):
        pass

    def test_health_check(self):
        self.assertTrue(self.ep_sg.health_check())

if __name__ == "__main__":
    unittest.main()