# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Docking.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QLabel,
    QMainWindow, QMenu, QMenuBar, QProgressBar,QLCDNumber,
    QPushButton, QRadioButton, QSizePolicy, QStatusBar,QCheckBox,
    QWidget)
from Views.CustomWidgets.SatelliteAnimation import SatelliteAnimation
import math
import json
class DockingSignal(QObject):
    value = Signal()

class Docking_MainWindow(object):

    def setupUi(self, MainWindow):
        super(Docking_MainWindow, self).__init__()
        self.value = DockingSignal()

        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        # MainWindow.resize(1265, 820)
        self.parent = MainWindow
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(30, 10, 841, 471))
        self.frame.setAutoFillBackground(True)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.satAnimationLabel = QLabel(self.frame)
        self.satAnimationLabel.setObjectName(u"label")
        self.satAnimationLabel.setGeometry(QRect(50, 120, 291, 51))

        self.satAnimation = SatelliteAnimation(self.centralwidget)
        self.satAnimation.setObjectName(u"satAnimation")
        self.satAnimation.setGeometry(QRect(30, 10, 600, 400))

        self.missionCommandGroupBox = QGroupBox(self.centralwidget)
        self.missionCommandGroupBox.setObjectName(u"missionCommandGroupBox")
        self.missionCommandGroupBox.setGeometry(QRect(950, 20, 300, 171))
        # self.missionCommandGroupBox.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.cancelMissionButton = QPushButton(self.missionCommandGroupBox)
        self.cancelMissionButton.setObjectName(u"pushButton")
        self.cancelMissionButton.setGeometry(QRect(30, 100, 240, 50))
        self.cancelMissionButton.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 2, 36);\n"
