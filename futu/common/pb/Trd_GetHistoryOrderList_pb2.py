<<<<<<< HEAD
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Trd_GetHistoryOrderList.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import Common_pb2 as Common__pb2
import Trd_Common_pb2 as Trd__Common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='Trd_GetHistoryOrderList.proto',
  package='Trd_GetHistoryOrderList',
  syntax='proto2',
  serialized_pb=_b('\n\x1dTrd_GetHistoryOrderList.proto\x12\x17Trd_GetHistoryOrderList\x1a\x0c\x43ommon.proto\x1a\x10Trd_Common.proto\"\x81\x01\n\x03\x43\x32S\x12%\n\x06header\x18\x01 \x02(\x0b\x32\x15.Trd_Common.TrdHeader\x12\x39\n\x10\x66ilterConditions\x18\x02 \x02(\x0b\x32\x1f.Trd_Common.TrdFilterConditions\x12\x18\n\x10\x66ilterStatusList\x18\x03 \x03(\x05\"R\n\x03S2C\x12%\n\x06header\x18\x01 \x02(\x0b\x32\x15.Trd_Common.TrdHeader\x12$\n\torderList\x18\x02 \x03(\x0b\x32\x11.Trd_Common.Order\"4\n\x07Request\x12)\n\x03\x63\x32s\x18\x01 \x02(\x0b\x32\x1c.Trd_GetHistoryOrderList.C2S\"m\n\x08Response\x12\x15\n\x07retType\x18\x01 \x02(\x05:\x04-400\x12\x0e\n\x06retMsg\x18\x02 \x01(\t\x12\x0f\n\x07\x65rrCode\x18\x03 \x01(\x05\x12)\n\x03s2c\x18\x04 \x01(\x0b\x32\x1c.Trd_GetHistoryOrderList.S2CB\x15\n\x13\x63om.futu.openapi.pb')
  ,
  dependencies=[Common__pb2.DESCRIPTOR,Trd__Common__pb2.DESCRIPTOR,])




_C2S = _descriptor.Descriptor(
  name='C2S',
  full_name='Trd_GetHistoryOrderList.C2S',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='Trd_GetHistoryOrderList.C2S.header', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filterConditions', full_name='Trd_GetHistoryOrderList.C2S.filterConditions', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filterStatusList', full_name='Trd_GetHistoryOrderList.C2S.filterStatusList', index=2,
      number=3, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=91,
  serialized_end=220,
)


_S2C = _descriptor.Descriptor(
  name='S2C',
  full_name='Trd_GetHistoryOrderList.S2C',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='Trd_GetHistoryOrderList.S2C.header', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='orderList', full_name='Trd_GetHistoryOrderList.S2C.orderList', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=222,
  serialized_end=304,
)


_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='Trd_GetHistoryOrderList.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='c2s', full_name='Trd_GetHistoryOrderList.Request.c2s', index=0,
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
  serialized_start=306,
  serialized_end=358,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='Trd_GetHistoryOrderList.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='retType', full_name='Trd_GetHistoryOrderList.Response.retType', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=True, default_value=-400,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='retMsg', full_name='Trd_GetHistoryOrderList.Response.retMsg', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='errCode', full_name='Trd_GetHistoryOrderList.Response.errCode', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='s2c', full_name='Trd_GetHistoryOrderList.Response.s2c', index=3,
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
  serialized_start=360,
  serialized_end=469,
)

_C2S.fields_by_name['header'].message_type = Trd__Common__pb2._TRDHEADER
_C2S.fields_by_name['filterConditions'].message_type = Trd__Common__pb2._TRDFILTERCONDITIONS
_S2C.fields_by_name['header'].message_type = Trd__Common__pb2._TRDHEADER
_S2C.fields_by_name['orderList'].message_type = Trd__Common__pb2._ORDER
_REQUEST.fields_by_name['c2s'].message_type = _C2S
_RESPONSE.fields_by_name['s2c'].message_type = _S2C
DESCRIPTOR.message_types_by_name['C2S'] = _C2S
DESCRIPTOR.message_types_by_name['S2C'] = _S2C
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

C2S = _reflection.GeneratedProtocolMessageType('C2S', (_message.Message,), dict(
  DESCRIPTOR = _C2S,
  __module__ = 'Trd_GetHistoryOrderList_pb2'
  # @@protoc_insertion_point(class_scope:Trd_GetHistoryOrderList.C2S)
  ))
_sym_db.RegisterMessage(C2S)

S2C = _reflection.GeneratedProtocolMessageType('S2C', (_message.Message,), dict(
  DESCRIPTOR = _S2C,
  __module__ = 'Trd_GetHistoryOrderList_pb2'
  # @@protoc_insertion_point(class_scope:Trd_GetHistoryOrderList.S2C)
  ))
_sym_db.RegisterMessage(S2C)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), dict(
  DESCRIPTOR = _REQUEST,
  __module__ = 'Trd_GetHistoryOrderList_pb2'
  # @@protoc_insertion_point(class_scope:Trd_GetHistoryOrderList.Request)
  ))
_sym_db.RegisterMessage(Request)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSE,
  __module__ = 'Trd_GetHistoryOrderList_pb2'
  # @@protoc_insertion_point(class_scope:Trd_GetHistoryOrderList.Response)
  ))
