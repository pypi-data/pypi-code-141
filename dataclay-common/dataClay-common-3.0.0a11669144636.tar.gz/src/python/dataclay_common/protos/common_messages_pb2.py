# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/common_messages.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1cprotos/common_messages.proto\x12\rprotos.common\"\x1e\n\nCredential\x12\x10\n\x08password\x18\x01 \x01(\t\":\n\rParamOrReturn\x12\x10\n\x08objectID\x18\x01 \x01(\t\x12\x17\n\x0fserializedParam\x18\x02 \x01(\x0c\"\x0e\n\x0c\x45mptyMessage\"\xeb\x05\n\x1cSerializedParametersOrReturn\x12\x11\n\tnumParams\x18\x01 \x01(\x05\x12M\n\timmParams\x18\x02 \x03(\x0b\x32:.protos.common.SerializedParametersOrReturn.ImmParamsEntry\x12O\n\nlangParams\x18\x03 \x03(\x0b\x32;.protos.common.SerializedParametersOrReturn.LangParamsEntry\x12W\n\x0evolatileParams\x18\x04 \x03(\x0b\x32?.protos.common.SerializedParametersOrReturn.VolatileParamsEntry\x12O\n\npersParams\x18\x05 \x03(\x0b\x32;.protos.common.SerializedParametersOrReturn.PersParamsEntry\x1aW\n\x0eImmParamsEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\x34\n\x05value\x18\x02 \x01(\x0b\x32%.protos.common.ImmutableParamOrReturn:\x02\x38\x01\x1aW\n\x0fLangParamsEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\x33\n\x05value\x18\x02 \x01(\x0b\x32$.protos.common.LanguageParamOrReturn:\x02\x38\x01\x1a\x61\n\x13VolatileParamsEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\x39\n\x05value\x18\x02 \x01(\x0b\x32*.protos.common.ObjectWithDataParamOrReturn:\x02\x38\x01\x1aY\n\x0fPersParamsEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\x35\n\x05value\x18\x02 \x01(\x0b\x32&.protos.common.PersistentParamOrReturn:\x02\x38\x01\"*\n\x16ImmutableParamOrReturn\x12\x10\n\x08objbytes\x18\x01 \x01(\x0c\"\\\n\x17PersistentParamOrReturn\x12\x0b\n\x03oid\x18\x01 \x01(\t\x12\x0c\n\x04hint\x18\x02 \x01(\t\x12\x0f\n\x07\x63lassID\x18\x03 \x01(\t\x12\x15\n\rextDataClayID\x18\x04 \x01(\t\"\x86\x01\n\x1bObjectWithDataParamOrReturn\x12\x0b\n\x03oid\x18\x01 \x01(\t\x12\x0f\n\x07\x63lassid\x18\x02 \x01(\t\x12\x37\n\x08metadata\x18\x03 \x01(\x0b\x32%.protos.common.DataClayObjectMetaData\x12\x10\n\x08objbytes\x18\x04 \x01(\x0c\"b\n\x15LanguageParamOrReturn\x12\x37\n\x08metadata\x18\x01 \x01(\x0b\x32%.protos.common.DataClayObjectMetaData\x12\x10\n\x08objbytes\x18\x02 \x01(\x0c\"\x93\x04\n\x16\x44\x61taClayObjectMetaData\x12=\n\x04oids\x18\x01 \x03(\x0b\x32/.protos.common.DataClayObjectMetaData.OidsEntry\x12\x45\n\x08\x63lassids\x18\x02 \x03(\x0b\x32\x33.protos.common.DataClayObjectMetaData.ClassidsEntry\x12?\n\x05hints\x18\x03 \x03(\x0b\x32\x30.protos.common.DataClayObjectMetaData.HintsEntry\x12\x0f\n\x07numRefs\x18\x04 \x01(\x05\x12\x14\n\x0corigObjectID\x18\x05 \x01(\t\x12\x14\n\x0crootLocation\x18\x06 \x01(\t\x12\x16\n\x0eoriginLocation\x18\x07 \x01(\t\x12\x18\n\x10replicaLocations\x18\x08 \x03(\t\x12\r\n\x05\x61lias\x18\t \x01(\t\x12\x12\n\nisReadOnly\x18\n \x01(\x08\x12\x14\n\x0c\x64\x61taset_name\x18\x0b \x01(\t\x1a+\n\tOidsEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a/\n\rClassidsEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a,\n\nHintsEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"]\n\x14PersistentObjectInDB\x12\x37\n\x08metadata\x18\x01 \x01(\x0b\x32%.protos.common.DataClayObjectMetaData\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\"j\n\x10RegistrationInfo\x12\x10\n\x08objectID\x18\x01 \x01(\t\x12\x0f\n\x07\x63lassID\x18\x02 \x01(\t\x12\x11\n\tsessionID\x18\x03 \x01(\t\x12\x11\n\tdataSetID\x18\x04 \x01(\t\x12\r\n\x05\x61lias\x18\x05 \x01(\t\"\\\n\x13\x46\x65\x64\x65ratedObjectInfo\x12\x10\n\x08objectID\x18\x01 \x01(\t\x12\x11\n\tclassName\x18\x02 \x01(\t\x12\x11\n\tnameSpace\x18\x03 \x01(\t\x12\r\n\x05\x61lias\x18\x04 \x03(\t\"\xaf\x01\n\x11GetTracesResponse\x12<\n\x06traces\x18\x01 \x03(\x0b\x32,.protos.common.GetTracesResponse.TracesEntry\x12-\n\x07\x65xcInfo\x18\x02 \x01(\x0b\x32\x1c.protos.common.ExceptionInfo\x1a-\n\x0bTracesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c:\x02\x38\x01\"[\n\rExceptionInfo\x12\x13\n\x0bisException\x18\x01 \x01(\x08\x12\x1b\n\x13serializedException\x18\x02 \x01(\x0c\x12\x18\n\x10\x65xceptionMessage\x18\x03 \x01(\x0c\"\x8f\x01\n\x0cMetaDataInfo\x12\x10\n\x08objectID\x18\x01 \x01(\t\x12\x12\n\nisReadOnly\x18\x02 \x01(\x08\x12\x11\n\tdatasetID\x18\x03 \x01(\t\x12\x13\n\x0bmetaclassID\x18\x04 \x01(\t\x12\x11\n\tlocations\x18\x05 \x03(\t\x12\r\n\x05\x61lias\x18\x06 \x01(\t\x12\x0f\n\x07ownerID\x18\x07 \x01(\t\"O\n\x13StorageLocationInfo\x12\n\n\x02id\x18\x01 \x01(\t\x12\x10\n\x08hostname\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0c\n\x04port\x18\x04 \x01(\x05\"\x98\x01\n\x18\x45xecutionEnvironmentInfo\x12\n\n\x02id\x18\x01 \x01(\t\x12\x10\n\x08hostname\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0c\n\x04port\x18\x04 \x01(\x05\x12&\n\x08language\x18\x05 \x01(\x0e\x32\x14.protos.common.Langs\x12\x1a\n\x12\x64\x61taClayInstanceID\x18\x06 \x01(\t\"<\n\x10\x44\x61taClayInstance\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05hosts\x18\x02 \x03(\t\x12\r\n\x05ports\x18\x03 \x03(\x05\"W\n\x15GetNumObjectsResponse\x12\x0f\n\x07numObjs\x18\x01 \x01(\x05\x12-\n\x07\x65xcInfo\x18\x02 \x01(\x0b\x32\x1c.protos.common.ExceptionInfo\"\x90\x01\n\x14\x45xecutionEnvironment\x12\n\n\x02id\x18\x01 \x01(\t\x12\x10\n\x08hostname\x18\x02 \x01(\t\x12\x0c\n\x04port\x18\x03 \x01(\x05\x12\x0f\n\x07sl_name\x18\x04 \x01(\t\x12&\n\x08language\x18\x05 \x01(\x0e\x32\x14.protos.common.Langs\x12\x13\n\x0b\x64\x61taclay_id\x18\x06 \x01(\t\"\xc6\x01\n\x0eObjectMetadata\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\nalias_name\x18\x02 \x01(\t\x12\x14\n\x0c\x64\x61taset_name\x18\x03 \x01(\t\x12\x12\n\nclass_name\x18\x04 \x01(\t\x12\x14\n\x0cmaster_ee_id\x18\x05 \x01(\t\x12\x16\n\x0ereplica_ee_ids\x18\x06 \x03(\t\x12&\n\x08language\x18\x07 \x01(\x0e\x32\x14.protos.common.Langs\x12\x14\n\x0cis_read_only\x18\x08 \x01(\x08\"P\n\x07Session\x12\n\n\x02id\x18\x01 \x01(\t\x12\x10\n\x08username\x18\x02 \x01(\t\x12\x14\n\x0c\x64\x61taset_name\x18\x03 \x01(\t\x12\x11\n\tis_active\x18\x04 \x01(\x08*6\n\x05Langs\x12\r\n\tLANG_NONE\x10\x00\x12\r\n\tLANG_JAVA\x10\x01\x12\x0f\n\x0bLANG_PYTHON\x10\x02\x42\x34\n2es.bsc.dataclay.communication.grpc.messages.commonb\x06proto3')

