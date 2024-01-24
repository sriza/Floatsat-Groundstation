# rodos-middleware: This file is a part of the Master Thesis of Sebastian Kind 2023
import threading
import time

from .linkinterface import *
from .networkmessage import *
from .topic import *


class Gateway():

    forwardingToppings = []
    parsestring = "!HiQIIhH"

    def __init__(self, linkinterface: LinkinterfaceI):
        self.li: linkinterface.LinkinterfaceI = linkinterface
        """Linkinterface of this Gateway"""
        pass

    def run(self):
        target = threading.Thread(target=self.__run, args=[])
        target.daemon = True
        target.start()

    def __run(self):
        while True:
            # polling loop uses select() syscall internally in waits
            # for new data print("main loop")
            # print("polling for message")
            self.pollMessage()

    def pollMessage(self):
        try:
            # print("message check")
            # print(self.li.getNetworkMsg())
            msg = self.li.getNetworkMsg()
            print("message found")
            self.analyseAndDistributeMessagesFromNetwork(msg)
        except Exception as e:
            # print("exception:", e)
            # print ("error in pollMessage")
            pass

    def prepareMessage(self):
        pass

    # fixme: code dirty here, make a beatiful parser in
    # networkmessages.py later
    def analyseAndDistributeMessagesFromNetwork(self, data):
        try:
            """parse message from LinkInterface and decide which topic to
            deliver it to"""
            print("data")
            print(bytes(data))

            receivedMsg = NetworkMessage(data)
            print("received data", receivedMsg)
            # assign right topic number, etc etc
            receivedMsg.parseHeader(self.li.BIGENDIAN_P)

            # debug print
            try:
                pass
                #print("Calced Checksum = {:02X},   transmittedChecksum = {:02X}".format(receivedMsg.calcChecksum(), receivedMsg.checksum))
            except Exception as e:
                print(e)


            # print(receivedMsg)
            # print(receivedMsg.header)
            # cheap hack ignore own messages on loopback device, big and little endian of magic number
            #print("analyse and distribute")
            # if receivedMsg.senderNode == 0xFF or receivedMsg.senderNode == 41716:
                #print("\n\ndropp message\n\n")
                #raise Exception("dropp")
                # return

            size = len(data)
            if receivedMsg.topicid >= 1000:
                print("whats the size", size, receivedMsg.topicid)
            #print("size = ", size)
            if size < 26:
                print("header broken")
                return

            # for top in self.topicPutter:
            #print("distribute to local topics")
            for top in localTopics:
                #print(top.topicId, receivedMsg.topicid)
                if top.topicId == receivedMsg.topicid:
                    top.publishFromGateway(receivedMsg.userDataC)
                    # print(top, receivedMsg.userDataC)

            pass
        except Exception as e:
            print(e)

    # gatewayhandler
    def forwardHandler(self, data, topicId):
        """Handler that is called, whenever a topic needs to forward
        data over a gateway"""
        try:
            # print("forwared handler of ", topicId)
            msg = NetworkMessage()
            msg.topicid = topicId
            msg.len = len(data)
            # print("under network message", msg.len)
            # print(msg.topicid, msg.len)
            msg.userDataC = data
            if msg.topicid >= 1000:
                print(msg.topicid, len(msg.userDataC))
            msg.senderNode = 0xFF
            msg.updateHeader()
            # print(msg, msg.userDataC)
            self.sendNetworkMessage(msg)  # this cant be right
            # print("message", msg.userDataC)
            # print("under topicid")
            pass
        except Exception as e:
            print("exception forward handler")
            print(e)
    

    def sendNetworkMessage(self, msg: NetworkMessage):
        # header = struct.pack("!iIhHHHiqII", -2, 0, 0, 0, 0, 36+len(data), 0,0 ,0, 1003)
        # msg = header + data
        msg.sentTime = time.time_ns()

        msg.senderNode = 0xFF
        print(msg)
        msg.updateHeader()
        msg.checksum = msg.calcChecksum()

        self.li.sendNetworkMsg(msg)
        # print("wrote this to linkinterface", msg.userDataC)
        # print(msg)

    def forwardTopic(self, topicp: Topic):
        self.forwardingToppings.append(topicp)

        print("forwarding topic", topicp)
        topicp.gwHandlers.append(self.forwardHandler)
        print(topicp.gwHandlers)

# void prepareNetworkMessage(NetworkMessage& netMsg, const uint32_t topicId,const void* data, size_t len, const NetMsgInfo& netMsgInfo) {
    def prepareNetworkMessage(self, msg: NetworkMessage, topicID:int, data: bytes, size: int):
        msg.topicid =  topicID
        msg.userDataC = data
        msg.sentTime = time.time_ns()
        pass