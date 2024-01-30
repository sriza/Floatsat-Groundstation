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
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QLabel,
    QMainWindow, QMenu, QMenuBar, QProgressBar,
    QPushButton, QRadioButton, QSizePolicy, QStatusBar,
    QWidget)
import math

class Docking_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        # MainWindow.resize(1265, 820)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(30, 10, 841, 471))
        self.frame.setAutoFillBackground(True)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(100, 120, 291, 51))
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(900, 300, 341, 171))
        self.pushButton = QPushButton(self.groupBox_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(30, 100, 291, 51))
        self.pushButton.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 2, 36);\n"
"background-color: rgb(184, 5, 14);")
        self.pushButton_3 = QPushButton(self.groupBox_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(30, 40, 291, 51))
        self.pushButton_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(15, 102, 28);")
        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(900, 20, 341, 261))
        self.radioButton = QRadioButton(self.groupBox_3)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(30, 90, 91, 22))
        self.radioButton_2 = QRadioButton(self.groupBox_3)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(30, 120, 141, 22))
        self.radioButton_3 = QRadioButton(self.groupBox_3)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setGeometry(QRect(30, 150, 141, 22))
        self.radioButton_4 = QRadioButton(self.groupBox_3)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setGeometry(QRect(30, 180, 141, 22))
        self.radioButton_5 = QRadioButton(self.groupBox_3)
        self.radioButton_5.setObjectName(u"radioButton_5")
        self.radioButton_5.setGeometry(QRect(30, 210, 141, 22))
        self.progressBar = QProgressBar(self.groupBox_3)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(30, 40, 291, 20))
        self.progressBar.setValue(24)
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

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Camera view of docking", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"IMU Command", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Cancel Docking Mission", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Initiate Docking", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Mission Profile", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"Initiated", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"Searching Debris", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"Debris located", None))
        self.radioButton_4.setText(QCoreApplication.translate("MainWindow", u"Docking initiated", None))
        self.radioButton_5.setText(QCoreApplication.translate("MainWindow", u"Docked", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Arm Position", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Rate of extension", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Arm Length", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Extended length", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Mockup Status", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Distance from floatsat", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Calculated Angular velocity", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Orientation", None))
    # retranslateUi
    
    def updateData(self, data):
        try:
            # hour = []
            # temperature = []

            topicName = "telemetryContinuous"
            # topicStruc = data[topicName]
            topicData = data[topicName]["data"]

            # if topicStruc["pairedData"]["temp"]:
            #     tempData = topicStruc["pairedData"]["temp"]
            #     print("tempData", tempData)
            #     hour = list(tempData.keys())
            #     temperature = list(tempData.values())
            
            # conversion of quaternion to roll, pitch and yaw
            q0 = topicData["q0"]/100
            q1 = topicData["q1"]/100
            q2 = topicData["q2"]/100
            q3 = topicData["q3"]/100

          
            # roll = math.degrees(math.atan2(2 * (q0 * q1 + q2 * q3), 1 - 2 * (q1 * q1 + q2 * q2)))%40
            # pitch = math.degrees(math.asin(2 * (q0 * q2 - q3 * q1)))%40                        
            # yaw = math.degrees(math.atan2(2 * (q0 * q3 + q1 * q2), 1 - 2 * (q2 * q2 + q3 * q3)))

            # # lcd data update
            # self.roll.display(roll)
            # self.pitch.display(pitch)
            # self.yaw.display(yaw)

            # # graph data update
            # # print("tempData",hour, temperature)
            # # self.graphWidget.plot(hour, temperature) 


            # # update yaw parameters
            # print("roll, pitch, yaw",roll,pitch, yaw)
            # self.yaw_viz.heading = yaw
            # self.yaw_viz.update()

            # #update roll and pitch parameters
            # self.roll_pitch_viz.roll = 40
            # self.roll_pitch_viz.pitch = 44
            # # self.roll_pitch_viz.yaw = yaw
            # self.roll_pitch_viz.update()

        except Exception as ex:
            print("exception imu update:", ex)