_LANGS = DESCRIPTOR.enum_types_by_name['Langs']
Langs = enum_type_wrapper.EnumTypeWrapper(_LANGS)
LANG_NONE = 0
LANG_JAVA = 1
LANG_PYTHON = 2


_CREDENTIAL = DESCRIPTOR.message_types_by_name['Credential']
_PARAMORRETURN = DESCRIPTOR.message_types_by_name['ParamOrReturn']
_EMPTYMESSAGE = DESCRIPTOR.message_types_by_name['EmptyMessage']
_SERIALIZEDPARAMETERSORRETURN = DESCRIPTOR.message_types_by_name['SerializedParametersOrReturn']
_SERIALIZEDPARAMETERSORRETURN_IMMPARAMSENTRY = _SERIALIZEDPARAMETERSORRETURN.nested_types_by_name['ImmParamsEntry']
_SERIALIZEDPARAMETERSORRETURN_LANGPARAMSENTRY = _SERIALIZEDPARAMETERSORRETURN.nested_types_by_name['LangParamsEntry']
_SERIALIZEDPARAMETERSORRETURN_VOLATILEPARAMSENTRY = _SERIALIZEDPARAMETERSORRETURN.nested_types_by_name['VolatileParamsEntry']
_SERIALIZEDPARAMETERSORRETURN_PERSPARAMSENTRY = _SERIALIZEDPARAMETERSORRETURN.nested_types_by_name['PersParamsEntry']
_IMMUTABLEPARAMORRETURN = DESCRIPTOR.message_types_by_name['ImmutableParamOrReturn']
_PERSISTENTPARAMORRETURN = DESCRIPTOR.message_types_by_name['PersistentParamOrReturn']
_OBJECTWITHDATAPARAMORRETURN = DESCRIPTOR.message_types_by_name['ObjectWithDataParamOrReturn']
_LANGUAGEPARAMORRETURN = DESCRIPTOR.message_types_by_name['LanguageParamOrReturn']
_DATACLAYOBJECTMETADATA = DESCRIPTOR.message_types_by_name['DataClayObjectMetaData']
_DATACLAYOBJECTMETADATA_OIDSENTRY = _DATACLAYOBJECTMETADATA.nested_types_by_name['OidsEntry']
_DATACLAYOBJECTMETADATA_CLASSIDSENTRY = _DATACLAYOBJECTMETADATA.nested_types_by_name['ClassidsEntry']
_DATACLAYOBJECTMETADATA_HINTSENTRY = _DATACLAYOBJECTMETADATA.nested_types_by_name['HintsEntry']
_PERSISTENTOBJECTINDB = DESCRIPTOR.message_types_by_name['PersistentObjectInDB']
_REGISTRATIONINFO = DESCRIPTOR.message_types_by_name['RegistrationInfo']
_FEDERATEDOBJECTINFO = DESCRIPTOR.message_types_by_name['FederatedObjectInfo']
_GETTRACESRESPONSE = DESCRIPTOR.message_types_by_name['GetTracesResponse']
_GETTRACESRESPONSE_TRACESENTRY = _GETTRACESRESPONSE.nested_types_by_name['TracesEntry']
_EXCEPTIONINFO = DESCRIPTOR.message_types_by_name['ExceptionInfo']
_METADATAINFO = DESCRIPTOR.message_types_by_name['MetaDataInfo']
_STORAGELOCATIONINFO = DESCRIPTOR.message_types_by_name['StorageLocationInfo']
_EXECUTIONENVIRONMENTINFO = DESCRIPTOR.message_types_by_name['ExecutionEnvironmentInfo']
_DATACLAYINSTANCE = DESCRIPTOR.message_types_by_name['DataClayInstance']
_GETNUMOBJECTSRESPONSE = DESCRIPTOR.message_types_by_name['GetNumObjectsResponse']
_EXECUTIONENVIRONMENT = DESCRIPTOR.message_types_by_name['ExecutionEnvironment']
_OBJECTMETADATA = DESCRIPTOR.message_types_by_name['ObjectMetadata']
_SESSION = DESCRIPTOR.message_types_by_name['Session']
Credential = _reflection.GeneratedProtocolMessageType('Credential', (_message.Message,), {
  'DESCRIPTOR' : _CREDENTIAL,
  '__module__' : 'protos.common_messages_pb2'
  # @@protoc_insertion_point(class_scope:protos.common.Credential)
  })
