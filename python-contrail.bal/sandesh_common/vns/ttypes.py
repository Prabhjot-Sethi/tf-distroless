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


class Module(object):
  CONTROL_NODE = 0
  VROUTER_AGENT = 1
  API_SERVER = 2
  SCHEMA_TRANSFORMER = 3
  OPSERVER = 4
  COLLECTOR = 5
  QUERY_ENGINE = 6
  SVC_MONITOR = 7
  DEVICE_MANAGER = 8
  DNS = 9
  DISCOVERY_SERVICE = 10
  IFMAP_SERVER = 11
  XMPP_SERVER = 12
  ANALYTICS_NODE_MGR = 13
  ANALYTICS_SNMP_NODE_MGR = 14
  ANALYTICS_ALARM_NODE_MGR = 15
  CONTROL_NODE_MGR = 16
  CONFIG_NODE_MGR = 17
  DATABASE_NODE_MGR = 18
  WEBUI_NODE_MGR = 19
  COMPUTE_NODE_MGR = 20
  STORAGE_STATS_MGR = 21
  IPMI_STATS_MGR = 22
  CONTRAIL_SNMP_COLLECTOR = 23
  CONTRAIL_TOPOLOGY = 24
  INVENTORY_AGENT = 25
  ALARM_GENERATOR = 26
  TOR_AGENT = 27
  CONTRAIL_BROADVIEW = 28
  KUBE_MANAGER = 29
  MESOS_MANAGER = 30
  MAX_MODULE = 31
  IRONIC_NOTIF_MANAGER = 32
  FABRIC_ANSIBLE = 33
  CONFIG_DATABASE_NODE_MGR = 34
  VCENTER_MANAGER = 35
  VCENTER_FABRIC_MANAGER = 36

  _VALUES_TO_NAMES = {
    0: "CONTROL_NODE",
    1: "VROUTER_AGENT",
    2: "API_SERVER",
    3: "SCHEMA_TRANSFORMER",
    4: "OPSERVER",
    5: "COLLECTOR",
    6: "QUERY_ENGINE",
    7: "SVC_MONITOR",
    8: "DEVICE_MANAGER",
    9: "DNS",
    10: "DISCOVERY_SERVICE",
    11: "IFMAP_SERVER",
    12: "XMPP_SERVER",
    13: "ANALYTICS_NODE_MGR",
    14: "ANALYTICS_SNMP_NODE_MGR",
    15: "ANALYTICS_ALARM_NODE_MGR",
    16: "CONTROL_NODE_MGR",
    17: "CONFIG_NODE_MGR",
    18: "DATABASE_NODE_MGR",
    19: "WEBUI_NODE_MGR",
    20: "COMPUTE_NODE_MGR",
    21: "STORAGE_STATS_MGR",
    22: "IPMI_STATS_MGR",
    23: "CONTRAIL_SNMP_COLLECTOR",
    24: "CONTRAIL_TOPOLOGY",
    25: "INVENTORY_AGENT",
    26: "ALARM_GENERATOR",
    27: "TOR_AGENT",
    28: "CONTRAIL_BROADVIEW",
    29: "KUBE_MANAGER",
    30: "MESOS_MANAGER",
    31: "MAX_MODULE",
    32: "IRONIC_NOTIF_MANAGER",
    33: "FABRIC_ANSIBLE",
    34: "CONFIG_DATABASE_NODE_MGR",
    35: "VCENTER_MANAGER",
    36: "VCENTER_FABRIC_MANAGER",
  }

  _NAMES_TO_VALUES = {
    "CONTROL_NODE": 0,
    "VROUTER_AGENT": 1,
    "API_SERVER": 2,
    "SCHEMA_TRANSFORMER": 3,
    "OPSERVER": 4,
    "COLLECTOR": 5,
    "QUERY_ENGINE": 6,
    "SVC_MONITOR": 7,
    "DEVICE_MANAGER": 8,
    "DNS": 9,
    "DISCOVERY_SERVICE": 10,
    "IFMAP_SERVER": 11,
    "XMPP_SERVER": 12,
    "ANALYTICS_NODE_MGR": 13,
    "ANALYTICS_SNMP_NODE_MGR": 14,
    "ANALYTICS_ALARM_NODE_MGR": 15,
    "CONTROL_NODE_MGR": 16,
    "CONFIG_NODE_MGR": 17,
    "DATABASE_NODE_MGR": 18,
    "WEBUI_NODE_MGR": 19,
    "COMPUTE_NODE_MGR": 20,
    "STORAGE_STATS_MGR": 21,
    "IPMI_STATS_MGR": 22,
    "CONTRAIL_SNMP_COLLECTOR": 23,
    "CONTRAIL_TOPOLOGY": 24,
    "INVENTORY_AGENT": 25,
    "ALARM_GENERATOR": 26,
    "TOR_AGENT": 27,
    "CONTRAIL_BROADVIEW": 28,
    "KUBE_MANAGER": 29,
    "MESOS_MANAGER": 30,
    "MAX_MODULE": 31,
    "IRONIC_NOTIF_MANAGER": 32,
    "FABRIC_ANSIBLE": 33,
    "CONFIG_DATABASE_NODE_MGR": 34,
    "VCENTER_MANAGER": 35,
    "VCENTER_FABRIC_MANAGER": 36,
  }

