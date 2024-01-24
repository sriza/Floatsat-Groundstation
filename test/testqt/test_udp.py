#!/bin/python3
# Sebastian Kind 2023 Python3 Rodos-Middleware
import struct
import rodos
import time


def topicHandler(data):
    try:
        print("in topic handler now")
        unpacked = struct.unpack("=f", data)
        print(unpacked)
        print("timeNow = ", unpacked[0])  # <-- print values that were sent from c++ rodos
        print("msgIndex = ", unpacked[1])
    except Exception as e:
        print(e)
        print(len(data))
        print(data)

# port = 50000

# server
# linux2rodos = rodos.Topic(1003)
# li_server = rodos.LinkinterfaceUDP()
# gwUDP = rodos.Gateway(li_server)
# gwUDP.forwardTopic(linux2rodos)
# gwUDP.run()

# client
# rodos2linux = rodos.Topic(501)
rodos2linux = rodos.Topic(501)
li_client = rodos.LinkinterfaceUDP()
gwUDP_client = rodos.Gateway(li_client)
rodos2linux.addSubscriber(topicHandler)
gwUDP_client.run()

cnt = 0
while True:
    # sendMe = struct.pack("f", 55.5)
    # linux2rodos.publish(sendMe)
    # cnt+=1

    time.sleep(4)