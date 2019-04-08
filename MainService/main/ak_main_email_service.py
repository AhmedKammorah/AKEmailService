# -*- coding: utf-8 -*-
# @Author: ahmedkammorah
# @Date:   2019-04-04 15:54:42
# @Last Modified by:   Ahmed kammorah
# @Last Modified time: 2019-04-08 20:40:39

from enum import Enum 


from MainService.main.email_provider_connector import RESPONSE_STATE
from MainService.main.ak_ep_services import AKEmailServices, AKProviderService,SERVICE_STATUS, logger

class EmailMessage(object):
    def __init__(self, to_emails, from_email, subject, body):
        if to_emails == None or from_email == None:
            return None
        if len(to_emails) == 0 or len(from_email) == 0:
            return None 
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

    def __str__(self):
        return 'Eamil for subject:{} from_email:{} to_emails:{} \nbody:{}'.format(self.subject, self.from_email, self.to_emails, self.body)
    

class AKMainEmailService(AKEmailServices):
    """The Main Email service Class 

    Attributes:
        redis_util: instance of the redis util to be manger of the commancation with redis
        service_provider_list: List of email provider names
        services: map of all avaiable and registered service
    """
    def __init__(self):
        """Intiialize the Main Email service with regestering all service providers"""
        super().__init__()
   
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

    def send_email(self, email_message:EmailMessage):
        """ Sending Email messgae by picking the first avaliblae running email service Provider
        
        Args: 
            email_message: full email email_message 
        Returns: 
            response to user
        """
        if email_message == None:
            logger.error("Can't send Empty or null Email")
            return
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
