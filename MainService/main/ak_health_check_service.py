# -*- coding: utf-8 -*-
# @Author: Ahmed kammorah
# @Date:   2019-04-06 11:10:08
# @Last Modified by:   Ahmed kammorah
# @Last Modified time: 2019-04-06 15:28:06

import time

from MainService.main.email_provider_connector import RESPONSE_STATE
from MainService.main.ak_ep_services import AKEmailServices, AKProviderService,SERVICE_STATUS, logger

TIME_INTERVAL = 50
class AKHealthCheckService(AKEmailServices):
    """
    """


    def __init__(self):
        """Initialize the health check service"""
        super().__init__()

    def start(self):
        """Starting the infinte loop of checking the service running ot not
        use this service to keep track of the email service providers running status 
        keep checking the service and store the service status into redis to be used by Email servide 
        """
        logger.info("Start backgroud health checking service")
        while(True):
            logger.info("Start Round of health_check for all registered services")
            for ser_name in self._service_provider_list:
                self._update_serv_status(ser_name)
            
            time.sleep(TIME_INTERVAL)

    def _update_serv_status(self, ser_name):
        ser = self.services.get(ser_name, None)
        if ser:
            isUp = ser.connector.health_check()
            current_status = self.redis_util.get_ser_status(ser_name)
            if current_status == SERVICE_STATUS.OVERLIMIT.value:
                # TODO: check the rate limit reset time and if we pass it then reset the service
                pass
            if isUp:
                logger.info("Service for connector {} is UP and running".format(ser_name))
                self.redis_util.set_ser_status(ser_name, SERVICE_STATUS.UP.value)
            else:
                logger.info("Service for connector {} is DOWN".format(ser_name))
                self.redis_util.set_ser_status(ser_name, SERVICE_STATUS.DOWN.value)
                
if __name__ == "__main__":
    AKHealthCheckService().start()