class VrouterAgentType(object):
  VROUTER_AGENT_TOR = 0
  VROUTER_AGENT_TSN = 1
  VROUTER_AGENT_EMBEDDED = 2

  _VALUES_TO_NAMES = {
    0: "VROUTER_AGENT_TOR",
    1: "VROUTER_AGENT_TSN",
    2: "VROUTER_AGENT_EMBEDDED",
  }

  _NAMES_TO_VALUES = {
    "VROUTER_AGENT_TOR": 0,
    "VROUTER_AGENT_TSN": 1,
    "VROUTER_AGENT_EMBEDDED": 2,
  }

class VrouterAgentPlatformType(object):
  VROUTER_AGENT_ON_NIC = 0
  VROUTER_AGENT_ON_HOST_DPDK = 1
  VROUTER_AGENT_ON_WINDOWS = 2
  VROUTER_AGENT_ON_HOST = 3

  _VALUES_TO_NAMES = {
    0: "VROUTER_AGENT_ON_NIC",
    1: "VROUTER_AGENT_ON_HOST_DPDK",
    2: "VROUTER_AGENT_ON_WINDOWS",
    3: "VROUTER_AGENT_ON_HOST",
  }

  _NAMES_TO_VALUES = {
    "VROUTER_AGENT_ON_NIC": 0,
    "VROUTER_AGENT_ON_HOST_DPDK": 1,
    "VROUTER_AGENT_ON_WINDOWS": 2,
    "VROUTER_AGENT_ON_HOST": 3,
  }

class VrouterAgentVmState(object):
  VROUTER_AGENT_VM_ACTIVE = 0
  VROUTER_AGENT_VM_PAUSED = 1
  VROUTER_AGENT_VM_SHUTDOWN = 2
  VROUTER_AGENT_VM_UNKNOWN = 3

  _VALUES_TO_NAMES = {
    0: "VROUTER_AGENT_VM_ACTIVE",
    1: "VROUTER_AGENT_VM_PAUSED",
    2: "VROUTER_AGENT_VM_SHUTDOWN",
    3: "VROUTER_AGENT_VM_UNKNOWN",
  }

  _NAMES_TO_VALUES = {
    "VROUTER_AGENT_VM_ACTIVE": 0,
    "VROUTER_AGENT_VM_PAUSED": 1,
    "VROUTER_AGENT_VM_SHUTDOWN": 2,
    "VROUTER_AGENT_VM_UNKNOWN": 3,
  }

class VrouterAgentGatewayMode(object):
  VCPE = 0
  SERVER = 1
  NONE = 2

  _VALUES_TO_NAMES = {
    0: "VCPE",
    1: "SERVER",
    2: "NONE",
  }

  _NAMES_TO_VALUES = {
    "VCPE": 0,
    "SERVER": 1,
    "NONE": 2,
  }

