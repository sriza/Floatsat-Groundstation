import struct

cnt = 4
packedData = struct.pack("c", b"a")
unpackedData = struct.unpack('c', packedData)

print(unpackedData)