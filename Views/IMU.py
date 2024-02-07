# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'imu.ui'
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
from PySide6.Qt3DRender import Qt3DRender
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QLCDNumber,
    QLabel, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTextEdit, QComboBox,
    QWidget)
from Views.CustomWidgets.QPrimaryFlightDisplay import QPrimaryFlightDisplay
from Views.CustomWidgets.YawVisualizer import YawVisualizer
import math
import json
import pyqtgraph as pg

class IMUSignal(QObject):
    value = Signal()

class IMU_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        # MainWindow.resize(1700, 1000)
        self.value= IMUSignal()
        self.data = {}
        self.parent = MainWindow
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 10, 841, 581))
        self.frame.setAutoFillBackground(True)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.textEdit = QTextEdit(self.frame)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(0, 0, 841, 51))
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 211, 31))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(20)
        self.label.setFont(font)
        self.groupBox = QGroupBox(self.frame)
        self.currentCommand = ""

        # orientation raw values
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(30, 80, 771, 321))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(14)
        self.groupBox.setFont(font1)
        self.x_label = QLabel(self.groupBox)
        self.x_label.setObjectName(u"label_3")
        self.x_label.setGeometry(QRect(190, 30, 21, 31))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(12)
        self.x_label.setFont(font2)

        self.gyroscope_x = QLCDNumber(self.groupBox)
        self.gyroscope_x.setObjectName(u"lcdNumber")
        self.gyroscope_x.setGeometry(QRect(140, 70, 201, 41))
        self.gyroscope_x.display(1) 

        self.gyroscope_y = QLCDNumber(self.groupBox)
        self.gyroscope_y.setObjectName(u"lcdNumber_4")
        self.gyroscope_y.setGeometry(QRect(350, 70, 201, 41))
        self.gyroscope_y.display(2)

        self.gyroscope_z = QLCDNumber(self.groupBox)
        self.gyroscope_z.setObjectName(u"lcdNumber_5")
        self.gyroscope_z.setGeometry(QRect(560, 70, 201, 41))
        self.gyroscope_z.display(3)

        self.y_label = QLabel(self.groupBox)
        self.y_label.setObjectName(u"label_6")
        self.y_label.setGeometry(QRect(420, 30, 21, 31))
        self.y_label.setFont(font2)

        self.z_label = QLabel(self.groupBox)
        self.z_label.setObjectName(u"label_7")
        self.z_label.setGeometry(QRect(640, 30, 21, 31))
        self.z_label.setFont(font2)

        self.accelerometer_x = QLCDNumber(self.groupBox)
        self.accelerometer_x.setObjectName(u"lcdNumber_2")
        self.accelerometer_x.setGeometry(QRect(140, 150, 201, 41))
        self.accelerometer_x.display(4)

        self.accelerometer_y = QLCDNumber(self.groupBox)
        self.accelerometer_y.setObjectName(u"lcdNumber_10")
        self.accelerometer_y.setGeometry(QRect(560, 240, 201, 41))
        self.accelerometer_y.display(5)

        self.accelerometer_z = QLCDNumber(self.groupBox)
        self.accelerometer_z.setObjectName(u"lcdNumber_8")
        self.accelerometer_z.setGeometry(QRect(560, 150, 201, 41))
        self.accelerometer_z.display(6)


        self.magnetometer_x = QLCDNumber(self.groupBox)
        self.magnetometer_x.setObjectName(u"lcdNumber_3")
        self.magnetometer_x.setGeometry(QRect(140, 240, 201, 41))
        self.magnetometer_x.display(7)

        self.magnetometer_y = QLCDNumber(self.groupBox)
        self.magnetometer_y.setObjectName(u"lcdNumber_12")
        self.magnetometer_y.setGeometry(QRect(350, 240, 201, 41))
        self.magnetometer_y.display(8)

        self.magnetometer_z = QLCDNumber(self.groupBox)
        self.magnetometer_z.setObjectName(u"lcdNumber_11")
        self.magnetometer_z.setGeometry(QRect(350, 150, 201, 41))
        self.magnetometer_z.display(9)

        self.accelerometer_label = QLabel(self.groupBox)
        self.accelerometer_label.setObjectName(u"label_4")
        self.accelerometer_label.setGeometry(QRect(10, 150, 121, 31))
        self.accelerometer_label.setFont(font2)
        self.gyroscope_label = QLabel(self.groupBox)
        self.gyroscope_label.setObjectName(u"label_13")
        self.gyroscope_label.setGeometry(QRect(10, 70, 121, 31))
        self.gyroscope_label.setFont(font2)
        self.magnetometer_label = QLabel(self.groupBox)
        self.magnetometer_label.setObjectName(u"label_5")
        self.magnetometer_label.setGeometry(QRect(10, 240, 121, 31))
        self.magnetometer_label.setFont(font2)
        self.groupBox_3 = QGroupBox(self.frame)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(30, 420, 771, 141))
        self.groupBox_3.setFont(font1)
        self.roll_label = QLabel(self.groupBox_3)
        self.roll_label.setObjectName(u"label_8")
        self.roll_label.setGeometry(QRect(20, 40, 61, 31))
        self.roll_label.setFont(font2)

        self.roll = QLCDNumber(self.groupBox_3)
        self.roll.setObjectName(u"roll")
        self.roll.setGeometry(QRect(10, 70, 201, 41))

        self.pitch = QLCDNumber(self.groupBox_3)
        self.pitch.setObjectName(u"pitch")
        self.pitch.setGeometry(QRect(270, 70, 201, 41))
    
        self.yaw = QLCDNumber(self.groupBox_3)
        self.yaw.setObjectName(u"yaw")
        self.yaw.setGeometry(QRect(510, 70, 201, 41))


        self.pitch_label = QLabel(self.groupBox_3)
        self.pitch_label.setObjectName(u"label_9")
        self.pitch_label.setGeometry(QRect(280, 40, 61, 31))
        self.pitch_label.setFont(font2)
        self.yaw_label = QLabel(self.groupBox_3)
        self.yaw_label.setObjectName(u"label_12")
        self.yaw_label.setGeometry(QRect(510, 40, 61, 31))
        self.yaw_label.setFont(font2)
        self.groupBox.raise_()
        self.textEdit.raise_()
        self.label.raise_()
        self.groupBox_3.raise_()

        self.tilt_viz = QLabel(self.centralwidget)
        self.tilt_viz.setObjectName(u"label_11")
        self.tilt_viz.setGeometry(QRect(890, 10, 191, 31))
        self.tilt_viz.setFont(font2)

        # telecommand for Imu
        self.imu_command_group = QGroupBox(self.centralwidget)
        self.imu_command_group.setObjectName(u"groupBox_2")
        self.imu_command_group.setGeometry(QRect(20, 610, 841, 121))
        
        self.command_type_label = QLabel(self.imu_command_group)
        self.command_type_label.setObjectName(u"label_10")
        self.command_type_label.setGeometry(QRect(20, 30, 101, 31))
        self.command_type_label.setFont(font2)

        self.command_type_dropdown = QComboBox(self.imu_command_group)
        self.command_type_dropdown.setObjectName(u"command_type_dropdown")
        self.command_type_dropdown.setGeometry(QRect(20, 60, 201, 41))
        self.modes = {}
        self.addDropdownItems()
        self.command_type_dropdown.currentTextChanged.connect(self.updateCommandInputField)

        self.command_data_label = QLabel(self.imu_command_group)
        self.command_data_label.setObjectName(u"label_14")
        self.command_data_label.setGeometry(QRect(260, 30, 131, 31))
        self.command_data_label.setFont(font2)
        self.updateCommandInputField()

        self.command_data = QTextEdit(self.imu_command_group)
        self.command_data.setObjectName(u"command_data")
        self.command_data.setGeometry(QRect(260, 60, 201, 41))

        # error message label for telecommand input
        self.command_error_label = QLabel(self.imu_command_group)
        self.command_error_label.setObjectName(u"label_command_error")
        self.command_error_label.setGeometry(QRect(260, 90, 201, 41))
        self.command_error_label.setStyleSheet(f'color:red')

        self.pushButton = QPushButton(self.imu_command_group)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(530, 50, 291, 51))
        self.pushButton.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(15, 102, 28);")
        self.pushButton.clicked.connect(self.mainTelecommand)
        # end telecommand for IMU
        
        # visualizer section

        self.dynamicGraph = pg.PlotWidget(self.centralwidget) 
        # self.dynamicGraph.setObjectName(u"dynamicGraph")
        self.dynamicGraph.setGeometry(QRect(890, 520, 341, 201))
        self.dynamicGraph.setMinimumSize(QSize(270, 200))
        self.dynamicGraph.show()

        self.dynamicData = {"yaw":{}, "velocity":{}}

        self.yaw_viz_label = QLabel(self.centralwidget)
        self.yaw_viz_label.setObjectName(u"label_15")
        self.yaw_viz_label.setGeometry(QRect(890, 250, 341, 31))
        self.yaw_viz_label.setFont(font2)

        self.roll_pitch_viz = QPrimaryFlightDisplay(self.centralwidget) 
        self.roll_pitch_viz.zoom = 0.3
        self.roll_pitch_viz.setGeometry(QRect(890, 40, 341, 201))
        # self.roll_pitch_viz.setGeometry(QRect(890, 520, 341, 201))
        self.roll_pitch_viz.setMinimumSize(QSize(270, 200))
        self.roll_pitch_viz.show()

        self.yaw_viz = YawVisualizer(self.centralwidget) 
        self.yaw_viz.zoom = 0.3
        self.yaw_viz.setGeometry(QRect(890, 280, 341, 201))
        self.yaw_viz.setMinimumSize(QSize(270, 200))
        self.yaw_viz.show()

        self.dynamic_graph_label = QLabel(self.centralwidget)
        self.dynamic_graph_label.setObjectName(u"dynamic_graph_label")
        self.dynamic_graph_label.setGeometry(QRect(890, 490, 191, 31))
        self.dynamic_graph_label.setFont(font2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        self.value.value.connect(self.updateData)

        QMetaObject.connectSlotsByName(MainWindow)
    
    # Just label for everything, can even translate it if necessary    
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"IMU Reading", None))

        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Raw Values", None))
        self.x_label.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.y_label.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.z_label.setText(QCoreApplication.translate("MainWindow", u"Z", None))
        self.accelerometer_label.setText(QCoreApplication.translate("MainWindow", u"Accelerometer", None))
        self.gyroscope_label.setText(QCoreApplication.translate("MainWindow", u"Gyroscope", None))
        self.magnetometer_label.setText(QCoreApplication.translate("MainWindow", u"Magnetometer", None))

        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Orientation", None))
        self.roll_label.setText(QCoreApplication.translate("MainWindow", u"Roll", None))
        self.pitch_label.setText(QCoreApplication.translate("MainWindow", u"Pitch", None))
        self.yaw_label.setText(QCoreApplication.translate("MainWindow", u"Yaw", None))

        self.tilt_viz.setText(QCoreApplication.translate("MainWindow", u"Tilt Visualizer", None))
        self.imu_command_group.setTitle(QCoreApplication.translate("MainWindow", u"Telecommands", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Command", None))
        self.command_type_label.setText(QCoreApplication.translate("MainWindow", u"Orientation", None))
        self.yaw_viz_label.setText(QCoreApplication.translate("MainWindow", u"Yaw Visualizer", None))
        self.dynamic_graph_label.setText(QCoreApplication.translate("MainWindow", u"Speed /  Orientation", None))

    # update command label based on command type
    def updateCommandInputField(self):
        currentText= self.command_type_dropdown.currentText()
        self.command_data_label.setText(self.modes[currentText]["data"]["x"])


    # prepare command dropdowns
    def addDropdownItems(self):
        f = open("Assets/telecommand_modes.json")
        json_array = json.load(f)

        for item in json_array:
            if "type" in json_array[item] and json_array[item]["type"] == "basic":
                self.command_type_dropdown.addItem(item)
                self.modes[item] = {}
                self.modes[item]["id"] = json_array[item]["id"]
                self.modes[item]["data"] = json_array[item]["data"]
    
    # prepare data for imu telecommand
    def mainTelecommand(self):
        try:
            self.command_error_label.setText("")
            data = []
            currentText= self.command_type_dropdown.currentText()
            currentMode = self.modes[currentText]

            if currentMode !="":
                data.append(currentMode["id"])
            # expectedData = currentMode["data"]
                data.append(float(self.command_data.toPlainText()))
                self.parent.sendTelecommand(data)
                self.currentCommand = currentText
            # self.command_error_label.setText("Please enter value to send telecommand")
        except Exception as ex:
                self.command_error_label.setText("The entered data must be numeric")

    # 
    def updateTrigger(self,data):
        try:
            # self.value+=1
            self.data = data
            self.value.value.emit()
        except Exception as ex:
            print("imu update trigger:", ex)

    @Slot()
    def updateData(self):  
        try:
            data= self.data

            topicName = "telemetryContinuous"
            topicStruc = data[topicName]
            topicData = data[topicName]["data"]
            
            # conversion of quaternion to roll, pitch and yaw
            q0 = topicData["q0"]
            q1 = topicData["q1"]
            q2 = topicData["q2"]
            q3 = topicData["q3"]
            timestamp = topicData["time"]

          
            roll = math.atan2(2 * (q0 * q1 + q2 * q3), 1 - 2 * (q1 * q1 + q2 * q2))
            pitch = math.asin(2 * (q0 * q2 - q3 * q1))                     
            yaw = math.degrees(math.atan2(2 * (q0 * q3 + q1 * q2), 1 - 2 * (q2 * q2 + q3 * q3)))

            # lcd data update
            self.roll.display(roll)
            self.pitch.display(pitch)
            self.yaw.display(yaw)

            self.dynamicData["yaw"][timestamp] = yaw

            self.gyroscope_x.display(topicData["wx"])
            self.gyroscope_y.display(topicData["wy"])
            self.gyroscope_z.display(topicData["wz"])
            self.accelerometer_x.display(topicData["ax"])
            self.accelerometer_y.display(topicData["ay"])
            self.accelerometer_z.display(topicData["az"])
            self.magnetometer_x.display(topicData["mx"])
            self.magnetometer_y.display(topicData["my"])
            self.magnetometer_z.display(topicData["mz"])

            # update yaw parameters
            self.yaw_viz.heading = yaw
            self.yaw_viz.update()

            tempData = topicStruc["pairedData"]["speed"]

            if self.currentCommand == "SetControlDesired_pos" :
                print("yaw data")
                tempData = self.dynamicData["yaw"]
                
            x = list(tempData.keys())
            y = list(tempData.values())

            self.dynamicGraph.clear()

            self.dynamicGraph.plot(x, y) 

            # todo: update roll and pitch parameters, issue with repainting
            self.roll_pitch_viz.roll = roll
            self.roll_pitch_viz.pitch = pitch
            self.roll_pitch_viz.update()
            self.dynamicGraph.roll = roll
            self.dynamicGraph.pitch = pitch
            self.dynamicGraph.update()

        except Exception as ex:
            print("exception imu update:", ex)
