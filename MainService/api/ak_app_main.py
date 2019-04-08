# -*- coding: utf-8 -*-
# @Author: ahmedkammorah
# @Date:   2017-01-21 16:58:27
# @Last Modified by:   Ahmed kammorah
# @Last Modified time: 2019-04-08 02:14:23
from pprint import pprint
from MainService.api.ak_base_api import *
from MainService.main.ak_main_email_service import AKMainEmailService, EmailMessage

email_service = AKMainEmailService()

@app.route('/api/email', methods=['POST'])
@jwt_required()
def send_email():
    """
    ---
    tags:
        - "AKEmailServiceAPI"
    summary: "Send email API Endpoint"
    description: "Send email API Endpoint"
    operationId: "sendEmail"
    consumes:
      - "application/json"
      - "application/xml"
    produces:
      - "application/xml"
      - "application/json"
    parameters:
      - in: "body"
        name: "body"
        description: "Full email message"
        required: true
        schema:
          $ref: "#/definitions/EmailMessage"
    responses:
      405:
        description: "Invalid input"
    definitions:
      EmailMessage:
        type: "object"
        required:
        - "from_email"
        - "to_emails"
        properties:
          subject:
            type: "string"
            example: "hello"
          from_email:
            type: "string"
            example: "ahmed@trendy.com"
          to_emails:
            type: "array"
            xml:
              name: "to_emails"
              wrapped: true
            items:
              type: "string"
          body:
            type: "string"
            description: "full email body"
        xml:
          name: "EmailMessage"
        example:
          to_emails:
          - "ahmedkammorah@gmail.com"
          - "ahmedkammorah+1@gmail.com"
          from_email: "ahmed@gmail.com"
          subject: "hello"
          body: "body"
      ApiResponse:
        type: "object"
        properties:
          code:
            type: "integer"
            format: "int32"
          type:
            type: "string"
          message:
            type: "string"

    """
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