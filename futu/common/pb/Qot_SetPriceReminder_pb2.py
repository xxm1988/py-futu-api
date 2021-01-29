# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Qot_SetPriceReminder.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import Common_pb2 as Common__pb2
import Qot_Common_pb2 as Qot__Common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='Qot_SetPriceReminder.proto',
  package='Qot_SetPriceReminder',
  syntax='proto2',
  serialized_pb=_b('\n\x1aQot_SetPriceReminder.proto\x12\x14Qot_SetPriceReminder\x1a\x0c\x43ommon.proto\x1a\x10Qot_Common.proto\"\x7f\n\x03\x43\x32S\x12&\n\x08security\x18\x01 \x02(\x0b\x32\x14.Qot_Common.Security\x12\n\n\x02op\x18\x02 \x02(\x05\x12\x0b\n\x03key\x18\x03 \x01(\x03\x12\x0c\n\x04type\x18\x04 \x01(\x05\x12\x0c\n\x04\x66req\x18\x07 \x01(\x05\x12\r\n\x05value\x18\x05 \x01(\x01\x12\x0c\n\x04note\x18\x06 \x01(\t\"\x12\n\x03S2C\x12\x0b\n\x03key\x18\x01 \x02(\x03\"1\n\x07Request\x12&\n\x03\x63\x32s\x18\x01 \x02(\x0b\x32\x19.Qot_SetPriceReminder.C2S\"j\n\x08Response\x12\x15\n\x07retType\x18\x01 \x02(\x05:\x04-400\x12\x0e\n\x06retMsg\x18\x02 \x01(\t\x12\x0f\n\x07\x65rrCode\x18\x03 \x01(\x05\x12&\n\x03s2c\x18\x04 \x01(\x0b\x32\x19.Qot_SetPriceReminder.S2C*\xe9\x01\n\x12SetPriceReminderOp\x12\x1e\n\x1aSetPriceReminderOp_Unknown\x10\x00\x12\x1a\n\x16SetPriceReminderOp_Add\x10\x01\x12\x1a\n\x16SetPriceReminderOp_Del\x10\x02\x12\x1d\n\x19SetPriceReminderOp_Enable\x10\x03\x12\x1e\n\x1aSetPriceReminderOp_Disable\x10\x04\x12\x1d\n\x19SetPriceReminderOp_Modify\x10\x05\x12\x1d\n\x19SetPriceReminderOp_DelAll\x10\x06\x42J\n\x13\x63om.futu.openapi.pbZ3github.com/futuopen/ftapi4go/pb/qotsetpricereminder')
  ,
  dependencies=[Common__pb2.DESCRIPTOR,Qot__Common__pb2.DESCRIPTOR,])

_SETPRICEREMINDEROP = _descriptor.EnumDescriptor(
  name='SetPriceReminderOp',
  full_name='Qot_SetPriceReminder.SetPriceReminderOp',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SetPriceReminderOp_Unknown', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SetPriceReminderOp_Add', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SetPriceReminderOp_Del', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SetPriceReminderOp_Enable', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SetPriceReminderOp_Disable', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SetPriceReminderOp_Modify', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SetPriceReminderOp_DelAll', index=6, number=6,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=393,
  serialized_end=626,
)
_sym_db.RegisterEnumDescriptor(_SETPRICEREMINDEROP)

SetPriceReminderOp = enum_type_wrapper.EnumTypeWrapper(_SETPRICEREMINDEROP)
SetPriceReminderOp_Unknown = 0
SetPriceReminderOp_Add = 1
SetPriceReminderOp_Del = 2
SetPriceReminderOp_Enable = 3
SetPriceReminderOp_Disable = 4
SetPriceReminderOp_Modify = 5
SetPriceReminderOp_DelAll = 6



_C2S = _descriptor.Descriptor(
  name='C2S',
  full_name='Qot_SetPriceReminder.C2S',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='security', full_name='Qot_SetPriceReminder.C2S.security', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='op', full_name='Qot_SetPriceReminder.C2S.op', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='key', full_name='Qot_SetPriceReminder.C2S.key', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='Qot_SetPriceReminder.C2S.type', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='freq', full_name='Qot_SetPriceReminder.C2S.freq', index=4,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='Qot_SetPriceReminder.C2S.value', index=5,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='note', full_name='Qot_SetPriceReminder.C2S.note', index=6,
      number=6, type=9, cpp_type=9, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=84,
  serialized_end=211,
)


_S2C = _descriptor.Descriptor(
  name='S2C',
  full_name='Qot_SetPriceReminder.S2C',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='Qot_SetPriceReminder.S2C.key', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=213,
  serialized_end=231,
)


_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='Qot_SetPriceReminder.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='c2s', full_name='Qot_SetPriceReminder.Request.c2s', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=233,
  serialized_end=282,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='Qot_SetPriceReminder.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='retType', full_name='Qot_SetPriceReminder.Response.retType', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=True, default_value=-400,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='retMsg', full_name='Qot_SetPriceReminder.Response.retMsg', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='errCode', full_name='Qot_SetPriceReminder.Response.errCode', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='s2c', full_name='Qot_SetPriceReminder.Response.s2c', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=284,
  serialized_end=390,
)

_C2S.fields_by_name['security'].message_type = Qot__Common__pb2._SECURITY
_REQUEST.fields_by_name['c2s'].message_type = _C2S
_RESPONSE.fields_by_name['s2c'].message_type = _S2C
DESCRIPTOR.message_types_by_name['C2S'] = _C2S
DESCRIPTOR.message_types_by_name['S2C'] = _S2C
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
DESCRIPTOR.enum_types_by_name['SetPriceReminderOp'] = _SETPRICEREMINDEROP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

C2S = _reflection.GeneratedProtocolMessageType('C2S', (_message.Message,), dict(
  DESCRIPTOR = _C2S,
  __module__ = 'Qot_SetPriceReminder_pb2'
  # @@protoc_insertion_point(class_scope:Qot_SetPriceReminder.C2S)
  ))
_sym_db.RegisterMessage(C2S)

S2C = _reflection.GeneratedProtocolMessageType('S2C', (_message.Message,), dict(
  DESCRIPTOR = _S2C,
  __module__ = 'Qot_SetPriceReminder_pb2'
  # @@protoc_insertion_point(class_scope:Qot_SetPriceReminder.S2C)
  ))
_sym_db.RegisterMessage(S2C)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), dict(
  DESCRIPTOR = _REQUEST,
  __module__ = 'Qot_SetPriceReminder_pb2'
  # @@protoc_insertion_point(class_scope:Qot_SetPriceReminder.Request)
  ))
_sym_db.RegisterMessage(Request)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSE,
  __module__ = 'Qot_SetPriceReminder_pb2'
  # @@protoc_insertion_point(class_scope:Qot_SetPriceReminder.Response)
  ))
_sym_db.RegisterMessage(Response)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\023com.futu.openapi.pbZ3github.com/futuopen/ftapi4go/pb/qotsetpricereminder'))
# @@protoc_insertion_point(module_scope)
