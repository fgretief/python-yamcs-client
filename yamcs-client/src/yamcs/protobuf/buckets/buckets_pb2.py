# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yamcs/protobuf/buckets/buckets.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from yamcs.api import annotations_pb2 as yamcs_dot_api_dot_annotations__pb2
from yamcs.api import httpbody_pb2 as yamcs_dot_api_dot_httpbody__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yamcs/protobuf/buckets/buckets.proto',
  package='yamcs.protobuf.buckets',
  syntax='proto2',
  serialized_options=_b('\n\022org.yamcs.protobufB\014BucketsProtoP\001'),
  serialized_pb=_b('\n$yamcs/protobuf/buckets/buckets.proto\x12\x16yamcs.protobuf.buckets\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1byamcs/api/annotations.proto\x1a\x18yamcs/api/httpbody.proto\"5\n\x13\x43reateBucketRequest\x12\x10\n\x08instance\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\";\n\x13\x44\x65leteBucketRequest\x12\x10\n\x08instance\x18\x01 \x01(\t\x12\x12\n\nbucketName\x18\x02 \x01(\t\"L\n\x10GetObjectRequest\x12\x10\n\x08instance\x18\x01 \x01(\t\x12\x12\n\nbucketName\x18\x02 \x01(\t\x12\x12\n\nobjectName\x18\x03 \x01(\t\"O\n\x13\x44\x65leteObjectRequest\x12\x10\n\x08instance\x18\x01 \x01(\t\x12\x12\n\nbucketName\x18\x02 \x01(\t\x12\x12\n\nobjectName\x18\x03 \x01(\t\"r\n\x13UploadObjectRequest\x12\x10\n\x08instance\x18\x01 \x01(\t\x12\x12\n\nbucketName\x18\x02 \x01(\t\x12\x12\n\nobjectName\x18\x03 \x01(\t\x12!\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\x13.yamcs.api.HttpBody\"\xa1\x01\n\nBucketInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04size\x18\x02 \x01(\x04\x12\x12\n\nnumObjects\x18\x03 \x01(\r\x12\x0f\n\x07maxSize\x18\x04 \x01(\x04\x12\x12\n\nmaxObjects\x18\x05 \x01(\r\x12+\n\x07\x63reated\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x11\n\tdirectory\x18\x07 \x01(\t\"\xca\x01\n\nObjectInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12+\n\x07\x63reated\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04size\x18\x03 \x01(\x04\x12\x42\n\x08metadata\x18\x04 \x03(\x0b\x32\x30.yamcs.protobuf.buckets.ObjectInfo.MetadataEntry\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"&\n\x12ListBucketsRequest\x12\x10\n\x08instance\x18\x01 \x01(\t\"8\n\x10GetBucketRequest\x12\x10\n\x08instance\x18\x01 \x01(\t\x12\x12\n\nbucketName\x18\x02 \x01(\t\"J\n\x13ListBucketsResponse\x12\x33\n\x07\x62uckets\x18\x01 \x03(\x0b\x32\".yamcs.protobuf.buckets.BucketInfo\"]\n\x12ListObjectsRequest\x12\x10\n\x08instance\x18\x01 \x01(\t\x12\x12\n\nbucketName\x18\x02 \x01(\t\x12\x11\n\tdelimiter\x18\x03 \x01(\t\x12\x0e\n\x06prefix\x18\x04 \x01(\t\"\\\n\x13ListObjectsResponse\x12\x10\n\x08prefixes\x18\x01 \x03(\t\x12\x33\n\x07objects\x18\x02 \x03(\x0b\x32\".yamcs.protobuf.buckets.ObjectInfo2\x85\t\n\nBucketsApi\x12\x85\x01\n\x0bListBuckets\x12*.yamcs.protobuf.buckets.ListBucketsRequest\x1a+.yamcs.protobuf.buckets.ListBucketsResponse\"\x1d\x8a\x92\x03\x19\n\x17/api/buckets/{instance}\x12\x85\x01\n\tGetBucket\x12(.yamcs.protobuf.buckets.GetBucketRequest\x1a\".yamcs.protobuf.buckets.BucketInfo\"*\x8a\x92\x03&\n$/api/buckets/{instance}/{bucketName}\x12u\n\x0c\x43reateBucket\x12+.yamcs.protobuf.buckets.CreateBucketRequest\x1a\x16.google.protobuf.Empty\" \x8a\x92\x03\x1c\x1a\x17/api/buckets/{instance}:\x01*\x12\x7f\n\x0c\x44\x65leteBucket\x12+.yamcs.protobuf.buckets.DeleteBucketRequest\x1a\x16.google.protobuf.Empty\"*\x8a\x92\x03&\"$/api/buckets/{instance}/{bucketName}\x12\x8c\x01\n\tGetObject\x12(.yamcs.protobuf.buckets.GetObjectRequest\x1a\x13.yamcs.api.HttpBody\"@\x8a\x92\x03<\n:/api/buckets/{instance}/{bucketName}/objects/{objectName*}\x12\xa1\x01\n\x0cUploadObject\x12+.yamcs.protobuf.buckets.UploadObjectRequest\x1a\x16.google.protobuf.Empty\"L\x8a\x92\x03H\x1a;/api/buckets/{instance}/{bucketName}/objects/{objectName**}:\x04\x64\x61ta@\x80\x80\xc0\x02\x12\xa3\x01\n\x0bListObjects\x12*.yamcs.protobuf.buckets.ListObjectsRequest\x1a+.yamcs.protobuf.buckets.ListObjectsResponse\";\x8a\x92\x03\x37\n,/api/buckets/{instance}/{bucketName}/objectsR\x07objects\x12\x95\x01\n\x0c\x44\x65leteObject\x12+.yamcs.protobuf.buckets.DeleteObjectRequest\x1a\x16.google.protobuf.Empty\"@\x8a\x92\x03<\":/api/buckets/{instance}/{bucketName}/objects/{objectName*}B$\n\x12org.yamcs.protobufB\x0c\x42ucketsProtoP\x01')
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,yamcs_dot_api_dot_annotations__pb2.DESCRIPTOR,yamcs_dot_api_dot_httpbody__pb2.DESCRIPTOR,])




