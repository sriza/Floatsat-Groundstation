#!/bin/python3


# bare bones example sending data
# make sure to install the library first

import time
import struct
from struct import *
from rodos import Gateway
from rodos import LinkinterfaceUDP
from rodos import Topic


# from rodos import *


port = 63455
luart = LinkinterfaceUDP(port)
gwUart = Gateway(luart)
# gwUart.run()

linux2rodos = Topic(1002)
gwUart.forwardTopic(linux2rodos)  # forward topic to another rodos device

cnt = 0
while True:
    # print("count", cnt)
    sendMe = struct.pack("i",  cnt)
    linux2rodos.publish(sendMe)
    print(sendMe)

    # print(struct.unpack("I", sendMe))
    print("------------------------")

    cnt += 1
    time.sleep(4)
