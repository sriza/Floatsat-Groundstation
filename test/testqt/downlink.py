#!/bin/python3
# Sebastian Kind 2023 Python3 Rodos-Middleware
# import struct
import rodos
import time
import struct


def topicHandler(data):
    try:
        # print("reached topic handler")
        pass
        # print("------------within the topic handler------------")
        # print('received data',data)
    
        # # unpacked = struct.unpack('<10f', data)
        unpacked = struct.unpack("=ii19f", data)
        # unpacked = struct.unpack('<c', data)
        print(unpacked)
        print("--------------------------------------------")
        # print("timeNow = ", unpacked[0])  # <-- print values that were sent from c++ rodos
        # print("msg = ", unpacked[1])  # <-- print values that were sent from c++ rodos
    except Exception as e:
        print("")
        print("error while handling topic")
        print(e)
        # print(len(data))
        # print(data)

def topicEchoHandler(data):
    try:
        # print("reached topic handler")
        pass
        print("------------within the echo topic handler------------")
        # print('received data',data)
        print("echo received", data)
        # # unpacked = struct.unpack('<10f', data)
        unpacked = struct.unpack("=i3f", data)
        # unpacked = struct.unpack('<c', data)
        print(unpacked)
        print("--------------------------------------------")
        # print("timeNow = ", unpacked[0])  # <-- print values that were sent from c++ rodos
        # print("msg = ", unpacked[1])  # <-- print values that were sent from c++ rodos
    except Exception as e:
        print("")
        print("error while handling topic")
        print(e)
        # print(len(data))
        # print(data)

try:
    print("Starting client")
    stm2rodos = rodos.Topic(40)
    # echo2rodos = rodos.Topic(60) #receive echo
    rodos2stm = rodos.Topic(50) #send echo command
    print("topic created")
    stm2rodos.addSubscriber(topicHandler)
    # echo2rodos.addSubscriber(topicEchoHandler)
    print("subscriber added")

    # changed MARK in linkinterfactUART.py
    liUart = rodos.LinkinterfaceUART(path="COM3")
    gwUDP = rodos.Gateway(liUart)
    gwUDP.forwardTopic(rodos2stm)
    gwUDP.run()

    # liUart_server = rodos.LinkinterfaceUART(path="COM3")
    # gwUDP_

    cnt = 0

    while True:
        # print("sending data to stm")
        sendData = struct.pack("i3f", 5,0,0,0)
        # sendData = struct.pack("f", 65.0)
        # print("sendData:", sendData)
        rodos2stm.publish(sendData)
        print("published")
        # msg = liUart.messageQueue.get()
        # print(msg)

        # data = struct.unpack("i",msg)
        # print(data)

        # print('-------------------------------------')
        # topicHandler(li.getNetworkMsg())
        cnt+=1
        time.sleep(2)
except Exception as e:
    print("exception",e) 

