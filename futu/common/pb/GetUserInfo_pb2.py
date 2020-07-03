<<<<<<< HEAD
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: GetUserInfo.proto

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


DESCRIPTOR = _descriptor.FileDescriptor(
  name='GetUserInfo.proto',
  package='GetUserInfo',
  syntax='proto2',
  serialized_pb=_b('\n\x11GetUserInfo.proto\x12\x0bGetUserInfo\x1a\x0c\x43ommon.proto\"\x13\n\x03\x43\x32S\x12\x0c\n\x04\x66lag\x18\x02 \x01(\x05\"\x82\x02\n\x03S2C\x12\x10\n\x08nickName\x18\x01 \x01(\t\x12\x11\n\tavatarUrl\x18\x02 \x01(\t\x12\x10\n\x08\x61piLevel\x18\x03 \x01(\t\x12\x12\n\nhkQotRight\x18\x04 \x01(\x05\x12\x12\n\nusQotRight\x18\x05 \x01(\x05\x12\x12\n\ncnQotRight\x18\x06 \x01(\x05\x12\x1d\n\x15isNeedAgreeDisclaimer\x18\x07 \x01(\x08\x12\x0e\n\x06userID\x18\x08 \x01(\x03\x12\x12\n\nupdateType\x18\t \x01(\x05\x12\x0e\n\x06webKey\x18\n \x01(\t\x12\x18\n\x10hkOptionQotRight\x18\x0b \x01(\x05\x12\x1b\n\x13hasUSOptionQotRight\x18\x0c \x01(\x08\"(\n\x07Request\x12\x1d\n\x03\x63\x32s\x18\x01 \x02(\x0b\x32\x10.GetUserInfo.C2S\"a\n\x08Response\x12\x15\n\x07retType\x18\x01 \x02(\x05:\x04-400\x12\x0e\n\x06retMsg\x18\x02 \x01(\t\x12\x0f\n\x07\x65rrCode\x18\x03 \x01(\x05\x12\x1d\n\x03s2c\x18\x04 \x01(\x0b\x32\x10.GetUserInfo.S2C*N\n\nUpdateType\x12\x13\n\x0fUpdateType_None\x10\x00\x12\x15\n\x11UpdateType_Advice\x10\x01\x12\x14\n\x10UpdateType_Force\x10\x02*\xae\x01\n\rUserInfoField\x12\x17\n\x13UserInfoField_Basic\x10\x01\x12\x15\n\x11UserInfoField_API\x10\x02\x12\x1a\n\x16UserInfoField_QotRight\x10\x04\x12\x1c\n\x18UserInfoField_Disclaimer\x10\x08\x12\x18\n\x14UserInfoField_Update\x10\x10\x12\x19\n\x14UserInfoField_WebKey\x10\x80\x10\x42\x15\n\x13\x63om.futu.openapi.pb')
  ,
  dependencies=[Common__pb2.DESCRIPTOR,])

_UPDATETYPE = _descriptor.EnumDescriptor(
  name='UpdateType',
  full_name='GetUserInfo.UpdateType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UpdateType_None', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UpdateType_Advice', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UpdateType_Force', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=471,
  serialized_end=549,
)
_sym_db.RegisterEnumDescriptor(_UPDATETYPE)

UpdateType = enum_type_wrapper.EnumTypeWrapper(_UPDATETYPE)
_USERINFOFIELD = _descriptor.EnumDescriptor(
  name='UserInfoField',
  full_name='GetUserInfo.UserInfoField',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UserInfoField_Basic', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UserInfoField_API', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UserInfoField_QotRight', index=2, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UserInfoField_Disclaimer', index=3, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UserInfoField_Update', index=4, number=16,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UserInfoField_WebKey', index=5, number=2048,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=552,
  serialized_end=726,
)
_sym_db.RegisterEnumDescriptor(_USERINFOFIELD)

UserInfoField = enum_type_wrapper.EnumTypeWrapper(_USERINFOFIELD)
UpdateType_None = 0
UpdateType_Advice = 1
UpdateType_Force = 2
UserInfoField_Basic = 1
UserInfoField_API = 2
UserInfoField_QotRight = 4
UserInfoField_Disclaimer = 8
UserInfoField_Update = 16
UserInfoField_WebKey = 2048



