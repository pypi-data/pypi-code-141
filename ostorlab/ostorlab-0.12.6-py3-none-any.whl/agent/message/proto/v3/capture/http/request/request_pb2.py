# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ostorlab/agent/message/proto/v3/capture/http/request/request.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nBostorlab/agent/message/proto/v3/capture/http/request/request.proto\x12\x34ostorlab.agent.message.proto.v3.capture.http.request\"%\n\x06header\x12\x0c\n\x04name\x18\x01 \x01(\x0c\x12\r\n\x05value\x18\x02 \x01(\x0c\"\xfb\x01\n\x07Message\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06method\x18\x02 \x01(\t\x12M\n\x07headers\x18\x03 \x03(\x0b\x32<.ostorlab.agent.message.proto.v3.capture.http.request.header\x12\x0f\n\x07\x63ontent\x18\x04 \x01(\x0c\x12\x0c\n\x04host\x18\x05 \x01(\t\x12\x0c\n\x04port\x18\x06 \x01(\r\x12\x14\n\x0chttp_version\x18\x07 \x01(\x0c\x12\x0e\n\x06scheme\x18\x08 \x01(\x0c\x12\x0c\n\x04path\x18\t \x01(\x0c\x12\x12\n\ntime_start\x18\n \x01(\x02\x12\x10\n\x08time_end\x18\x0b \x01(\x02')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ostorlab.agent.message.proto.v3.capture.http.request.request_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _HEADER._serialized_start=124
  _HEADER._serialized_end=161
  _MESSAGE._serialized_start=164
  _MESSAGE._serialized_end=415
# @@protoc_insertion_point(module_scope)
