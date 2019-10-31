#
# Autogenerated by Sandesh Compiler (1.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py:new_style
# Copyright (c) 2013 Juniper Networks, Inc. All rights reserved.
#

from pysandesh.Thrift import TType, TMessageType, TException

from pysandesh.transport import TTransport
from pysandesh.protocol import TBinaryProtocol, TProtocol
try:
  from pysandesh.protocol import fastbinary
except:
  fastbinary = None

import cStringIO
import uuid
import netaddr
from sys import getsizeof
from itertools import chain
import bottle
from pysandesh import sandesh_base
from pysandesh.sandesh_http import SandeshHttp
from pysandesh.sandesh_uve import SandeshUVETypeMaps
from pysandesh.util import UTCTimestampUsec, UTCTimestampUsecToString
from pysandesh import util
from pysandesh.gen_py.sandesh.constants import *



class UveVirtualNetworkConfig(object):
  """
  Attributes:
   - name
   - deleted
   - connected_networks
   - partially_connected_networks
   - routing_instance_list
   - total_acl_rules
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'name', None, None, ), # 1
    (2, TType.BOOL, 'deleted', None, None, ), # 2
    None, # 3
    (4, TType.LIST, 'connected_networks', (TType.STRING,None), None, ), # 4
    (5, TType.LIST, 'partially_connected_networks', (TType.STRING,None), None, ), # 5
    (6, TType.LIST, 'routing_instance_list', (TType.STRING,None), None, ), # 6
    (7, TType.I32, 'total_acl_rules', None, None, ), # 7
  )

  def __init__(self, name=None, deleted=None, connected_networks=None, partially_connected_networks=None, routing_instance_list=None, total_acl_rules=None,):
    self.name = name
    self.deleted = deleted
    self.connected_networks = connected_networks
    self.partially_connected_networks = partially_connected_networks
    self.routing_instance_list = routing_instance_list
    self.total_acl_rules = total_acl_rules
    self._table = 'ObjectVNTable'

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return 0
    read_cnt = 0
    length = iprot.readStructBegin()
    if length < 0: return -1
    read_cnt += length
    while True:
      (length, fname, ftype, fid) = iprot.readFieldBegin()
      if length < 0: return -1
      read_cnt += length
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          (length, self.name) = iprot.readString();
          if length < 0: return -1
          read_cnt += length
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.BOOL:
          (length, self.deleted) = iprot.readBool();
          if length < 0: return -1
          read_cnt += length
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.LIST:
          self.connected_networks = []
          (length, _etype3, _size0) = iprot.readListBegin()
          read_cnt += length
          for _i4 in xrange(_size0):
            read_cnt += iprot.readContainerElementBegin()
            (length, _elem5) = iprot.readString();
            if length < 0: return -1
            read_cnt += length
            self.connected_networks.append(_elem5)
            read_cnt += iprot.readContainerElementEnd()
          read_cnt += iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.LIST:
          self.partially_connected_networks = []
          (length, _etype9, _size6) = iprot.readListBegin()
          read_cnt += length
          for _i10 in xrange(_size6):
            read_cnt += iprot.readContainerElementBegin()
            (length, _elem11) = iprot.readString();
            if length < 0: return -1
            read_cnt += length
            self.partially_connected_networks.append(_elem11)
            read_cnt += iprot.readContainerElementEnd()
          read_cnt += iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.LIST:
          self.routing_instance_list = []
          (length, _etype15, _size12) = iprot.readListBegin()
          read_cnt += length
          for _i16 in xrange(_size12):
            read_cnt += iprot.readContainerElementBegin()
            (length, _elem17) = iprot.readString();
            if length < 0: return -1
            read_cnt += length
            self.routing_instance_list.append(_elem17)
            read_cnt += iprot.readContainerElementEnd()
          read_cnt += iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.I32:
          (length, self.total_acl_rules) = iprot.readI32();
          if length < 0: return -1
          read_cnt += length
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      length = iprot.readFieldEnd()
      if length < 0: return -1
      read_cnt += length
    length = iprot.readStructEnd()
    if length < 0: return -1
    read_cnt += length
    return read_cnt

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return 0
    if oprot.writeStructBegin(self.__class__.__name__) < 0: return -1
    if self.name is not None:
      annotations = {}
      if self._table is None or self._table is '': return -1
      annotations['key'] = self._table
      if oprot.writeFieldBegin('name', TType.STRING, 1, annotations) < 0: return -1
      if oprot.writeString(self.name) < 0: return -1
      if oprot.writeFieldEnd() < 0: return -1
    if self.deleted is not None:
      annotations = {}
      if oprot.writeFieldBegin('deleted', TType.BOOL, 2, annotations) < 0: return -1
      if oprot.writeBool(self.deleted) < 0: return -1
      if oprot.writeFieldEnd() < 0: return -1
    if self.connected_networks is not None:
      annotations = {}
      annotations['aggtype'] = 'union'
      if oprot.writeFieldBegin('connected_networks', TType.LIST, 4, annotations) < 0: return -1
      if oprot.writeListBegin(TType.STRING, len(self.connected_networks)) < 0: return -1
      for iter18 in self.connected_networks:
        if oprot.writeContainerElementBegin() < 0: return -1
        if oprot.writeString(iter18) < 0: return -1
        if oprot.writeContainerElementEnd() < 0: return -1
      if oprot.writeListEnd() < 0: return -1
      if oprot.writeFieldEnd() < 0: return -1
    if self.partially_connected_networks is not None:
      annotations = {}
      annotations['aggtype'] = 'union'
      if oprot.writeFieldBegin('partially_connected_networks', TType.LIST, 5, annotations) < 0: return -1
      if oprot.writeListBegin(TType.STRING, len(self.partially_connected_networks)) < 0: return -1
      for iter19 in self.partially_connected_networks:
        if oprot.writeContainerElementBegin() < 0: return -1
        if oprot.writeString(iter19) < 0: return -1
        if oprot.writeContainerElementEnd() < 0: return -1
      if oprot.writeListEnd() < 0: return -1
      if oprot.writeFieldEnd() < 0: return -1
    if self.routing_instance_list is not None:
      annotations = {}
      annotations['aggtype'] = 'union'
      if oprot.writeFieldBegin('routing_instance_list', TType.LIST, 6, annotations) < 0: return -1
      if oprot.writeListBegin(TType.STRING, len(self.routing_instance_list)) < 0: return -1
      for iter20 in self.routing_instance_list:
        if oprot.writeContainerElementBegin() < 0: return -1
        if oprot.writeString(iter20) < 0: return -1
        if oprot.writeContainerElementEnd() < 0: return -1
      if oprot.writeListEnd() < 0: return -1
      if oprot.writeFieldEnd() < 0: return -1
    if self.total_acl_rules is not None:
      annotations = {}
      if oprot.writeFieldBegin('total_acl_rules', TType.I32, 7, annotations) < 0: return -1
      if oprot.writeI32(self.total_acl_rules) < 0: return -1
      if oprot.writeFieldEnd() < 0: return -1
    if oprot.writeFieldStop() < 0: return -1
    if oprot.writeStructEnd() < 0: return -1
    return 0

  def validate(self):
    return


  def log(self):
    log_str = cStringIO.StringIO()
    if self.name is not None:
      log_str.write('name = ')
      log_str.write(self.name)
      log_str.write('  ')
    if self.deleted is not None:
      log_str.write('deleted = ')
      if self.deleted:
        log_str.write('True')
      else:
        log_str.write('False')
      log_str.write('  ')
    if self.connected_networks is not None:
      log_str.write('connected_networks = ')
      log_str.write('[ ')
      for iter21 in self.connected_networks:
        log_str.write(iter21)
        log_str.write(', ')
      log_str.write(' ]')
      log_str.write('  ')
    if self.partially_connected_networks is not None:
      log_str.write('partially_connected_networks = ')
      log_str.write('[ ')
      for iter22 in self.partially_connected_networks:
        log_str.write(iter22)
        log_str.write(', ')
      log_str.write(' ]')
      log_str.write('  ')
    if self.routing_instance_list is not None:
      log_str.write('routing_instance_list = ')
      log_str.write('[ ')
      for iter23 in self.routing_instance_list:
        log_str.write(iter23)
        log_str.write(', ')
      log_str.write(' ]')
      log_str.write('  ')
    if self.total_acl_rules is not None:
      log_str.write('total_acl_rules = ')
      log_str.write(str(self.total_acl_rules))
      log_str.write('  ')
    return log_str.getvalue()

  def __sizeof__(self):
    size = 0
    if self.name is not None:
      size += getsizeof(self.name)
    if self.deleted is not None:
      size += getsizeof(self.deleted)
    if self.connected_networks is not None:
      size += getsizeof(self.connected_networks)
      size += sum(map(getsizeof, self.connected_networks))
    if self.partially_connected_networks is not None:
      size += getsizeof(self.partially_connected_networks)
      size += sum(map(getsizeof, self.partially_connected_networks))
    if self.routing_instance_list is not None:
      size += getsizeof(self.routing_instance_list)
      size += sum(map(getsizeof, self.routing_instance_list))
    if self.total_acl_rules is not None:
      size += getsizeof(self.total_acl_rules)
    return size

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class UveServiceChainData(object):
  """
  Attributes:
   - name
   - deleted
   - source_virtual_network
   - destination_virtual_network
   - source_ports
   - destination_ports
   - protocol
   - direction
   - services
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'name', None, None, ), # 1
    (2, TType.BOOL, 'deleted', None, None, ), # 2
    (3, TType.STRING, 'source_virtual_network', None, None, ), # 3
    (4, TType.STRING, 'destination_virtual_network', None, None, ), # 4
    (5, TType.STRING, 'source_ports', None, None, ), # 5
    (6, TType.STRING, 'destination_ports', None, None, ), # 6
    (7, TType.STRING, 'protocol', None, None, ), # 7
    (8, TType.STRING, 'direction', None, None, ), # 8
    (9, TType.LIST, 'services', (TType.STRING,None), None, ), # 9
  )

  def __init__(self, name=None, deleted=None, source_virtual_network=None, destination_virtual_network=None, source_ports=None, destination_ports=None, protocol=None, direction=None, services=None,):
    self.name = name
    self.deleted = deleted
    self.source_virtual_network = source_virtual_network
    self.destination_virtual_network = destination_virtual_network
    self.source_ports = source_ports
    self.destination_ports = destination_ports
    self.protocol = protocol
    self.direction = direction
    self.services = services
    self._table = 'ServiceChain'

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return 0
    read_cnt = 0
    length = iprot.readStructBegin()
    if length < 0: return -1
    read_cnt += length
    while True:
      (length, fname, ftype, fid) = iprot.readFieldBegin()
      if length < 0: return -1
      read_cnt += length
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          (length, self.name) = iprot.readString();
          if length < 0: return -1
          read_cnt += length
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.BOOL:
          (length, self.deleted) = iprot.readBool();
          if length < 0: return -1
          read_cnt += length
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          (length, self.source_virtual_network) = iprot.readString();
          if length < 0: return -1
          read_cnt += length
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          (length, self.destination_virtual_network) = iprot.readString();
          if length < 0: return -1
          read_cnt += length
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.STRING:
          (length, self.source_ports) = iprot.readString();
          if length < 0: return -1
          read_cnt += length
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.STRING:
          (length, self.destination_ports) = iprot.readString();
          if length < 0: return -1
          read_cnt += length
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.STRING:
          (length, self.protocol) = iprot.readString();
          if length < 0: return -1
          read_cnt += length
        else:
          iprot.skip(ftype)
      elif fid == 8:
        if ftype == TType.STRING:
          (length, self.direction) = iprot.readString();
          if length < 0: return -1
          read_cnt += length
        else:
          iprot.skip(ftype)
      elif fid == 9:
        if ftype == TType.LIST:
          self.services = []
          (length, _etype27, _size24) = iprot.readListBegin()
          read_cnt += length
          for _i28 in xrange(_size24):
            read_cnt += iprot.readContainerElementBegin()
            (length, _elem29) = iprot.readString();
            if length < 0: return -1
            read_cnt += length
            self.services.append(_elem29)
            read_cnt += iprot.readContainerElementEnd()
          read_cnt += iprot.readListEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      length = iprot.readFieldEnd()
      if length < 0: return -1
      read_cnt += length
    length = iprot.readStructEnd()
    if length < 0: return -1
    read_cnt += length
    return read_cnt

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return 0
    if oprot.writeStructBegin(self.__class__.__name__) < 0: return -1
    if self.name is not None:
      annotations = {}
      if self._table is None or self._table is '': return -1
      annotations['key'] = self._table
      if oprot.writeFieldBegin('name', TType.STRING, 1, annotations) < 0: return -1
      if oprot.writeString(self.name) < 0: return -1
      if oprot.writeFieldEnd() < 0: return -1
    if self.deleted is not None:
      annotations = {}
      if oprot.writeFieldBegin('deleted', TType.BOOL, 2, annotations) < 0: return -1
      if oprot.writeBool(self.deleted) < 0: return -1
      if oprot.writeFieldEnd() < 0: return -1
    if self.source_virtual_network is not None:
      annotations = {}
      if oprot.writeFieldBegin('source_virtual_network', TType.STRING, 3, annotations) < 0: return -1
      if oprot.writeString(self.source_virtual_network) < 0: return -1
      if oprot.writeFieldEnd() < 0: return -1
    if self.destination_virtual_network is not None:
      annotations = {}
      if oprot.writeFieldBegin('destination_virtual_network', TType.STRING, 4, annotations) < 0: return -1
      if oprot.writeString(self.destination_virtual_network) < 0: return -1
      if oprot.writeFieldEnd() < 0: return -1
    if self.source_ports is not None:
      annotations = {}
      if oprot.writeFieldBegin('source_ports', TType.STRING, 5, annotations) < 0: return -1
      if oprot.writeString(self.source_ports) < 0: return -1
      if oprot.writeFieldEnd() < 0: return -1
    if self.destination_ports is not None:
      annotations = {}
      if oprot.writeFieldBegin('destination_ports', TType.STRING, 6, annotations) < 0: return -1
      if oprot.writeString(self.destination_ports) < 0: return -1
      if oprot.writeFieldEnd() < 0: return -1
    if self.protocol is not None:
      annotations = {}
      if oprot.writeFieldBegin('protocol', TType.STRING, 7, annotations) < 0: return -1
      if oprot.writeString(self.protocol) < 0: return -1
      if oprot.writeFieldEnd() < 0: return -1
    if self.direction is not None:
      annotations = {}
      if oprot.writeFieldBegin('direction', TType.STRING, 8, annotations) < 0: return -1
      if oprot.writeString(self.direction) < 0: return -1
      if oprot.writeFieldEnd() < 0: return -1
    if self.services is not None:
      annotations = {}
      if oprot.writeFieldBegin('services', TType.LIST, 9, annotations) < 0: return -1
      if oprot.writeListBegin(TType.STRING, len(self.services)) < 0: return -1
      for iter30 in self.services:
        if oprot.writeContainerElementBegin() < 0: return -1
        if oprot.writeString(iter30) < 0: return -1
        if oprot.writeContainerElementEnd() < 0: return -1
      if oprot.writeListEnd() < 0: return -1
      if oprot.writeFieldEnd() < 0: return -1
    if oprot.writeFieldStop() < 0: return -1
    if oprot.writeStructEnd() < 0: return -1
    return 0

  def validate(self):
    return


  def log(self):
    log_str = cStringIO.StringIO()
    if self.name is not None:
      log_str.write('name = ')
      log_str.write(self.name)
      log_str.write('  ')
    if self.deleted is not None:
      log_str.write('deleted = ')
      if self.deleted:
        log_str.write('True')
      else:
        log_str.write('False')
      log_str.write('  ')
    if self.source_virtual_network is not None:
      log_str.write('source_virtual_network = ')
      log_str.write(self.source_virtual_network)
      log_str.write('  ')
    if self.destination_virtual_network is not None:
      log_str.write('destination_virtual_network = ')
      log_str.write(self.destination_virtual_network)
      log_str.write('  ')
    if self.source_ports is not None:
      log_str.write('source_ports = ')
      log_str.write(self.source_ports)
      log_str.write('  ')
    if self.destination_ports is not None:
      log_str.write('destination_ports = ')
      log_str.write(self.destination_ports)
      log_str.write('  ')
    if self.protocol is not None:
      log_str.write('protocol = ')
      log_str.write(self.protocol)
      log_str.write('  ')
    if self.direction is not None:
      log_str.write('direction = ')
      log_str.write(self.direction)
      log_str.write('  ')
    if self.services is not None:
      log_str.write('services = ')
      log_str.write('[ ')
      for iter31 in self.services:
        log_str.write(iter31)
        log_str.write(', ')
      log_str.write(' ]')
      log_str.write('  ')
    return log_str.getvalue()

  def __sizeof__(self):
    size = 0
    if self.name is not None:
      size += getsizeof(self.name)
    if self.deleted is not None:
      size += getsizeof(self.deleted)
    if self.source_virtual_network is not None:
      size += getsizeof(self.source_virtual_network)
    if self.destination_virtual_network is not None:
      size += getsizeof(self.destination_virtual_network)
    if self.source_ports is not None:
      size += getsizeof(self.source_ports)
    if self.destination_ports is not None:
      size += getsizeof(self.destination_ports)
    if self.protocol is not None:
      size += getsizeof(self.protocol)
    if self.direction is not None:
      size += getsizeof(self.direction)
    if self.services is not None:
      size += getsizeof(self.services)
      size += sum(map(getsizeof, self.services))
    return size

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class UveVirtualNetworkConfigTrace(sandesh_base.SandeshUVE):

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'data', (UveVirtualNetworkConfig, UveVirtualNetworkConfig.thrift_spec), None, ), # 1
  )

  def __init__(self, data=None, table=None, sandesh=sandesh_base.sandesh_global):
    sandesh_base.SandeshUVE.__init__(self)
    self.data = data
    self._scope = sandesh.scope()
    self._module = sandesh.module()
    self._source = sandesh.source_id()
    self._node_type = sandesh.node_type()
    self._instance_id = sandesh.instance_id()
    self._seqnum = 0
    self._timestamp = UTCTimestampUsec()
    self._versionsig = 74672981
    self._hints = 0 | SANDESH_KEY_HINT
    if table is not None:
      self.data._table = table

  def update_uve(self, tdata):
    if self.data.name is not None:
      tdata.name = self.data.name
    if self.data.deleted is not None:
      tdata.deleted = self.data.deleted
    if self.data.connected_networks is not None:
      tdata.connected_networks = self.data.connected_networks
    if self.data.partially_connected_networks is not None:
      tdata.partially_connected_networks = self.data.partially_connected_networks
    if self.data.routing_instance_list is not None:
      tdata.routing_instance_list = self.data.routing_instance_list
    if self.data.total_acl_rules is not None:
      tdata.total_acl_rules = self.data.total_acl_rules
    return tdata

  def log(self, trace=False):
    log_str = cStringIO.StringIO()
    if trace:
      log_str.write(str(self._timestamp))
      log_str.write(' ')
    log_str.write(self.__class__.__name__ + ': ')
    if self.data is not None:
      log_str.write('data = ')
      log_str.write('<<  ')
      log_str.write(self.data.log())
      log_str.write('>>')
      log_str.write('  ')
    return log_str.getvalue()

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return -1
    read_cnt = 0
    (length, sandesh_name) = iprot.readSandeshBegin()
    if length < 0: return -1
    read_cnt += length
    while True:
      (length, fname, ftype, fid) = iprot.readFieldBegin()
      if length < 0: return -1
      read_cnt += length
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRUCT:
          self.data = UveVirtualNetworkConfig()
          read_cnt += self.data.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      length = iprot.readFieldEnd()
      if length < 0: return -1
      read_cnt += length
    length = iprot.readSandeshEnd()
    if length < 0: return -1
    read_cnt += length
    return read_cnt

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return 0
    if oprot.writeSandeshBegin(self.__class__.__name__) < 0: return -1
    if self.data is not None:
      annotations = {}
      if oprot.writeFieldBegin('data', TType.STRUCT, 1, annotations) < 0: return -1
      if self.data.write(oprot) < 0: return -1
      if oprot.writeFieldEnd() < 0: return -1
    if oprot.writeFieldStop() < 0: return -1
    if oprot.writeSandeshEnd() < 0: return -1
    return 0

  def validate(self):
    return


  def compare(self, other):
    if not isinstance(other, self.__class__):
      return False
    if self.data != other.data:
      return False
    return True

  def __sizeof__(self):
    size = 0
    if self.data is not None:
      size += getsizeof(self.data)
    return size

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class UveServiceChain(sandesh_base.SandeshUVE):

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'data', (UveServiceChainData, UveServiceChainData.thrift_spec), None, ), # 1
  )

  def __init__(self, data=None, table=None, sandesh=sandesh_base.sandesh_global):
    sandesh_base.SandeshUVE.__init__(self)
    self.data = data
    self._scope = sandesh.scope()
    self._module = sandesh.module()
    self._source = sandesh.source_id()
    self._node_type = sandesh.node_type()
    self._instance_id = sandesh.instance_id()
    self._seqnum = 0
    self._timestamp = UTCTimestampUsec()
    self._versionsig = 2360766836
    self._hints = 0 | SANDESH_KEY_HINT
    if table is not None:
      self.data._table = table

  def update_uve(self, tdata):
    if self.data.name is not None:
      tdata.name = self.data.name
    if self.data.deleted is not None:
      tdata.deleted = self.data.deleted
    if self.data.source_virtual_network is not None:
      tdata.source_virtual_network = self.data.source_virtual_network
    if self.data.destination_virtual_network is not None:
      tdata.destination_virtual_network = self.data.destination_virtual_network
    if self.data.source_ports is not None:
      tdata.source_ports = self.data.source_ports
    if self.data.destination_ports is not None:
      tdata.destination_ports = self.data.destination_ports
    if self.data.protocol is not None:
      tdata.protocol = self.data.protocol
    if self.data.direction is not None:
      tdata.direction = self.data.direction
    if self.data.services is not None:
      tdata.services = self.data.services
    return tdata

  def log(self, trace=False):
    log_str = cStringIO.StringIO()
    if trace:
      log_str.write(str(self._timestamp))
      log_str.write(' ')
    log_str.write(self.__class__.__name__ + ': ')
    if self.data is not None:
      log_str.write('data = ')
      log_str.write('<<  ')
      log_str.write(self.data.log())
      log_str.write('>>')
      log_str.write('  ')
    return log_str.getvalue()

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return -1
    read_cnt = 0
    (length, sandesh_name) = iprot.readSandeshBegin()
    if length < 0: return -1
    read_cnt += length
    while True:
      (length, fname, ftype, fid) = iprot.readFieldBegin()
      if length < 0: return -1
      read_cnt += length
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRUCT:
          self.data = UveServiceChainData()
          read_cnt += self.data.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      length = iprot.readFieldEnd()
      if length < 0: return -1
      read_cnt += length
    length = iprot.readSandeshEnd()
    if length < 0: return -1
    read_cnt += length
    return read_cnt

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return 0
    if oprot.writeSandeshBegin(self.__class__.__name__) < 0: return -1
    if self.data is not None:
      annotations = {}
      if oprot.writeFieldBegin('data', TType.STRUCT, 1, annotations) < 0: return -1
      if self.data.write(oprot) < 0: return -1
      if oprot.writeFieldEnd() < 0: return -1
    if oprot.writeFieldStop() < 0: return -1
    if oprot.writeSandeshEnd() < 0: return -1
    return 0

  def validate(self):
    return


  def compare(self, other):
    if not isinstance(other, self.__class__):
      return False
    if self.data != other.data:
      return False
    return True

  def __sizeof__(self):
    size = 0
    if self.data is not None:
      size += getsizeof(self.data)
    return size

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)


_SANDESH_REQUEST_LIST = [
]


_SANDESH_UVE_LIST = [
(UveVirtualNetworkConfigTrace, UveVirtualNetworkConfig),
(UveServiceChain, UveServiceChainData),
]


_SANDESH_ALARM_LIST = [
]
