# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'telecommand.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, Signal, Slot)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtOpenGLWidgets import QOpenGLWidget
from PySide6.QtWidgets import (QApplication, QFrame, QGraphicsView,
    QGroupBox, QLabel, QMainWindow, QMenu,
    QMenuBar, QPlainTextEdit, QPushButton, QSizePolicy, QComboBox,
    QStatusBar, QWidget)
from Views.CustomWidgets.SatelliteAnimation import SatelliteAnimation
import json
import math
import pyqtgraph as pg
import numpy as np

class TeleCommandSignal(QObject):
    value = Signal()

class Telecommand_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        self.value = TeleCommandSignal()
        self.parent = MainWindow
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(30, 10, 280, 750))
        self.frame.setAutoFillBackground(False)
        # self.frame.setStyleSheet(u"background-color: rgb(225, 225, 225);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.motorSpeedGraphLabel = QLabel(self.frame)
        self.motorSpeedGraphLabel.setObjectName(u"motorSpeedGraphLabel")
        self.motorSpeedGraphLabel.setGeometry(QRect(0, 0, 261, 25))
        self.motorSpeedGraphLabel.setText("Motor Speed")

        self.motorSpeedGraph = pg.PlotWidget(self.frame)
        self.motorSpeedGraph.setGeometry(QRect(0,30,280,200))
        self.motorSpeedGraph.setMinimumSize(QSize(270, 200))
        self.motorSpeedGraph.setWindowTitle("Motor Speed")

        self.orientationLabel = QLabel(self.frame)
        self.orientationLabel.setObjectName(u"orientationLabel")
        self.orientationLabel.setGeometry(QRect(0, 250, 261, 25))
        self.orientationLabel.setText("Orientation")

        self.orientationGraph = pg.PlotWidget(self.frame)
        self.orientationGraph.setGeometry(QRect(0,275,280,200))
        self.orientationGraph.setMinimumSize(QSize(270, 200))
        self.orientationGraph.setWindowTitle("Orientation")

        self.angularVelocityLabel = QLabel(self.frame)
        self.angularVelocityLabel.setObjectName(u"angularVelocityLabel")
        self.angularVelocityLabel.setGeometry(QRect(0, 500, 261, 25))
        self.angularVelocityLabel.setText("Angular Velocity")

        self.angularVelocityGraph = pg.PlotWidget(self.frame)
        self.angularVelocityGraph.setGeometry(QRect(0,525,280,200))
        self.angularVelocityGraph.setMinimumSize(QSize(270, 200))
        self.angularVelocityGraph.setWindowTitle("Angular Velocity")

        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(10)

        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(16)

        self.limit = 0
        self.currentCommand = ""
   
        self.graphicsView_4 = QGraphicsView(self.centralwidget)
        self.graphicsView_4.setObjectName(u"graphicsView_4")
        self.graphicsView_4.setGeometry(QRect(940, 450, 271, 270))
        self.graphicsView_4.setAutoFillBackground(True)
        brush = QBrush(QColor(255, 124, 234, 255))
        brush.setStyle(Qt.NoBrush)
        self.graphicsView_4.setBackgroundBrush(brush)
        self.graphicsView_5 = QGraphicsView(self.centralwidget)
        self.graphicsView_5.setObjectName(u"graphicsView_5")
        self.graphicsView_5.setGeometry(QRect(940, 10, 271, 411))
        self.graphicsView_5.setAutoFillBackground(True)
        self.graphicsView_5.setStyleSheet(u"background-color: rgb(225, 225, 225);")
        brush1 = QBrush(QColor(255, 124, 234, 255))
        brush1.setStyle(Qt.NoBrush)
        self.graphicsView_5.setBackgroundBrush(brush1)

        self.satAnimation = SatelliteAnimation(self.centralwidget)
        self.satAnimation.setObjectName(u"satAnimation")
        self.satAnimation.setGeometry(QRect(320, 10, 600, 400))

        self.Connection = QWidget(self.centralwidget)
        self.Connection.setObjectName(u"Connection")
        self.Connection.setGeometry(QRect(940, 10, 271, 51))
        font2 = QFont()
        font2.setPointSize(14)
        self.Connection.setFont(font2)
        self.Connection.setStyleSheet(u"background-color: rgb(211, 211, 211);")
        self.label_2 = QLabel(self.Connection)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 10, 261, 31))
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.Connection_2 = QWidget(self.centralwidget)
        self.Connection_2.setObjectName(u"Connection_2")
        self.Connection_2.setGeometry(QRect(940, 450, 271, 51))
        self.Connection_2.setFont(font2)
        self.Connection_2.setStyleSheet(u"background-color: rgb(211, 211, 211);")
        self.serverMessageLabel = QLabel(self.Connection_2)
        self.serverMessageLabel.setObjectName(u"label_10")
        self.serverMessageLabel.setGeometry(QRect(10, 10, 231, 31))
        self.serverMessageLabel.setFont(font1)
        self.serverMessageLabel.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.shutDownButton = QPushButton(self.centralwidget)
        self.shutDownButton.setObjectName(u"pushButton_3")
        self.shutDownButton.setGeometry(QRect(960, 300, 231, 41))
        self.shutDownButton.setStyleSheet(u"color: rgb(255, 255, 255);\n"
        "background-color: rgb(182, 41, 16);")

        self.shutDownButton.clicked.connect(self.shutDown)
        self.groupBox_4 = QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(960, 520, 231, 180))
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(1)
        self.groupBox_4.setFont(font3)
        self.groupBox_4.setStyleSheet(u"color: rgb(255, 255, 255);\n"
        "background-color: rgb(26, 29, 56);")
        font4 = QFont()
        font4.setPointSize(12)

        self.messageText = QLabel(self.groupBox_4)
        self.messageText.setWordWrap(True)
        self.messageText.setObjectName(u"messageText")
        self.messageText.setGeometry(QRect(20,30,171,60))
        # self.messageText.setFont(font)

        self.missionStartButton = QPushButton(self.centralwidget)
        self.missionStartButton.setObjectName(u"missionStartButton")
        self.missionStartButton.setGeometry(QRect(960, 370, 231, 41))
        self.missionStartButton.setStyleSheet(u"color: rgb(255, 255, 255);\n"
        "background-color: rgb(50, 107, 29);")
        self.missionStartButton.clicked.connect(self.initiateMission)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(950, 350, 251, 16))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.commandCountLabel = QLabel(self.centralwidget)
        self.commandCountLabel.setObjectName(u"label_8")
        self.commandCountLabel.setGeometry(QRect(960, 70, 201, 25))
        self.commandCountLabel.setFont(font)
        self.commandCountLabel.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.commandCnt = QLabel(self.centralwidget)
        self.commandCnt.setObjectName(u"label_13")
        self.commandCnt.setGeometry(QRect(960, 95, 231, 30))
        self.commandCnt.setFont(font)
        self.commandCnt.setStyleSheet(u"background-color: rgb(26, 29, 56); color: rgb(255, 255, 255);")

        self.lastCommandLabel = QLabel(self.centralwidget)
        self.lastCommandLabel.setObjectName(u"label_8")
        self.lastCommandLabel.setGeometry(QRect(960, 125, 201, 25))
        self.lastCommandLabel.setFont(font)
        self.lastCommandLabel.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.lastCommandLabel.setText("Last command")

        self.lastCommand = QLabel(self.centralwidget)
        self.lastCommand.setObjectName(u"label_13")
        self.lastCommand.setGeometry(QRect(960, 150, 231, 30))
        self.lastCommand.setFont(font)
        self.lastCommand.setStyleSheet(u"background-color: rgb(26, 29, 56); color: rgb(255, 255, 255);")

        self.modeLabel = QLabel(self.centralwidget)
        self.modeLabel.setObjectName(u"modeLabel")
        self.modeLabel.setGeometry(QRect(960, 180, 201, 25))
        self.modeLabel.setFont(font)
        self.modeLabel.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.modeText = QLabel(self.centralwidget)
        self.modeText.setObjectName(u"label_14")
        self.modeText.setGeometry(QRect(960, 205, 231, 30))
        self.modeText.setFont(font)
        self.modeText.setStyleSheet(u"background-color: rgb(26, 29, 56); color: rgb(255, 255, 255);")

        self.motorSpeedLabel = QLabel(self.centralwidget)
        self.motorSpeedLabel.setObjectName(u"motorSpeedLabel")
        self.motorSpeedLabel.setGeometry(QRect(960, 235, 201, 25))
        self.motorSpeedLabel.setFont(font)
        self.motorSpeedLabel.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.motorSpeed = QLabel(self.centralwidget)
        self.motorSpeed.setObjectName(u"label_14")
        self.motorSpeed.setGeometry(QRect(960, 260, 231, 31))
        self.motorSpeed.setFont(font)
        self.motorSpeed.setStyleSheet(u"background-color: rgb(26, 29, 56); color: rgb(255, 255, 255);")

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(330, 450, 600, 281))
        self.frame_2.setAutoFillBackground(False)
        self.frame_2.setStyleSheet(u"background-color: rgb(225, 225, 225);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.groupBox_7 = QGroupBox(self.frame_2)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setGeometry(QRect(20, 60, 811, 205))
        self.groupBox_7.setFont(font)
        self.groupBox_7.setStyleSheet(u"color: rgb(9, 10, 17);")

        # send telecommand button
        self.telecommandButton = QPushButton(self.groupBox_7)
        self.telecommandButton.setObjectName(u"pushButton_11")
        self.telecommandButton.setGeometry(QRect(10, 150, 201, 41))
        self.telecommandButton.setStyleSheet(u"color: rgb(255, 255, 255);\n"
        "background-color: rgb(50, 107, 29);")
        self.telecommandButton.clicked.connect(self.mainTelecommand)

        self.telecommandModeLabel = QLabel(self.groupBox_7)
        self.telecommandModeLabel.setObjectName(u"telecommandModeLabel")
        self.telecommandModeLabel.setGeometry(QRect(10, 0, 121, 31))
        self.telecommandModeLabel.setFont(font)

        self.xTextEdit = QPlainTextEdit(self.groupBox_7)
        self.xTextEdit.setObjectName(u"x")
        self.xTextEdit.setGeometry(QRect(10, 80, 130, 41))
        self.xTextEdit.setPlaceholderText("Propertional")

        self.yTextEdit = QPlainTextEdit(self.groupBox_7)
        self.yTextEdit.setObjectName(u"y")
        self.yTextEdit.setGeometry(QRect(160, 80, 130, 41))
        self.yTextEdit.setPlaceholderText("Integrator")

        self.zTextEdit = QPlainTextEdit(self.groupBox_7)
        self.zTextEdit.setObjectName(u"z")
        self.zTextEdit.setGeometry(QRect(310, 80, 130, 41))
        self.zTextEdit.setPlaceholderText("Derivative")

        self.modeDropdown = QComboBox(self.groupBox_7)
        self.modes = {}
        self.addDropdownItems()
        
        # self.plainTextEdit = QPlainTextEdit(self.groupBox_7)
        self.modeDropdown.setObjectName(u"plainTextEdit")
        self.modeDropdown.setGeometry(QRect(10, 25, 311, 41))
        self.modeDropdown.setPlaceholderText("Select the mode")
        self.modeDropdown.currentTextChanged.connect(self.updateModeParameters)


        self.allTelecommandsLabel = QLabel(self.frame_2)
        self.allTelecommandsLabel.setObjectName(u"allTelecommandsLabel")
        self.allTelecommandsLabel.setGeometry(QRect(0, 0, 881, 41))
        self.allTelecommandsLabel.setFont(font1)
        self.allTelecommandsLabel.setStyleSheet(u"color: rgb(0, 0, 0);\n"
        "background-color: rgb(211, 211, 211);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.satelliteModes = {}
        self.setSatelliteModes()

        self.data = {}
        self.value.value.connect(self.updateData)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    # add text to ui, no translation
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Satellite Status ", None))
        self.serverMessageLabel.setText(QCoreApplication.translate("MainWindow", u"Message from Server", None))
        self.shutDownButton.setText(QCoreApplication.translate("MainWindow", u"Shut Down", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Sensor Calibration Status", None))
        self.missionStartButton.setText(QCoreApplication.translate("MainWindow", u"Initiate Mission Mode", None))
        self.commandCountLabel.setText(QCoreApplication.translate("MainWindow", u"Command count :", None))
        self.modeLabel.setText(QCoreApplication.translate("MainWindow", u"Mode :", None))
        self.motorSpeedLabel.setText(QCoreApplication.translate("MainWindow", u"Motor speed :", None))
        self.commandCnt.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.modeText.setText(QCoreApplication.translate("MainWindow", u"Docking", None))
        self.telecommandButton.setText(QCoreApplication.translate("MainWindow", u"Send Telecommand", None))
        self.telecommandModeLabel.setText(QCoreApplication.translate("MainWindow", u"Telecommand mode", None))
        self.allTelecommandsLabel.setText(QCoreApplication.translate("MainWindow", u"All Telecommands", None))
    
    # add dropdown in telecommand type combobox
    def addDropdownItems(self):
        f = open("Assets/telecommand_modes.json")
        json_array = json.load(f)

        for item in json_array:
            self.modes[item] = {}
            self.modes[item]["id"] = json_array[item]["id"]
            self.modeDropdown.addItem(str(item)+" "+"("+str(json_array[item]["id"]) +")")
            self.modes[item]["data"] = json_array[item]["data"]
            self.modes[item]["data_type"] = json_array[item]["data_type"]
    
    # set satellite mode
    def setSatelliteModes(self):
        f = open("Assets/satellite_modes.json")
        json_array = json.load(f)

        for item in json_array:
            self.satelliteModes[json_array[item]["id"]] = item
    
    # initiate docking mission
    def initiateMission(self):
        data = []
        command_id = self.modes["SetMode_Mission"]["id"]
        data.append(command_id)
        self.parent.sendTelecommand(data)
    
    # electrical shutdown of satellite
    def shutDown(self):
        data = []
        command_id = self.modes["Shutdown"]["id"]
        data.append(command_id)
        self.parent.sendTelecommand(data)
    
    # update the mode parameters
    def updateModeParameters(self):
        currentText= self.modeDropdown.currentText()
        print("mode has been updated to:", currentText)

        data = self.modes[currentText]["data"]
        types = {
            "x": {
                "input":self.xTextEdit,
                },
            "y": {
                "input":self.yTextEdit,
                },
            "z": {
                "input":self.zTextEdit,
                }
        }
        
        for type in types:
            if type in data:
                (types[type]["input"]).setPlaceholderText(data[type])
                (types[type]["input"]).show()
                continue

            (types[type]["input"]).hide()

    # common platform to send all telecommands
    def mainTelecommand(self):
        try:
            data = []
            currentText= self.modeDropdown.currentText()
            currentMode = self.modes[currentText]
            limitingMode = ["SetControlDesired_vel", "SetControlDesired_speed", "SetControlDesired_pos"]
            data.append(currentMode["id"])
            expectedData = currentMode["data"]

            types = {"x": self.xTextEdit,
                    "y": self.yTextEdit, 
                    "z": self.zTextEdit}
            
            if currentText in limitingMode:
                self.currentCommand = currentText
                self.limit = float(self.xTextEdit.toPlainText())

            for key in expectedData.keys():
                value = float(types[key].toPlainText())

                if currentMode["data_type"] == "radian":
                    value = math.radians(value)
                    
                data.append(value)

            self.parent.sendTelecommand(data)
        except Exception as ex:
            print("exception sending telecommand:", ex)
            self.currentCommand = ""
            self.limit = 0

    # update the value, called when new data is received
    def updateTrigger(self,data):
        try:
            # self.value+=1
            self.data = data
            self.value.value.emit()
        except Exception as ex:
            print("telecommand update trigger:", ex)
        
    # slot that actually updates the value
    def updateData(self):      
        try:
            data = self.data

            if "telemetryMessage" in data.keys():
                topicName = "telemetryMessage"
                topicData = data[topicName]["data"]
                self.messageText.setText(str(topicData["message"])[2:-1])

            if "telemetryCalibIMU" in data.keys():
                topicName = "telemetryCalibIMU"
                topicData = data[topicName]["data"]

            if "telemetryContinuous" in data.keys():
                topicName = "telemetryContinuous"
                topicData = data[topicName]["data"]
                topicStruc = data[topicName]
                self.commandCnt.setText(str(topicData["cmdCnt"]))

                mode_id = topicData["modeid"]
                self.modeText.setText(self.satelliteModes[mode_id]+"("+str(mode_id)+")")
                self.motorSpeed.setText(str(topicData["speed"]))
                self.lastCommand.setText(str(topicData["lastcmdid"]))

                q0 = topicData["q0"]
                q1 = topicData["q1"]
                q2 = topicData["q2"]
                q3 = topicData["q3"]

                yaw = math.degrees(math.atan2(2 * (q0 * q3 + q1 * q2), 1 - 2 * (q2 * q2 + q3 * q3)))

                # update satellite visualization
                self.satAnimation.inMission = self.parent.programStatus["inMission"]

                # armVelocity
                self.satAnimation.mocksatVelocity = topicData["mockupAngularVelocity"] 
                self.satAnimation.floatsatAngle =  yaw
                self.satAnimation.armTranslate = topicData["arm_extension"]

                # mockup
                self.satAnimation.mocksatDistance= topicData["mockupDistance"]
                self.satAnimation.mocksatAngle =  topicData["mockupYaw"]
                self.satAnimation.yaw2mockup = topicData["yaw2mockup"]

                self.satAnimation.update()
                #end update sat vizualization    

                # update motor speed graph
                tempData = topicStruc["pairedData"]["speed"]

                x = list(tempData.keys())
                y = list(tempData.values())

                self.motorSpeedGraph.clear()
                self.motorSpeedGraph.plot(x, y, pen='g', symbol='x',
                         symbolPen='g', symbolBrush=0.2, name='green')

                if self.currentCommand == "SetControlDesired_speed" :
                    limit = self.limit
                    self.motorSpeedGraph.plot(x,np.full(len(x), float(limit)), pen='b', symbol='o',
                         symbolPen='b', symbolBrush=0.2, name='blue')
                # end update motor speed
                
                # update orientation graph
                tempData = topicStruc["pairedData"]["yaw"]

                x = list(tempData.keys())
                y = list(tempData.values())

                self.orientationGraph.clear()
                self.orientationGraph.plot(x, y, pen='g', symbol='x',
                         symbolPen='g', symbolBrush=0.2, name='green')

                if self.currentCommand == "SetControlDesired_pos" :
                    limit = self.limit
                    self.orientationGraph.plot(x,np.full(len(x), float(limit)), pen='b', symbol='o',
                         symbolPen='b', symbolBrush=0.2, name='blue')
                # end update orientation
                

                # update angular velocity
                tempData = topicStruc["pairedData"]["velocity"]

                x = list(tempData.keys())
                y = list(tempData.values())

                self.angularVelocityGraph.clear()
                self.angularVelocityGraph.plot(x, y, pen='g', symbol='x',
                         symbolPen='g', symbolBrush=0.2, name='green')

                if self.currentCommand == "SetControlDesired_vel" :
                    limit = self.limit
                    self.angularVelocityGraph.plot(x,np.full(len(x), float(limit)), pen='b', symbol='o',
                         symbolPen='b', symbolBrush=0.2, name='blue')

        except Exception as expe:
            print("exception telecommand update:", expe)
