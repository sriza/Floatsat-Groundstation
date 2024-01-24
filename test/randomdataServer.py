# this randomDataServer.py is udp server generating random data for given topics

import time
import struct
from struct import *
from rodos import Gateway
from rodos import LinkinterfaceUDP
from rodos import Topic
import json
import sys

# sys.setrecursionlimit(10)


# from rodos import *


luart = LinkinterfaceUDP()
gwUart = Gateway(luart)
telemetry = {}

def initializeTopics():
    try:
        print("data initialized")
        f = open("../Assets/data.json")
        json_array = json.load(f)

        for item in json_array:
            dataStruct = json_array[item]

            # initialization of topic
            topic = Topic(dataStruct["topicId"])
            gwUart.forwardTopic(topic) 

            telemetry[item] = {}
            telemetry[item]["topic"] = topic

            # # copy remaining data to structure
            telemetry[item]["topicId"] = dataStruct["topicId"]
            telemetry[item]["structure"] = dataStruct["structure"]
            telemetry[item]["data"] = {}

            # # copy the structure of data
            for datum in dataStruct["data"]:
                telemetry[item]["data"][datum] = 1 

            print(item)

    except Exception as e:
        print(e)

def setAndPublish(cnt):
    try:
        for tele_name in telemetry:
            print(tele_name)
            data_array = []

            for datum in telemetry[tele_name]["data"]:
                new_value = (telemetry[tele_name]["data"][datum]+cnt)%360
                telemetry[tele_name]["data"][datum] = new_value
                data_array.append(new_value)

            dataStruct = struct.pack(telemetry[tele_name]["structure"],*tuple(data_array))

            (telemetry[tele_name]["topic"]).publish(dataStruct)

    except Exception as e:
        print(e)

initializeTopics()


cnt = 0

while cnt<50:
    setAndPublish(cnt)

    # sendMe = struct.pack("i",  cnt)
    # linux2rodos.publish(sendMe)
    # print("sendMe")

    # print(struct.unpack("I", sendMe))
    print("------------------------")

    cnt += 1
    time.sleep(4)