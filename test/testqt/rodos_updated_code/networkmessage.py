# rodos-middleware: This file is a part of the Master Thesis of Sebastian Kind 2023

import struct

from .checksums import *


"""
Stand 5.7.23

ich habe byteorder probleme? Wenn ich eine Nachricht sende (header big endian), dann kommt er little endian zurück? stimmt das?

"""


class NetworkMessage:
    """Type wich abstracts acces to encapsulated NetworkMessages, enabling easy parsing, formatting and subfield aware manipulation"""
    HEADER_SIZE = 26
    MAX_NETWORK_MESSAGE_LENGTH = 1300

    PARSE_STRING_OG = "!iIhHHHiQII"
    PARSE_STRING = ">HiQIIhH"  # BigEndian
    PARSE_STRING_LE = "@iIhHHHiQII"  # LittleEndian

    def __init__(self, rawBytes=b"", BIGENDIAN_H=True):
        """
        Create new NetworkMessage
        :param rawBytes: binary NetworkMessage, first 36bytes, are big-endian-byteorder header bytes, rest is little endian data
        """

        self.BIGENDIAN_P = BIGENDIAN_H

        self.header = [0] * 7
        self.userDataC = b""
        """userDataC Payload of NetworkMessage, no header, just bytes"""

        self.rawMsg = b""
        self.rawHeader = b""
        self._size = 0
        self.packedH = b""

        if len(rawBytes) != 0:
            self.rawMsg = rawBytes
            self.parseHeader()

        # zero intialize header fields

        # self._receiverNode = 0
        # self._receiverNodeBitMap = 0
        # self._max_StepsToForward = 0
        # self._checksum = 0
        # self._type = 0
        # self._len = 0
        # self._senderNode = 0
        # self._sentTime = 0
        # self._senderThreadId = 0
        # self._topicid = 0

        self._max_StepsToForward = 0
        self._checksum = 0
        self._len = 0
        self._senderNode = 0
        self._sentTime = 0
        self._senderThreadId = 0
        self._topicid = 0
        pass

    def __repr__(self):
        return repr(
            "NetworkMessage: MaxStp = {} Chksum = {}  LEN = {} SenN = {} STime = {} SThreadID = {} TopicID = {}".format(
                self.max_StepsToForward, self.checksum, self.len, self.senderNode, self.sentTime, self.senderThreadId, self.topicid))
        # return repr(
        #     "NetworkMessage: RecN = {} RecNBM = {} MaxStp = {} Chksum = {} T = {} LEN = {} SenN = {} STime = {} SThreadID = {} TopicID = {}".format(
        #         self.receiverNode, self.receiverNodeBitMap, self.max_StepsToForward, self.checksum, self.type, self.len, self.senderNode, self.sentTime, self.senderThreadId, self.topicid))

    @property
    def max_StepsToForward(self):
        return self._max_StepsToForward

    @max_StepsToForward.setter
    def max_StepsToForward(self, value):
        self._max_StepsToForward = value

    @property
    def checksum(self):
        return self._checksum

    @checksum.setter
    def checksum(self, value):
        self._checksum = value

    @property
    def sentTime(self):
        return self._sentTime

    @sentTime.setter
    def sentTime(self, value):
        self._sentTime = value

    @property
    def senderNode(self):
        return self._senderNode

    @senderNode.setter
    def senderNode(self, value):
        self._senderNode = value

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    @property
    def receiverNode(self):
        return self._receiverNode

    @receiverNode.setter
    def receiverNode(self, value):
        self._receiverNode = value

    @property
    def topicid(self):
        return self._topicid

    @topicid.setter
    def topicid(self, value):
        self._topicid = value

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value

    @property
    def receiverNodeBitMap(self):
        return self._receiverNodeBitMap

    @receiverNodeBitMap.setter
    def receiverNodeBitMap(self, value):
        self._receiverNodeBitMap = value

    @property
    def senderThreadId(self):
        return self._senderThreadId

    @senderThreadId.setter
    def senderThreadId(self, value):
        self._senderThreadId = value

    @property
    def len(self):
        return self._len

    @len.setter
    def len(self, value):
        self._len = value

    """
        inline int32_t  get_receiverNode()         const { return bigEndianToInt32_t(header + 0); } // see receiverNode+receiverNodesBitMap.txt
        inline uint32_t get_receiverNodesBitMap()  const { return bigEndianToUint32_t(header+ 4); } // see receiverNode+receiverNodesBitMap.txt
        inline int16_t  get_maxStepsToForward()    const { return bigEndianToInt16_t(header + 8); }
        inline uint16_t get_checksum()             const { return bigEndianToUint16_t(header+10); }
        // from here protected with checksum : next index (12) will be used as literal : calculateCheckSum()
        inline uint16_t get_type()                 const { return bigEndianToUint16_t(header+12); }
        inline uint16_t get_len()                  const { return bigEndianToUint16_t(header+14); } // only user data
        inline int32_t  get_senderNode()           const { return bigEndianToInt32_t(header +16); }
        inline int64_t  get_sentTime ()            const { return bigEndianToInt64_t(header +20); }
        inline uint32_t get_senderThreadId()       const { return bigEndianToUint32_t(header+28); }
        inline uint32_t get_topicId()              const { return bigEndianToUint32_t(header+32); } 
    """

    def parseHeader(self, BigEndian=True):
        try:
            parseString = ""
            # if BigEndian:
            #     parseString = "!HiQIIhH"
            # else:
            #     parseString = "@HiQIIhH"
            # if len(self.rawmsg) < 26:
            #     return
            print("header")
            """parse header of NetworkMessage and set values accordingly"""
            # print("length",len(self.rawMsg)
            print(self.rawMsg, len(self.rawMsg))
            # self.rawHeader = self.rawMsg[:36]
            self.rawHeader = self.rawMsg[:26]
            # print(self.rawHeader)
            unpacked = struct.unpack(">HiQIIhH", self.rawHeader)
            print(unpacked)
            # unpacked = struct.unpack("=iIhHHHiQII", self.rawHeader)

            # self._receiverNode = unpacked[0] i
            # self._receiverNodeBitMap = unpacked[1] I
            # self._max_StepsToForward = unpacked[2] h
            # self._checksum = unpacked[3] H
            # self._type = unpacked[4] H
            # self._len = unpacked[5] H
            # self._senderNode = unpacked[6] i
            # self._sentTime = unpacked[7] Q
            # self._senderThreadId = unpacked[8] I
            # self._topicid = unpacked[9] I

            self._checksum = unpacked[0]
            self._senderNode = unpacked[1]
            self._sentTime = unpacked[2]
            self._senderThreadId = unpacked[3]
            self._topicid = unpacked[4]
            self._max_StepsToForward = unpacked[5]
            self._len = unpacked[6]

            # self._type = unpacked[4]

            self.updateHeader()
            self.userDataC = self.rawMsg[26:]
            # print("user data",self.userDataC)
            # print("unpacked data", struct.unpack("=f", self.userDataC))
            # self.userDataC = self.rawMsg
        except Exception as e:
            print("Exception in parsing header")
            print(e)

    def updateHeader(self):
        # self.header[0] = self._receiverNode
        # self.header[1] = self._receiverNodeBitMap
        # self.header[2] = self._max_StepsToForward
        # self.header[3] = self._checksum
        # self.header[4] = self._type
        # self.header[5] = self._len
        # self.header[6] = self._senderNode

        # self.header[7] = self._sentTime
        # self.header[8] = self._senderThreadId
        # self.header[9] = self._topicid
        try:
            self.header[0] = self._checksum
            self.header[1] = self._senderNode
            self.header[2] = self._sentTime
            self.header[3] = self._senderThreadId
            self.header[4] = self._topicid
            self.header[5] = self._max_StepsToForward
            self.header[6] = self._len

            self.rawHeader = struct.pack(self.PARSE_STRING, *(self.header))
        except Exception as e:
            print("exception update header",e)

    def getBinaryMsg(self):
        """
        returns NetoworkMessage header and data as uint8 array here a python3-bytes-type
        Message Header will be encoded as Big-Endian
        """
        try:
            # print("in binary message", self.header)
            if len(self.header) < 7:
                return b""
                #raise IndexError
            self.updateHeader()
            # + self.userDataC))
            packedHeader = struct.pack(self.PARSE_STRING, *(self.header))
            packed = packedHeader + self.userDataC
            # print("Packed data", packed)

            return packed
        except Exception as e:
            print("error while creating binary message")
            print(e)

    def getUserData(self, maxLen=1300):
        """ returns userData and length"""
        return self.userDataC[:1300]  # only return the first 1300 bytes

    def setUserData(self, data):
        self.userDataC = data[:1300]  # only take first 1300 bytes

    def calcChecksum(self) -> int:
        slice = (self.rawHeader + self.getUserData())[2:]
        # slice = (self.rawHeader + self.getUserData())[2:]
        return calcCheckSum(slice)
        # return calcCheckSum(self.rawHeader[2:])

