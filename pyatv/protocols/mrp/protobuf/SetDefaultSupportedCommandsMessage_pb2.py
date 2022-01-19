# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pyatv/protocols/mrp/protobuf/SetDefaultSupportedCommandsMessage.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyatv.protocols.mrp.protobuf import ProtocolMessage_pb2 as pyatv_dot_protocols_dot_mrp_dot_protobuf_dot_ProtocolMessage__pb2
from pyatv.protocols.mrp.protobuf import NowPlayingInfo_pb2 as pyatv_dot_protocols_dot_mrp_dot_protobuf_dot_NowPlayingInfo__pb2
from pyatv.protocols.mrp.protobuf import PlaybackQueue_pb2 as pyatv_dot_protocols_dot_mrp_dot_protobuf_dot_PlaybackQueue__pb2
from pyatv.protocols.mrp.protobuf import SupportedCommands_pb2 as pyatv_dot_protocols_dot_mrp_dot_protobuf_dot_SupportedCommands__pb2
from pyatv.protocols.mrp.protobuf import PlaybackQueueCapabilities_pb2 as pyatv_dot_protocols_dot_mrp_dot_protobuf_dot_PlaybackQueueCapabilities__pb2
from pyatv.protocols.mrp.protobuf import PlayerPath_pb2 as pyatv_dot_protocols_dot_mrp_dot_protobuf_dot_PlayerPath__pb2
from pyatv.protocols.mrp.protobuf import PlaybackQueueRequestMessage_pb2 as pyatv_dot_protocols_dot_mrp_dot_protobuf_dot_PlaybackQueueRequestMessage__pb2
from pyatv.protocols.mrp.protobuf import Common_pb2 as pyatv_dot_protocols_dot_mrp_dot_protobuf_dot_Common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nEpyatv/protocols/mrp/protobuf/SetDefaultSupportedCommandsMessage.proto\x1a\x32pyatv/protocols/mrp/protobuf/ProtocolMessage.proto\x1a\x31pyatv/protocols/mrp/protobuf/NowPlayingInfo.proto\x1a\x30pyatv/protocols/mrp/protobuf/PlaybackQueue.proto\x1a\x34pyatv/protocols/mrp/protobuf/SupportedCommands.proto\x1a<pyatv/protocols/mrp/protobuf/PlaybackQueueCapabilities.proto\x1a-pyatv/protocols/mrp/protobuf/PlayerPath.proto\x1a>pyatv/protocols/mrp/protobuf/PlaybackQueueRequestMessage.proto\x1a)pyatv/protocols/mrp/protobuf/Common.proto\"\xa6\x03\n\"SetDefaultSupportedCommandsMessage\x12\'\n\x0enowPlayingInfo\x18\x01 \x01(\x0b\x32\x0f.NowPlayingInfo\x12-\n\x11supportedCommands\x18\x02 \x01(\x0b\x32\x12.SupportedCommands\x12%\n\rplaybackQueue\x18\x03 \x01(\x0b\x32\x0e.PlaybackQueue\x12\x11\n\tdisplayID\x18\x04 \x01(\t\x12\x13\n\x0b\x64isplayName\x18\x05 \x01(\t\x12*\n\rplaybackState\x18\x06 \x01(\x0e\x32\x13.PlaybackState.Enum\x12=\n\x19playbackQueueCapabilities\x18\x08 \x01(\x0b\x32\x1a.PlaybackQueueCapabilities\x12\x1f\n\nplayerPath\x18\t \x01(\x0b\x32\x0b.PlayerPath\x12-\n\x07request\x18\n \x01(\x0b\x32\x1c.PlaybackQueueRequestMessage\x12\x1e\n\x16playbackStateTimestamp\x18\x0b \x01(\x01:a\n\"setDefaultSupportedCommandsMessage\x12\x10.ProtocolMessage\x18K \x01(\x0b\x32#.SetDefaultSupportedCommandsMessage')


SETDEFAULTSUPPORTEDCOMMANDSMESSAGE_FIELD_NUMBER = 75
setDefaultSupportedCommandsMessage = DESCRIPTOR.extensions_by_name['setDefaultSupportedCommandsMessage']

_SETDEFAULTSUPPORTEDCOMMANDSMESSAGE = DESCRIPTOR.message_types_by_name['SetDefaultSupportedCommandsMessage']
SetDefaultSupportedCommandsMessage = _reflection.GeneratedProtocolMessageType('SetDefaultSupportedCommandsMessage', (_message.Message,), {
  'DESCRIPTOR' : _SETDEFAULTSUPPORTEDCOMMANDSMESSAGE,
  '__module__' : 'pyatv.protocols.mrp.protobuf.SetDefaultSupportedCommandsMessage_pb2'
  # @@protoc_insertion_point(class_scope:SetDefaultSupportedCommandsMessage)
  })
_sym_db.RegisterMessage(SetDefaultSupportedCommandsMessage)

if _descriptor._USE_C_DESCRIPTORS == False:
  pyatv_dot_protocols_dot_mrp_dot_protobuf_dot_ProtocolMessage__pb2.ProtocolMessage.RegisterExtension(setDefaultSupportedCommandsMessage)

  DESCRIPTOR._options = None
  _SETDEFAULTSUPPORTEDCOMMANDSMESSAGE._serialized_start=497
  _SETDEFAULTSUPPORTEDCOMMANDSMESSAGE._serialized_end=919
# @@protoc_insertion_point(module_scope)
