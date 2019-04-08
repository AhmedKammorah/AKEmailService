# -*- coding: utf-8 -*-
# @Author: Ahmed kammorah
# @Date:   2019-04-06 23:39:42
# @Last Modified by:   Ahmed kammorah
# @Last Modified time: 2019-04-08 02:55:18
from concurrent import futures
import time
import logging

import grpc

from ak_email_service_pb2 import RersponseMsg
import ak_email_service_pb2_grpc

from MainService.config.config import RPC_SERVER, RPC_PORT
from MainService.main.ak_main_email_service import AKMainEmailService, EmailMessage

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class AKEmailServiceRPC(ak_email_service_pb2_grpc.AKEmailServiceRPCServicer):
    def __init__(self):
        # super().__init()
        self.email_service = AKMainEmailService()

    def send_email(self, request_email_msg, context):
        print(request_email_msg)
        email_message = EmailMessage(from_email=request_email_msg.from_email, to_emails=list(request_email_msg.to_emails), subject=request_email_msg.subject, body=request_email_msg.body)
        print("email_message: {}".format(email_message))
        status, res = self.email_service.send_email(email_message)
        return RersponseMsg(status=str(status), message=res)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    ak_email_service_pb2_grpc.add_AKEmailServiceRPCServicer_to_server(AKEmailServiceRPC(), server)
    server.add_insecure_port('[::]:{}'.format(RPC_PORT))
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    logging.basicConfig()
    serve()