_sym_db.RegisterMessage(Credential)

ParamOrReturn = _reflection.GeneratedProtocolMessageType('ParamOrReturn', (_message.Message,), {
  'DESCRIPTOR' : _PARAMORRETURN,
  '__module__' : 'protos.common_messages_pb2'
  # @@protoc_insertion_point(class_scope:protos.common.ParamOrReturn)
  })
_sym_db.RegisterMessage(ParamOrReturn)

EmptyMessage = _reflection.GeneratedProtocolMessageType('EmptyMessage', (_message.Message,), {
  'DESCRIPTOR' : _EMPTYMESSAGE,
  '__module__' : 'protos.common_messages_pb2'
  # @@protoc_insertion_point(class_scope:protos.common.EmptyMessage)
  })
_sym_db.RegisterMessage(EmptyMessage)

SerializedParametersOrReturn = _reflection.GeneratedProtocolMessageType('SerializedParametersOrReturn', (_message.Message,), {

  'ImmParamsEntry' : _reflection.GeneratedProtocolMessageType('ImmParamsEntry', (_message.Message,), {
    'DESCRIPTOR' : _SERIALIZEDPARAMETERSORRETURN_IMMPARAMSENTRY,
    '__module__' : 'protos.common_messages_pb2'
    # @@protoc_insertion_point(class_scope:protos.common.SerializedParametersOrReturn.ImmParamsEntry)
    })
  ,

  'LangParamsEntry' : _reflection.GeneratedProtocolMessageType('LangParamsEntry', (_message.Message,), {
    'DESCRIPTOR' : _SERIALIZEDPARAMETERSORRETURN_LANGPARAMSENTRY,
    '__module__' : 'protos.common_messages_pb2'
    # @@protoc_insertion_point(class_scope:protos.common.SerializedParametersOrReturn.LangParamsEntry)
    })
  ,

  'VolatileParamsEntry' : _reflection.GeneratedProtocolMessageType('VolatileParamsEntry', (_message.Message,), {
    'DESCRIPTOR' : _SERIALIZEDPARAMETERSORRETURN_VOLATILEPARAMSENTRY,
    '__module__' : 'protos.common_messages_pb2'
    # @@protoc_insertion_point(class_scope:protos.common.SerializedParametersOrReturn.VolatileParamsEntry)
    })
  ,

  'PersParamsEntry' : _reflection.GeneratedProtocolMessageType('PersParamsEntry', (_message.Message,), {
    'DESCRIPTOR' : _SERIALIZEDPARAMETERSORRETURN_PERSPARAMSENTRY,
    '__module__' : 'protos.common_messages_pb2'
    # @@protoc_insertion_point(class_scope:protos.common.SerializedParametersOrReturn.PersParamsEntry)
    })
  ,
  'DESCRIPTOR' : _SERIALIZEDPARAMETERSORRETURN,
  '__module__' : 'protos.common_messages_pb2'
  # @@protoc_insertion_point(class_scope:protos.common.SerializedParametersOrReturn)
  })
