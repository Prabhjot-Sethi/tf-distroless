#
# Autogenerated by Sandesh Compiler (1.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py:new_style
# Copyright (c) 2013 Juniper Networks, Inc. All rights reserved.
#


# This autogenerated skeleton file illustrates the implementation of
# derived class to handle the sandesh request.


# Create a derived class from "SandeshTraceRequest" to handle 
# the sandesh request. Add this derived class "SandeshTraceRequest_derived"
# in module SandeshTraceRequest_derived.py and add it in your package

class SandeshTraceRequest_derived(SandeshTraceRequest):

  def __init__(self):
    SandeshTraceRequest.__init__(self, buf_name=None, count=None)

  def handle_request(self):
    # Add your code to handle the "SandeshTraceRequest" request
    pass
  

# Create a derived class from "SandeshTraceBufferListRequest" to handle 
# the sandesh request. Add this derived class "SandeshTraceBufferListRequest_derived"
# in module SandeshTraceBufferListRequest_derived.py and add it in your package

class SandeshTraceBufferListRequest_derived(SandeshTraceBufferListRequest):


  def handle_request(self):
    # Add your code to handle the "SandeshTraceBufferListRequest" request
    pass
  

# Create a derived class from "SandeshTraceEnableDisableReq" to handle 
# the sandesh request. Add this derived class "SandeshTraceEnableDisableReq_derived"
# in module SandeshTraceEnableDisableReq_derived.py and add it in your package

class SandeshTraceEnableDisableReq_derived(SandeshTraceEnableDisableReq):

  def __init__(self):
    SandeshTraceEnableDisableReq.__init__(self, enable=None)

  def handle_request(self):
    # Add your code to handle the "SandeshTraceEnableDisableReq" request
    pass
  

# Create a derived class from "SandeshTraceBufStatusReq" to handle 
# the sandesh request. Add this derived class "SandeshTraceBufStatusReq_derived"
# in module SandeshTraceBufStatusReq_derived.py and add it in your package

class SandeshTraceBufStatusReq_derived(SandeshTraceBufStatusReq):


  def handle_request(self):
    # Add your code to handle the "SandeshTraceBufStatusReq" request
    pass
  

# Create a derived class from "SandeshTraceBufferEnableDisableReq" to handle 
# the sandesh request. Add this derived class "SandeshTraceBufferEnableDisableReq_derived"
# in module SandeshTraceBufferEnableDisableReq_derived.py and add it in your package

class SandeshTraceBufferEnableDisableReq_derived(SandeshTraceBufferEnableDisableReq):

  def __init__(self):
    SandeshTraceBufferEnableDisableReq.__init__(self, trace_buf_name=None, enable=None)

  def handle_request(self):
    # Add your code to handle the "SandeshTraceBufferEnableDisableReq" request
    pass
  