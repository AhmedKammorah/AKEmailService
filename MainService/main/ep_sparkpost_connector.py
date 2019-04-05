# -*- coding: utf-8 -*-
# @Author: ahmedkammorah
# @Date:   2019-04-04 11:24:11
# @Last Modified by:   Ahmed kammorah
# @Last Modified time: 2019-04-05 19:20:40

SPARTPOST_API_KEY = "45b036dbdb872be184355255c0e81293ecd94a12"
EMAIL_SERVICE_COMPONENT_NAME = "Transmissions API"

from EmailProviderConnector import EmailProviderConnector
from sparkpost import SparkPost


class EPSparkPostConnector(EmailProviderConnector):
    """
        
    """
    def __init__(self):
        self.sparky = SparkPost(SPARTPOST_API_KEY)

    def send_email(self, message):
    
        try:
            response = self.sparky.transmissions.send(
                                            use_sandbox = True,
                                            recipients = ['developers+python@sparkpost.com'],
                                            html = '<html><body><p>Testing SparkPost - the most awesomest email service!</p></body></html>',
                                            from_email = 'testing@sparkpostbox.com',
                                            subject = 'Oh hey')

            print(response.status_code)
            if response.status_code == 200 or response.status_code == 202:
                return RESPONSE_STATE.OK, response
            elif response.status_code >= 500:
                return RESPONSE_STATE.SERVICE_ERROR, response
            elif response.status_code == 429:
                return RESPONSE_STATE.OVERRATE_ERROR, response
            elif response.status_code in [401, 403, 404, 405]:
                # service error
                # request problem
                # 
            elif response.status_code >= 400 and response.status_code < 500:
                return RESPONSE_STATE.USER_ERROR, response
        except Exception as e:
            print(e.message)
        return RESPONSE_STATE.OTHER_ERROR, response

    def health_check(self):
        """ Checking the health of the email conponent in sendgrid service 
        """
        url = SERVICE_STATUS_URL
        response = requests.request("GET", url)
        if response.status_code >= 200 and response.status_code < 300:
            ser_components = response.json().get('components', [])
            # pprint(ser_components)
            comps = list(filter(lambda e: e.get('name', None) == EMAIL_SERVICE_COMPONENT_NAME, ser_components))
            if len(comps) > 1
                pprint(comps)
                comp = comps[0]
                if comp.get('status', None) == 'operational':
                    return True
        return False


if __name__ == "__main__":
