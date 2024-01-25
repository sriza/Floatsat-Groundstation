# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'summary.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, Qt, QSize)
from PySide6.QtGui import (QAction, QBrush, QColor, QFont)
from PySide6.QtOpenGLWidgets import QOpenGLWidget
from PySide6.QtWidgets import (QFrame, QGraphicsView, QGroupBox, QLCDNumber, 
    QLabel, QMenu, QMenuBar, QProgressBar, QPushButton, QStatusBar, QTextEdit, 
    QWidget, QHBoxLayout, QWidgetItem)
import pyqtgraph as pg
from Views.CustomWidgets.QPrimaryFlightDisplay import QPrimaryFlightDisplay
from Views.CustomWidgets.YawVisualizer import YawVisualizer
import time
# import threading
import math

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1265, 802)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(30, 10, 261, 721))
        # self.centralwidget.setStyleSheet(u"background-color: rgb(26, 29, 56);")
        self.frame.setAutoFillBackground(True)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.textEdit = QTextEdit(self.frame)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(0, 0, 261, 51))
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 211, 31))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(20)
        self.label.setFont(font)
        self.lcdRoll = QLCDNumber(self.frame)
        self.lcdRoll.setObjectName(u"lcdRoll")
        self.lcdRoll.setGeometry(QRect(30, 130, 201, 41))
        self.lcdRoll.display(5000.9986)

        self.lcdYaw = QLCDNumber(self.frame)
        self.lcdYaw.setObjectName(u"lcdYaw")
        self.lcdYaw.setGeometry(QRect(30, 310, 201, 41))
        self.lcdYaw.display(2)
    
        self.lcdPitch = QLCDNumber(self.frame)
        self.lcdPitch.setObjectName(u"lcdPitch")
        self.lcdPitch.setGeometry(QRect(30, 220, 201, 41))
        self.lcdPitch.display(3)


        self.lcdTemperature = QLCDNumber(self.frame)
        self.lcdTemperature.setObjectName(u"lcdTemperature")
        self.lcdTemperature.setGeometry(QRect(30, 510, 201, 41))
        self.lcdTemperature.display(4)

        self.lcdAngVelocity = QLCDNumber(self.frame)
        self.lcdAngVelocity.setObjectName(u"lcdAngVelocity")
        self.lcdAngVelocity.setGeometry(QRect(30, 620, 201, 41))
        self.lcdAngVelocity.display(5)

        self.roll_label = QLabel(self.frame)
        self.roll_label.setObjectName(u"label_3")
        self.roll_label.setGeometry(QRect(30, 100, 121, 31))

        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(12)
        self.roll_label.setFont(font1)

        self.pitch_label = QLabel(self.frame)
        self.pitch_label.setObjectName(u"label_4")
        self.pitch_label.setGeometry(QRect(30, 190, 121, 31))
        self.pitch_label.setFont(font1)

        self.yaw_label = QLabel(self.frame)
        self.yaw_label.setObjectName(u"label_5")
        self.yaw_label.setGeometry(QRect(30, 280, 121, 31))
        self.yaw_label.setFont(font1)

        self.orientation_groupBox = QGroupBox(self.frame)
        self.orientation_groupBox.setObjectName(u"groupBox")
        self.orientation_groupBox.setGeometry(QRect(20, 70, 231, 321))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(14)
        self.orientation_groupBox.setFont(font2)

        self.parameter_groupBox = QGroupBox(self.frame)
        self.parameter_groupBox.setObjectName(u"groupBox_2")
        self.parameter_groupBox.setGeometry(QRect(20, 430, 221, 271))
        self.parameter_groupBox.setFont(font2)

        self.temperature = QLabel(self.parameter_groupBox)
        self.temperature.setObjectName(u"label_6")
        self.temperature.setGeometry(QRect(10, 50, 121, 31))
        self.temperature.setFont(font1)

        self.label_7 = QLabel(self.parameter_groupBox)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 160, 161, 31))
        self.label_7.setFont(font1)
        
        self.parameter_groupBox.raise_()
        self.orientation_groupBox.raise_()
        self.textEdit.raise_()
        self.label.raise_()
        self.lcdRoll.raise_()
        self.lcdYaw.raise_()
        self.lcdPitch.raise_()
        self.lcdTemperature.raise_()
        self.lcdAngVelocity.raise_()
        self.roll_label.raise_()
        self.pitch_label.raise_()
        self.yaw_label.raise_()

        self.graphicsView = QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(330, 10, 571, 491))
        self.graphicsView.setAutoFillBackground(True)
        brush = QBrush(QColor(255, 124, 234, 255))
        brush.setStyle(Qt.NoBrush)
        self.graphicsView.setBackgroundBrush(brush)
        self.graphicsView_4 = QGraphicsView(self.centralwidget)
        self.graphicsView_4.setObjectName(u"graphicsView_4")
        self.graphicsView_4.setGeometry(QRect(930, 10, 271, 291))
        self.graphicsView_4.setAutoFillBackground(True)
        brush1 = QBrush(QColor(255, 124, 234, 255))
        brush1.setStyle(Qt.NoBrush)
        self.graphicsView_4.setBackgroundBrush(brush1)
        self.graphicsView_5 = QGraphicsView(self.centralwidget)
        self.graphicsView_5.setObjectName(u"graphicsView_5")
        self.graphicsView_5.setGeometry(QRect(930, 320, 271, 411))
        self.graphicsView_5.setAutoFillBackground(True)
        self.graphicsView_5.setStyleSheet(u"background-color: rgb(225, 225, 225);")
        brush2 = QBrush(QColor(255, 124, 234, 255))
        brush2.setStyle(Qt.NoBrush)
        self.graphicsView_5.setBackgroundBrush(brush2)

        self.satelliteVisualization = QOpenGLWidget(self.centralwidget)
        self.satelliteVisualization.setObjectName(u"satelliteVisualization")
        self.satelliteVisualization.setGeometry(QRect(330, 530, 271, 200))
        self.Connection = QWidget(self.centralwidget)
        self.Connection.setObjectName(u"Connection")
        self.Connection.setGeometry(QRect(930, 320, 271, 51))
        font3 = QFont()
        font3.setPointSize(14)
        self.Connection.setFont(font3)
        self.Connection.setStyleSheet(u"background-color: rgb(211, 211, 211);")
        self.label_2 = QLabel(self.Connection)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 10, 261, 31))
        font4 = QFont()
        font4.setFamilies([u"Arial"])
        font4.setPointSize(16)
        self.label_2.setFont(font4)
        self.label_2.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.Connection_2 = QWidget(self.centralwidget)
        self.Connection_2.setObjectName(u"Connection_2")
        self.Connection_2.setGeometry(QRect(930, 10, 271, 51))
        self.Connection_2.setFont(font3)
        self.Connection_2.setStyleSheet(u"background-color: rgb(211, 211, 211);")
        self.label_10 = QLabel(self.Connection_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(10, 10, 231, 31))
        self.label_10.setFont(font4)
        self.label_10.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(950, 390, 231, 261))
        self.groupBox_3.setFont(font2)
        self.groupBox_3.setStyleSheet(u"background-color: rgb(112, 112, 112);")
        self.label_8 = QLabel(self.groupBox_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(20, 50, 121, 31))
        self.label_8.setFont(font1)
        self.label_9 = QLabel(self.groupBox_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 140, 161, 31))
        self.label_9.setFont(font1)

        self.lcdNumber_6 = QTextEdit(self.groupBox_3)
        self.lcdNumber_6.setObjectName(u"lcdNumber_6")
        self.lcdNumber_6.setGeometry(QRect(10, 80, 201, 41))

        self.lcdNumber_7 = QTextEdit(self.groupBox_3)
        self.lcdNumber_7.setObjectName(u"lcdNumber_7")
        self.lcdNumber_7.setGeometry(QRect(20, 180, 201, 41))

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(950, 670, 231, 41))
        self.pushButton_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
        "background-color: rgb(50, 107, 29);")
        self.orientation_visualizer_label = QLabel(self.centralwidget)
        self.orientation_visualizer_label.setObjectName(u"label_11")
        self.orientation_visualizer_label.setGeometry(QRect(330, 500, 191, 31))
        self.orientation_visualizer_label.setFont(font1)

        self.pfd = YawVisualizer(self.centralwidget) 
        self.pfd.zoom = 0.3
        self.pfd.setGeometry(QRect(330, 530, 270, 200))
        self.pfd.setMinimumSize(QSize(270, 200))
        self.pfd.show()

        # self.visualization = QHBoxLayout(self.centralwidget)

        self.temp_visualizer = QLabel(self.centralwidget)
        self.temp_visualizer.setObjectName(u"temp_visualizer")
        self.temp_visualizer.setGeometry(QRect(630, 500, 191, 31))
        self.temp_visualizer.setFont(font1)

        # temperature graph
        self.graphWidget = pg.PlotWidget(self.centralwidget)
        self.graphWidget.setGeometry(QRect(630,530,270,200))
        self.graphWidget.setMinimumSize(QSize(270, 200))
        # self.graphWidget.setMaximumSize(QSize(500, 16777215))

        self.graphWidget.setBackground('w')
        # self.graphWidget.plot(hour, temperature)   


        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(440, 150, 191, 31))
        self.label_13.setFont(font1)
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(950, 240, 231, 41))
        self.pushButton_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
        "background-color: rgb(182, 41, 16);")
        self.lcdVoltage = QLCDNumber(self.centralwidget)
        self.lcdVoltage.setObjectName(u"lcdNumber_9")
        self.lcdVoltage.setGeometry(QRect(950, 180, 191, 41))
        self.lcdVoltage.display(9)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(950, 80, 221, 51))
        self.progressBar.setValue(24)
        self.label_14 = QLabel(self.centralwidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(950, 150, 121, 31))
        self.label_14.setFont(font1)
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

        QMetaObject.connectSlotsByName(MainWindow)
    
    # setupUi
    

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Satellite overview", None))
        self.roll_label.setText(QCoreApplication.translate("MainWindow", u"Roll", None))
        self.pitch_label.setText(QCoreApplication.translate("MainWindow", u"Pitch", None))
        self.yaw_label.setText(QCoreApplication.translate("MainWindow", u"Yaw", None))
        self.orientation_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Orientation", None))
        self.parameter_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Other Parameters", None))
        self.temperature.setText(QCoreApplication.translate("MainWindow", u"Temperature", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Angular Velocity", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Connection Overview", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Battery", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Connection Parameters", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Baud Rate", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Port", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.orientation_visualizer_label.setText(QCoreApplication.translate("MainWindow", u"Orientation Visualizer", None))
        self.temp_visualizer.setText(QCoreApplication.translate("MainWindow", u"Temperature Visualizer", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"View from Camera", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Shut Down", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Voltage", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"V", None))
    
    def updateData(self, data):
        try:
            max_voltage = 14.4
            hour = []
            temperature = []

            topicName = "telemetryContinuous"
            topicStruc = data[topicName]
            topicData = data[topicName]["data"]

            if topicStruc["pairedData"]["temp"]:
                tempData = topicStruc["pairedData"]["temp"]
                print("tempData", tempData)
                hour = list(tempData.keys())
                temperature = list(tempData.values())
            
            # conversion of quaternion to roll, pitch and yaw
            q0 = topicData["q0"]/100
            q1 = topicData["q1"]/100
            q2 = topicData["q2"]/100
            q3 = topicData["q3"]/100
          
            roll = math.degrees(math.atan2(2 * (q0 * q1 + q2 * q3), 1 - 2 * (q1 * q1 + q2 * q2)))
            pitch = math.degrees(math.asin(2 * (q0 * q2 - q3 * q1)))                         
            yaw = math.degrees(math.atan2(2 * (q0 * q3 + q1 * q2), 1 - 2 * (q2 * q2 + q3 * q3)))

            # lcd data update
            self.lcdRoll.display(roll)
            self.lcdPitch.display(pitch)
            self.lcdYaw.display(yaw)
            self.lcdTemperature.display(topicData["temp"])
            self.lcdVoltage.display(topicData["U_bat"])

            value = (topicData["U_bat"]/max_voltage)
            print("battery:", value)

            # todo: update progress bar and its styling
            # self.progressBar.valueChanged(value)

            # graph data update
            print("tempData",hour, temperature)
            self.graphWidget.plot(hour, temperature) 

            # update yaw parameter
            print("roll, pitch, yaw",roll,pitch, yaw)
            self.pfd.heading = yaw
            self.pfd.update()

        except Exception as ex:
            print("exception summary update:", ex)

    # retranslateUi
    def close(self):
        pass


