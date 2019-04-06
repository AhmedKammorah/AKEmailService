# -*- coding: utf-8 -*-
# @Author: Ahmed kammorah
# @Date:   2019-04-06 14:19:34
# @Last Modified by:   Ahmed kammorah
# @Last Modified time: 2019-04-06 14:55:16

from enum import Enum 
from MainService.main.ak_redis_util import AKRedisUtil
from MainService.main.ep_sendgrid_connector import EPSendGridConnector
from MainService.main.ep_sparkpost_connector import EPSparkPostConnector

from MainService.main.AKLogUtil.AKLogUtil import getLogger
logger = getLogger('AKMainEmailService')


class SERVICE_STATUS(Enum):
    UP = "up"
    DOWN = "down"
    OVERLIMIT = "overlimit"

EAMIL_PROVIDER_LIST = ['sendgrid', 'sparkpost']
EMAIL_PROVIDER_CONNECTORE = {
                            'sendgrid':  EPSendGridConnector(),
                            'sparkpost': EPSparkPostConnector(),
                            }


class AKEmailServices(object):
    def __init__(self):
        """Intiialize the Main Email service with regestering all service providers"""
        self._redis_util = AKRedisUtil() 
        self._service_provider_list = EAMIL_PROVIDER_LIST
        self._services = self._register_all_providers(self.service_provider_list)

    def _register_all_providers(self, provider_names):
        """ Regestring new service for all email profider list
        Build a map and register all the AKProviderService to it 
        And Reister this email provider status to redis in memory cash to easy access 
        Args:
             provider_names: List of all eamil service providers 

        Returns:
            services: <proder_name, AKProviderService> Map of proder_name and AKProviderService
            which containe the connector, name , status and the other meta data for the service 
        """
        logger.info('Start register all service provider and ther connectors to be used to end emails')
        services = {}
        for ser_name in self.service_provider_list:
            services[ser_name] = AKProviderService(ser_name) 
            # Register the service status in redis
            self.redis_util.set_ser_status(ser_name, services[ser_name].status)
        return services
    
    @property
    def redis_util(self):
        return self._redis_util
    
    @property
    def service_provider_list(self):
        return self._service_provider_list
    
    @property
    def services(self):
        return self._services
    
class AKProviderService(object):
    def __init__(self, name):
        if name not in EAMIL_PROVIDER_LIST:
            print("This service name not has connector")
        self._name = name
        self.config = ""
        self._status = SERVICE_STATUS.DOWN.value
        self._connector = EMAIL_PROVIDER_CONNECTORE.get(self._name, None)
        if self._connector:
            if self.connector.health_check():
                self._status = SERVICE_STATUS.UP.value
      
    @property
    def connector(self):
        """Gets  Email provider connector """
        
        return self._connector
    
    @property
    def name(self):
        """Gets or sets service name. """
        return self._name
    
    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def periority(self):
        """Gets or sets service running periority."""
        return self._periority
    
    @periority.setter
    def periority(self, new_periority):
        self._periority = new_periority

    @property
    def limt(self):
        """Gets or sets service requests Limt. """
        return self._limt
    @limt.setter
    def limt(self, new_limt):
        self._limt = new_limt

    @property
    def status(self):
        """Gets or sets service running status. """
        
        return self._status

    @status.setter
    def status(self, new_status):
        self._status = new_status
