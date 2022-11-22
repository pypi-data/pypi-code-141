# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: octoml/octomizer/v1/workflows.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from octoml.octomizer.v1 import hardware_pb2 as octoml_dot_octomizer_dot_v1_dot_hardware__pb2
from octoml.octomizer.v1 import autotune_pb2 as octoml_dot_octomizer_dot_v1_dot_autotune__pb2
from octoml.octomizer.v1 import benchmark_pb2 as octoml_dot_octomizer_dot_v1_dot_benchmark__pb2
from octoml.octomizer.v1 import package_pb2 as octoml_dot_octomizer_dot_v1_dot_package__pb2
from octoml.octomizer.v1 import error_pb2 as octoml_dot_octomizer_dot_v1_dot_error__pb2
from octoml.octomizer.v1 import model_inputs_pb2 as octoml_dot_octomizer_dot_v1_dot_model__inputs__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='octoml/octomizer/v1/workflows.proto',
  package='octoml.octomizer.v1',
  syntax='proto3',
  serialized_options=b'ZCgitlab.com/octoml/platform/protobufs/golang/gen/octoml/octomizer/v1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n#octoml/octomizer/v1/workflows.proto\x12\x13octoml.octomizer.v1\x1a\"octoml/octomizer/v1/hardware.proto\x1a\"octoml/octomizer/v1/autotune.proto\x1a#octoml/octomizer/v1/benchmark.proto\x1a!octoml/octomizer/v1/package.proto\x1a\x1foctoml/octomizer/v1/error.proto\x1a&octoml/octomizer/v1/model_inputs.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\x81\x05\n\x08Workflow\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x12\n\nmodel_uuid\x18\x02 \x01(\t\x12\x1a\n\x12model_variant_uuid\x18\x03 \x01(\t\x12\x33\n\x06status\x18\x04 \x01(\x0b\x32#.octoml.octomizer.v1.WorkflowStatus\x12\x33\n\x08hardware\x18\x05 \x01(\x0b\x32!.octoml.octomizer.v1.HardwareSpec\x12\x43\n\x13\x61utotune_stage_spec\x18\x06 \x01(\x0b\x32&.octoml.octomizer.v1.AutotuneStageSpec\x12\x45\n\x14\x62\x65nchmark_stage_spec\x18\x07 \x01(\x0b\x32\'.octoml.octomizer.v1.BenchmarkStageSpec\x12\x41\n\x12package_stage_spec\x18\x08 \x01(\x0b\x32%.octoml.octomizer.v1.PackageStageSpec\x12/\n\x0b\x63reate_time\x18\t \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\n \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x12\n\ncreated_by\x18\x0b \x01(\t\x12=\n\x08metadata\x18\r \x03(\x0b\x32+.octoml.octomizer.v1.Workflow.MetadataEntry\x12\x12\n\ngroup_uuid\x18\x0e \x01(\t\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01J\x04\x08\x0c\x10\r\"\xe8\x03\n\x0eWorkflowStatus\x12-\n\ttimestamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12@\n\x05state\x18\x02 \x01(\x0e\x32\x31.octoml.octomizer.v1.WorkflowStatus.WorkflowState\x12\x16\n\x0estatus_message\x18\x03 \x01(\t\x12\x38\n\x11workflow_progress\x18\x04 \x01(\x0b\x32\x1d.octoml.octomizer.v1.Progress\x12\x33\n\x06result\x18\x05 \x01(\x0b\x32#.octoml.octomizer.v1.WorkflowResult\x12\x38\n\rerror_details\x18\x06 \x01(\x0b\x32!.octoml.octomizer.v1.ErrorDetails\x12=\n\x16\x63urrent_stage_progress\x18\x08 \x01(\x0b\x32\x1d.octoml.octomizer.v1.Progress\"_\n\rWorkflowState\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0b\n\x07PENDING\x10\x01\x12\x0b\n\x07RUNNING\x10\x02\x12\r\n\tCOMPLETED\x10\x03\x12\n\n\x06\x46\x41ILED\x10\x04\x12\x0c\n\x08\x43\x41NCELED\x10\x05J\x04\x08\x07\x10\x08\"8\n\x08Progress\x12\x17\n\x0f\x63ompleted_steps\x18\x01 \x01(\r\x12\x13\n\x0btotal_steps\x18\x02 \x01(\r\"\xdf\x01\n\x0eWorkflowResult\x12\x41\n\x0f\x61utotune_result\x18\x01 \x01(\x0b\x32(.octoml.octomizer.v1.AutotuneStageResult\x12\x43\n\x10\x62\x65nchmark_result\x18\x02 \x01(\x0b\x32).octoml.octomizer.v1.BenchmarkStageResult\x12?\n\x0epackage_result\x18\x03 \x01(\x0b\x32\'.octoml.octomizer.v1.PackageStageResultJ\x04\x08\x04\x10\x05\"\x1e\n\x16WorkflowFailureDetailsJ\x04\x08\x01\x10\x02\"\xdb\x03\n\x14PackageWorkflowGroup\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x12\n\nmodel_uuid\x18\x02 \x01(\t\x12\x1a\n\x12model_variant_uuid\x18\x03 \x01(\t\x12@\n\x11\x61\x63\x63\x65leration_mode\x18\x04 \x01(\x0e\x32%.octoml.octomizer.v1.AccelerationMode\x12\x36\n\x0cmodel_inputs\x18\x05 \x01(\x0b\x32 .octoml.octomizer.v1.ModelInputs\x12\x33\n\x08hardware\x18\x06 \x01(\x0b\x32!.octoml.octomizer.v1.HardwareSpec\x12\x14\n\x0cpackage_name\x18\x07 \x01(\t\x12I\n\x08metadata\x18\x08 \x03(\x0b\x32\x37.octoml.octomizer.v1.PackageWorkflowGroup.MetadataEntry\x12\x12\n\ncreated_by\x18\t \x01(\t\x12\x30\n\tworkflows\x18\n \x03(\x0b\x32\x1d.octoml.octomizer.v1.Workflow\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01*G\n\x10\x41\x63\x63\x65lerationMode\x12\x08\n\x04\x41UTO\x10\x00\x12\n\n\x06NORMAL\x10\x01\x12\x0c\n\x08\x45XTENDED\x10\x02\x12\x0b\n\x07\x45XPRESS\x10\x01\x1a\x02\x10\x01\x42\x45ZCgitlab.com/octoml/platform/protobufs/golang/gen/octoml/octomizer/v1b\x06proto3'
  ,
  dependencies=[octoml_dot_octomizer_dot_v1_dot_hardware__pb2.DESCRIPTOR,octoml_dot_octomizer_dot_v1_dot_autotune__pb2.DESCRIPTOR,octoml_dot_octomizer_dot_v1_dot_benchmark__pb2.DESCRIPTOR,octoml_dot_octomizer_dot_v1_dot_package__pb2.DESCRIPTOR,octoml_dot_octomizer_dot_v1_dot_error__pb2.DESCRIPTOR,octoml_dot_octomizer_dot_v1_dot_model__inputs__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])