_sym_db.RegisterMessage(SerializedParametersOrReturn)
_sym_db.RegisterMessage(SerializedParametersOrReturn.ImmParamsEntry)
_sym_db.RegisterMessage(SerializedParametersOrReturn.LangParamsEntry)
_sym_db.RegisterMessage(SerializedParametersOrReturn.VolatileParamsEntry)
_sym_db.RegisterMessage(SerializedParametersOrReturn.PersParamsEntry)

ImmutableParamOrReturn = _reflection.GeneratedProtocolMessageType('ImmutableParamOrReturn', (_message.Message,), {
  'DESCRIPTOR' : _IMMUTABLEPARAMORRETURN,
  '__module__' : 'protos.common_messages_pb2'
  # @@protoc_insertion_point(class_scope:protos.common.ImmutableParamOrReturn)
  })
_sym_db.RegisterMessage(ImmutableParamOrReturn)

PersistentParamOrReturn = _reflection.GeneratedProtocolMessageType('PersistentParamOrReturn', (_message.Message,), {
  'DESCRIPTOR' : _PERSISTENTPARAMORRETURN,
  '__module__' : 'protos.common_messages_pb2'
  # @@protoc_insertion_point(class_scope:protos.common.PersistentParamOrReturn)
  })
_sym_db.RegisterMessage(PersistentParamOrReturn)