_CREATEBUCKETREQUEST = _descriptor.Descriptor(
  name='CreateBucketRequest',
  full_name='yamcs.protobuf.buckets.CreateBucketRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance', full_name='yamcs.protobuf.buckets.CreateBucketRequest.instance', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='yamcs.protobuf.buckets.CreateBucketRequest.name', index=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=181,
  serialized_end=234,
)


_DELETEBUCKETREQUEST = _descriptor.Descriptor(
  name='DeleteBucketRequest',
  full_name='yamcs.protobuf.buckets.DeleteBucketRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance', full_name='yamcs.protobuf.buckets.DeleteBucketRequest.instance', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bucketName', full_name='yamcs.protobuf.buckets.DeleteBucketRequest.bucketName', index=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=236,
  serialized_end=295,
)


_GETOBJECTREQUEST = _descriptor.Descriptor(
  name='GetObjectRequest',
  full_name='yamcs.protobuf.buckets.GetObjectRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance', full_name='yamcs.protobuf.buckets.GetObjectRequest.instance', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bucketName', full_name='yamcs.protobuf.buckets.GetObjectRequest.bucketName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='objectName', full_name='yamcs.protobuf.buckets.GetObjectRequest.objectName', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=297,
  serialized_end=373,
)


_DELETEOBJECTREQUEST = _descriptor.Descriptor(
  name='DeleteObjectRequest',
  full_name='yamcs.protobuf.buckets.DeleteObjectRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance', full_name='yamcs.protobuf.buckets.DeleteObjectRequest.instance', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bucketName', full_name='yamcs.protobuf.buckets.DeleteObjectRequest.bucketName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='objectName', full_name='yamcs.protobuf.buckets.DeleteObjectRequest.objectName', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=375,
  serialized_end=454,
)


_UPLOADOBJECTREQUEST = _descriptor.Descriptor(
  name='UploadObjectRequest',
  full_name='yamcs.protobuf.buckets.UploadObjectRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance', full_name='yamcs.protobuf.buckets.UploadObjectRequest.instance', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bucketName', full_name='yamcs.protobuf.buckets.UploadObjectRequest.bucketName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='objectName', full_name='yamcs.protobuf.buckets.UploadObjectRequest.objectName', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='yamcs.protobuf.buckets.UploadObjectRequest.data', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=456,
  serialized_end=570,
)


_BUCKETINFO = _descriptor.Descriptor(
  name='BucketInfo',
  full_name='yamcs.protobuf.buckets.BucketInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='yamcs.protobuf.buckets.BucketInfo.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='size', full_name='yamcs.protobuf.buckets.BucketInfo.size', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='numObjects', full_name='yamcs.protobuf.buckets.BucketInfo.numObjects', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='maxSize', full_name='yamcs.protobuf.buckets.BucketInfo.maxSize', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='maxObjects', full_name='yamcs.protobuf.buckets.BucketInfo.maxObjects', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created', full_name='yamcs.protobuf.buckets.BucketInfo.created', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='directory', full_name='yamcs.protobuf.buckets.BucketInfo.directory', index=6,
      number=7, type=9, cpp_type=9, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=573,
  serialized_end=734,
)


