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
    QMainWindow, QMenu, QMenuBar, QProgressBar,
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

        self.satelliteVisualization = SatelliteAnimation(self.centralwidget)
        self.satelliteVisualization.setObjectName(u"satelliteVisualization")
        self.satelliteVisualization.setGeometry(QRect(30, 10, 600, 400))

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(900, 300, 341, 171))


        self.cancelMissionButton = QPushButton(self.groupBox_2)
        self.cancelMissionButton.setObjectName(u"pushButton")
        self.cancelMissionButton.setGeometry(QRect(30, 100, 291, 51))
        self.cancelMissionButton.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 2, 36);\n"
"background-color: rgb(184, 5, 14);")
        self.cancelMissionButton.clicked.connect(self.stopMission)

        self.initiateDockingButton = QPushButton(self.groupBox_2)
        self.initiateDockingButton.setObjectName(u"initiateDockingButton")
        self.initiateDockingButton.setGeometry(QRect(30, 40, 291, 51))
        self.initiateDockingButton.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(15, 102, 28);")
        self.initiateDockingButton.clicked.connect(self.initiateMission)

        self.missionGroupBox = QGroupBox(self.centralwidget)
        self.missionGroupBox.setObjectName(u"groupBox_3")
        self.missionGroupBox.setGeometry(QRect(900, 20, 341, 261))
     
        self.progressBar = QProgressBar(self.missionGroupBox)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(30, 40, 291, 20))
        self.progressBar.setValue(0)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(30, 500, 1211, 241))
        self.frame_2.setStyleSheet(u"background-color: rgb(200, 200, 200);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.groupBox = QGroupBox(self.frame_2)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(30, 20, 301, 191))
        self.groupBox.setStyleSheet(u"color: rgb(4, 4, 4);")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 50, 141, 16))
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 100, 141, 16))
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 150, 141, 16))
        self.groupBox_4 = QGroupBox(self.frame_2)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(380, 20, 361, 191))
        self.groupBox_4.setStyleSheet(u"color: rgb(4, 4, 4);")
        self.label_6 = QLabel(self.groupBox_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 90, 141, 16))
        self.label_7 = QLabel(self.groupBox_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 130, 161, 16))
        self.label_8 = QLabel(self.groupBox_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 50, 141, 16))
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
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"IMU Command", None))
        self.cancelMissionButton.setText(QCoreApplication.translate("MainWindow", u"Cancel Docking Mission", None))
        self.initiateDockingButton.setText(QCoreApplication.translate("MainWindow", u"Initiate Docking", None))
        self.missionGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Mission Profile", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Arm Position", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Rate of extension", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Arm Length", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Extended length", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Mockup Status", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Distance from floatsat", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Calculated Angular velocity", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Orientation", None))
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

                # update satellite visualization
                # armVelocity
                self.satAnimation.mocksatVelocity = topicData["mocksatAngularVelocity"] 
                self.satAnimation.floatsatAngle = yaw
                self.satAnimation.armExtension =  topicData["armExtension"]

                # mockup
                self.satAnimation.mocksatDistance= topicData["mockupDistance"]
                self.satAnimation.mocksatAngle =  topicData["mockupYaw"]

                self.satAnimation.armTranslate+=15
                self.satAnimation.update()

        except Exception as ex:
            print("exception docking update:", ex)