ObjectWithDataParamOrReturn = _reflection.GeneratedProtocolMessageType('ObjectWithDataParamOrReturn', (_message.Message,), {
  'DESCRIPTOR' : _OBJECTWITHDATAPARAMORRETURN,
  '__module__' : 'protos.common_messages_pb2'
  # @@protoc_insertion_point(class_scope:protos.common.ObjectWithDataParamOrReturn)
  })
_sym_db.RegisterMessage(ObjectWithDataParamOrReturn)

LanguageParamOrReturn = _reflection.GeneratedProtocolMessageType('LanguageParamOrReturn', (_message.Message,), {
  'DESCRIPTOR' : _LANGUAGEPARAMORRETURN,
  '__module__' : 'protos.common_messages_pb2'
  # @@protoc_insertion_point(class_scope:protos.common.LanguageParamOrReturn)
  })
_sym_db.RegisterMessage(LanguageParamOrReturn)

DataClayObjectMetaData = _reflection.GeneratedProtocolMessageType('DataClayObjectMetaData', (_message.Message,), {

  'OidsEntry' : _reflection.GeneratedProtocolMessageType('OidsEntry', (_message.Message,), {
    'DESCRIPTOR' : _DATACLAYOBJECTMETADATA_OIDSENTRY,
    '__module__' : 'protos.common_messages_pb2'
    # @@protoc_insertion_point(class_scope:protos.common.DataClayObjectMetaData.OidsEntry)
    })
  ,

  'ClassidsEntry' : _reflection.GeneratedProtocolMessageType('ClassidsEntry', (_message.Message,), {
    'DESCRIPTOR' : _DATACLAYOBJECTMETADATA_CLASSIDSENTRY,
    '__module__' : 'protos.common_messages_pb2'
    # @@protoc_insertion_point(class_scope:protos.common.DataClayObjectMetaData.ClassidsEntry)
    })
  ,

  'HintsEntry' : _reflection.GeneratedProtocolMessageType('HintsEntry', (_message.Message,), {
    'DESCRIPTOR' : _DATACLAYOBJECTMETADATA_HINTSENTRY,
    '__module__' : 'protos.common_messages_pb2'
    # @@protoc_insertion_point(class_scope:protos.common.DataClayObjectMetaData.HintsEntry)
    })
  ,
  'DESCRIPTOR' : _DATACLAYOBJECTMETADATA,
  '__module__' : 'protos.common_messages_pb2'
  # @@protoc_insertion_point(class_scope:protos.common.DataClayObjectMetaData)
  })