_sym_db.RegisterMessage(Response)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\023com.futu.openapi.pb'))
# @@protoc_insertion_point(module_scope)
=======
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Trd_GetHistoryOrderList.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import Common_pb2 as Common__pb2
import Trd_Common_pb2 as Trd__Common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='Trd_GetHistoryOrderList.proto',
  package='Trd_GetHistoryOrderList',
  syntax='proto2',
  serialized_pb=_b('\n\x1dTrd_GetHistoryOrderList.proto\x12\x17Trd_GetHistoryOrderList\x1a\x0c\x43ommon.proto\x1a\x10Trd_Common.proto\"\x81\x01\n\x03\x43\x32S\x12%\n\x06header\x18\x01 \x02(\x0b\x32\x15.Trd_Common.TrdHeader\x12\x39\n\x10\x66ilterConditions\x18\x02 \x02(\x0b\x32\x1f.Trd_Common.TrdFilterConditions\x12\x18\n\x10\x66ilterStatusList\x18\x03 \x03(\x05\"R\n\x03S2C\x12%\n\x06header\x18\x01 \x02(\x0b\x32\x15.Trd_Common.TrdHeader\x12$\n\torderList\x18\x02 \x03(\x0b\x32\x11.Trd_Common.Order\"4\n\x07Request\x12)\n\x03\x63\x32s\x18\x01 \x02(\x0b\x32\x1c.Trd_GetHistoryOrderList.C2S\"m\n\x08Response\x12\x15\n\x07retType\x18\x01 \x02(\x05:\x04-400\x12\x0e\n\x06retMsg\x18\x02 \x01(\t\x12\x0f\n\x07\x65rrCode\x18\x03 \x01(\x05\x12)\n\x03s2c\x18\x04 \x01(\x0b\x32\x1c.Trd_GetHistoryOrderList.S2CBM\n\x13\x63om.futu.openapi.pbZ6github.com/futuopen/ftapi4go/pb/trdgethistoryorderlist')
  ,
  dependencies=[Common__pb2.DESCRIPTOR,Trd__Common__pb2.DESCRIPTOR,])




_C2S = _descriptor.Descriptor(
  name='C2S',
  full_name='Trd_GetHistoryOrderList.C2S',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='Trd_GetHistoryOrderList.C2S.header', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filterConditions', full_name='Trd_GetHistoryOrderList.C2S.filterConditions', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filterStatusList', full_name='Trd_GetHistoryOrderList.C2S.filterStatusList', index=2,
      number=3, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=91,
  serialized_end=220,
)


_S2C = _descriptor.Descriptor(
  name='S2C',
  full_name='Trd_GetHistoryOrderList.S2C',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='Trd_GetHistoryOrderList.S2C.header', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='orderList', full_name='Trd_GetHistoryOrderList.S2C.orderList', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=222,
  serialized_end=304,
)


_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='Trd_GetHistoryOrderList.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='c2s', full_name='Trd_GetHistoryOrderList.Request.c2s', index=0,
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
  serialized_start=306,
  serialized_end=358,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='Trd_GetHistoryOrderList.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='retType', full_name='Trd_GetHistoryOrderList.Response.retType', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=True, default_value=-400,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='retMsg', full_name='Trd_GetHistoryOrderList.Response.retMsg', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='errCode', full_name='Trd_GetHistoryOrderList.Response.errCode', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='s2c', full_name='Trd_GetHistoryOrderList.Response.s2c', index=3,
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
  serialized_start=360,
  serialized_end=469,
)

_C2S.fields_by_name['header'].message_type = Trd__Common__pb2._TRDHEADER
_C2S.fields_by_name['filterConditions'].message_type = Trd__Common__pb2._TRDFILTERCONDITIONS
_S2C.fields_by_name['header'].message_type = Trd__Common__pb2._TRDHEADER
_S2C.fields_by_name['orderList'].message_type = Trd__Common__pb2._ORDER
_REQUEST.fields_by_name['c2s'].message_type = _C2S
_RESPONSE.fields_by_name['s2c'].message_type = _S2C
DESCRIPTOR.message_types_by_name['C2S'] = _C2S
DESCRIPTOR.message_types_by_name['S2C'] = _S2C
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

C2S = _reflection.GeneratedProtocolMessageType('C2S', (_message.Message,), dict(
  DESCRIPTOR = _C2S,
  __module__ = 'Trd_GetHistoryOrderList_pb2'
  # @@protoc_insertion_point(class_scope:Trd_GetHistoryOrderList.C2S)
  ))
_sym_db.RegisterMessage(C2S)

S2C = _reflection.GeneratedProtocolMessageType('S2C', (_message.Message,), dict(
  DESCRIPTOR = _S2C,
  __module__ = 'Trd_GetHistoryOrderList_pb2'
  # @@protoc_insertion_point(class_scope:Trd_GetHistoryOrderList.S2C)
  ))
_sym_db.RegisterMessage(S2C)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), dict(
  DESCRIPTOR = _REQUEST,
  __module__ = 'Trd_GetHistoryOrderList_pb2'
  # @@protoc_insertion_point(class_scope:Trd_GetHistoryOrderList.Request)
  ))
_sym_db.RegisterMessage(Request)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSE,
  __module__ = 'Trd_GetHistoryOrderList_pb2'
  # @@protoc_insertion_point(class_scope:Trd_GetHistoryOrderList.Response)
  ))
_sym_db.RegisterMessage(Response)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\023com.futu.openapi.pbZ6github.com/futuopen/ftapi4go/pb/trdgethistoryorderlist'))
# @@protoc_insertion_point(module_scope)
>>>>>>> c6d8737232b7342604a2c3c8808fc22682a8b3f7
