import math
import struct

q0 = 0.5
q1 = 0.15
q2 = 0.35
q3 = 0.15

roll = math.atan2(2 * (q0 * q1 + q2 * q3), 1 - 2 * (q1 * q1 + q2 * q2)) 
pitch = math.asin(2 * (q0 * q2 - q3 * q1))                             
yaw = math.atan2(2 * (q0 * q3 + q1 * q2), 1 - 2 * (q2 * q2 + q3 * q3))

print(roll, pitch, yaw)
testlist = [0,0]
print(len(testlist))

stringData = "akajsdfkja lsdjkf lakjsdfl ajksdf lkajs dlfj alksdjf laj dlf jalsdj flajsds"
packed = struct.pack("=200p", bytes(stringData,'ascii'))
print("packed:", packed)
unpacked = struct.unpack("=200p",packed)
print("unpacked:", unpacked)
print("data:", unpacked[0])


