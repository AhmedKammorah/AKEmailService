# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ak_email_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ak_email_service.proto',
  package='AKEmailServiceRPC',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x16\x61k_email_service.proto\x12\x11\x41KEmailServiceRPC\"[\n\x13\x45mailMessageRequest\x12\x12\n\nfrom_email\x18\x01 \x01(\t\x12\x0f\n\x07subject\x18\x02 \x01(\t\x12\x0c\n\x04\x62ody\x18\x03 \x01(\t\x12\x11\n\tto_emails\x18\x04 \x03(\t\"/\n\x0cRersponseMsg\x12\x0e\n\x06status\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t2j\n\x11\x41KEmailServiceRPC\x12U\n\nsend_email\x12&.AKEmailServiceRPC.EmailMessageRequest\x1a\x1f.AKEmailServiceRPC.RersponseMsgb\x06proto3')
)




_EMAILMESSAGEREQUEST = _descriptor.Descriptor(
  name='EmailMessageRequest',
  full_name='AKEmailServiceRPC.EmailMessageRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='from_email', full_name='AKEmailServiceRPC.EmailMessageRequest.from_email', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='subject', full_name='AKEmailServiceRPC.EmailMessageRequest.subject', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='body', full_name='AKEmailServiceRPC.EmailMessageRequest.body', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='to_emails', full_name='AKEmailServiceRPC.EmailMessageRequest.to_emails', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=45,
  serialized_end=136,
)


_RERSPONSEMSG = _descriptor.Descriptor(
  name='RersponseMsg',
  full_name='AKEmailServiceRPC.RersponseMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='AKEmailServiceRPC.RersponseMsg.status', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='AKEmailServiceRPC.RersponseMsg.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=138,
  serialized_end=185,
)

DESCRIPTOR.message_types_by_name['EmailMessageRequest'] = _EMAILMESSAGEREQUEST
DESCRIPTOR.message_types_by_name['RersponseMsg'] = _RERSPONSEMSG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EmailMessageRequest = _reflection.GeneratedProtocolMessageType('EmailMessageRequest', (_message.Message,), dict(
  DESCRIPTOR = _EMAILMESSAGEREQUEST,
  __module__ = 'ak_email_service_pb2'
  # @@protoc_insertion_point(class_scope:AKEmailServiceRPC.EmailMessageRequest)
  ))
_sym_db.RegisterMessage(EmailMessageRequest)

RersponseMsg = _reflection.GeneratedProtocolMessageType('RersponseMsg', (_message.Message,), dict(
  DESCRIPTOR = _RERSPONSEMSG,
  __module__ = 'ak_email_service_pb2'
  # @@protoc_insertion_point(class_scope:AKEmailServiceRPC.RersponseMsg)
  ))
_sym_db.RegisterMessage(RersponseMsg)



_AKEMAILSERVICERPC = _descriptor.ServiceDescriptor(
  name='AKEmailServiceRPC',
  full_name='AKEmailServiceRPC.AKEmailServiceRPC',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=187,
  serialized_end=293,
  methods=[
  _descriptor.MethodDescriptor(
    name='send_email',
    full_name='AKEmailServiceRPC.AKEmailServiceRPC.send_email',
    index=0,
    containing_service=None,
    input_type=_EMAILMESSAGEREQUEST,
    output_type=_RERSPONSEMSG,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_AKEMAILSERVICERPC)

DESCRIPTOR.services_by_name['AKEmailServiceRPC'] = _AKEMAILSERVICERPC

# @@protoc_insertion_point(module_scope)
