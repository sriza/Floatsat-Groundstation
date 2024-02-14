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
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QLabel,
    QMainWindow, QMenu, QMenuBar, QProgressBar,
    QPushButton, QRadioButton, QSizePolicy, QStatusBar, QLCDNumber,
    QWidget)
import math

class DebugSignal(QObject):
    value = Signal()

class Debug_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        # MainWindow.resize(1265, 820)
        self.parent = MainWindow
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(30, 10, 1200, 800))
        self.frame.setAutoFillBackground(True)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(100, 120, 291, 51))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.createDebugList()
        self.retranslateUi(MainWindow)

        self.data = {}
        self.value = DebugSignal()
        self.value.value.connect(self.updateData)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
    # retranslateUi
        
    def createDebugList(self):
        try:
            max_height = 600
            max_width = 1200

            # keep track of the length of table
            segment_width = max_width/7-20

            # keep track of where the pen should be
            x_pos = 0
            y_pos = 0

            # keeps track of starting point of groupbox
            groupbox_x = 0
            groupbox_y = 0

            # debug and topic header + groupbox items
            data = self.parent.telemetry
            self.topicDataUI = {}
            self.topicUI = {}

            for topic in data:
                # data
                topicName = topic
                topicData = data[topicName]["data"]

                # update pointer in the screen
                y_pos = 0
                data_height = 35


                #create topic header
                self.topicUI[topic] = {}
                self.topicUI[topic]["topic"]= QLabel(self.frame)
                self.topicUI[topic]["topic"].setGeometry(QRect(x_pos, y_pos, segment_width-10, 45))
                self.topicUI[topic]["topic"].setText(topic+":")
                y_pos = 35

                self.topicDataUI[topic] = {}

                # update height of message if it is topic telemetry message
                if topic == "telemetryMessage":
                    data_height = 200

                for key in topicData.keys():
                    if y_pos+data_height > max_height:
                        x_pos+=segment_width+10
                        groupbox_y = y_pos+10
                        y_pos = 35

                    self.topicDataUI[topic][key] = {}
                    self.topicDataUI[topic][key]["label_ui"] = QLabel(self.frame)
                    self.topicDataUI[topic][key]["label_ui"].setWordWrap(True)
                    (self.topicDataUI[topic][key]["label_ui"]).setGeometry(QRect(x_pos, y_pos, segment_width-10, 15))
                    (self.topicDataUI[topic][key]["label_ui"]).setText(key+":")

                    self.topicDataUI[topic][key]["data_ui"] = QLabel(self.frame)
                    (self.topicDataUI[topic][key]["data_ui"]).setWordWrap(True)
                    (self.topicDataUI[topic][key]["data_ui"]).setGeometry(QRect(x_pos, y_pos+15, segment_width-10, data_height-15))
                    (self.topicDataUI[topic][key]["data_ui"]).setStyleSheet(u"background-color: rgb(26, 29, 56); color: rgb(255, 255, 255);")
                    (self.topicDataUI[topic][key]["data_ui"]).setText(str(topicData[key]))
                    y_pos +=data_height 

                self.topicUI[topic]["groupBox"]= QGroupBox(self.frame)
                self.topicUI[topic]["groupBox"].setGeometry(QRect(groupbox_x, 0, x_pos-groupbox_x+3+segment_width, groupbox_y+10))

                x_pos += segment_width+10
                groupbox_x = x_pos-5 
        except Exception as ex:
            print("debug create exception:", ex)
    
    # triggers data update
    def updateTrigger(self, data):
        try:
            print("update trigger")
            self.data = data
            self.value.value.emit()
        except Exception as ex:
            print("debug update trigger:", ex)
        
    @Slot()
    def updateData(self):
        try:
            data = self.data
            for topic in data:
                topicName = topic
                topicData = data[topicName]["data"]

                for key in topicData.keys():
                    keyData = topicData[key]

                    if isinstance(keyData, float):
                        keyData = round(keyData, 10)

                    (self.topicDataUI[topic][key]["data_ui"]).setText(str(topicData[key]))
        except Exception as ex:
            print("exception debug update:", ex)

