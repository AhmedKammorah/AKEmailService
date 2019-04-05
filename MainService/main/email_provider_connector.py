# -*- coding: utf-8 -*-
# @Author: ahmedkammorah
# @Date:   2019-04-04 11:25:23
# @Last Modified by:   Ahmed kammorah
# @Last Modified time: 2019-04-05 15:34:46
from enum import Enum

class RESPONSE_STATE(Enum):
    OK=1
    USER_ERROR=2
    SERVICE_ERROR=3
    OVERRATE_ERROR=3
    OTHER_ERROR=4


class EmailProviderConnector:
	def __init__(self):
		pass

	def send_email(self, email):
		pass
		
	def health_check(self):
		pass