_OBJECTINFO_METADATAENTRY = _descriptor.Descriptor(
  name='MetadataEntry',
  full_name='yamcs.protobuf.buckets.ObjectInfo.MetadataEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='yamcs.protobuf.buckets.ObjectInfo.MetadataEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='yamcs.protobuf.buckets.ObjectInfo.MetadataEntry.value', index=1,
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
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=892,
  serialized_end=939,
)

_OBJECTINFO = _descriptor.Descriptor(
  name='ObjectInfo',
  full_name='yamcs.protobuf.buckets.ObjectInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='yamcs.protobuf.buckets.ObjectInfo.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created', full_name='yamcs.protobuf.buckets.ObjectInfo.created', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='size', full_name='yamcs.protobuf.buckets.ObjectInfo.size', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='yamcs.protobuf.buckets.ObjectInfo.metadata', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_OBJECTINFO_METADATAENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=737,
  serialized_end=939,
)


_LISTBUCKETSREQUEST = _descriptor.Descriptor(
  name='ListBucketsRequest',
  full_name='yamcs.protobuf.buckets.ListBucketsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance', full_name='yamcs.protobuf.buckets.ListBucketsRequest.instance', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=941,
  serialized_end=979,
)


_GETBUCKETREQUEST = _descriptor.Descriptor(
  name='GetBucketRequest',
  full_name='yamcs.protobuf.buckets.GetBucketRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance', full_name='yamcs.protobuf.buckets.GetBucketRequest.instance', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bucketName', full_name='yamcs.protobuf.buckets.GetBucketRequest.bucketName', index=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=981,
  serialized_end=1037,
)


_LISTBUCKETSRESPONSE = _descriptor.Descriptor(
  name='ListBucketsResponse',
  full_name='yamcs.protobuf.buckets.ListBucketsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='buckets', full_name='yamcs.protobuf.buckets.ListBucketsResponse.buckets', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1039,
  serialized_end=1113,
)


_LISTOBJECTSREQUEST = _descriptor.Descriptor(
  name='ListObjectsRequest',
  full_name='yamcs.protobuf.buckets.ListObjectsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance', full_name='yamcs.protobuf.buckets.ListObjectsRequest.instance', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bucketName', full_name='yamcs.protobuf.buckets.ListObjectsRequest.bucketName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='delimiter', full_name='yamcs.protobuf.buckets.ListObjectsRequest.delimiter', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prefix', full_name='yamcs.protobuf.buckets.ListObjectsRequest.prefix', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1115,
  serialized_end=1208,
)


_LISTOBJECTSRESPONSE = _descriptor.Descriptor(
  name='ListObjectsResponse',
  full_name='yamcs.protobuf.buckets.ListObjectsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='prefixes', full_name='yamcs.protobuf.buckets.ListObjectsResponse.prefixes', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='objects', full_name='yamcs.protobuf.buckets.ListObjectsResponse.objects', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1210,
  serialized_end=1302,
)

