import sys
from PySide6.QtCore import (QRect, QCoreApplication, QTimer)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenuBar, QMenu, QLabel)
from PySide6.QtGui import (QAction)
from Views.Summary import Ui_MainWindow
# from Views.Summary_test import Ui_MainWindow
from Views.IMU import IMU_MainWindow
from Views.Telecommand import Telecommand_MainWindow
from Views.Docking import Docking_MainWindow

# for rodos and data manipulation
from rodos import Gateway
from rodos import LinkinterfaceUDP
from rodos import Topic
import json
import struct

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

        #rodos
        self.pairedData = {"temp":{}}
        self.luart = LinkinterfaceUDP()
        self.gwUDP = Gateway(self.luart)
        self.telemetry = {}
        self.telecommandTopic = {}
        self.topics = {}
        self.initializeTelemetryTopics()
        # todo: need to run this in a different thread
        self.initializeTelecommandTopics()
        self.gwUDP.run()

        self.summary.setupUi(self)
        self.currentView = self.summary

        # connection Status checking with time interval of a second
        self.programStatus = {"connectionStatus":False}
        self.lastConnectedTime = 0
        self.connectionTimer = QTimer()
        self.connectionTimer.setInterval(1000)
        self.connectionTimer.timeout.connect(self.checkConnectionStatus)
        self.connectionTimer.start()
    
    def initializeTelemetryTopics(self):
        try:
            print("initializing telemetry topics")
            f = open("Assets/telemetry.json")
            json_array = json.load(f)

            for item in json_array:
                dataStruct = json_array[item]

                # initialization of topic
                topic = Topic(dataStruct["topicId"])
                func = getattr(self, item)
                topic.addSubscriber(func)

                self.telemetry[item] = {}
                self.telemetry[item]["topic"] = topic
                self.topics[dataStruct["topicId"]] = item

                # # copy remaining data to structure
                self.telemetry[item]["topicId"] = dataStruct["topicId"]
                self.telemetry[item]["structure"] = dataStruct["structure"]
                self.telemetry[item]["data"] = {}

                # # copy the structure of data
                for datum in dataStruct["data"]:
                    self.telemetry[item]["data"][datum] = 0

                self.telemetry[item]["pairedData"] = self.pairedData

        except Exception as e:
            print(e)

    def initializeTelecommandTopics(self):
        try:
            print("data initialized telecommand topics")
            f = open("Assets/telecommand.json")
            json_array = json.load(f)

            for item in json_array:
                print("initializing...")
                dataStruct = json_array[item]

                # initialization of topic
                # self.telecommandTopicID = Topic(dataStruct["topicId"])
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

    def telemetryContinuous(self, data):
        topicName = "telemetryContinuous"
        self.setAndUpdate(data,topicName)
    
    def telemetryContinuousExtendedTopicID(self, data):
        topicName = "telemetryContinuousExtendedTopicID"
        self.setAndUpdate(data,topicName)
    
    def telemetryCalibIMU(self, data):
        topicName = "telemetryContinuous"
        self.setAndUpdate(data,topicName)
    
    def telemetryControlParams(self, data):
        topicName = "telemetryControlParams"
        self.setAndUpdate(data,topicName)
    
    def telemetryMessage(self, data):
        topicName = "telemetryMessage"
        self.setAndUpdate(data,topicName)

    # set data from the telemetry and update view
    def setAndUpdate(self, data, topicName):
        try:
            print("struct data size:", struct.calcsize(self.telemetry[topicName]["structure"]));  
            print("set and update", self.telemetry[topicName]["structure"])

            # updates last connected time to present time
            self.lastConnectedTime = time.time()
            self.programStatus["connectionStatus"]= True

            #unpacks data
            unpackedData = struct.unpack(self.telemetry[topicName]["structure"],data)
            i = 0

            for datum in self.telemetry[topicName]["data"]:
                dataInIndex = unpackedData[i]

                if datum in self.pairedData.keys():
                    # print("the data:", datum)
                    satTime = self.telemetry[topicName]["data"]["time"]
                    self.pairedData[datum][satTime] = dataInIndex

                self.telemetry[topicName]["data"][datum] = dataInIndex
                i+=1

            self.telemetry[topicName]["pairedData"] = self.pairedData
            self.currentView.updateData(self.telemetry)
        except Exception as ex:
            print("set and update exception:",ex)
            self.currentView.updateData(self.telemetry)

    # send telecommand: common interface for all child windows
    def sendTelecommand(self, data):
        try:
            i = len(data)-1

            while i<3:
                data.append(0.0)
                i+=1

            dataStruct = struct.pack("=i3f",*tuple(data))
            print(self.telecommandTopic["TelecommandTopicId"]["topicId"])
            (self.telecommandTopicID).publish(dataStruct)
            print("published data", dataStruct, tuple(data))
        except Exception as ex:
            print("exception in sending telecommand:", ex)
    
    # sends echo telecommand: will be used in telecommand window only
    def sendEchoTelecommand(self, data):
        i = len(data)-1

        while i<4:
            data.append(0)
            i+=1

        dataStruct = struct.pack("=3f",*tuple(data))
        (self.telecommandTopic["TelecommandEchoTopicId"]["topic"]).publish(dataStruct)

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

        self.setMenuBar(self.menubar)

        self.menubar.addActions([
            self.menuSummary.menuAction(),
            self.menuIMU.menuAction(),
            self.menuDocking.menuAction(),
            self.menuTelecommand.menuAction(),
            # self.menuTesting.menuAction()
        ])

        self.menuSummary.aboutToShow.connect(self.show_new_window_summary)
        self.menuIMU.aboutToShow.connect(self.show_new_window)
        self.menuDocking.aboutToShow.connect(self.show_new_window_docking)
        self.menuTelecommand.aboutToShow.connect(self.show_new_window_telecommand)

        self.menuSummary.setTitle(QCoreApplication.translate("MainWindow", u"Summary", None))
        self.menuIMU.setTitle(QCoreApplication.translate("MainWindow", u"IMU", None))
        self.menuDocking.setTitle(QCoreApplication.translate("MainWindow", u"Docking", None))
        self.menuTelecommand.setTitle(QCoreApplication.translate("MainWindow", u"TeleCommand", None))

        self.connectionStatus = QLabel(self)
        self.connectionStatus.setObjectName(u"label_13")
        self.connectionStatus.setGeometry(QRect(1050, 760, 150, 31))
        self.connectionStatus.setStyleSheet(u"background-color: rgb(26, 29, 56); color: rgb(255, 255, 255);")
    
    def show_new_window_summary(self):
        print("clicked")
        self.summary.setupUi(self)
        self.currentView = self.summary
        self.currentView.updateData(self.telemetry)

    def show_new_window(self):
        print("clicked")
        self.imu.setupUi(self)
        self.currentView = self.imu
        self.currentView.updateData(self.telemetry)
    
    def show_new_window_docking(self):
        print("clicked docking")
        self.docking.setupUi(self)
        self.currentView = self.docking
        self.currentView.updateData(self.telemetry)
    
    def show_new_window_telecommand(self):
        print("clicked telecommand")
        self.telecommand.setupUi(self)
        self.currentView = self.telecommand
        self.currentView.updateData(self.telemetry)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec()