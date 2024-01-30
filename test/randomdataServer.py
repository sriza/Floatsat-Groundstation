# this randomDataServer.py is udp server generating random data for given topics

import time
import struct
from rodos import Gateway
from rodos import LinkinterfaceUDP
from rodos import Topic
import json
import time

luart = LinkinterfaceUDP()
gwUart = Gateway(luart)
gwUart.run()
telemetry = {}

def initializeTopics():
    try:
        print("data initialized")
        f = open("../Assets/telemetry.json")
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
                telemetry[item]["data"][datum] = 0.0

            print(item)

    except Exception as e:
        print(e)

def initializeTelecommandTopics():
    try:
        print("data initialized telecommand topics")

        print("initializing...")

        # initialization of topic
        topic = Topic(50)
        topic.addSubscriber(testSubscriber)

    except Exception as e:
        print("exception in receiving telecommand", e)

def testSubscriber(data):
    try:
        print("received data")
        unpackedData = struct.unpack("=4f",data)
        # print("unpacked Data:", unpackedData)
    except Exception as e:
        print("exception in receiving data:", e)

def setAndPublish(cnt):
    for tele_name in telemetry:
        try:
            print(tele_name)
            data_array = []
            last_data = 0

            if tele_name == "telemetryMessage":
                print("-----------------telemetry message---------------")
                stringData = "akajsdfkja lsdjkf lakjsdfl ajksdf lkajs dlfj alksdjf laj dlf jalsdj flajsds"
                dataStruct = struct.pack("=200p", bytes(stringData,'ascii'))

            else:    
                for datum in telemetry[tele_name]["data"]:
                    # new_value = (telemetry[tele_name]["data"][datum]+cnt)%360
                    new_value = (int(time.time())+cnt+last_data%15)%360
                    telemetry[tele_name]["data"][datum] = new_value
                    data_array.append(new_value)
                    last_data = new_value

                dataStruct = struct.pack(telemetry[tele_name]["structure"],*tuple(data_array))

            (telemetry[tele_name]["topic"]).publish(dataStruct)

        except Exception as e:
            print("excption on publish: ",e)
            continue

initializeTopics()
initializeTelecommandTopics()


cnt = 0

while True:
    setAndPublish(cnt)

    # sendMe = struct.pack("i",  cnt)
    # linux2rodos.publish(sendMe)
    # print("sendMe")

    # print(struct.unpack("I", sendMe))
    print("------------------------")

    cnt += 1
    
    if cnt==30:
        cnt=0

    time.sleep(2)