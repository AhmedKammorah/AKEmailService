# -*- coding: utf-8 -*-
# @Author: Ahmed kammorah
# @Date:   2019-04-06 23:49:04
# @Last Modified by:   Ahmed kammorah
# @Last Modified time: 2019-04-08 02:45:26
import logging

import grpc

from ak_email_service_pb2 import EmailMessageRequest
from ak_email_service_pb2_grpc import AKEmailServiceRPCStub

from MainService.config.config import RPC_SERVER, RPC_PORT

def run():
    server_url = "{}:{}".format(RPC_SERVER, RPC_PORT)
    with grpc.insecure_channel(server_url) as channel:
        stub = AKEmailServiceRPCStub(channel) 
        msg = EmailMessageRequest(from_email="ahmed@xyz.com",subject="Hi all", body="<p>Hello form the other side</p>", to_emails=["ahmedkammorah@gmail.com","ahmedkammorah+1@gmail.com"])
        response = stub.send_email(msg)
    print("Send Eamil response {}  with status {}".format(response.message, response.status))


if __name__ == '__main__':
    logging.basicConfig()
    run()