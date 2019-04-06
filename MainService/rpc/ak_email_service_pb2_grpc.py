# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import ak_email_service_pb2 as ak__email__service__pb2


class AKEmailServiceRPCStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.send_email = channel.unary_unary(
        '/AKEmailServiceRPC.AKEmailServiceRPC/send_email',
        request_serializer=ak__email__service__pb2.EmailMessageRequest.SerializeToString,
        response_deserializer=ak__email__service__pb2.RersponseMsg.FromString,
        )


class AKEmailServiceRPCServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def send_email(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_AKEmailServiceRPCServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'send_email': grpc.unary_unary_rpc_method_handler(
          servicer.send_email,
          request_deserializer=ak__email__service__pb2.EmailMessageRequest.FromString,
          response_serializer=ak__email__service__pb2.RersponseMsg.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'AKEmailServiceRPC.AKEmailServiceRPC', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
