#!/bin/python3
# Sebastian Kind 2023 Python3 Rodos-Middleware
import struct
import rodos
import time


def topicHandler(data):
    try:
        # print("handling topic")
        # print(data)
        # print(len(data))
        # size = struct.calcsize('4sIddd')
        # buff = ctypes.create_string_buffer(size)
        # unpacked = struct.unpack_from('4sIddd', buff, 0)
        print("-----------handling topic------------")
        print("unpacked data",data)
        unpacked = struct.unpack("i", data)
        print(unpacked)
        # print("timeNow = ", unpacked[0])  # <-- print values that were sent from c++ rodos
        # print("msg = ", unpacked[1])  # <-- print values that were sent from c++ rodos
        # print("int1 = ", unpacked[2])  # <-- print values that were sent from c++ rodos
        # print("int2 = ", unpacked[3])  # <-- print values that were sent from c++ rodos
        # print("int3 = ", unpacked[4])  # <-- print values that were sent from c++ rodos
        # print("timeNow = ", unpacked[0])  # <-- print values that were sent from c++ rodos
    except Exception as e:
        print("error while handling topic")
        print(e)
        # print(len(data))
        # print(data)



try:
    print("Starting client")
    linux2rodos = rodos.Topic(1002)
    rodos2linux = rodos.Topic(1003)
    print("topic created")
    # rodos2linux.addSubscriber(topicHandler)
    linux2rodos.addSubscriber(topicHandler)
    print("subscriber added")

    li = rodos.LinkinterfaceUDP(63455)
    gwUDP = rodos.Gateway(li)
    gwUDP.run()

    while True:
        msg = li.messageQueue.get()
        print(msg)

        # data = struct.unpack("i",msg)
        # print(data)

        print('-------------------------------------')
        # topicHandler(li.getNetworkMsg())

        time.sleep(1)
except Exception as e:
    print(e)