_C2S = _descriptor.Descriptor(
  name='C2S',
  full_name='GetUserInfo.C2S',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='flag', full_name='GetUserInfo.C2S.flag', index=0,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=48,
  serialized_end=67,
)


_S2C = _descriptor.Descriptor(
  name='S2C',
  full_name='GetUserInfo.S2C',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nickName', full_name='GetUserInfo.S2C.nickName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='avatarUrl', full_name='GetUserInfo.S2C.avatarUrl', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='apiLevel', full_name='GetUserInfo.S2C.apiLevel', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hkQotRight', full_name='GetUserInfo.S2C.hkQotRight', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='usQotRight', full_name='GetUserInfo.S2C.usQotRight', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cnQotRight', full_name='GetUserInfo.S2C.cnQotRight', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='isNeedAgreeDisclaimer', full_name='GetUserInfo.S2C.isNeedAgreeDisclaimer', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='userID', full_name='GetUserInfo.S2C.userID', index=7,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='updateType', full_name='GetUserInfo.S2C.updateType', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='webKey', full_name='GetUserInfo.S2C.webKey', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hkOptionQotRight', full_name='GetUserInfo.S2C.hkOptionQotRight', index=10,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hasUSOptionQotRight', full_name='GetUserInfo.S2C.hasUSOptionQotRight', index=11,
      number=12, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=70,
  serialized_end=328,
)


_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='GetUserInfo.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='c2s', full_name='GetUserInfo.Request.c2s', index=0,
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
  serialized_start=330,
  serialized_end=370,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='GetUserInfo.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='retType', full_name='GetUserInfo.Response.retType', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=True, default_value=-400,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='retMsg', full_name='GetUserInfo.Response.retMsg', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='errCode', full_name='GetUserInfo.Response.errCode', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='s2c', full_name='GetUserInfo.Response.s2c', index=3,
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
  serialized_start=372,
  serialized_end=469,
)

_REQUEST.fields_by_name['c2s'].message_type = _C2S
_RESPONSE.fields_by_name['s2c'].message_type = _S2C
DESCRIPTOR.message_types_by_name['C2S'] = _C2S
DESCRIPTOR.message_types_by_name['S2C'] = _S2C
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
DESCRIPTOR.enum_types_by_name['UpdateType'] = _UPDATETYPE
DESCRIPTOR.enum_types_by_name['UserInfoField'] = _USERINFOFIELD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

C2S = _reflection.GeneratedProtocolMessageType('C2S', (_message.Message,), dict(
  DESCRIPTOR = _C2S,
  __module__ = 'GetUserInfo_pb2'
  # @@protoc_insertion_point(class_scope:GetUserInfo.C2S)
  ))
_sym_db.RegisterMessage(C2S)

S2C = _reflection.GeneratedProtocolMessageType('S2C', (_message.Message,), dict(
  DESCRIPTOR = _S2C,
  __module__ = 'GetUserInfo_pb2'
  # @@protoc_insertion_point(class_scope:GetUserInfo.S2C)
  ))
_sym_db.RegisterMessage(S2C)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), dict(
  DESCRIPTOR = _REQUEST,
  __module__ = 'GetUserInfo_pb2'
  # @@protoc_insertion_point(class_scope:GetUserInfo.Request)
  ))
_sym_db.RegisterMessage(Request)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSE,
  __module__ = 'GetUserInfo_pb2'
  # @@protoc_insertion_point(class_scope:GetUserInfo.Response)
  ))
_sym_db.RegisterMessage(Response)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\023com.futu.openapi.pb'))
# @@protoc_insertion_point(module_scope)
=======
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: GetUserInfo.proto

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


