# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pyatv/protocols/mrp/protobuf/SendButtonEventMessage.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyatv.protocols.mrp.protobuf import ProtocolMessage_pb2 as pyatv_dot_protocols_dot_mrp_dot_protobuf_dot_ProtocolMessage__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9pyatv/protocols/mrp/protobuf/SendButtonEventMessage.proto\x1a\x32pyatv/protocols/mrp/protobuf/ProtocolMessage.proto\"N\n\x16SendButtonEventMessage\x12\x11\n\tusagePage\x18\x01 \x01(\r\x12\r\n\x05usage\x18\x02 \x01(\r\x12\x12\n\nbuttonDown\x18\x03 \x01(\x08:I\n\x16sendButtonEventMessage\x12\x10.ProtocolMessage\x18+ \x01(\x0b\x32\x17.SendButtonEventMessage')


SENDBUTTONEVENTMESSAGE_FIELD_NUMBER = 43
sendButtonEventMessage = DESCRIPTOR.extensions_by_name['sendButtonEventMessage']

_SENDBUTTONEVENTMESSAGE = DESCRIPTOR.message_types_by_name['SendButtonEventMessage']
SendButtonEventMessage = _reflection.GeneratedProtocolMessageType('SendButtonEventMessage', (_message.Message,), {
  'DESCRIPTOR' : _SENDBUTTONEVENTMESSAGE,
  '__module__' : 'pyatv.protocols.mrp.protobuf.SendButtonEventMessage_pb2'
  # @@protoc_insertion_point(class_scope:SendButtonEventMessage)
  })
_sym_db.RegisterMessage(SendButtonEventMessage)

if _descriptor._USE_C_DESCRIPTORS == False:
  pyatv_dot_protocols_dot_mrp_dot_protobuf_dot_ProtocolMessage__pb2.ProtocolMessage.RegisterExtension(sendButtonEventMessage)

  DESCRIPTOR._options = None
  _SENDBUTTONEVENTMESSAGE._serialized_start=113
  _SENDBUTTONEVENTMESSAGE._serialized_end=191
# @@protoc_insertion_point(module_scope)