_UPLOADOBJECTREQUEST.fields_by_name['data'].message_type = yamcs_dot_api_dot_httpbody__pb2._HTTPBODY
_BUCKETINFO.fields_by_name['created'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_OBJECTINFO_METADATAENTRY.containing_type = _OBJECTINFO
_OBJECTINFO.fields_by_name['created'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_OBJECTINFO.fields_by_name['metadata'].message_type = _OBJECTINFO_METADATAENTRY
_LISTBUCKETSRESPONSE.fields_by_name['buckets'].message_type = _BUCKETINFO
_LISTOBJECTSRESPONSE.fields_by_name['objects'].message_type = _OBJECTINFO
DESCRIPTOR.message_types_by_name['CreateBucketRequest'] = _CREATEBUCKETREQUEST
DESCRIPTOR.message_types_by_name['DeleteBucketRequest'] = _DELETEBUCKETREQUEST
DESCRIPTOR.message_types_by_name['GetObjectRequest'] = _GETOBJECTREQUEST
DESCRIPTOR.message_types_by_name['DeleteObjectRequest'] = _DELETEOBJECTREQUEST
DESCRIPTOR.message_types_by_name['UploadObjectRequest'] = _UPLOADOBJECTREQUEST
DESCRIPTOR.message_types_by_name['BucketInfo'] = _BUCKETINFO
DESCRIPTOR.message_types_by_name['ObjectInfo'] = _OBJECTINFO
DESCRIPTOR.message_types_by_name['ListBucketsRequest'] = _LISTBUCKETSREQUEST
DESCRIPTOR.message_types_by_name['GetBucketRequest'] = _GETBUCKETREQUEST
DESCRIPTOR.message_types_by_name['ListBucketsResponse'] = _LISTBUCKETSRESPONSE
DESCRIPTOR.message_types_by_name['ListObjectsRequest'] = _LISTOBJECTSREQUEST
DESCRIPTOR.message_types_by_name['ListObjectsResponse'] = _LISTOBJECTSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateBucketRequest = _reflection.GeneratedProtocolMessageType('CreateBucketRequest', (_message.Message,), dict(
  DESCRIPTOR = _CREATEBUCKETREQUEST,
  __module__ = 'yamcs.protobuf.buckets.buckets_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.buckets.CreateBucketRequest)
  ))
_sym_db.RegisterMessage(CreateBucketRequest)

DeleteBucketRequest = _reflection.GeneratedProtocolMessageType('DeleteBucketRequest', (_message.Message,), dict(
  DESCRIPTOR = _DELETEBUCKETREQUEST,
  __module__ = 'yamcs.protobuf.buckets.buckets_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.buckets.DeleteBucketRequest)
  ))
_sym_db.RegisterMessage(DeleteBucketRequest)

GetObjectRequest = _reflection.GeneratedProtocolMessageType('GetObjectRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETOBJECTREQUEST,
  __module__ = 'yamcs.protobuf.buckets.buckets_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.buckets.GetObjectRequest)
  ))
_sym_db.RegisterMessage(GetObjectRequest)

DeleteObjectRequest = _reflection.GeneratedProtocolMessageType('DeleteObjectRequest', (_message.Message,), dict(
  DESCRIPTOR = _DELETEOBJECTREQUEST,
  __module__ = 'yamcs.protobuf.buckets.buckets_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.buckets.DeleteObjectRequest)
  ))
_sym_db.RegisterMessage(DeleteObjectRequest)

UploadObjectRequest = _reflection.GeneratedProtocolMessageType('UploadObjectRequest', (_message.Message,), dict(
  DESCRIPTOR = _UPLOADOBJECTREQUEST,
  __module__ = 'yamcs.protobuf.buckets.buckets_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.buckets.UploadObjectRequest)
  ))
_sym_db.RegisterMessage(UploadObjectRequest)

BucketInfo = _reflection.GeneratedProtocolMessageType('BucketInfo', (_message.Message,), dict(
  DESCRIPTOR = _BUCKETINFO,
  __module__ = 'yamcs.protobuf.buckets.buckets_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.buckets.BucketInfo)
  ))
_sym_db.RegisterMessage(BucketInfo)

ObjectInfo = _reflection.GeneratedProtocolMessageType('ObjectInfo', (_message.Message,), dict(

  MetadataEntry = _reflection.GeneratedProtocolMessageType('MetadataEntry', (_message.Message,), dict(
    DESCRIPTOR = _OBJECTINFO_METADATAENTRY,
    __module__ = 'yamcs.protobuf.buckets.buckets_pb2'
    # @@protoc_insertion_point(class_scope:yamcs.protobuf.buckets.ObjectInfo.MetadataEntry)
    ))
  ,
  DESCRIPTOR = _OBJECTINFO,
  __module__ = 'yamcs.protobuf.buckets.buckets_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.buckets.ObjectInfo)
  ))
_sym_db.RegisterMessage(ObjectInfo)
_sym_db.RegisterMessage(ObjectInfo.MetadataEntry)

ListBucketsRequest = _reflection.GeneratedProtocolMessageType('ListBucketsRequest', (_message.Message,), dict(
  DESCRIPTOR = _LISTBUCKETSREQUEST,
  __module__ = 'yamcs.protobuf.buckets.buckets_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.buckets.ListBucketsRequest)
  ))
_sym_db.RegisterMessage(ListBucketsRequest)

GetBucketRequest = _reflection.GeneratedProtocolMessageType('GetBucketRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETBUCKETREQUEST,
  __module__ = 'yamcs.protobuf.buckets.buckets_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.buckets.GetBucketRequest)
  ))
_sym_db.RegisterMessage(GetBucketRequest)

ListBucketsResponse = _reflection.GeneratedProtocolMessageType('ListBucketsResponse', (_message.Message,), dict(
  DESCRIPTOR = _LISTBUCKETSRESPONSE,
  __module__ = 'yamcs.protobuf.buckets.buckets_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.buckets.ListBucketsResponse)
  ))
