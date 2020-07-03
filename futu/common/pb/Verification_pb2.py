<<<<<<< HEAD
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Verification.proto

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
  name='Verification.proto',
  package='Verification',
  syntax='proto2',
  serialized_pb=_b('\n\x12Verification.proto\x12\x0cVerification\x1a\x0c\x43ommon.proto\"-\n\x03\x43\x32S\x12\x0c\n\x04type\x18\x01 \x02(\x05\x12\n\n\x02op\x18\x02 \x02(\x05\x12\x0c\n\x04\x63ode\x18\x03 \x01(\t\"\x05\n\x03S2C\")\n\x07Request\x12\x1e\n\x03\x63\x32s\x18\x01 \x02(\x0b\x32\x11.Verification.C2S\"b\n\x08Response\x12\x15\n\x07retType\x18\x01 \x02(\x05:\x04-400\x12\x0e\n\x06retMsg\x18\x02 \x01(\t\x12\x0f\n\x07\x65rrCode\x18\x03 \x01(\x05\x12\x1e\n\x03s2c\x18\x04 \x01(\x0b\x32\x11.Verification.S2C*i\n\x10VerificationType\x12\x1b\n\x17VerificationType_Unknow\x10\x00\x12\x1c\n\x18VerificationType_Picture\x10\x01\x12\x1a\n\x16VerificationType_Phone\x10\x02*i\n\x0eVerificationOp\x12\x19\n\x15VerificationOp_Unknow\x10\x00\x12\x1a\n\x16VerificationOp_Request\x10\x01\x12 \n\x1cVerificationOp_InputAndLogin\x10\x02\x42\x15\n\x13\x63om.futu.openapi.pb')
  ,
  dependencies=[Common__pb2.DESCRIPTOR,])

_VERIFICATIONTYPE = _descriptor.EnumDescriptor(
  name='VerificationType',
  full_name='Verification.VerificationType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='VerificationType_Unknow', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VerificationType_Picture', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VerificationType_Phone', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=247,
  serialized_end=352,
)
_sym_db.RegisterEnumDescriptor(_VERIFICATIONTYPE)

VerificationType = enum_type_wrapper.EnumTypeWrapper(_VERIFICATIONTYPE)
_VERIFICATIONOP = _descriptor.EnumDescriptor(
  name='VerificationOp',
  full_name='Verification.VerificationOp',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='VerificationOp_Unknow', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VerificationOp_Request', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VerificationOp_InputAndLogin', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=354,
  serialized_end=459,
)
_sym_db.RegisterEnumDescriptor(_VERIFICATIONOP)

VerificationOp = enum_type_wrapper.EnumTypeWrapper(_VERIFICATIONOP)
VerificationType_Unknow = 0
VerificationType_Picture = 1
VerificationType_Phone = 2
VerificationOp_Unknow = 0
VerificationOp_Request = 1
VerificationOp_InputAndLogin = 2



_C2S = _descriptor.Descriptor(
  name='C2S',
  full_name='Verification.C2S',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='Verification.C2S.type', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='op', full_name='Verification.C2S.op', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='code', full_name='Verification.C2S.code', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=50,
  serialized_end=95,
)


_S2C = _descriptor.Descriptor(
  name='S2C',
  full_name='Verification.S2C',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=97,
  serialized_end=102,
)


_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='Verification.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='c2s', full_name='Verification.Request.c2s', index=0,
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
  serialized_start=104,
  serialized_end=145,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='Verification.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='retType', full_name='Verification.Response.retType', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=True, default_value=-400,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='retMsg', full_name='Verification.Response.retMsg', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='errCode', full_name='Verification.Response.errCode', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='s2c', full_name='Verification.Response.s2c', index=3,
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
  serialized_start=147,
  serialized_end=245,
)

_REQUEST.fields_by_name['c2s'].message_type = _C2S
_RESPONSE.fields_by_name['s2c'].message_type = _S2C
DESCRIPTOR.message_types_by_name['C2S'] = _C2S
DESCRIPTOR.message_types_by_name['S2C'] = _S2C
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
DESCRIPTOR.enum_types_by_name['VerificationType'] = _VERIFICATIONTYPE
DESCRIPTOR.enum_types_by_name['VerificationOp'] = _VERIFICATIONOP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

C2S = _reflection.GeneratedProtocolMessageType('C2S', (_message.Message,), dict(
  DESCRIPTOR = _C2S,
  __module__ = 'Verification_pb2'
  # @@protoc_insertion_point(class_scope:Verification.C2S)
  ))
_sym_db.RegisterMessage(C2S)

S2C = _reflection.GeneratedProtocolMessageType('S2C', (_message.Message,), dict(
  DESCRIPTOR = _S2C,
  __module__ = 'Verification_pb2'
  # @@protoc_insertion_point(class_scope:Verification.S2C)
  ))
_sym_db.RegisterMessage(S2C)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), dict(
  DESCRIPTOR = _REQUEST,
  __module__ = 'Verification_pb2'
  # @@protoc_insertion_point(class_scope:Verification.Request)
  ))
_sym_db.RegisterMessage(Request)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSE,
  __module__ = 'Verification_pb2'
  # @@protoc_insertion_point(class_scope:Verification.Response)
  ))