"background-color: rgb(184, 5, 14);")
        self.cancelMissionButton.clicked.connect(self.stopMission)

        self.initiateDockingButton = QPushButton(self.missionCommandGroupBox)
        self.initiateDockingButton.setObjectName(u"initiateDockingButton")
        self.initiateDockingButton.setGeometry(QRect(30, 40, 240, 50))
        self.initiateDockingButton.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(15, 102, 28);")
        self.initiateDockingButton.clicked.connect(self.initiateMission)

        self.missionGroupBox = QGroupBox(self.centralwidget)
        self.missionGroupBox.setObjectName(u"armPositionGroupBox_3")
        self.missionGroupBox.setGeometry(QRect(650, 20, 250, 261))
     
        self.progressBar = QProgressBar(self.missionGroupBox)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(30, 40, 200, 30))
        self.progressBar.setValue(0)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(30, 425, 1211, 350))
        self.frame_2.setStyleSheet(u"background-color: rgb(200, 200, 200);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        # arm position group
        self.armPositionGroupBox = QGroupBox(self.frame_2)
        self.armPositionGroupBox.setObjectName(u"armPositionGroupBox")
        self.armPositionGroupBox.setGeometry(QRect(30, 20, 301, 250))
        # self.armPositionGroupBox.setStyleSheet(u"color: rgb(4, 4, 4);")
        
        self.extensionVelocityLabel = QLabel(self.armPositionGroupBox)
        self.extensionVelocityLabel.setObjectName(u"extensionVelocityLabel")
        self.extensionVelocityLabel.setGeometry(QRect(10, 30, 141, 16))

        self.extensionVelocity = QLCDNumber(self.armPositionGroupBox)
        self.extensionVelocity.setObjectName(u"extensionVelocity")
        self.extensionVelocity.setGeometry(QRect(10, 50, 200, 40))
        self.extensionVelocity.display(2)

        self.armLengthLabel = QLabel(self.armPositionGroupBox)
        self.armLengthLabel.setObjectName(u"armLengthLabel")
        self.armLengthLabel.setGeometry(QRect(10, 100, 141, 16))

        self.armLength = QLCDNumber(self.armPositionGroupBox)
        self.armLength.setObjectName(u"armLength")
        self.armLength.setGeometry(QRect(10, 120, 200, 40))
        self.extensionVelocity.display(100)

        self.extendedLengthLabel = QLabel(self.armPositionGroupBox)
        self.extendedLengthLabel.setObjectName(u"extendedLengthLabel")
        self.extendedLengthLabel.setGeometry(QRect(10, 170, 141, 16))

        self.extendedLength = QLCDNumber(self.armPositionGroupBox)
        self.extendedLength.setObjectName(u"extendedLength")
        self.extendedLength.setGeometry(QRect(10, 190, 200, 40))
        self.extensionVelocity.display(2)

        # mocksat group
        self.mockupStatusGroupBox = QGroupBox(self.frame_2)
        self.mockupStatusGroupBox.setObjectName(u"mockupStatusGroupBox")
        self.mockupStatusGroupBox.setGeometry(QRect(380, 20, 361, 250))
        self.mockupStatusGroupBox.setStyleSheet(u"color: rgb(4, 4, 4);")

        self.mockupDistanceLabel = QLabel(self.mockupStatusGroupBox)
        self.mockupDistanceLabel.setObjectName(u"mockupDistanceLabel")
        self.mockupDistanceLabel.setGeometry(QRect(10, 30, 141, 16))

        self.mockupDistance = QLCDNumber(self.mockupStatusGroupBox)
        self.mockupDistance.setObjectName(u"mockupDistance")
        self.mockupDistance.setGeometry(QRect(10, 50, 200, 40))

        self.mockupVelocityLabel = QLabel(self.mockupStatusGroupBox)
        self.mockupVelocityLabel.setObjectName(u"mockupVelocityLabel")
        self.mockupVelocityLabel.setGeometry(QRect(10, 100, 161, 16))

        self.mockupVelocity = QLCDNumber(self.mockupStatusGroupBox)
        self.mockupVelocity.setObjectName(u"mockupVelocity")
        self.mockupVelocity.setGeometry(QRect(10, 120, 200, 40))

        self.mockupOrientationLabel = QLabel(self.mockupStatusGroupBox)
        self.mockupOrientationLabel.setObjectName(u"mockupOrientationLabel")
        self.mockupOrientationLabel.setGeometry(QRect(10, 170, 141, 16))

        self.mockupOrientation = QLCDNumber(self.mockupStatusGroupBox)
        self.mockupOrientation.setObjectName(u"mockupOrientation")
        self.mockupOrientation.setGeometry(QRect(10, 190, 200, 40))

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.data = {}
        self.value.value.connect(self.updateData)

        self.modes = {}
        self.setModes()

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.satAnimationLabel.setText(QCoreApplication.translate("MainWindow", u"Camera view of docking", None))
        self.missionCommandGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Mission Command", None))
        self.cancelMissionButton.setText(QCoreApplication.translate("MainWindow", u"Cancel Docking Mission", None))
        self.initiateDockingButton.setText(QCoreApplication.translate("MainWindow", u"Initiate Docking", None))
        self.missionGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Mission Profile", None))
        self.armPositionGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Arm Position", None))
        self.extensionVelocityLabel.setText(QCoreApplication.translate("MainWindow", u"Rate of extension", None))
        self.armLengthLabel.setText(QCoreApplication.translate("MainWindow", u"Arm Length", None))
        self.extendedLengthLabel.setText(QCoreApplication.translate("MainWindow", u"Extended length", None))
        self.mockupStatusGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Mockup Status", None))
        self.mockupDistanceLabel.setText(QCoreApplication.translate("MainWindow", u"Distance from floatsat", None))
        self.mockupVelocityLabel.setText(QCoreApplication.translate("MainWindow", u"Calculated Angular velocity", None))
        self.mockupOrientationLabel.setText(QCoreApplication.translate("MainWindow", u"Orientation", None))
    # retranslateUi

    def setModes(self):
        f = open("Assets/telecommand_modes.json")
        json_array = json.load(f)

        for item in json_array:
            self.modes[item] = {}
            self.modes[item]["id"] = json_array[item]["id"]
            self.modes[item]["data"] = json_array[item]["data"]

    # create UI for mission modes
    def createMissionModes(self, missionModes):
        try:
            print("in create mission modes", missionModes)
            self.modesUI = {}
            i = 0
            completedCount = 0

            for mode in missionModes:
                print("mode")
                self.modesUI[mode] = {}
                self.modesUI[mode]["radioButton"] = QCheckBox(self.missionGroupBox)
                (self.modesUI[mode]["radioButton"]).setObjectName("checkbox")
                (self.modesUI[mode]["radioButton"]).setGeometry(QRect(30, 90+30*i, 250, 22))
                (self.modesUI[mode]["radioButton"]).setText(missionModes[mode]["name"])

                if missionModes[mode]["status"]:
                    completedCount+=1
                    (self.modesUI[mode]["radioButton"]).toggle()

                i+=1
            
            self.progressBar.value = (100*completedCount/i)
            
        except Exception as ex:
            print("exception in creating mission modes",ex)

    def initiateMission(self):
        data = []
        command_id = self.modes["SetMode_Mission"]["id"]
        data.append(command_id)
        self.parent.sendTelecommand(data)

            
    def stopMission(self):
        data = []
        command_id = self.modes["SetMode_Idle"]["id"]
        data.append(command_id)
        self.parent.sendTelecommand(data)

    def updateTrigger(self,data):
        try:
            # self.value+=1
            self.data = data
            self.value.value.emit()
        except Exception as ex:
            print("docking update trigger:", ex)
    
    # @Slot()
    def updateData(self):        
        try:
            data = self.data

            if "telemetryContinuous" in data.keys():
                topicName = "telemetryContinuous"
                topicData = data[topicName]["data"]

                # print(data[topicName])
                missionData = data[topicName]["missionModes"]
                print(missionData)

                i= 0 
                total = len(self.modesUI)
                per = 100/total

                for mode in self.modesUI:
                    radioButton = self.modesUI[mode]["radioButton"]
                    buttonStatus = radioButton.isChecked()
                    missionStatus = missionData[mode]["status"]
                    print(mode, buttonStatus, missionStatus)

                    if buttonStatus != missionStatus:
                        radioButton.toggle()

                    if radioButton.isChecked():
                        i+=per
                
                self.progressBar.setValue(i)

                self.mockupDistance.display(topicData["mockupDistance"])
                self.mockupOrientation.display(topicData["mockupYaw"])
                self.mockupVelocity.display(topicData["mockupAngularVelocity"])
                self.armLength.display(100)
                self.extensionVelocity.display(topicData["armVelocity"])
                self.extendedLength.display(topicData["arm_extension"])

                q0 = topicData["q0"]
                q1 = topicData["q1"]
                q2 = topicData["q2"]
                q3 = topicData["q3"]
            
                roll = math.degrees(math.atan2(2 * (q0 * q1 + q2 * q3), 1 - 2 * (q1 * q1 + q2 * q2)))
                pitch = math.degrees(math.asin(2 * (q0 * q2 - q3 * q1)))                         
                yaw = math.degrees(math.atan2(2 * (q0 * q3 + q1 * q2), 1 - 2 * (q2 * q2 + q3 * q3)))

                # update satellite visualization
                # armVelocity
                # self.satAnimation.mocksatVelocity = topicData["mocksatAngularVelocity"] 
                # self.satAnimation.floatsatAngle = yaw
                # self.satAnimation.armExtension =  topicData["armExtension"]

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

                # # mockup
                # self.satAnimation.mocksatDistance= topicData["mockupDistanceLabel"]
                # self.satAnimation.mocksatAngle =  topicData["mockupYaw"]

                # self.satAnimation.armTranslate+=15
                # self.satAnimation.update()

        except Exception as ex:
            print("exception docking update:", ex)

