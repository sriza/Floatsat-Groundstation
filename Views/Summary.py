# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'summary.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, Qt, QSize, Signal, Slot, QObject)
from PySide6.QtGui import (QAction, QBrush, QColor, QFont)
from PySide6.QtOpenGLWidgets import QOpenGLWidget
from PySide6.QtWidgets import (QFrame, QGraphicsView, QGroupBox, QLCDNumber, 
    QLabel, QMenu, QMenuBar, QProgressBar, QPushButton, QStatusBar, QTextEdit, 
    QWidget, QHBoxLayout, QWidgetItem, )
import pyqtgraph as pg
from Views.CustomWidgets.YawVisualizer import YawVisualizer
from Views.CustomWidgets.SatelliteAnimation import SatelliteAnimation
import math
import json

class SummarySignal(QObject):
    value = Signal()
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        self.centralwidget = QWidget(MainWindow)
        MainWindow.resize(1265, 825)
        self.parent = MainWindow
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(30, 10, 261, 721))
        self.frame.setAutoFillBackground(True)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        # fonts
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(20)

        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(12)

        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(14)

        font3 = QFont()
        font3.setPointSize(14)

        font4 = QFont()
        font4.setFamilies([u"Arial"])
        font4.setPointSize(16)
        #font end

        self.textEdit = QWidget(self.frame)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(0, 0, 261, 51))
        self.textEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 211, 30))
        self.label.setFont(font)

        self.roll_label = QLabel(self.frame)
        self.roll_label.setObjectName(u"label_3")
        self.roll_label.setGeometry(QRect(30, 100, 121, 30))
        self.roll_label.setFont(font1)

        self.lcdRoll = QLCDNumber(self.frame)
        self.lcdRoll.setObjectName(u"lcdRoll")
        self.lcdRoll.setGeometry(QRect(30, 130, 201, 40))

        self.pitch_label = QLabel(self.frame)
        self.pitch_label.setObjectName(u"label_4")
        self.pitch_label.setGeometry(QRect(30, 170, 121, 30))
        self.pitch_label.setFont(font1)

        self.lcdPitch = QLCDNumber(self.frame)
        self.lcdPitch.setObjectName(u"lcdPitch")
        self.lcdPitch.setGeometry(QRect(30, 200, 201, 40))

        self.yaw_label = QLabel(self.frame)
        self.yaw_label.setObjectName(u"label_5")
        self.yaw_label.setGeometry(QRect(30, 240, 121, 30))
        self.yaw_label.setFont(font1)

        self.lcdYaw = QLCDNumber(self.frame)
        self.lcdYaw.setObjectName(u"lcdYaw")
        self.lcdYaw.setGeometry(QRect(30, 270, 201, 40))

        self.orientation_groupBox = QGroupBox(self.frame)
        self.orientation_groupBox.setObjectName(u"groupBox")
        self.orientation_groupBox.setGeometry(QRect(20, 70, 231, 270))
        self.orientation_groupBox.setFont(font2)

        self.parameter_groupBox = QGroupBox(self.frame)
        self.parameter_groupBox.setObjectName(u"groupBox_2")
        self.parameter_groupBox.setGeometry(QRect(20, 340, 221, 250))
        self.parameter_groupBox.setFont(font2)

        self.temperature = QLabel(self.parameter_groupBox)
        self.temperature.setObjectName(u"label_6")
        self.temperature.setGeometry(QRect(10, 30, 121, 30))
        self.temperature.setFont(font1)

        self.lcdTemperature = QLCDNumber(self.parameter_groupBox)
        self.lcdTemperature.setObjectName(u"lcdTemperature")
        self.lcdTemperature.setGeometry(QRect(10, 60, 201, 40))

        self.motorSpeedLabel = QLabel(self.parameter_groupBox)
        self.motorSpeedLabel.setObjectName(u"motorSpeedLabel")
        self.motorSpeedLabel.setGeometry(QRect(10, 100, 161, 31))
        self.motorSpeedLabel.setFont(font1)

        self.lcdSpeed = QLCDNumber(self.parameter_groupBox)
        self.lcdSpeed.setObjectName(u"lcdSpeed")
        self.lcdSpeed.setGeometry(QRect(10, 130, 201, 41))

        self.velocityLabel = QLabel(self.parameter_groupBox)
        self.velocityLabel.setObjectName(u"velocityLabel")
        self.velocityLabel.setGeometry(QRect(10, 170, 161, 31))
        self.velocityLabel.setFont(font1)

        self.satelliteVelocity = QLCDNumber(self.parameter_groupBox)
        self.satelliteVelocity.setObjectName(u"satelliteVelocity")
        self.satelliteVelocity.setGeometry(QRect(10, 200, 201, 41))
        
        self.parameter_groupBox.raise_()
        self.orientation_groupBox.raise_()
        self.textEdit.raise_()
        self.label.raise_()
        self.lcdRoll.raise_()
        self.lcdYaw.raise_()
        self.lcdPitch.raise_()
        self.lcdTemperature.raise_()
        self.lcdSpeed.raise_()
        self.roll_label.raise_()
        self.pitch_label.raise_()
        self.yaw_label.raise_()

        self.satAnimation = SatelliteAnimation(self.centralwidget)
        self.satAnimation.setObjectName(u"graphicsView")
        self.satAnimation.setGeometry(QRect(330, 10, 571, 400))
        self.satAnimation.setAutoFillBackground(True)

        # self.satAnimation.setBackgroundBrush(brush)
        brush = QBrush(QColor(255, 124, 234, 255))
        brush.setStyle(Qt.NoBrush)

        self.graphicsView_4 = QGraphicsView(self.centralwidget)
        self.graphicsView_4.setObjectName(u"graphicsView_4")
        self.graphicsView_4.setGeometry(QRect(930, 10, 271, 411))
        self.graphicsView_4.setAutoFillBackground(True)
        brush1 = QBrush(QColor(255, 124, 234, 255))
        brush1.setStyle(Qt.NoBrush)
        self.graphicsView_4.setBackgroundBrush(brush1)

        self.graphicsView_5 = QGraphicsView(self.centralwidget)
        self.graphicsView_5.setObjectName(u"graphicsView_5")
        self.graphicsView_5.setGeometry(QRect(930, 530, 271, 151))
        self.graphicsView_5.setAutoFillBackground(True)
        self.graphicsView_5.setStyleSheet(u"background-color: rgb(225, 225, 225);")
        brush2 = QBrush(QColor(255, 124, 234, 255))
        brush2.setStyle(Qt.NoBrush)
        self.graphicsView_5.setBackgroundBrush(brush2)
        
        self.Connection = QWidget(self.centralwidget)
        self.Connection.setObjectName(u"Connection")
        self.Connection.setGeometry(QRect(930, 480, 271, 51))
        self.Connection.setFont(font3)
        self.Connection.setStyleSheet(u"background-color: rgb(211, 211, 211);")
        
        self.connectionOverviewLabel = QLabel(self.Connection)
        self.connectionOverviewLabel.setObjectName(u"label_2")
        self.connectionOverviewLabel.setGeometry(QRect(10, 10, 261, 31))
        self.connectionOverviewLabel.setFont(font4)
        self.connectionOverviewLabel.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.Connection_2 = QWidget(self.centralwidget)
        self.Connection_2.setObjectName(u"Connection_2")
        self.Connection_2.setGeometry(QRect(930, 10, 271, 51))
        self.Connection_2.setFont(font3)
        self.Connection_2.setStyleSheet(u"background-color: rgb(211, 211, 211);")

        self.battery_label = QLabel(self.Connection_2)
        self.battery_label.setObjectName(u"battery_label")
        self.battery_label.setGeometry(QRect(10, 10, 231, 31))
        self.battery_label.setFont(font4)
        self.battery_label.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.connectButton = QPushButton(self.centralwidget)
        self.connectButton.setObjectName(u"connectButton")
        self.connectButton.setGeometry(QRect(950, 550, 231, 41))
        self.connectButton.setStyleSheet(u"color: rgb(255, 255, 255);\n"
        "background-color: rgb(50, 107, 29);")
        self.connectButton.clicked.connect(self.startUDP)

        self.disconnectButton = QPushButton(self.centralwidget)
        self.disconnectButton.setObjectName(u"disconnectButton")
        self.disconnectButton.setGeometry(QRect(950, 600, 231, 41))
        self.disconnectButton.setStyleSheet(u"color: rgb(255, 255, 255);\n"
        "background-color: rgb(182, 41, 16);")
        self.disconnectButton.clicked.connect(self.stopUDP)

        self.orientation_visualizer_label = QLabel(self.centralwidget)
        self.orientation_visualizer_label.setObjectName(u"label_11")
        self.orientation_visualizer_label.setGeometry(QRect(330, 450, 191, 31))
        self.orientation_visualizer_label.setFont(font1)

        self.pfd = YawVisualizer(self.centralwidget) 
        self.pfd.zoom = 0.3
        self.pfd.setGeometry(QRect(330, 480, 270, 200))
        self.pfd.setMinimumSize(QSize(270, 200))
        self.pfd.show()

        self.volt_visualizer = QLabel(self.centralwidget)
        self.volt_visualizer.setObjectName(u"volt_visualizer")
        self.volt_visualizer.setGeometry(QRect(630, 450, 191, 31))
        self.volt_visualizer.setFont(font1)

        # temperature graph
        self.graphWidget = pg.PlotWidget(self.centralwidget)
        self.graphWidget.setGeometry(QRect(630,480,270,200))
        self.graphWidget.setMinimumSize(QSize(270, 200))
        self.graphWidget.setYRange(10,15)

        # self.graphWidget.setBackground('w')

        self.shutDownButton = QPushButton(self.centralwidget)
        self.shutDownButton.setObjectName(u"shutDownButton")
        self.shutDownButton.setGeometry(QRect(950, 350, 231, 50))
        self.shutDownButton.setStyleSheet(u"color: rgb(255, 255, 255);\n"
        "background-color: rgb(182, 41, 16);")
        self.shutDownButton.clicked.connect(self.shutDown)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(950, 80, 221, 51))

        self.voltageLabel = QLabel(self.centralwidget)
        self.voltageLabel.setObjectName(u"voltageLabel")
        self.voltageLabel.setGeometry(QRect(950, 150, 121, 31))
        self.voltageLabel.setFont(font1)

        self.lcdVoltage = QLCDNumber(self.centralwidget)
        self.lcdVoltage.setObjectName(u"lcdNumber_9")
        self.lcdVoltage.setGeometry(QRect(950, 180, 191, 41))

        self.currentLabel = QLabel(self.centralwidget)
        self.currentLabel.setObjectName(u"currentLabel")
        self.currentLabel.setGeometry(QRect(950, 230, 121, 31))
        self.currentLabel.setFont(font1)

        self.lcdCurrent = QLCDNumber(self.centralwidget)
        self.lcdCurrent.setObjectName(u"lcdNumber_9")
        self.lcdCurrent.setGeometry(QRect(950, 260, 191, 41))

        self.label_15 = QLabel(self.centralwidget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(1150, 190, 21, 31))
        self.label_15.setFont(font1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
    
        # self.menubarCollection(MainWindow)
        self.retranslateUi(MainWindow)
        self.modes = {}
        self.setModes()

        self.value = SummarySignal()
        self.value.value.connect(self.updateData)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi
    
    # translation is not required, just used to seperate settext of label for now
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Satellite overview", None))
        self.roll_label.setText(QCoreApplication.translate("MainWindow", u"Roll (degree)", None))
        self.pitch_label.setText(QCoreApplication.translate("MainWindow", u"Pitch (degree)", None))
        self.yaw_label.setText(QCoreApplication.translate("MainWindow", u"Yaw (degree)", None))
        self.orientation_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Orientation", None))
        self.parameter_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Other Parameters", None))
        self.temperature.setText(QCoreApplication.translate("MainWindow", u"Temperature", None))
        self.motorSpeedLabel.setText(QCoreApplication.translate("MainWindow", u"Motor Speed", None))
        self.connectionOverviewLabel.setText(QCoreApplication.translate("MainWindow", u"Connection Overview", None))
        self.battery_label.setText(QCoreApplication.translate("MainWindow", u"Battery", None))
        self.connectButton.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.disconnectButton.setText(QCoreApplication.translate("MainWindow", u"Disconnect", None))
        self.orientation_visualizer_label.setText(QCoreApplication.translate("MainWindow", u"Orientation Visualizer", None))
        self.volt_visualizer.setText(QCoreApplication.translate("MainWindow", u"Voltage Visualizer", None))
        self.shutDownButton.setText(QCoreApplication.translate("MainWindow", u"Shut Down", None))
        self.voltageLabel.setText(QCoreApplication.translate("MainWindow", u"Voltage", None))
        self.currentLabel.setText(QCoreApplication.translate("MainWindow", u"Current(A)", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"V", None))
    
    def setModes(self):
        f = open("Assets/telecommand_modes.json")
        json_array = json.load(f)

        for item in json_array:
            self.modes[item] = {}
            self.modes[item]["id"] = json_array[item]["id"]
            self.modes[item]["data"] = json_array[item]["data"]

    def startUDP(self):
        self.parent.setConnectionStatus(True)

    def stopUDP(self):
        self.parent.setConnectionStatus(False)


    # shutdown of satellite
    def shutDown(self):
        data = []
        command_id = self.modes["Shutdown"]["id"]
        data.append(command_id)
        self.parent.sendTelecommand(data)
    
    def updateTrigger(self,data):
        try:
            # self.value+=1
            self.data = data
            self.value.value.emit()
        except Exception as ex:
            print("summary update trigger:", ex)

    @Slot()
    def updateData(self):
        try:
            data = self.data
            max_voltage = 14.4
            hour = []
            voltage = []

            if "telemetryContinuous" in data.keys():
                topicName = "telemetryContinuous"
                topicStruc = data[topicName]
                topicData = data[topicName]["data"]

                if topicStruc["pairedData"]["U_bat"]:
                    tempData = topicStruc["pairedData"]["U_bat"]
                    hour = list(tempData.keys())
                    voltage = list(tempData.values())
                
                roll = math.degrees(self.parent.satOrientation["roll"])
                pitch = math.degrees(self.parent.satOrientation["pitch"])
                yaw = math.degrees(self.parent.satOrientation["yaw"])

                # lcd data update
                self.lcdRoll.display(roll)
                self.lcdPitch.display(pitch)
                self.lcdYaw.display(yaw)
                self.lcdTemperature.display(topicData["temp"])
                self.lcdSpeed.display(topicData["speed"])
                self.lcdVoltage.display(topicData["U_bat"])
                self.lcdCurrent.display(topicData["I_total"])
                self.satelliteVelocity.display(topicData["velocity"])

                # battery percentage
                batterPer = (topicData["U_bat"]-11.2)/(max_voltage-11.2)*100
                self.progressBar.setValue(batterPer)
                
                if batterPer<0:
                    self.progressBar.setStyleSheet(u"background-color: rgb(182, 41, 16)")
                else:
                    self.progressBar.setStyleSheet(u"background-color: rgb(182, 41, 16)")

                # todo: update progress bar styling
                self.graphWidget.clear()
                self.graphWidget.plot(hour, voltage,pen='g', name='green')


                # update yaw parameter
                self.pfd.heading = yaw
                self.pfd.update()

                # update satellite visualization\
                self.satAnimation.inMission = self.parent.programStatus["inMission"]
                # armVelocity
                self.satAnimation.mocksatVelocity = topicData["mockupAngularVelocity"] 
                # self.satAnimation.mocksatVelocity += .5 
                self.satAnimation.floatsatAngle =  yaw
                self.satAnimation.armTranslate = topicData["arm_extension"]

                # mockup
                self.satAnimation.mocksatDistance= topicData["mockupDistance"]
                # self.satAnimation.mocksatDistance= 44
                self.satAnimation.mocksatAngle =  topicData["mockupYaw"]
                # self.satAnimation.mocksatAngle =  
                self.satAnimation.yaw2mockup = topicData["yaw2mockup"]
                # self.satAnimation.mocksatAngle = 0

                self.satAnimation.update()

        except Exception as ex:
            print("exception summary update:", ex)

    # retranslateUi
    def close(self):
        pass