_sym_db.RegisterMessage(Response)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\023com.futu.openapi.pb'))
# @@protoc_insertion_point(module_scope)
=======
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Verification.proto

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
  name='Verification.proto',
  package='Verification',
  syntax='proto2',
  serialized_pb=_b('\n\x12Verification.proto\x12\x0cVerification\x1a\x0c\x43ommon.proto\"-\n\x03\x43\x32S\x12\x0c\n\x04type\x18\x01 \x02(\x05\x12\n\n\x02op\x18\x02 \x02(\x05\x12\x0c\n\x04\x63ode\x18\x03 \x01(\t\"\x05\n\x03S2C\")\n\x07Request\x12\x1e\n\x03\x63\x32s\x18\x01 \x02(\x0b\x32\x11.Verification.C2S\"b\n\x08Response\x12\x15\n\x07retType\x18\x01 \x02(\x05:\x04-400\x12\x0e\n\x06retMsg\x18\x02 \x01(\t\x12\x0f\n\x07\x65rrCode\x18\x03 \x01(\x05\x12\x1e\n\x03s2c\x18\x04 \x01(\x0b\x32\x11.Verification.S2C*i\n\x10VerificationType\x12\x1b\n\x17VerificationType_Unknow\x10\x00\x12\x1c\n\x18VerificationType_Picture\x10\x01\x12\x1a\n\x16VerificationType_Phone\x10\x02*i\n\x0eVerificationOp\x12\x19\n\x15VerificationOp_Unknow\x10\x00\x12\x1a\n\x16VerificationOp_Request\x10\x01\x12 \n\x1cVerificationOp_InputAndLogin\x10\x02\x42\x43\n\x13\x63om.futu.openapi.pbZ,github.com/futuopen/ftapi4go/pb/verification')
  ,
  dependencies=[Common__pb2.DESCRIPTOR,])

_VERIFICATIONTYPE = _descriptor.EnumDescriptor(
  name='VerificationType',
  full_name='Verification.VerificationType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='VerificationType_Unknow', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VerificationType_Picture', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VerificationType_Phone', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=247,
  serialized_end=352,
)
_sym_db.RegisterEnumDescriptor(_VERIFICATIONTYPE)

VerificationType = enum_type_wrapper.EnumTypeWrapper(_VERIFICATIONTYPE)
_VERIFICATIONOP = _descriptor.EnumDescriptor(
  name='VerificationOp',
  full_name='Verification.VerificationOp',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='VerificationOp_Unknow', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VerificationOp_Request', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VerificationOp_InputAndLogin', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=354,
  serialized_end=459,
)
_sym_db.RegisterEnumDescriptor(_VERIFICATIONOP)

VerificationOp = enum_type_wrapper.EnumTypeWrapper(_VERIFICATIONOP)
VerificationType_Unknow = 0
VerificationType_Picture = 1
VerificationType_Phone = 2
VerificationOp_Unknow = 0
VerificationOp_Request = 1
VerificationOp_InputAndLogin = 2



_C2S = _descriptor.Descriptor(
  name='C2S',
  full_name='Verification.C2S',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='Verification.C2S.type', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='op', full_name='Verification.C2S.op', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='code', full_name='Verification.C2S.code', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=50,
  serialized_end=95,
)


_S2C = _descriptor.Descriptor(
  name='S2C',
  full_name='Verification.S2C',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=97,
  serialized_end=102,
)


_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='Verification.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='c2s', full_name='Verification.Request.c2s', index=0,
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
  serialized_start=104,
  serialized_end=145,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='Verification.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='retType', full_name='Verification.Response.retType', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=True, default_value=-400,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='retMsg', full_name='Verification.Response.retMsg', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='errCode', full_name='Verification.Response.errCode', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='s2c', full_name='Verification.Response.s2c', index=3,
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
  serialized_start=147,
  serialized_end=245,
)

_REQUEST.fields_by_name['c2s'].message_type = _C2S
_RESPONSE.fields_by_name['s2c'].message_type = _S2C
DESCRIPTOR.message_types_by_name['C2S'] = _C2S
DESCRIPTOR.message_types_by_name['S2C'] = _S2C
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
DESCRIPTOR.enum_types_by_name['VerificationType'] = _VERIFICATIONTYPE
DESCRIPTOR.enum_types_by_name['VerificationOp'] = _VERIFICATIONOP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

C2S = _reflection.GeneratedProtocolMessageType('C2S', (_message.Message,), dict(
  DESCRIPTOR = _C2S,
  __module__ = 'Verification_pb2'
  # @@protoc_insertion_point(class_scope:Verification.C2S)
  ))
_sym_db.RegisterMessage(C2S)

S2C = _reflection.GeneratedProtocolMessageType('S2C', (_message.Message,), dict(
  DESCRIPTOR = _S2C,
  __module__ = 'Verification_pb2'
  # @@protoc_insertion_point(class_scope:Verification.S2C)
  ))
_sym_db.RegisterMessage(S2C)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), dict(
  DESCRIPTOR = _REQUEST,
  __module__ = 'Verification_pb2'
  # @@protoc_insertion_point(class_scope:Verification.Request)
  ))
_sym_db.RegisterMessage(Request)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSE,
  __module__ = 'Verification_pb2'
  # @@protoc_insertion_point(class_scope:Verification.Response)
  ))
_sym_db.RegisterMessage(Response)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\023com.futu.openapi.pbZ,github.com/futuopen/ftapi4go/pb/verification'))
# @@protoc_insertion_point(module_scope)
>>>>>>> c6d8737232b7342604a2c3c8808fc22682a8b3f7