_ACCELERATIONMODE = _descriptor.EnumDescriptor(
  name='AccelerationMode',
  full_name='octoml.octomizer.v1.AccelerationMode',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='AUTO', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NORMAL', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='EXTENDED', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='EXPRESS', index=3, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=b'\020\001',
  serialized_start=2239,
  serialized_end=2310,
)
_sym_db.RegisterEnumDescriptor(_ACCELERATIONMODE)

AccelerationMode = enum_type_wrapper.EnumTypeWrapper(_ACCELERATIONMODE)
AUTO = 0
NORMAL = 1
EXTENDED = 2
EXPRESS = 1


_WORKFLOWSTATUS_WORKFLOWSTATE = _descriptor.EnumDescriptor(
  name='WorkflowState',
  full_name='octoml.octomizer.v1.WorkflowStatus.WorkflowState',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PENDING', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RUNNING', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='COMPLETED', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FAILED', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CANCELED', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1342,
  serialized_end=1437,
)
_sym_db.RegisterEnumDescriptor(_WORKFLOWSTATUS_WORKFLOWSTATE)


_WORKFLOW_METADATAENTRY = _descriptor.Descriptor(
  name='MetadataEntry',
  full_name='octoml.octomizer.v1.Workflow.MetadataEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='octoml.octomizer.v1.Workflow.MetadataEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='octoml.octomizer.v1.Workflow.MetadataEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=899,
  serialized_end=946,
)

