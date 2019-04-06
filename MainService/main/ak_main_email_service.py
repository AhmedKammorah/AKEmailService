# -*- coding: utf-8 -*-
# @Author: ahmedkammorah
# @Date:   2019-04-04 15:54:42
# @Last Modified by:   Ahmed kammorah
# @Last Modified time: 2019-04-06 14:14:08

from enum import Enum 
from MainService.main.email_provider_connector import RESPONSE_STATE
from MainService.main.ep_sendgrid_connector import EPSendGridConnector
from MainService.main.ep_sparkpost_connector import EPSparkPostConnector

class SERVICE_STATUS(Enum):
    UP = "up"
    DOWN = "down"
    OVERLIMIT = "overlimit"

EAMIL_PROVIDER_LIST = ['sendgrid', 'sparkpost']
EMAIL_PROVIDER_CONNECTORE = {
                            'sendgrid':  EPSendGridConnector(),
                            'sparkpost': EPSparkPostConnector(),
                            }
from MainService.main.ak_redis_util import AKRedisUtil
from MainService.main.AKLogUtil.AKLogUtil import getLogger

logger = getLogger('AKMainEmailService')

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

class EmailMessage(object):
    def __init__(self, to_emails, from_email, subject, body):
        self._to_emails = to_emails
        self._from_email = from_email
        self._subject = subject
        self._body = body
    
    @property
    def to_emails(self):
        return self._to_emails
    @property
    def from_email(self):
        return self._from_email
    @property
    def subject(self):
        return self._subject
    @property
    def body(self):
        return self._body
    

class AKMainEmailService(object):
    """The Main Email service Class 

    Attributes:
        redis_util: instance of the redis util to be manger of the commancation with redis
        service_provider_list: List of email provider names
        services: map of all avaiable and registered service
    """
    def __init__(self):
        """Intiialize the Main Email service with regestering all service providers"""
        self.redis_util = AKRedisUtil() 
        self.service_provider_list = EAMIL_PROVIDER_LIST
        self.services = self._register_all_providers(self.service_provider_list)

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

    def _pick_service(self):
        """Picking the first operational service provider
        
        Args:
            
        Returns:
            AKProviderService instance of the first running provider
            OR None if there is no up and running provider
        """
        logger.debug('Start picking one of the running service provider service ')
        for ser_name in self.service_provider_list:
            status = self.redis_util.get_ser_status(ser_name)
            print(status)
            print(SERVICE_STATUS.UP.value)
            if status == SERVICE_STATUS.UP.value:
                return self.services.get(ser_name, AKProviderService(ser_name))
        logger.error("No Service Provider is up right now")
        return None

    def send_email(self, email_message):
        """ Sending Email messgae by picking the first avaliblae running email service Provider
        
        Args: 
            email_message: full email email_message 
        Returns: 
            response to user
        """
        logger.info('Start the process of Sending Eamil  email_message')
        email_ser = self._pick_service()
        if email_ser == None:
            logger.error("No Email Service Provider up and running to Use ")
            # TODO: fire slack event to notify the dev team
            # TODO: add this request to a queue for next run when there is service to use
            return
        logger.info("Start using email provider {} for sending email".format(email_ser.name))
        email_connector = email_ser.connector
        res_status, response = email_connector.send_email(email_message)
        if res_status == RESPONSE_STATE.OK:
            logger.info("Successfully sending the email by {}".format(email_ser.name))
            return  (res_status, 'success send the email')
        elif res_status == RESPONSE_STATE.USER_ERROR:
            logger.error("User email_message related error: {} when sending email by: {} provider".format(response, email_ser.name))
            return (res_status, response)
        elif res_status == RESPONSE_STATE.SERVICE_ERROR:
            # Fail over start use different provider
            logger.error("Email Service provider {} is down for now".format(email_ser.name))
            email_ser.status = SERVICE_STATUS.DOWN
            self.redis_util.set_ser_status(email_ser)
            return self.send_email(email_message)
        elif res_status == RESPONSE_STATE.OVERRATE_ERROR:
             # Fail over start use different provider
             logger.error("Email Service provider {} is overlimt for now".format(email_ser.name))
             email_ser.status = SERVICE_STATUS.OVERLIMIT
             self.redis_util.set_ser_status(email_ser)
             return self.send_email(email_message)
        elif res_status == RESPONSE_STATE.REQUEST_ERROR:
            logger.error("Request related error: {}  when sending by: {} provider".format(response, email_ser.name))
            # TODO: Notify dev team with this error by slack or push it to error topic in kafka
            return
        elif res_status == RESPONSE_STATE.OTHER_ERROR:
            logger.error("unidentified error: {} when use provider {}".format(response, email_ser.name))
            return
        return

if __name__ == "__main__":
    ak = AKMainEmailService()