_sym_db.RegisterMessage(ListBucketsResponse)

ListObjectsRequest = _reflection.GeneratedProtocolMessageType('ListObjectsRequest', (_message.Message,), dict(
  DESCRIPTOR = _LISTOBJECTSREQUEST,
  __module__ = 'yamcs.protobuf.buckets.buckets_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.buckets.ListObjectsRequest)
  ))
_sym_db.RegisterMessage(ListObjectsRequest)

ListObjectsResponse = _reflection.GeneratedProtocolMessageType('ListObjectsResponse', (_message.Message,), dict(
  DESCRIPTOR = _LISTOBJECTSRESPONSE,
  __module__ = 'yamcs.protobuf.buckets.buckets_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.buckets.ListObjectsResponse)
  ))
_sym_db.RegisterMessage(ListObjectsResponse)


DESCRIPTOR._options = None
_OBJECTINFO_METADATAENTRY._options = None

_BUCKETSAPI = _descriptor.ServiceDescriptor(
  name='BucketsApi',
  full_name='yamcs.protobuf.buckets.BucketsApi',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1305,
  serialized_end=2462,
  methods=[
  _descriptor.MethodDescriptor(
    name='ListBuckets',
    full_name='yamcs.protobuf.buckets.BucketsApi.ListBuckets',
    index=0,
    containing_service=None,
    input_type=_LISTBUCKETSREQUEST,
    output_type=_LISTBUCKETSRESPONSE,
    serialized_options=_b('\212\222\003\031\n\027/api/buckets/{instance}'),
  ),
  _descriptor.MethodDescriptor(
    name='GetBucket',
    full_name='yamcs.protobuf.buckets.BucketsApi.GetBucket',
    index=1,
    containing_service=None,
    input_type=_GETBUCKETREQUEST,
    output_type=_BUCKETINFO,
    serialized_options=_b('\212\222\003&\n$/api/buckets/{instance}/{bucketName}'),
  ),
  _descriptor.MethodDescriptor(
    name='CreateBucket',
    full_name='yamcs.protobuf.buckets.BucketsApi.CreateBucket',
    index=2,
    containing_service=None,
    input_type=_CREATEBUCKETREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=_b('\212\222\003\034\032\027/api/buckets/{instance}:\001*'),
  ),
  _descriptor.MethodDescriptor(
    name='DeleteBucket',
    full_name='yamcs.protobuf.buckets.BucketsApi.DeleteBucket',
    index=3,
    containing_service=None,
    input_type=_DELETEBUCKETREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=_b('\212\222\003&\"$/api/buckets/{instance}/{bucketName}'),
  ),
  _descriptor.MethodDescriptor(
    name='GetObject',
    full_name='yamcs.protobuf.buckets.BucketsApi.GetObject',
    index=4,
    containing_service=None,
    input_type=_GETOBJECTREQUEST,
    output_type=yamcs_dot_api_dot_httpbody__pb2._HTTPBODY,
    serialized_options=_b('\212\222\003<\n:/api/buckets/{instance}/{bucketName}/objects/{objectName*}'),
  ),
  _descriptor.MethodDescriptor(
    name='UploadObject',
    full_name='yamcs.protobuf.buckets.BucketsApi.UploadObject',
    index=5,
    containing_service=None,
    input_type=_UPLOADOBJECTREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=_b('\212\222\003H\032;/api/buckets/{instance}/{bucketName}/objects/{objectName**}:\004data@\200\200\300\002'),
  ),
  _descriptor.MethodDescriptor(
    name='ListObjects',
    full_name='yamcs.protobuf.buckets.BucketsApi.ListObjects',
    index=6,
    containing_service=None,
    input_type=_LISTOBJECTSREQUEST,
    output_type=_LISTOBJECTSRESPONSE,
    serialized_options=_b('\212\222\0037\n,/api/buckets/{instance}/{bucketName}/objectsR\007objects'),
  ),
  _descriptor.MethodDescriptor(
    name='DeleteObject',
    full_name='yamcs.protobuf.buckets.BucketsApi.DeleteObject',
    index=7,
    containing_service=None,
    input_type=_DELETEOBJECTREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=_b('\212\222\003<\":/api/buckets/{instance}/{bucketName}/objects/{objectName*}'),
  ),
])
_sym_db.RegisterServiceDescriptor(_BUCKETSAPI)

DESCRIPTOR.services_by_name['BucketsApi'] = _BUCKETSAPI

# @@protoc_insertion_point(module_scope)