_sym_db.RegisterMessage(DataClayObjectMetaData)
_sym_db.RegisterMessage(DataClayObjectMetaData.OidsEntry)
_sym_db.RegisterMessage(DataClayObjectMetaData.ClassidsEntry)
_sym_db.RegisterMessage(DataClayObjectMetaData.HintsEntry)

PersistentObjectInDB = _reflection.GeneratedProtocolMessageType('PersistentObjectInDB', (_message.Message,), {
  'DESCRIPTOR' : _PERSISTENTOBJECTINDB,
  '__module__' : 'protos.common_messages_pb2'
  # @@protoc_insertion_point(class_scope:protos.common.PersistentObjectInDB)
  })
_sym_db.RegisterMessage(PersistentObjectInDB)

RegistrationInfo = _reflection.GeneratedProtocolMessageType('RegistrationInfo', (_message.Message,), {
  'DESCRIPTOR' : _REGISTRATIONINFO,
  '__module__' : 'protos.common_messages_pb2'
  # @@protoc_insertion_point(class_scope:protos.common.RegistrationInfo)
  })
_sym_db.RegisterMessage(RegistrationInfo)

FederatedObjectInfo = _reflection.GeneratedProtocolMessageType('FederatedObjectInfo', (_message.Message,), {
  'DESCRIPTOR' : _FEDERATEDOBJECTINFO,
  '__module__' : 'protos.common_messages_pb2'
  # @@protoc_insertion_point(class_scope:protos.common.FederatedObjectInfo)
  })
_sym_db.RegisterMessage(FederatedObjectInfo)

GetTracesResponse = _reflection.GeneratedProtocolMessageType('GetTracesResponse', (_message.Message,), {

  'TracesEntry' : _reflection.GeneratedProtocolMessageType('TracesEntry', (_message.Message,), {
    'DESCRIPTOR' : _GETTRACESRESPONSE_TRACESENTRY,
    '__module__' : 'protos.common_messages_pb2'
    # @@protoc_insertion_point(class_scope:protos.common.GetTracesResponse.TracesEntry)
    })
  ,
  'DESCRIPTOR' : _GETTRACESRESPONSE,
  '__module__' : 'protos.common_messages_pb2'
  # @@protoc_insertion_point(class_scope:protos.common.GetTracesResponse)
  })
_sym_db.RegisterMessage(GetTracesResponse)
_sym_db.RegisterMessage(GetTracesResponse.TracesEntry)

ExceptionInfo = _reflection.GeneratedProtocolMessageType('ExceptionInfo', (_message.Message,), {
  'DESCRIPTOR' : _EXCEPTIONINFO,
  '__module__' : 'protos.common_messages_pb2'
  # @@protoc_insertion_point(class_scope:protos.common.ExceptionInfo)
  })
_sym_db.RegisterMessage(ExceptionInfo)

MetaDataInfo = _reflection.GeneratedProtocolMessageType('MetaDataInfo', (_message.Message,), {
  'DESCRIPTOR' : _METADATAINFO,
  '__module__' : 'protos.common_messages_pb2'
  # @@protoc_insertion_point(class_scope:protos.common.MetaDataInfo)
  })
_sym_db.RegisterMessage(MetaDataInfo)

StorageLocationInfo = _reflection.GeneratedProtocolMessageType('StorageLocationInfo', (_message.Message,), {
  'DESCRIPTOR' : _STORAGELOCATIONINFO,
  '__module__' : 'protos.common_messages_pb2'
  # @@protoc_insertion_point(class_scope:protos.common.StorageLocationInfo)
  })
_sym_db.RegisterMessage(StorageLocationInfo)

ExecutionEnvironmentInfo = _reflection.GeneratedProtocolMessageType('ExecutionEnvironmentInfo', (_message.Message,), {
  'DESCRIPTOR' : _EXECUTIONENVIRONMENTINFO,
  '__module__' : 'protos.common_messages_pb2'
  # @@protoc_insertion_point(class_scope:protos.common.ExecutionEnvironmentInfo)
  })
