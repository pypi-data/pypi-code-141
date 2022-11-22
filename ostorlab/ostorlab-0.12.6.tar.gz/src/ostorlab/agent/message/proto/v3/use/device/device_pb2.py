# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ostorlab/agent/message/proto/v3/use/device/device.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7ostorlab/agent/message/proto/v3/use/device/device.proto\x12*ostorlab.agent.message.proto.v3.use.device\"3\n\rLoginPassword\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"1\n\x06SSHKey\x12\x13\n\x0bprivate_key\x18\x01 \x01(\t\x12\x12\n\npublic_key\x18\x02 \x01(\t\"\xb8\x01\n\x0b\x43redentials\x12S\n\x0elogin_password\x18\x01 \x01(\x0b\x32\x39.ostorlab.agent.message.proto.v3.use.device.LoginPasswordH\x00\x12\x45\n\x07ssh_key\x18\x02 \x01(\x0b\x32\x32.ostorlab.agent.message.proto.v3.use.device.SSHKeyH\x00\x42\r\n\x0b\x63redentials\":\n\x0b\x44\x65viceRelay\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\t\x12\x0c\n\x04port\x18\x03 \x01(\x11\"*\n\x08\x44uration\x12\r\n\x05nanos\x18\x01 \x01(\x05\x12\x0f\n\x07seconds\x18\x02 \x01(\x03\"/\n\x08\x41rgument\x12\x10\n\x08\x61rg_name\x18\x01 \x01(\t\x12\x11\n\targ_value\x18\x02 \x03(\t\"\xe9\x03\n\x07Message\x12\x11\n\tdevice_id\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65vice_type\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65vice_name\x18\x03 \x01(\t\x12\x16\n\x0e\x64\x65vice_version\x18\x04 \x01(\t\x12S\n\x12\x64\x65vice_credentials\x18\x05 \x01(\x0b\x32\x37.ostorlab.agent.message.proto.v3.use.device.Credentials\x12M\n\x0c\x64\x65vice_relay\x18\x06 \x01(\x0b\x32\x37.ostorlab.agent.message.proto.v3.use.device.DeviceRelay\x12Y\n\x18\x64\x65vice_relay_credentials\x18\x07 \x01(\x0b\x32\x37.ostorlab.agent.message.proto.v3.use.device.Credentials\x12\x46\n\x08\x64uration\x18\x08 \x01(\x0b\x32\x34.ostorlab.agent.message.proto.v3.use.device.Duration\x12\x42\n\x04\x61rgs\x18\t \x03(\x0b\x32\x34.ostorlab.agent.message.proto.v3.use.device.Argument')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ostorlab.agent.message.proto.v3.use.device.device_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _LOGINPASSWORD._serialized_start=103
  _LOGINPASSWORD._serialized_end=154
  _SSHKEY._serialized_start=156
  _SSHKEY._serialized_end=205
  _CREDENTIALS._serialized_start=208
  _CREDENTIALS._serialized_end=392
  _DEVICERELAY._serialized_start=394
  _DEVICERELAY._serialized_end=452
  _DURATION._serialized_start=454
  _DURATION._serialized_end=496
  _ARGUMENT._serialized_start=498
  _ARGUMENT._serialized_end=545
  _MESSAGE._serialized_start=548
  _MESSAGE._serialized_end=1037
# @@protoc_insertion_point(module_scope)
