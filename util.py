import struct


def f2i(float):
  return struct.unpack('<Q', struct.pack('<d', float))[0]

def f2h(float):
  return hex(struct.unpack('<Q', struct.pack('<d', float))[0])

def h2f(hex):
  return struct.unpack('<d', struct.pack('<Q', int(hex,16)))[0]