_sym_db.RegisterMessage(ExecutionEnvironmentInfo)

DataClayInstance = _reflection.GeneratedProtocolMessageType('DataClayInstance', (_message.Message,), {
  'DESCRIPTOR' : _DATACLAYINSTANCE,
  '__module__' : 'protos.common_messages_pb2'
  # @@protoc_insertion_point(class_scope:protos.common.DataClayInstance)
  })
_sym_db.RegisterMessage(DataClayInstance)

GetNumObjectsResponse = _reflection.GeneratedProtocolMessageType('GetNumObjectsResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETNUMOBJECTSRESPONSE,
  '__module__' : 'protos.common_messages_pb2'
  # @@protoc_insertion_point(class_scope:protos.common.GetNumObjectsResponse)
  })
_sym_db.RegisterMessage(GetNumObjectsResponse)

ExecutionEnvironment = _reflection.GeneratedProtocolMessageType('ExecutionEnvironment', (_message.Message,), {
  'DESCRIPTOR' : _EXECUTIONENVIRONMENT,
  '__module__' : 'protos.common_messages_pb2'
  # @@protoc_insertion_point(class_scope:protos.common.ExecutionEnvironment)
  })
_sym_db.RegisterMessage(ExecutionEnvironment)

ObjectMetadata = _reflection.GeneratedProtocolMessageType('ObjectMetadata', (_message.Message,), {
  'DESCRIPTOR' : _OBJECTMETADATA,
  '__module__' : 'protos.common_messages_pb2'
  # @@protoc_insertion_point(class_scope:protos.common.ObjectMetadata)
  })
_sym_db.RegisterMessage(ObjectMetadata)

Session = _reflection.GeneratedProtocolMessageType('Session', (_message.Message,), {
  'DESCRIPTOR' : _SESSION,
  '__module__' : 'protos.common_messages_pb2'
  # @@protoc_insertion_point(class_scope:protos.common.Session)
  })
