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
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtOpenGLWidgets import QOpenGLWidget
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGraphicsView,
    QGroupBox, QLabel, QMainWindow, QMenu,
    QMenuBar, QPlainTextEdit, QPushButton, QSizePolicy, QComboBox,
    QStatusBar, QWidget)
import json

class Telecommand_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1265, 802)
        self.parent = MainWindow
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(30, 10, 261, 441))
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet(u"background-color: rgb(225, 225, 225);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.groupBox = QGroupBox(self.frame)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 40, 231, 151))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.pushButton_7 = QPushButton(self.groupBox)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(10, 100, 201, 41))
        self.pushButton_7.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(50, 107, 29);")
        self.label_12 = QLabel(self.groupBox)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(10, 20, 121, 31))
        self.label_12.setFont(font)
        self.plainTextEdit_7 = QPlainTextEdit(self.groupBox)
        self.plainTextEdit_7.setObjectName(u"plainTextEdit_7")
        self.plainTextEdit_7.setGeometry(QRect(10, 50, 201, 41))
        self.groupBox_2 = QGroupBox(self.frame)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 200, 231, 231))
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet(u"color: rgb(9, 10, 17);")
        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 20, 121, 31))
        self.label_6.setFont(font)
        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 90, 161, 31))
        self.label_7.setFont(font)
        self.pushButton_6 = QPushButton(self.groupBox_2)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(10, 170, 201, 41))
        self.pushButton_6.setStyleSheet(u"color: rgb(255, 255, 255);\n"
        "background-color: rgb(50, 107, 29);")
        self.plainTextEdit_5 = QPlainTextEdit(self.groupBox_2)
        self.plainTextEdit_5.setObjectName(u"plainTextEdit_5")
        self.plainTextEdit_5.setGeometry(QRect(10, 120, 201, 41))
        self.plainTextEdit_6 = QPlainTextEdit(self.groupBox_2)
        self.plainTextEdit_6.setObjectName(u"plainTextEdit_6")
        self.plainTextEdit_6.setGeometry(QRect(10, 50, 201, 41))
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, 0, 261, 35))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(16)
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"color: rgb(0, 0, 0);\n"
        "background-color: rgb(211, 211, 211);")
        self.groupBox_2.raise_()
        self.groupBox.raise_()
        self.label_4.raise_()
        self.graphicsView_4 = QGraphicsView(self.centralwidget)
        self.graphicsView_4.setObjectName(u"graphicsView_4")
        self.graphicsView_4.setGeometry(QRect(940, 450, 271, 291))
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
        self.satelliteVisualization = QOpenGLWidget(self.centralwidget)
        self.satelliteVisualization.setObjectName(u"satelliteVisualization")
        self.satelliteVisualization.setGeometry(QRect(320, 10, 591, 441))
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
        self.label_10 = QLabel(self.Connection_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(10, 10, 231, 31))
        self.label_10.setFont(font1)
        self.label_10.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(330, 20, 191, 31))
        self.label_11.setFont(font)
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(960, 250, 231, 41))
        self.pushButton_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
        "background-color: rgb(182, 41, 16);")
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(960, 660, 231, 41))
        self.pushButton_4.setStyleSheet(u"color: rgb(255, 255, 255);\n"
        "background-color: rgb(50, 107, 29);")
        self.groupBox_4 = QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(960, 520, 231, 111))
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(1)
        self.groupBox_4.setFont(font3)
        self.groupBox_4.setStyleSheet(u"color: rgb(255, 255, 255);\n"
        "background-color: rgb(26, 29, 56);")
        self.checkBox = QCheckBox(self.groupBox_4)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(20, 30, 171, 16))
        font4 = QFont()
        font4.setPointSize(12)
        self.checkBox.setFont(font4)
        self.checkBox_3 = QCheckBox(self.groupBox_4)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setGeometry(QRect(20, 70, 171, 16))
        self.checkBox_3.setFont(font4)
        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(960, 340, 231, 41))
        self.pushButton_5.setStyleSheet(u"color: rgb(255, 255, 255);\n"
        "background-color: rgb(50, 107, 29);")
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(950, 310, 251, 16))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(960, 90, 201, 31))
        self.label_8.setFont(font1)
        self.label_8.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(960, 170, 201, 31))
        self.label_9.setFont(font1)
        self.label_9.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(960, 120, 231, 31))
        self.label_13.setFont(font)
        self.label_13.setStyleSheet(u"background-color: rgb(26, 29, 56); color: rgb(255, 255, 255);")
        self.label_14 = QLabel(self.centralwidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(960, 200, 231, 31))
        self.label_14.setFont(font)
        self.label_14.setStyleSheet(u"background-color: rgb(26, 29, 56); color: rgb(255, 255, 255);")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(20, 470, 881, 281))
        self.frame_2.setAutoFillBackground(False)
        self.frame_2.setStyleSheet(u"background-color: rgb(225, 225, 225);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.groupBox_7 = QGroupBox(self.frame_2)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setGeometry(QRect(20, 60, 811, 201))
        self.groupBox_7.setFont(font)
        self.groupBox_7.setStyleSheet(u"color: rgb(9, 10, 17);")
        self.x_label = QLabel(self.groupBox_7)
        self.x_label.setObjectName(u"label_19")
        self.x_label.setGeometry(QRect(30, 20, 121, 31))
        self.x_label.setFont(font)

        # send telecommand button
        self.telecommandButton = QPushButton(self.groupBox_7)
        self.telecommandButton.setObjectName(u"pushButton_11")
        self.telecommandButton.setGeometry(QRect(590, 150, 201, 41))
        self.telecommandButton.setStyleSheet(u"color: rgb(255, 255, 255);\n"
        "background-color: rgb(50, 107, 29);")
        self.telecommandButton.clicked.connect(self.mainTelecommand)
        
        self.y_label = QLabel(self.groupBox_7)
        self.y_label.setObjectName(u"label_20")
        self.y_label.setGeometry(QRect(290, 20, 121, 31))
        self.y_label.setFont(font)
        self.z_label = QLabel(self.groupBox_7)
        self.z_label.setObjectName(u"label_22")
        self.z_label.setGeometry(QRect(550, 20, 121, 31))
        self.z_label.setFont(font)
        self.label_23 = QLabel(self.groupBox_7)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(30, 100, 121, 31))
        self.label_23.setFont(font)

        # tuning parameters
        self.modeDropdown = QComboBox(self.groupBox_7)
        # self.plainTextEdit = QPlainTextEdit(self.groupBox_7)
        self.modeDropdown.setObjectName(u"plainTextEdit")
        self.modeDropdown.setGeometry(QRect(30, 133, 311, 51))
        self.modeDropdown.setPlaceholderText("Propertional")

        self.xTextEdit = QPlainTextEdit(self.groupBox_7)
        self.xTextEdit.setObjectName(u"x")
        self.xTextEdit.setGeometry(QRect(30, 50, 231, 41))
        self.xTextEdit.setPlaceholderText("Propertional")


        self.yTextEdit = QPlainTextEdit(self.groupBox_7)
        self.yTextEdit.setObjectName(u"y")
        self.yTextEdit.setGeometry(QRect(290, 50, 231, 41))
        self.yTextEdit.setPlaceholderText("Integrator")

        self.zTextEdit = QPlainTextEdit(self.groupBox_7)
        self.zTextEdit.setObjectName(u"z")
        self.zTextEdit.setGeometry(QRect(550, 50, 231, 41))
        self.zTextEdit.setPlaceholderText("Derivative")

        self.modeDropdown = QComboBox(self.groupBox_7)
        self.modes = {}
        self.addDropdownItems()
        # self.plainTextEdit = QPlainTextEdit(self.groupBox_7)
        self.modeDropdown.setObjectName(u"plainTextEdit")
        self.modeDropdown.setGeometry(QRect(30, 133, 311, 51))
        self.modeDropdown.setPlaceholderText("Select the mode")
        self.modeDropdown.currentTextChanged.connect(self.updateModeParameters)


        self.label_21 = QLabel(self.frame_2)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(0, 0, 881, 41))
        self.label_21.setFont(font1)
        self.label_21.setStyleSheet(u"color: rgb(0, 0, 0);\n"
        "background-color: rgb(211, 211, 211);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Motor Telecommand", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Set Motor Parameter", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Angular Velocity", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Satellite Telecommand", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Orientation", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Angular Velocity", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Set Satellite Parameters", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Basic Telecommands", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Satellite Status ", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Calibration", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Orientation Visualizer", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Shut Down", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Initiate Caliberation", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Sensor Calibration Status", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Magnetometer", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"Gyroscope", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Initiate Telecommand Mode", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Battery status :", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Mode :", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Nominal", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Docking", None))
        self.x_label.setText(QCoreApplication.translate("MainWindow", u"Propertional", None))
        self.telecommandButton.setText(QCoreApplication.translate("MainWindow", u"Send Telecommand", None))
        self.y_label.setText(QCoreApplication.translate("MainWindow", u"Integral", None))
        self.z_label.setText(QCoreApplication.translate("MainWindow", u"Derivative", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Telecommand mode", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Tuning Parameters", None))
    
    def addDropdownItems(self):
        f = open("Assets/telecommand_modes.json")
        json_array = json.load(f)

        for item in json_array:
            self.modeDropdown.addItem(item)
            self.modes[item] = {}
            self.modes[item]["id"] = json_array[item]["id"]
            self.modes[item]["data"] = json_array[item]["data"]
    
    def updateModeParameters(self):
        currentText= self.modeDropdown.currentText()
        print("mode has been updated to:", currentText)

        data = self.modes[currentText]["data"]
        types = {
            "x": {
                "input":self.xTextEdit,
                "label":self.x_label
                },
            "y": {
                "input":self.yTextEdit,
                "label":self.y_label
                },
            "z": {
                "input":self.zTextEdit,
                "label":self.z_label
                }
        }
        

        for type in types:
            if type in data:
                (types[type]["input"]).setPlaceholderText(data[type])
                (types[type]["input"]).show()
                (types[type]["label"]).show()
                continue

            (types[type]["input"]).hide()
            (types[type]["label"]).hide()

    def mainTelecommand(self):
        data = []
        currentText= self.modeDropdown.currentText()
        currentMode = self.modes[currentText]
        data.append(currentMode["id"])
        expectedData = currentMode["data"]

        types = {"x": self.xTextEdit,
                  "y": self.yTextEdit, 
                  "z": self.zTextEdit}
        
        for key in expectedData.keys():
            value = float(types[key].toPlainText())
            data.append(value)

        print("data",data)
        'e'
        self.parent.sendTelecommand(data)

        
    def updateData(self, data):
        try:
            topicName = "telemetryCalibIMU"
            topicData = data[topicName]["data"]

            topicName = "telemetryCalibIMU"
            

        except Exception as ex:
            print("exception imu update:", ex)