_WORKFLOW = _descriptor.Descriptor(
  name='Workflow',
  full_name='octoml.octomizer.v1.Workflow',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='octoml.octomizer.v1.Workflow.uuid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='model_uuid', full_name='octoml.octomizer.v1.Workflow.model_uuid', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='model_variant_uuid', full_name='octoml.octomizer.v1.Workflow.model_variant_uuid', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='octoml.octomizer.v1.Workflow.status', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='hardware', full_name='octoml.octomizer.v1.Workflow.hardware', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='autotune_stage_spec', full_name='octoml.octomizer.v1.Workflow.autotune_stage_spec', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='benchmark_stage_spec', full_name='octoml.octomizer.v1.Workflow.benchmark_stage_spec', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='package_stage_spec', full_name='octoml.octomizer.v1.Workflow.package_stage_spec', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='create_time', full_name='octoml.octomizer.v1.Workflow.create_time', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='update_time', full_name='octoml.octomizer.v1.Workflow.update_time', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='created_by', full_name='octoml.octomizer.v1.Workflow.created_by', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='octoml.octomizer.v1.Workflow.metadata', index=11,
      number=13, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='group_uuid', full_name='octoml.octomizer.v1.Workflow.group_uuid', index=12,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_WORKFLOW_METADATAENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=311,
  serialized_end=952,
)


_WORKFLOWSTATUS = _descriptor.Descriptor(
  name='WorkflowStatus',
  full_name='octoml.octomizer.v1.WorkflowStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='octoml.octomizer.v1.WorkflowStatus.timestamp', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='state', full_name='octoml.octomizer.v1.WorkflowStatus.state', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status_message', full_name='octoml.octomizer.v1.WorkflowStatus.status_message', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='workflow_progress', full_name='octoml.octomizer.v1.WorkflowStatus.workflow_progress', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='result', full_name='octoml.octomizer.v1.WorkflowStatus.result', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='error_details', full_name='octoml.octomizer.v1.WorkflowStatus.error_details', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='current_stage_progress', full_name='octoml.octomizer.v1.WorkflowStatus.current_stage_progress', index=6,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _WORKFLOWSTATUS_WORKFLOWSTATE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=955,
  serialized_end=1443,
)


_PROGRESS = _descriptor.Descriptor(
  name='Progress',
  full_name='octoml.octomizer.v1.Progress',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='completed_steps', full_name='octoml.octomizer.v1.Progress.completed_steps', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='total_steps', full_name='octoml.octomizer.v1.Progress.total_steps', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1445,
  serialized_end=1501,
)


_WORKFLOWRESULT = _descriptor.Descriptor(
  name='WorkflowResult',
  full_name='octoml.octomizer.v1.WorkflowResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='autotune_result', full_name='octoml.octomizer.v1.WorkflowResult.autotune_result', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='benchmark_result', full_name='octoml.octomizer.v1.WorkflowResult.benchmark_result', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='package_result', full_name='octoml.octomizer.v1.WorkflowResult.package_result', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1504,
  serialized_end=1727,
)


_WORKFLOWFAILUREDETAILS = _descriptor.Descriptor(
  name='WorkflowFailureDetails',
  full_name='octoml.octomizer.v1.WorkflowFailureDetails',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=1729,
  serialized_end=1759,
)


_PACKAGEWORKFLOWGROUP_METADATAENTRY = _descriptor.Descriptor(
  name='MetadataEntry',
  full_name='octoml.octomizer.v1.PackageWorkflowGroup.MetadataEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='octoml.octomizer.v1.PackageWorkflowGroup.MetadataEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='octoml.octomizer.v1.PackageWorkflowGroup.MetadataEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=899,
  serialized_end=946,
)

