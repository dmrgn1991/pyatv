# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pyatv/protocols/mrp/protobuf/NowPlayingClient.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3pyatv/protocols/mrp/protobuf/NowPlayingClient.proto\"\xe8\x01\n\x10NowPlayingClient\x12\x19\n\x11processIdentifier\x18\x01 \x01(\x05\x12\x18\n\x10\x62undleIdentifier\x18\x02 \x01(\t\x12)\n!parentApplicationBundleIdentifier\x18\x03 \x01(\t\x12\x1d\n\x15processUserIdentifier\x18\x04 \x01(\x05\x12\x1c\n\x14nowPlayingVisibility\x18\x05 \x01(\x05\x12\x13\n\x0b\x64isplayName\x18\x07 \x01(\t\x12\"\n\x1a\x62undleIdentifierHierarchys\x18\x08 \x03(\t')



_NOWPLAYINGCLIENT = DESCRIPTOR.message_types_by_name['NowPlayingClient']
NowPlayingClient = _reflection.GeneratedProtocolMessageType('NowPlayingClient', (_message.Message,), {
  'DESCRIPTOR' : _NOWPLAYINGCLIENT,
  '__module__' : 'pyatv.protocols.mrp.protobuf.NowPlayingClient_pb2'
  # @@protoc_insertion_point(class_scope:NowPlayingClient)
  })
_sym_db.RegisterMessage(NowPlayingClient)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _NOWPLAYINGCLIENT._serialized_start=56
  _NOWPLAYINGCLIENT._serialized_end=288
# @@protoc_insertion_point(module_scope)
