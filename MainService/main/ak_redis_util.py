# -*- coding: utf-8 -*-
# @Author: ahmedkammorah
# @Date:   2019-04-04 21:44:27
# @Last Modified by:   Ahmed kammorah
# @Last Modified time: 2019-04-06 15:09:38
import redis 
from MainService.config.config import REDIS_PORT, REDIS_HOST
class AKRedisUtil(object):

    def __init__(self):
        self.red = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0)
    
    def getService(self):
        pass

    def get_ser_status(self, ser_name):
        key = f'{ser_name}:status'
        status = self.red.get(key)
        if status != None:
            return status.decode("utf-8") 
        return None
    def set_ser_status(self, ser_name, state):
        key = f'{ser_name}:status'
        return self.red.set(key, state)    

    def get_ser_reset_time(self, ser_name):
        key = f'{ser_name}:resettime'
        status = self.red.get(key)
        if status != None:
            return status.decode("utf-8") 
        return None
    def set_ser_reset_time(self, ser_name, state):
        key = f'{ser_name}:resettime'
        return self.red.set(key, state) 
            
if __name__ == "__main__":
    red = AKRedisUtil()
    # print(red.set_ser_status('ahmed', 'AAAA'))
    print(red.get_ser_status('ahmed'))