_PACKAGEWORKFLOWGROUP = _descriptor.Descriptor(
  name='PackageWorkflowGroup',
  full_name='octoml.octomizer.v1.PackageWorkflowGroup',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='octoml.octomizer.v1.PackageWorkflowGroup.uuid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='model_uuid', full_name='octoml.octomizer.v1.PackageWorkflowGroup.model_uuid', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='model_variant_uuid', full_name='octoml.octomizer.v1.PackageWorkflowGroup.model_variant_uuid', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='acceleration_mode', full_name='octoml.octomizer.v1.PackageWorkflowGroup.acceleration_mode', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='model_inputs', full_name='octoml.octomizer.v1.PackageWorkflowGroup.model_inputs', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='hardware', full_name='octoml.octomizer.v1.PackageWorkflowGroup.hardware', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='package_name', full_name='octoml.octomizer.v1.PackageWorkflowGroup.package_name', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='octoml.octomizer.v1.PackageWorkflowGroup.metadata', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='created_by', full_name='octoml.octomizer.v1.PackageWorkflowGroup.created_by', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='workflows', full_name='octoml.octomizer.v1.PackageWorkflowGroup.workflows', index=9,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_PACKAGEWORKFLOWGROUP_METADATAENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1762,
  serialized_end=2237,
)