class NodeType(object):
  INVALID = 0
  CONFIG = 1
  CONTROL = 2
  ANALYTICS = 3
  ANALYTICS_ALARM = 4
  ANALYTICS_SNMP = 5
  COMPUTE = 6
  WEBUI = 7
  DATABASE = 8
  OPENSTACK = 9
  SERVERMGR = 10
  KUBERNETESMGR = 11
  CONFIG_DATABASE = 12

  _VALUES_TO_NAMES = {
    0: "INVALID",
    1: "CONFIG",
    2: "CONTROL",
    3: "ANALYTICS",
    4: "ANALYTICS_ALARM",
    5: "ANALYTICS_SNMP",
    6: "COMPUTE",
    7: "WEBUI",
    8: "DATABASE",
    9: "OPENSTACK",
    10: "SERVERMGR",
    11: "KUBERNETESMGR",
    12: "CONFIG_DATABASE",
  }

  _NAMES_TO_VALUES = {
    "INVALID": 0,
    "CONFIG": 1,
    "CONTROL": 2,
    "ANALYTICS": 3,
    "ANALYTICS_ALARM": 4,
    "ANALYTICS_SNMP": 5,
    "COMPUTE": 6,
    "WEBUI": 7,
    "DATABASE": 8,
    "OPENSTACK": 9,
    "SERVERMGR": 10,
    "KUBERNETESMGR": 11,
    "CONFIG_DATABASE": 12,
  }

class Category(object):
  DEFAULT = 0
  XMPP = 1
  BGP = 2
  BGP_CONFIG = 3
  BGP_PEER = 4
  IFMAP = 5
  IFMAP_AGENT = 6
  IFMAP_PEER = 7
  IFMAP_STATE_MACHINE = 8
  IFMAP_XMPP = 9
  TCP = 10
  ROUTING_INSTANCE = 11
  VROUTER = 12
  DISCOVERY = 13
  DNSAGENT = 14
  DISCOVERYCLIENT = 15
  UDP = 16
  CONFIG_CLIENT = 17
  EQL = 18

  _VALUES_TO_NAMES = {
    0: "DEFAULT",
    1: "XMPP",
    2: "BGP",
    3: "BGP_CONFIG",
    4: "BGP_PEER",
    5: "IFMAP",
    6: "IFMAP_AGENT",
    7: "IFMAP_PEER",
    8: "IFMAP_STATE_MACHINE",
    9: "IFMAP_XMPP",
    10: "TCP",
    11: "ROUTING_INSTANCE",
    12: "VROUTER",
    13: "DISCOVERY",
    14: "DNSAGENT",
    15: "DISCOVERYCLIENT",
    16: "UDP",
    17: "CONFIG_CLIENT",
    18: "EQL",
  }

  _NAMES_TO_VALUES = {
    "DEFAULT": 0,
    "XMPP": 1,
    "BGP": 2,
    "BGP_CONFIG": 3,
    "BGP_PEER": 4,
    "IFMAP": 5,
    "IFMAP_AGENT": 6,
    "IFMAP_PEER": 7,
    "IFMAP_STATE_MACHINE": 8,
    "IFMAP_XMPP": 9,
    "TCP": 10,
    "ROUTING_INSTANCE": 11,
    "VROUTER": 12,
    "DISCOVERY": 13,
    "DNSAGENT": 14,
    "DISCOVERYCLIENT": 15,
    "UDP": 16,
    "CONFIG_CLIENT": 17,
    "EQL": 18,
  }

class TagTypeEnum(object):
  LABEL = 0
  APPLICATION = 1
  TIER = 2
  DEPLOYMENT = 3
  SITE = 4
  NEUTRON_FWAAS = 5

  _VALUES_TO_NAMES = {
    0: "LABEL",
    1: "APPLICATION",
    2: "TIER",
    3: "DEPLOYMENT",
    4: "SITE",
    5: "NEUTRON_FWAAS",
  }

  _NAMES_TO_VALUES = {
    "LABEL": 0,
    "APPLICATION": 1,
    "TIER": 2,
    "DEPLOYMENT": 3,
    "SITE": 4,
    "NEUTRON_FWAAS": 5,
  }



_SANDESH_REQUEST_LIST = [
]


_SANDESH_UVE_LIST = [
]


_SANDESH_ALARM_LIST = [
]