_sym_db.RegisterMessage(Session)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n2es.bsc.dataclay.communication.grpc.messages.common'
  _SERIALIZEDPARAMETERSORRETURN_IMMPARAMSENTRY._options = None
  _SERIALIZEDPARAMETERSORRETURN_IMMPARAMSENTRY._serialized_options = b'8\001'
  _SERIALIZEDPARAMETERSORRETURN_LANGPARAMSENTRY._options = None
  _SERIALIZEDPARAMETERSORRETURN_LANGPARAMSENTRY._serialized_options = b'8\001'
  _SERIALIZEDPARAMETERSORRETURN_VOLATILEPARAMSENTRY._options = None
  _SERIALIZEDPARAMETERSORRETURN_VOLATILEPARAMSENTRY._serialized_options = b'8\001'
  _SERIALIZEDPARAMETERSORRETURN_PERSPARAMSENTRY._options = None
  _SERIALIZEDPARAMETERSORRETURN_PERSPARAMSENTRY._serialized_options = b'8\001'
  _DATACLAYOBJECTMETADATA_OIDSENTRY._options = None
  _DATACLAYOBJECTMETADATA_OIDSENTRY._serialized_options = b'8\001'
  _DATACLAYOBJECTMETADATA_CLASSIDSENTRY._options = None
  _DATACLAYOBJECTMETADATA_CLASSIDSENTRY._serialized_options = b'8\001'
  _DATACLAYOBJECTMETADATA_HINTSENTRY._options = None
  _DATACLAYOBJECTMETADATA_HINTSENTRY._serialized_options = b'8\001'
  _GETTRACESRESPONSE_TRACESENTRY._options = None
  _GETTRACESRESPONSE_TRACESENTRY._serialized_options = b'8\001'
  _LANGS._serialized_start=3345
  _LANGS._serialized_end=3399
  _CREDENTIAL._serialized_start=47
  _CREDENTIAL._serialized_end=77
  _PARAMORRETURN._serialized_start=79
  _PARAMORRETURN._serialized_end=137
  _EMPTYMESSAGE._serialized_start=139
  _EMPTYMESSAGE._serialized_end=153
  _SERIALIZEDPARAMETERSORRETURN._serialized_start=156
  _SERIALIZEDPARAMETERSORRETURN._serialized_end=903
  _SERIALIZEDPARAMETERSORRETURN_IMMPARAMSENTRY._serialized_start=537
  _SERIALIZEDPARAMETERSORRETURN_IMMPARAMSENTRY._serialized_end=624
  _SERIALIZEDPARAMETERSORRETURN_LANGPARAMSENTRY._serialized_start=626
  _SERIALIZEDPARAMETERSORRETURN_LANGPARAMSENTRY._serialized_end=713
  _SERIALIZEDPARAMETERSORRETURN_VOLATILEPARAMSENTRY._serialized_start=715
  _SERIALIZEDPARAMETERSORRETURN_VOLATILEPARAMSENTRY._serialized_end=812
  _SERIALIZEDPARAMETERSORRETURN_PERSPARAMSENTRY._serialized_start=814
  _SERIALIZEDPARAMETERSORRETURN_PERSPARAMSENTRY._serialized_end=903
  _IMMUTABLEPARAMORRETURN._serialized_start=905
  _IMMUTABLEPARAMORRETURN._serialized_end=947
  _PERSISTENTPARAMORRETURN._serialized_start=949
  _PERSISTENTPARAMORRETURN._serialized_end=1041
  _OBJECTWITHDATAPARAMORRETURN._serialized_start=1044
  _OBJECTWITHDATAPARAMORRETURN._serialized_end=1178
  _LANGUAGEPARAMORRETURN._serialized_start=1180
  _LANGUAGEPARAMORRETURN._serialized_end=1278
  _DATACLAYOBJECTMETADATA._serialized_start=1281
  _DATACLAYOBJECTMETADATA._serialized_end=1812
  _DATACLAYOBJECTMETADATA_OIDSENTRY._serialized_start=1674
  _DATACLAYOBJECTMETADATA_OIDSENTRY._serialized_end=1717
  _DATACLAYOBJECTMETADATA_CLASSIDSENTRY._serialized_start=1719
  _DATACLAYOBJECTMETADATA_CLASSIDSENTRY._serialized_end=1766
  _DATACLAYOBJECTMETADATA_HINTSENTRY._serialized_start=1768
  _DATACLAYOBJECTMETADATA_HINTSENTRY._serialized_end=1812
  _PERSISTENTOBJECTINDB._serialized_start=1814
  _PERSISTENTOBJECTINDB._serialized_end=1907
  _REGISTRATIONINFO._serialized_start=1909
  _REGISTRATIONINFO._serialized_end=2015
  _FEDERATEDOBJECTINFO._serialized_start=2017
  _FEDERATEDOBJECTINFO._serialized_end=2109
  _GETTRACESRESPONSE._serialized_start=2112
  _GETTRACESRESPONSE._serialized_end=2287
  _GETTRACESRESPONSE_TRACESENTRY._serialized_start=2242
  _GETTRACESRESPONSE_TRACESENTRY._serialized_end=2287
  _EXCEPTIONINFO._serialized_start=2289
  _EXCEPTIONINFO._serialized_end=2380
  _METADATAINFO._serialized_start=2383
  _METADATAINFO._serialized_end=2526
  _STORAGELOCATIONINFO._serialized_start=2528
  _STORAGELOCATIONINFO._serialized_end=2607
  _EXECUTIONENVIRONMENTINFO._serialized_start=2610
  _EXECUTIONENVIRONMENTINFO._serialized_end=2762
  _DATACLAYINSTANCE._serialized_start=2764
  _DATACLAYINSTANCE._serialized_end=2824
  _GETNUMOBJECTSRESPONSE._serialized_start=2826
  _GETNUMOBJECTSRESPONSE._serialized_end=2913
  _EXECUTIONENVIRONMENT._serialized_start=2916
  _EXECUTIONENVIRONMENT._serialized_end=3060
  _OBJECTMETADATA._serialized_start=3063
  _OBJECTMETADATA._serialized_end=3261
  _SESSION._serialized_start=3263
  _SESSION._serialized_end=3343
# @@protoc_insertion_point(module_scope)