_WORKFLOW_METADATAENTRY.containing_type = _WORKFLOW
_WORKFLOW.fields_by_name['status'].message_type = _WORKFLOWSTATUS
_WORKFLOW.fields_by_name['hardware'].message_type = octoml_dot_octomizer_dot_v1_dot_hardware__pb2._HARDWARESPEC
_WORKFLOW.fields_by_name['autotune_stage_spec'].message_type = octoml_dot_octomizer_dot_v1_dot_autotune__pb2._AUTOTUNESTAGESPEC
_WORKFLOW.fields_by_name['benchmark_stage_spec'].message_type = octoml_dot_octomizer_dot_v1_dot_benchmark__pb2._BENCHMARKSTAGESPEC
_WORKFLOW.fields_by_name['package_stage_spec'].message_type = octoml_dot_octomizer_dot_v1_dot_package__pb2._PACKAGESTAGESPEC
_WORKFLOW.fields_by_name['create_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_WORKFLOW.fields_by_name['update_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_WORKFLOW.fields_by_name['metadata'].message_type = _WORKFLOW_METADATAENTRY
_WORKFLOWSTATUS.fields_by_name['timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_WORKFLOWSTATUS.fields_by_name['state'].enum_type = _WORKFLOWSTATUS_WORKFLOWSTATE
_WORKFLOWSTATUS.fields_by_name['workflow_progress'].message_type = _PROGRESS
_WORKFLOWSTATUS.fields_by_name['result'].message_type = _WORKFLOWRESULT
_WORKFLOWSTATUS.fields_by_name['error_details'].message_type = octoml_dot_octomizer_dot_v1_dot_error__pb2._ERRORDETAILS
_WORKFLOWSTATUS.fields_by_name['current_stage_progress'].message_type = _PROGRESS
_WORKFLOWSTATUS_WORKFLOWSTATE.containing_type = _WORKFLOWSTATUS
_WORKFLOWRESULT.fields_by_name['autotune_result'].message_type = octoml_dot_octomizer_dot_v1_dot_autotune__pb2._AUTOTUNESTAGERESULT
_WORKFLOWRESULT.fields_by_name['benchmark_result'].message_type = octoml_dot_octomizer_dot_v1_dot_benchmark__pb2._BENCHMARKSTAGERESULT
_WORKFLOWRESULT.fields_by_name['package_result'].message_type = octoml_dot_octomizer_dot_v1_dot_package__pb2._PACKAGESTAGERESULT
_PACKAGEWORKFLOWGROUP_METADATAENTRY.containing_type = _PACKAGEWORKFLOWGROUP
_PACKAGEWORKFLOWGROUP.fields_by_name['acceleration_mode'].enum_type = _ACCELERATIONMODE
_PACKAGEWORKFLOWGROUP.fields_by_name['model_inputs'].message_type = octoml_dot_octomizer_dot_v1_dot_model__inputs__pb2._MODELINPUTS
_PACKAGEWORKFLOWGROUP.fields_by_name['hardware'].message_type = octoml_dot_octomizer_dot_v1_dot_hardware__pb2._HARDWARESPEC
_PACKAGEWORKFLOWGROUP.fields_by_name['metadata'].message_type = _PACKAGEWORKFLOWGROUP_METADATAENTRY
_PACKAGEWORKFLOWGROUP.fields_by_name['workflows'].message_type = _WORKFLOW
DESCRIPTOR.message_types_by_name['Workflow'] = _WORKFLOW
DESCRIPTOR.message_types_by_name['WorkflowStatus'] = _WORKFLOWSTATUS
DESCRIPTOR.message_types_by_name['Progress'] = _PROGRESS
DESCRIPTOR.message_types_by_name['WorkflowResult'] = _WORKFLOWRESULT
DESCRIPTOR.message_types_by_name['WorkflowFailureDetails'] = _WORKFLOWFAILUREDETAILS
DESCRIPTOR.message_types_by_name['PackageWorkflowGroup'] = _PACKAGEWORKFLOWGROUP
DESCRIPTOR.enum_types_by_name['AccelerationMode'] = _ACCELERATIONMODE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Workflow = _reflection.GeneratedProtocolMessageType('Workflow', (_message.Message,), {

  'MetadataEntry' : _reflection.GeneratedProtocolMessageType('MetadataEntry', (_message.Message,), {
    'DESCRIPTOR' : _WORKFLOW_METADATAENTRY,
    '__module__' : 'octoml.octomizer.v1.workflows_pb2'
    # @@protoc_insertion_point(class_scope:octoml.octomizer.v1.Workflow.MetadataEntry)
    })
  ,
  'DESCRIPTOR' : _WORKFLOW,
  '__module__' : 'octoml.octomizer.v1.workflows_pb2'
  # @@protoc_insertion_point(class_scope:octoml.octomizer.v1.Workflow)
  })
_sym_db.RegisterMessage(Workflow)
_sym_db.RegisterMessage(Workflow.MetadataEntry)

WorkflowStatus = _reflection.GeneratedProtocolMessageType('WorkflowStatus', (_message.Message,), {
  'DESCRIPTOR' : _WORKFLOWSTATUS,
  '__module__' : 'octoml.octomizer.v1.workflows_pb2'
  # @@protoc_insertion_point(class_scope:octoml.octomizer.v1.WorkflowStatus)
  })
_sym_db.RegisterMessage(WorkflowStatus)

Progress = _reflection.GeneratedProtocolMessageType('Progress', (_message.Message,), {
  'DESCRIPTOR' : _PROGRESS,
  '__module__' : 'octoml.octomizer.v1.workflows_pb2'
  # @@protoc_insertion_point(class_scope:octoml.octomizer.v1.Progress)
  })
_sym_db.RegisterMessage(Progress)

WorkflowResult = _reflection.GeneratedProtocolMessageType('WorkflowResult', (_message.Message,), {
  'DESCRIPTOR' : _WORKFLOWRESULT,
  '__module__' : 'octoml.octomizer.v1.workflows_pb2'
  # @@protoc_insertion_point(class_scope:octoml.octomizer.v1.WorkflowResult)
  })
_sym_db.RegisterMessage(WorkflowResult)

WorkflowFailureDetails = _reflection.GeneratedProtocolMessageType('WorkflowFailureDetails', (_message.Message,), {
  'DESCRIPTOR' : _WORKFLOWFAILUREDETAILS,
  '__module__' : 'octoml.octomizer.v1.workflows_pb2'
  # @@protoc_insertion_point(class_scope:octoml.octomizer.v1.WorkflowFailureDetails)
  })
_sym_db.RegisterMessage(WorkflowFailureDetails)

PackageWorkflowGroup = _reflection.GeneratedProtocolMessageType('PackageWorkflowGroup', (_message.Message,), {

  'MetadataEntry' : _reflection.GeneratedProtocolMessageType('MetadataEntry', (_message.Message,), {
    'DESCRIPTOR' : _PACKAGEWORKFLOWGROUP_METADATAENTRY,
    '__module__' : 'octoml.octomizer.v1.workflows_pb2'
    # @@protoc_insertion_point(class_scope:octoml.octomizer.v1.PackageWorkflowGroup.MetadataEntry)
    })
  ,
  'DESCRIPTOR' : _PACKAGEWORKFLOWGROUP,
  '__module__' : 'octoml.octomizer.v1.workflows_pb2'
  # @@protoc_insertion_point(class_scope:octoml.octomizer.v1.PackageWorkflowGroup)
  })
_sym_db.RegisterMessage(PackageWorkflowGroup)
_sym_db.RegisterMessage(PackageWorkflowGroup.MetadataEntry)


DESCRIPTOR._options = None
_ACCELERATIONMODE._options = None
_WORKFLOW_METADATAENTRY._options = None
_PACKAGEWORKFLOWGROUP_METADATAENTRY._options = None
# @@protoc_insertion_point(module_scope)
