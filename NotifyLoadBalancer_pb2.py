# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: NotifyLoadBalancer.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='NotifyLoadBalancer.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x18NotifyLoadBalancer.proto\"5\n\x08Instance\x12\x13\n\x0binstance_id\x18\x01 \x01(\t\x12\x14\n\x0cinstance_dns\x18\x02 \x01(\t\"&\n\x13NotifyRequestResult\x12\x0f\n\x07message\x18\x01 \x01(\t2~\n\x12NotifyLoadBalancer\x12\x32\n\rStartInstance\x12\t.Instance\x1a\x14.NotifyRequestResult\"\x00\x12\x34\n\rStopInstances\x12\t.Instance\x1a\x14.NotifyRequestResult\"\x00(\x01\x62\x06proto3')
)




_INSTANCE = _descriptor.Descriptor(
  name='Instance',
  full_name='Instance',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance_id', full_name='Instance.instance_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='instance_dns', full_name='Instance.instance_dns', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=28,
  serialized_end=81,
)


_NOTIFYREQUESTRESULT = _descriptor.Descriptor(
  name='NotifyRequestResult',
  full_name='NotifyRequestResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='NotifyRequestResult.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=83,
  serialized_end=121,
)

DESCRIPTOR.message_types_by_name['Instance'] = _INSTANCE
DESCRIPTOR.message_types_by_name['NotifyRequestResult'] = _NOTIFYREQUESTRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Instance = _reflection.GeneratedProtocolMessageType('Instance', (_message.Message,), dict(
  DESCRIPTOR = _INSTANCE,
  __module__ = 'NotifyLoadBalancer_pb2'
  # @@protoc_insertion_point(class_scope:Instance)
  ))
_sym_db.RegisterMessage(Instance)

NotifyRequestResult = _reflection.GeneratedProtocolMessageType('NotifyRequestResult', (_message.Message,), dict(
  DESCRIPTOR = _NOTIFYREQUESTRESULT,
  __module__ = 'NotifyLoadBalancer_pb2'
  # @@protoc_insertion_point(class_scope:NotifyRequestResult)
  ))
_sym_db.RegisterMessage(NotifyRequestResult)



_NOTIFYLOADBALANCER = _descriptor.ServiceDescriptor(
  name='NotifyLoadBalancer',
  full_name='NotifyLoadBalancer',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=123,
  serialized_end=249,
  methods=[
  _descriptor.MethodDescriptor(
    name='StartInstance',
    full_name='NotifyLoadBalancer.StartInstance',
    index=0,
    containing_service=None,
    input_type=_INSTANCE,
    output_type=_NOTIFYREQUESTRESULT,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='StopInstances',
    full_name='NotifyLoadBalancer.StopInstances',
    index=1,
    containing_service=None,
    input_type=_INSTANCE,
    output_type=_NOTIFYREQUESTRESULT,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_NOTIFYLOADBALANCER)

DESCRIPTOR.services_by_name['NotifyLoadBalancer'] = _NOTIFYLOADBALANCER

# @@protoc_insertion_point(module_scope)
