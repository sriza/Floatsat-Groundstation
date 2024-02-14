import sys
from PySide6.QtCore import (QRect, QCoreApplication, QTimer)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenuBar, QMenu, QLabel)
from PySide6.QtGui import (QAction)
from Views.Summary import Ui_MainWindow
# from Views.Summary_test import Ui_MainWindow
from Views.IMU import IMU_MainWindow
from Views.Telecommand import Telecommand_MainWindow
from Views.Docking import Docking_MainWindow
from Views.Debug import Debug_MainWindow

# for rodos and data manipulation
from rodos import Gateway
from rodos import LinkinterfaceUDP
from rodos import Topic
import json
import struct
import math

# for time tracking and data tracking
import time

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "StarStation"
        self.menubarCollection()
        self.summary = Ui_MainWindow()
        self.imu = IMU_MainWindow()
        self.telecommand = Telecommand_MainWindow()
        self.docking = Docking_MainWindow()   
        self.debug = Debug_MainWindow()
        self.programStatus = {"connectionStatus":False, "currentMode": 0, "time": 0, "inMission": False}
        self.lastTelecommand = {"id":0, "data":[], "count":0, "resend": False, "lastId": 0}
        self.satOrientation = {"roll":0, "pitch":0, "yaw":0}

        # self mission modes
        self.modes = {}
        self.missionModes = {}
        self.setModes()
        self.setMissionModes()

        # connection status
        self.setConnection = False

        #rodos
        self.pairedData = {"U_bat":{}, "speed":{}, "yaw":{}, "velocity":{}}
        self.luart = LinkinterfaceUDP()
        self.gwUDP = Gateway(self.luart)
        self.telemetry = {}
        self.telecommandTopic = {}
        self.topics = {}
        self.initializeTelemetryTopics()
        self.initializeTelecommandTopics()
        self.gwUDP.run()

        self.summary.setupUi(self)
        self.currentView = self.summary

        # connection Status checking with time interval of a second
        self.lastConnectedTime = 0
        self.connectionTimer = QTimer()
        self.connectionTimer.setInterval(1000)
        self.connectionTimer.timeout.connect(self.checkConnectionStatus)
        self.connectionTimer.start()
        
    #init
        
    # set modes
    def setModes(self):
        f = open("Assets/satellite_modes.json")
        json_array = json.load(f)

        for item in json_array:
            mode = json_array[item]
            id = mode["id"]
            self.modes[id] = {}
            self.modes[id]["name"] = item
    # end set modes

    #initialize telemetry
    def initializeTelemetryTopics(self):
        try:
            f = open("Assets/telemetry.json")
            json_array = json.load(f)

            for item in json_array:
                dataStruct = json_array[item]

                # initialization of topic
                topic = Topic(dataStruct["topicId"])
                # dynamic pointer to function corresponding to the topic
                func = getattr(self, item)
                topic.addSubscriber(func)

                self.telemetry[item] = {}
                self.telemetry[item]["topic"] = topic
                self.topics[dataStruct["topicId"]] = item

                # copy remaining data to structure
                self.telemetry[item]["topicId"] = dataStruct["topicId"]
                self.telemetry[item]["structure"] = dataStruct["structure"]
                self.telemetry[item]["data"] = {}

                # copy the structure of data
                for datum in dataStruct["data"]:
                    self.telemetry[item]["data"][datum] = 0

                self.telemetry[item]["pairedData"] = self.pairedData
                self.telemetry[item]["programData"] = self.programStatus
                self.telemetry[item]["missionModes"] = self.missionModes

        except Exception as e:
            print("telemetry initialization exception",e)
    # initializeTelecommand end

    # initialize telecommand topics
    def initializeTelecommandTopics(self):
        try:
            f = open("Assets/telecommand.json")
            json_array = json.load(f)

            for item in json_array:
                print("initializing telecommand topics...")
                dataStruct = json_array[item]

                # initialization of topic
                self.telecommandTopicID = Topic(51)
                self.gwUDP.forwardTopic(self.telecommandTopicID) 

                self.telecommandTopic[item] = {}
                self.telecommandTopic[item]["topic"] = self.telecommandTopicID

                # # copy remaining data to structure
                self.telecommandTopic[item]["topicId"] = dataStruct["topicId"]
                self.telecommandTopic[item]["structure"] = dataStruct["structure"]
                self.telecommandTopic[item]["data"] = {}

                # copy the structure of data
                for datum in dataStruct["data"]:
                    self.telecommandTopic[item]["data"][datum] = 0
        except Exception as e:
            print(e)
    #initializeTelecommandTopics

    # set mission modes status
    def setMissionModes(self):
        f = open("Assets/satellite_modes.json")
        json_array = json.load(f)

        for item in json_array:
            mode = json_array[item]

            if "type" in mode.keys() and mode["type"] =="mission":
                self.missionModes[mode["id"]] = {}
                self.missionModes[mode["id"]]["type"] = mode["type"]
                self.missionModes[mode["id"]]["name"] = item
                self.missionModes[mode["id"]]["status"] = False
    #set mission modes
    
    #update mission modes
    def updateMissionModes(self):
        inMission = False
        updated = False

        if self.programStatus["currentMode"] in self.missionModes.keys():
            inMission = True

        # update mission flag
        self.programStatus["inMission"] = inMission

        for modeid in self.missionModes:
            if inMission and not updated:
                self.missionModes[modeid]["status"] = True

                if modeid == self.programStatus["currentMode"]:
                    updated = True
            else:
                self.missionModes[modeid]["status"] = False
    #updateMissionModes
        
    # set data from the telemetry and update view
    def setAndUpdate(self, data, topicName):
        try:
            if not self.setConnection:
                return
                        
            # updates last connected time to present time
            self.programStatus["connectionStatus"]= True
            #unpacks data
            unpackedData = struct.unpack(self.telemetry[topicName]["structure"],data)
            i = 0

            telemetryData = self.telemetry[topicName]["data"]

            if "modeid" in telemetryData.keys():
                self.programStatus["currentMode"] = telemetryData["modeid"]
                self.updateMissionModes()

            for datum in telemetryData:
                dataInIndex = unpackedData[i]

                if datum == "q0":
                    # conversion of quaternion to roll, pitch and yaw
                    q0 = telemetryData["q0"]
                    q1 = telemetryData["q1"]
                    q2 = telemetryData["q2"]
                    q3 = telemetryData["q3"]
                    lastYaw = self.satOrientation["yaw"]
                    lastTime = self.programStatus["time"]
                
                    self.satOrientation["roll"] = math.atan2(2 * (q0 * q1 + q2 * q3), 1 - 2 * (q1 * q1 + q2 * q2))
                    self.satOrientation["pitch"] = math.asin(2 * (q0 * q2 - q3 * q1))
                    self.satOrientation["yaw"] = math.atan2(2 * (q0 * q3 + q1 * q2), 1 - 2 * (q2 * q2 + q3 * q3))

                    if telemetryData["time"] < self.programStatus["time"] :
                        self.pairedData["yaw"] = {}
                        self.pairedData["velocity"] = {}
                        self.pairedData["speed"] = {}
                        self.pairedData["U_bat"] = {}
                    
                    satTime = telemetryData["time"]
                    self.pairedData["yaw"][satTime] = math.degrees(self.satOrientation["yaw"])
                    self.pairedData["velocity"][satTime] = (lastYaw-self.satOrientation["yaw"])/(lastTime-satTime)
                    self.programStatus["time"] = satTime

                if datum in self.pairedData.keys():
                    satTime = telemetryData["time"]
                    # self.programStatus["time"] = satTime
                    self.pairedData[datum][satTime] = dataInIndex

                
                # resend telecommand if not same
                if datum == "lastcmdid":
                    commandId = dataInIndex

                    if self.lastTelecommand["id"] != dataInIndex and self.lastTelecommand["count"] <3 and self.lastTelecommand["resend"] == True:
                        self.lastTelecommand["count"]+=1

                    if self.lastTelecommand["count"] >=5 or self.lastTelecommand["lastId"] != commandId:
                        self.lastTelecommand["id"] = commandId
                        self.lastTelecommand["data"] = []
                        self.lastTelecommand["count"] = 0
                        self.lastTelecommand["resend"] = False

                telemetryData[datum] = dataInIndex
                i+=1

            self.telemetry[topicName]["pairedData"] = self.pairedData
            self.telemetry[topicName]["programData"] = self.programStatus
            self.telemetry[topicName]["missionModes"] = self.missionModes

            # set last connected time, and trigger changes on views
            self.lastConnectedTime = time.time()
            self.currentView.updateTrigger(self.telemetry)
        except Exception as ex:
            print("set and update exception:",ex)
            if self.setConnection:
                self.currentView.updateTrigger(self.telemetry)
    #setAndUpdate
            
    # send telecommand: common interface for all child windows
    def sendTelecommand(self, data, resend = False):
        try:
            if self.setConnection:
                i = len(data)-1

                while i<3:
                    data.append(0.0)
                    i+=1

                dataStruct = struct.pack("=i3f",*tuple(data))
                (self.telecommandTopicID).publish(dataStruct)
                print("telecommand sent:", data)

                if not resend:
                    self.lastTelecommand["id"] = data[0]
                    self.lastTelecommand["data"] = data
                    self.lastTelecommand["count"] = 0
                    self.lastTelecommand["resend"] = True
        except Exception as ex:
            print("exception in sending telecommand:", ex)
    #sendTelecommand
            
    # sends echo telecommand: will be used in telecommand window only
    def sendEchoTelecommand(self, data):
        if self.setConnection:
            i = len(data)-1

            while i<4:
                data.append(0)
                i+=1

            dataStruct = struct.pack("=3f",*tuple(data))
            (self.telecommandTopic["TelecommandEchoTopicId"]["topic"]).publish(dataStruct)
    #sendEchoTelecommand
        
    # checks and updates connection status
    def checkConnectionStatus(self):
        connectionStatus = "Connected"
        connectionStatusStyle = "background-color: rgb(26, 29, 56); color: rgb(255, 255, 255); qproperty-alignment: AlignCenter;"

        if time.time()-self.lastConnectedTime > 2:
            self.programStatus["connectionStatus"]= False
            connectionStatus = "Disconnected"
            connectionStatusStyle = "color: rgb(255, 255, 255); background-color: rgb(182, 41, 16);qproperty-alignment: AlignCenter;"

        self.connectionStatus.setText(connectionStatus)
        self.connectionStatus.setStyleSheet(connectionStatusStyle)

        # update current mode
        self.currentModeStatus.setText(self.modes[self.programStatus["currentMode"]]["name"])
    #checkConnectionStatus
        
    def setConnectionStatus(self, status):
        self.setConnection = status
        
    # create collection of menubar
    def menubarCollection(self):
        # add menu to menubar
        self.menubar = QMenuBar(self)
        # self.menubar.addAction(button_action)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 2560, 40))

        self.menuSummary = QMenu(self.menubar)
        self.menuSummary.setObjectName(u"menuSummary")

        self.menuIMU = QMenu(self.menubar)
        self.menuIMU.setObjectName(u"menuIMU")

        self.menuDocking = QMenu(self.menubar)
        self.menuDocking.setObjectName(u"menuDocking")

        self.menuTelecommand = QMenu(self.menubar)
        self.menuTelecommand.setObjectName(u"menuTelecommand")

        self.menuTesting = QMenu(self.menubar)
        self.menuTesting.setObjectName(u"menuTelecommand")

        self.menuDebug = QMenu(self.menubar)
        self.menuDebug.setObjectName(u"menuDebug")

        self.setMenuBar(self.menubar)

        self.menubar.addActions([
            self.menuSummary.menuAction(),
            self.menuIMU.menuAction(),
            self.menuDocking.menuAction(),
            self.menuTelecommand.menuAction(),
            self.menuDebug.menuAction()
        ])

        self.menuSummary.aboutToShow.connect(self.show_new_window_summary)
        self.menuIMU.aboutToShow.connect(self.show_new_window)
        self.menuDocking.aboutToShow.connect(self.show_new_window_docking)
        self.menuTelecommand.aboutToShow.connect(self.show_new_window_telecommand)
        self.menuDebug.aboutToShow.connect(self.show_new_window_debug)

        self.menuSummary.setTitle(QCoreApplication.translate("MainWindow", u"Summary", None))
        self.menuIMU.setTitle(QCoreApplication.translate("MainWindow", u"IMU", None))
        self.menuDocking.setTitle(QCoreApplication.translate("MainWindow", u"Docking", None))
        self.menuTelecommand.setTitle(QCoreApplication.translate("MainWindow", u"TeleCommand", None))
        self.menuDebug.setTitle(QCoreApplication.translate("MainWindow", u"Debug", None))

        self.connectionStatus = QLabel(self)
        self.connectionStatus.setObjectName(u"label_13")
        self.connectionStatus.setGeometry(QRect(1050, 760, 150, 31))
        self.connectionStatus.setStyleSheet(u"background-color: rgb(26, 29, 56); color: rgb(255, 255, 255);")

        self.currentModeStatus = QLabel(self)
        self.currentModeStatus.setObjectName(u"label_13")
        self.currentModeStatus.setGeometry(QRect(800, 760, 150, 31))
        self.currentModeStatus.setStyleSheet(u"background-color: rgb(26, 29, 56); color: rgb(255, 255, 255); qproperty-alignment: AlignCenter;")
        self.currentModeStatus.setText("Not Connected")
    #menubarCollection
        
    def show_new_window_summary(self):
        self.summary.setupUi(self)
        self.currentView = self.summary
        self.currentView.updateTrigger(self.telemetry)
    #show_new_window_summary
        
    def show_new_window(self):
        self.imu.setupUi(self)
        self.currentView = self.imu
        self.currentView.updateTrigger(self.telemetry)
    #show_new_window
        
    def show_new_window_docking(self):
        self.docking.setupUi(self)
        self.docking.createMissionModes(self.missionModes)
        self.currentView = self.docking
        self.currentView.updateTrigger(self.telemetry)
    #show_new_window_docking
        
    def show_new_window_telecommand(self):
        self.telecommand.setupUi(self)
        self.currentView = self.telecommand
        self.currentView.updateTrigger(self.telemetry)
    #show_new_window_telecommand
        
    def show_new_window_debug(self):
        self.debug.setupUi(self)
        self.currentView = self.debug
        self.currentView.updateTrigger(self.debug)
    #show_new_window_debug
        
    def telemetryContinuous(self, data):
        topicName = "telemetryContinuous"
        self.setAndUpdate(data,topicName)
    #telemetryContinuous
        
    def telemetryContinuousExtendedTopicID(self, data):
        topicName = "telemetryContinuousExtendedTopicID"
        self.setAndUpdate(data,topicName)
    #telemetryContinuousExtendedTopicID
        
    def telemetryCalibIMU(self, data):
        topicName = "telemetryContinuous"
        self.setAndUpdate(data,topicName)
    #telemetryCalibIMU
        
    def telemetryControlParams(self, data):
        topicName = "telemetryControlParams"
        self.setAndUpdate(data,topicName)
    #telemetryControlParams
        
    def telemetryMessage(self, data):
        topicName = "telemetryMessage"
        self.setAndUpdate(data,topicName)
    #telemetryMessage
        
    def docking(self, data):
        topicName = "docking"
        self.setAndUpdate(data,topicName)
    #telemetryMessage
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec()