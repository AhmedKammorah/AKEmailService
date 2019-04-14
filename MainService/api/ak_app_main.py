# -*- coding: utf-8 -*-
# @Author: ahmedkammorah
# @Date:   2017-01-21 16:58:27
# @Last Modified by:   Ahmed kammorah
# @Last Modified time: 2019-04-15 00:48:55
from pprint import pprint
from MainService.api.ak_base_api import *
from MainService.main.ak_main_email_service import AKMainEmailService, EmailMessage

email_service = AKMainEmailService()

@app.route('/api/email', methods=['POST'])
@jwt_required()
def send_email():
    email_message = request.get_json()
    pprint(email_message)

    msg = EmailMessage(to_emails=email_message['to_emails'], from_email=email_message['from_email'], subject=email_message['subject'], body=email_message['body'])
    if msg == None:
        return app.make_response(("one of the required feilds is not fullfiled", 400))    
    
    email_service.send_email(msg)
    app.logger.debug("Sending email by email service")
    return app.make_response(("Successfully send email", 200))
        



if __name__== "__main__":
    app.run(debug=True, host='0.0.0.0')