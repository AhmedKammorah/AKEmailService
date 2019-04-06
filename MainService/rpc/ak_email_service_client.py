# -*- coding: utf-8 -*-
# @Author: Ahmed kammorah
# @Date:   2019-04-06 23:49:04
# @Last Modified by:   Ahmed kammorah
# @Last Modified time: 2019-04-07 00:57:01
import logging

import grpc

from ak_email_service_pb2 import EmailMessageRequest
from ak_email_service_pb2_grpc import AKEmailServiceRPCStub

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = AKEmailServiceRPCStub(channel) 
        msg = EmailMessageRequest(from_email="ahmed@xyz.com",subject="Hi all", body="<p>Hello form the other side</p>", to_emails=["ahmedkammorah@gmail.com","ahmedkammorah+1@gmail.com"])
        response = stub.send_email(msg)
    print("Send Eamil response {}  with status {}".format(response.message, response.status))


if __name__ == '__main__':
    logging.basicConfig()
    run()