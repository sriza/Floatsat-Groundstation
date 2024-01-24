import sys
from PySide6.QtCore import (QRect, QCoreApplication)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenuBar, QMenu)
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
        self.luart = LinkinterfaceUDP()
        self.gwUDP = Gateway(self.luart)
        self.telemetry = {}
        self.topics = {}
        self.initializeTelemetryTopics()
        # self.initializeTelecommandTopics()
        self.gwUDP.run()

        self.summary.setupUi(self)
        self.currentView = self.summary

    
    def initializeTelemetryTopics(self):
        try:
            print("data initialized")
            f = open("Assets/data.json")
            json_array = json.load(f)

            for item in json_array:
                print("initializing...")
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

                print(item)

        except Exception as e:
            print(e)


    def initializeTelecommandTopics(self):
        try:
            print("data initialized")
            f = open("Assets/data.json")
            json_array = json.load(f)

            for item in json_array:
                print("initializing...")
                dataStruct = json_array[item]

                # initialization of topic
                topic = Topic(dataStruct["topicId"])
                self.gwUart.forwardTopic(topic) 

                self.telemetry[item] = {}
                # try:
                self.telemetry[item]["topic"] = topic
                # except Exception as ex:
                    # print(ex)
                    # exit
                # gwUart.forwardTopic(telemetry[item]["topic"]) 

                # # copy remaining data to structure
                self.telemetry[item]["topicId"] = dataStruct["topicId"]
                self.telemetry[item]["structure"] = dataStruct["structure"]
                self.telemetry[item]["data"] = {}

                # # copy the structure of data
                for datum in dataStruct["data"]:
                    self.telemetry[item]["data"][datum] = 0

                print(item)

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

    def setAndUpdate(self, data, topicName):
        try:       
            print("set and update", self.telemetry[topicName]["structure"])
            unpackedData = struct.unpack(self.telemetry[topicName]["structure"],data)
            i = 0

            for datum in self.telemetry[topicName]["data"]:
                self.telemetry[topicName]["data"][datum] = unpackedData[i]
                i+=1
            print("got data", unpackedData)

            self.currentView.updateData(self.telemetry)
        except Exception as ex:
            print(ex)

    
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
            self.menuTesting.menuAction()
        ])

        self.menuSummary.aboutToShow.connect(self.show_new_window_summary)
        self.menuIMU.aboutToShow.connect(self.show_new_window)
        self.menuDocking.aboutToShow.connect(self.show_new_window_docking)
        self.menuTelecommand.aboutToShow.connect(self.show_new_window_telecommand)

        self.menuSummary.setTitle(QCoreApplication.translate("MainWindow", u"Summary", None))
        self.menuIMU.setTitle(QCoreApplication.translate("MainWindow", u"IMU", None))
        self.menuDocking.setTitle(QCoreApplication.translate("MainWindow", u"Docking", None))
        self.menuTelecommand.setTitle(QCoreApplication.translate("MainWindow", u"TeleCommand", None))
        # self.menuTesting.setTitle(QCoreApplication.translate("MainWindow", u"Testing", None))
    
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