DESCRIPTOR = _descriptor.FileDescriptor(
  name='GetUserInfo.proto',
  package='GetUserInfo',
  syntax='proto2',
  serialized_pb=_b('\n\x11GetUserInfo.proto\x12\x0bGetUserInfo\x1a\x0c\x43ommon.proto\"\x13\n\x03\x43\x32S\x12\x0c\n\x04\x66lag\x18\x02 \x01(\x05\"\xc6\x02\n\x03S2C\x12\x10\n\x08nickName\x18\x01 \x01(\t\x12\x11\n\tavatarUrl\x18\x02 \x01(\t\x12\x10\n\x08\x61piLevel\x18\x03 \x01(\t\x12\x12\n\nhkQotRight\x18\x04 \x01(\x05\x12\x12\n\nusQotRight\x18\x05 \x01(\x05\x12\x12\n\ncnQotRight\x18\x06 \x01(\x05\x12\x1d\n\x15isNeedAgreeDisclaimer\x18\x07 \x01(\x08\x12\x0e\n\x06userID\x18\x08 \x01(\x03\x12\x12\n\nupdateType\x18\t \x01(\x05\x12\x0e\n\x06webKey\x18\n \x01(\t\x12\x18\n\x10hkOptionQotRight\x18\x0b \x01(\x05\x12\x1b\n\x13hasUSOptionQotRight\x18\x0c \x01(\x08\x12\x18\n\x10hkFutureQotRight\x18\r \x01(\x05\x12\x10\n\x08subQuota\x18\x0e \x01(\x05\x12\x16\n\x0ehistoryKLQuota\x18\x0f \x01(\x05\"(\n\x07Request\x12\x1d\n\x03\x63\x32s\x18\x01 \x02(\x0b\x32\x10.GetUserInfo.C2S\"a\n\x08Response\x12\x15\n\x07retType\x18\x01 \x02(\x05:\x04-400\x12\x0e\n\x06retMsg\x18\x02 \x01(\t\x12\x0f\n\x07\x65rrCode\x18\x03 \x01(\x05\x12\x1d\n\x03s2c\x18\x04 \x01(\x0b\x32\x10.GetUserInfo.S2C*N\n\nUpdateType\x12\x13\n\x0fUpdateType_None\x10\x00\x12\x15\n\x11UpdateType_Advice\x10\x01\x12\x14\n\x10UpdateType_Force\x10\x02*\xae\x01\n\rUserInfoField\x12\x17\n\x13UserInfoField_Basic\x10\x01\x12\x15\n\x11UserInfoField_API\x10\x02\x12\x1a\n\x16UserInfoField_QotRight\x10\x04\x12\x1c\n\x18UserInfoField_Disclaimer\x10\x08\x12\x18\n\x14UserInfoField_Update\x10\x10\x12\x19\n\x14UserInfoField_WebKey\x10\x80\x10\x42\x15\n\x13\x63om.futu.openapi.pb')
  ,
  dependencies=[Common__pb2.DESCRIPTOR,])

_UPDATETYPE = _descriptor.EnumDescriptor(
  name='UpdateType',
  full_name='GetUserInfo.UpdateType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UpdateType_None', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UpdateType_Advice', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UpdateType_Force', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=539,
  serialized_end=617,
)
_sym_db.RegisterEnumDescriptor(_UPDATETYPE)

UpdateType = enum_type_wrapper.EnumTypeWrapper(_UPDATETYPE)
_USERINFOFIELD = _descriptor.EnumDescriptor(
  name='UserInfoField',
  full_name='GetUserInfo.UserInfoField',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UserInfoField_Basic', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UserInfoField_API', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UserInfoField_QotRight', index=2, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UserInfoField_Disclaimer', index=3, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UserInfoField_Update', index=4, number=16,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UserInfoField_WebKey', index=5, number=2048,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=620,
  serialized_end=794,
)
_sym_db.RegisterEnumDescriptor(_USERINFOFIELD)

UserInfoField = enum_type_wrapper.EnumTypeWrapper(_USERINFOFIELD)
UpdateType_None = 0
UpdateType_Advice = 1
UpdateType_Force = 2
UserInfoField_Basic = 1
UserInfoField_API = 2
UserInfoField_QotRight = 4
UserInfoField_Disclaimer = 8
UserInfoField_Update = 16
UserInfoField_WebKey = 2048



_C2S = _descriptor.Descriptor(
  name='C2S',
  full_name='GetUserInfo.C2S',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='flag', full_name='GetUserInfo.C2S.flag', index=0,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=48,
  serialized_end=67,
)


_S2C = _descriptor.Descriptor(
  name='S2C',
  full_name='GetUserInfo.S2C',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nickName', full_name='GetUserInfo.S2C.nickName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='avatarUrl', full_name='GetUserInfo.S2C.avatarUrl', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='apiLevel', full_name='GetUserInfo.S2C.apiLevel', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hkQotRight', full_name='GetUserInfo.S2C.hkQotRight', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='usQotRight', full_name='GetUserInfo.S2C.usQotRight', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cnQotRight', full_name='GetUserInfo.S2C.cnQotRight', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='isNeedAgreeDisclaimer', full_name='GetUserInfo.S2C.isNeedAgreeDisclaimer', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='userID', full_name='GetUserInfo.S2C.userID', index=7,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='updateType', full_name='GetUserInfo.S2C.updateType', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='webKey', full_name='GetUserInfo.S2C.webKey', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hkOptionQotRight', full_name='GetUserInfo.S2C.hkOptionQotRight', index=10,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hasUSOptionQotRight', full_name='GetUserInfo.S2C.hasUSOptionQotRight', index=11,
      number=12, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hkFutureQotRight', full_name='GetUserInfo.S2C.hkFutureQotRight', index=12,
      number=13, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='subQuota', full_name='GetUserInfo.S2C.subQuota', index=13,
      number=14, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='historyKLQuota', full_name='GetUserInfo.S2C.historyKLQuota', index=14,
      number=15, type=5, cpp_type=1, label=1,
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
  serialized_start=70,
  serialized_end=396,
)


_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='GetUserInfo.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='c2s', full_name='GetUserInfo.Request.c2s', index=0,
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
  serialized_start=398,
  serialized_end=438,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='GetUserInfo.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='retType', full_name='GetUserInfo.Response.retType', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=True, default_value=-400,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='retMsg', full_name='GetUserInfo.Response.retMsg', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='errCode', full_name='GetUserInfo.Response.errCode', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='s2c', full_name='GetUserInfo.Response.s2c', index=3,
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
  serialized_start=440,
  serialized_end=537,
)

_REQUEST.fields_by_name['c2s'].message_type = _C2S
_RESPONSE.fields_by_name['s2c'].message_type = _S2C
DESCRIPTOR.message_types_by_name['C2S'] = _C2S
DESCRIPTOR.message_types_by_name['S2C'] = _S2C
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
DESCRIPTOR.enum_types_by_name['UpdateType'] = _UPDATETYPE
DESCRIPTOR.enum_types_by_name['UserInfoField'] = _USERINFOFIELD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

C2S = _reflection.GeneratedProtocolMessageType('C2S', (_message.Message,), dict(
  DESCRIPTOR = _C2S,
  __module__ = 'GetUserInfo_pb2'
  # @@protoc_insertion_point(class_scope:GetUserInfo.C2S)
  ))
_sym_db.RegisterMessage(C2S)

S2C = _reflection.GeneratedProtocolMessageType('S2C', (_message.Message,), dict(
  DESCRIPTOR = _S2C,
  __module__ = 'GetUserInfo_pb2'
  # @@protoc_insertion_point(class_scope:GetUserInfo.S2C)
  ))
_sym_db.RegisterMessage(S2C)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), dict(
  DESCRIPTOR = _REQUEST,
  __module__ = 'GetUserInfo_pb2'
  # @@protoc_insertion_point(class_scope:GetUserInfo.Request)
  ))
_sym_db.RegisterMessage(Request)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSE,
  __module__ = 'GetUserInfo_pb2'
  # @@protoc_insertion_point(class_scope:GetUserInfo.Response)
  ))
_sym_db.RegisterMessage(Response)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\023com.futu.openapi.pb'))
# @@protoc_insertion_point(module_scope)
>>>>>>> b4d5a0dfc64df08e085462d5fb0b025e83bad5f8
