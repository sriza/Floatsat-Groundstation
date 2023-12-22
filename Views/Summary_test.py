# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLCDNumber,
    QLabel, QLayout, QMainWindow, QMenu,
    QMenuBar, QProgressBar, QPushButton, QSizePolicy,
    QStatusBar, QTextEdit, QVBoxLayout, QWidget)
import PySide6.QtOpenGL as QtOpenGL

import pyqtgraph as pg
from Views.CustomWidgets.QPrimaryFlightDisplay import QPrimaryFlightDisplay


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1700, 1000)
        MainWindow.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setStyleSheet(u"background-color: rgb(9, 10, 17);")
        self.horizontalWidget = QWidget(self.centralwidget)
        self.horizontalWidget.setObjectName(u"horizontalWidget")
        self.horizontalWidget.setGeometry(QRect(49, 10, 1600, 950))
        sizePolicy.setHeightForWidth(self.horizontalWidget.sizePolicy().hasHeightForWidth())
        self.horizontalWidget.setSizePolicy(sizePolicy)
        self.horizontalWidget.setStyleSheet(u"background-color: rgb(9, 10, 17);")
        self.mainLayout = QHBoxLayout(self.horizontalWidget)
        self.mainLayout.setSpacing(25)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.mainLayout.setContentsMargins(20, 20, 20, 20)
        self.satelliteOrientationVisualization = QWidget(self.horizontalWidget)
        self.satelliteOrientationVisualization.setObjectName(u"satelliteOrientationVisualization")
        self.satelliteOrientationVisualization.setMinimumSize(QSize(300, 0))
        self.satelliteOrientationVisualization.setMaximumSize(QSize(350, 16777215))
        self.satelliteOrientationVisualization.setStyleSheet(u"background-color: rgb(26, 29, 56);")
        self.verticalLayout_4 = QVBoxLayout(self.satelliteOrientationVisualization)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(4, 4, 4, 4)
        self.satelliteVisualizerLabel = QLabel(self.satelliteOrientationVisualization)
        self.satelliteVisualizerLabel.setObjectName(u"satelliteVisualizerLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.satelliteVisualizerLabel.sizePolicy().hasHeightForWidth())
        self.satelliteVisualizerLabel.setSizePolicy(sizePolicy1)
        self.satelliteVisualizerLabel.setMinimumSize(QSize(0, 30))
        self.satelliteVisualizerLabel.setMaximumSize(QSize(16777215, 40))
        font = QFont()
        font.setPointSize(16)
        self.satelliteVisualizerLabel.setFont(font)

        self.verticalLayout_4.addWidget(self.satelliteVisualizerLabel)

        self.verticalWidget = QWidget(self.satelliteOrientationVisualization)
        self.verticalWidget.setObjectName(u"verticalWidget")
        self.verticalWidget.setMinimumSize(QSize(0, 500))
        self.verticalWidget.setMaximumSize(QSize(16777215, 1500))
        self.verticalLayout_2 = QVBoxLayout(self.verticalWidget)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(4, 4, 4, 4)
        self.line_2 = QFrame(self.verticalWidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setMaximumSize(QSize(16777215, 1))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_2)

        self.label_6 = QLabel(self.verticalWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(16777215, 20))
        self.label_6.setFont(font)

        self.verticalLayout_2.addWidget(self.label_6)

        self.label_2 = QLabel(self.verticalWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 20))
        self.label_2.setMaximumSize(QSize(16777215, 10))
        font1 = QFont()
        font1.setPointSize(12)
        self.label_2.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_2)

        self.lcdNumber_2 = QLCDNumber(self.verticalWidget)
        self.lcdNumber_2.setObjectName(u"lcdNumber_2")
        self.lcdNumber_2.setMinimumSize(QSize(0, 40))
        self.lcdNumber_2.setMaximumSize(QSize(16777215, 60))
        self.lcdNumber_2.setStyleSheet(u"background-color: rgb(45, 45, 45);\n"
"background-color: rgb(49, 50, 56);")

        self.verticalLayout_2.addWidget(self.lcdNumber_2)

        self.label = QLabel(self.verticalWidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 20))
        self.label.setMaximumSize(QSize(16777215, 10))
        self.label.setFont(font1)

        self.verticalLayout_2.addWidget(self.label)

        self.lcdNumber_3 = QLCDNumber(self.verticalWidget)
        self.lcdNumber_3.setObjectName(u"lcdNumber_3")
        self.lcdNumber_3.setMinimumSize(QSize(0, 40))
        self.lcdNumber_3.setMaximumSize(QSize(16777215, 60))
        self.lcdNumber_3.setStyleSheet(u"background-color: rgb(45, 45, 45);\n"
"background-color: rgb(49, 50, 56);")

        self.verticalLayout_2.addWidget(self.lcdNumber_3)

        self.label_3 = QLabel(self.verticalWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 20))
        self.label_3.setMaximumSize(QSize(16777215, 20))
        self.label_3.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_3)

        self.lcdNumber = QLCDNumber(self.verticalWidget)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setMinimumSize(QSize(0, 40))
        self.lcdNumber.setMaximumSize(QSize(16777215, 60))
        self.lcdNumber.setStyleSheet(u"background-color: rgb(45, 45, 45);\n"
"background-color: rgb(49, 50, 56);")

        self.verticalLayout_2.addWidget(self.lcdNumber)

        self.line = QFrame(self.verticalWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.label_7 = QLabel(self.verticalWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(16777215, 20))
        self.label_7.setFont(font)

        self.verticalLayout_2.addWidget(self.label_7)

        self.label_4 = QLabel(self.verticalWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 20))
        self.label_4.setMaximumSize(QSize(16777215, 20))
        self.label_4.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_4)

        self.lcdNumber_4 = QLCDNumber(self.verticalWidget)
        self.lcdNumber_4.setObjectName(u"lcdNumber_4")
        self.lcdNumber_4.setMinimumSize(QSize(0, 40))
        self.lcdNumber_4.setMaximumSize(QSize(16777215, 60))
        self.lcdNumber_4.setStyleSheet(u"background-color: rgb(45, 45, 45);\n"
"background-color: rgb(49, 50, 56);")

        self.verticalLayout_2.addWidget(self.lcdNumber_4)

        self.label_5 = QLabel(self.verticalWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 20))
        self.label_5.setMaximumSize(QSize(16777215, 20))
        self.label_5.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_5)

        self.lcdNumber_5 = QLCDNumber(self.verticalWidget)
        self.lcdNumber_5.setObjectName(u"lcdNumber_5")
        self.lcdNumber_5.setMinimumSize(QSize(0, 40))
        self.lcdNumber_5.setMaximumSize(QSize(16777215, 60))
        self.lcdNumber_5.setStyleSheet(u"background-color: rgb(45, 45, 45);\n"
"background-color: rgb(49, 50, 56);")

        self.verticalLayout_2.addWidget(self.lcdNumber_5)


        self.verticalLayout_4.addWidget(self.verticalWidget)


        self.mainLayout.addWidget(self.satelliteOrientationVisualization)

        self.visualizationWidget = QWidget(self.horizontalWidget)
        self.visualizationWidget.setObjectName(u"visualizationWidget")
        self.visualizationWidget.setStyleSheet(u"background-color: rgb(26, 29, 56);")
        # sizePolicy.setHeightForWidth(self.visualizationWidget.sizePolicy().hasHeightForWidth())
        # self.visualizationWidget.setSizePolicy(sizePolicy)
        # self.visualizationWidget.setMinimumSize(QSize(0, 0))
        # self.visualizationWidget.setMaximumSize(QSize(200, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.visualizationWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.vizWidget = QWidget(self.visualizationWidget)
        self.vizWidget.setObjectName(u"vizWidget")
        self.vizWidget.setMaximumSize(QSize(16777215, 800))
        self.horizontalLayout = QHBoxLayout(self.vizWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.verticalLayout_3.addWidget(self.vizWidget)


        self.mainLayout.addWidget(self.visualizationWidget)

        self.batteryVisualizationWidget = QWidget(self.horizontalWidget)
        self.batteryVisualizationWidget.setObjectName(u"batteryVisualizationWidget")
        sizePolicy.setHeightForWidth(self.batteryVisualizationWidget.sizePolicy().hasHeightForWidth())
        self.batteryVisualizationWidget.setSizePolicy(sizePolicy)
        self.batteryVisualizationWidget.setMinimumSize(QSize(300, 0))
        self.batteryVisualizationWidget.setMaximumSize(QSize(200, 16777215))
        self.batteryVisualizationWidget.setStyleSheet(u"background-color: rgb(26, 29, 56);")
        self.verticalLayout = QVBoxLayout(self.batteryVisualizationWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalWidget_3 = QWidget(self.batteryVisualizationWidget)
        self.verticalWidget_3.setObjectName(u"verticalWidget_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.verticalWidget_3.sizePolicy().hasHeightForWidth())
        self.verticalWidget_3.setSizePolicy(sizePolicy2)
        self.verticalWidget_3.setMinimumSize(QSize(0, 200))
        self.verticalWidget_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.verticalLayout_6 = QVBoxLayout(self.verticalWidget_3)
        self.verticalLayout_6.setSpacing(2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.line_5 = QFrame(self.verticalWidget_3)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setMaximumSize(QSize(16777215, 1))
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_6.addWidget(self.line_5)

        self.label_15 = QLabel(self.verticalWidget_3)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(0, 30))
        self.label_15.setMaximumSize(QSize(16777215, 15))
        self.label_15.setFont(font)

        self.verticalLayout_6.addWidget(self.label_15)

        self.progressBar = QProgressBar(self.verticalWidget_3)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMinimumSize(QSize(0, 60))
        self.progressBar.setValue(24)

        self.verticalLayout_6.addWidget(self.progressBar)

        self.label_16 = QLabel(self.verticalWidget_3)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(0, 20))
        self.label_16.setMaximumSize(QSize(16777215, 10))
        self.label_16.setFont(font1)

        self.verticalLayout_6.addWidget(self.label_16)

        self.lcdNumber_11 = QLCDNumber(self.verticalWidget_3)
        self.lcdNumber_11.setObjectName(u"lcdNumber_11")
        self.lcdNumber_11.setMinimumSize(QSize(0, 40))
        self.lcdNumber_11.setMaximumSize(QSize(16777215, 60))
        self.lcdNumber_11.setStyleSheet(u"background-color: rgb(45, 45, 45);\n"
"background-color: rgb(49, 50, 56);")

        self.verticalLayout_6.addWidget(self.lcdNumber_11)

        self.label_17 = QLabel(self.verticalWidget_3)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(0, 20))
        self.label_17.setMaximumSize(QSize(16777215, 10))
        self.label_17.setFont(font1)

        self.verticalLayout_6.addWidget(self.label_17)

        self.lcdNumber_12 = QLCDNumber(self.verticalWidget_3)
        self.lcdNumber_12.setObjectName(u"lcdNumber_12")
        self.lcdNumber_12.setMinimumSize(QSize(0, 40))
        self.lcdNumber_12.setMaximumSize(QSize(16777215, 60))
        self.lcdNumber_12.setStyleSheet(u"background-color: rgb(45, 45, 45);\n"
"background-color: rgb(49, 50, 56);")

        self.verticalLayout_6.addWidget(self.lcdNumber_12)

        self.label_18 = QLabel(self.verticalWidget_3)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(0, 20))
        self.label_18.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_6.addWidget(self.label_18)

        self.line_6 = QFrame(self.verticalWidget_3)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_6.addWidget(self.line_6)

        self.label_20 = QLabel(self.verticalWidget_3)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(0, 30))
        self.label_20.setMaximumSize(QSize(16777215, 15))
        self.label_20.setFont(font)

        self.verticalLayout_6.addWidget(self.label_20)

        self.label_21 = QLabel(self.verticalWidget_3)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(0, 20))
        self.label_21.setMaximumSize(QSize(16777215, 10))
        self.label_21.setFont(font1)

        self.verticalLayout_6.addWidget(self.label_21)

        self.textEdit = QTextEdit(self.verticalWidget_3)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(0, 40))
        self.textEdit.setMaximumSize(QSize(16777215, 60))
        font2 = QFont()
        font2.setPointSize(14)
        self.textEdit.setFont(font2)
        self.textEdit.setStyleSheet(u"background-color: rgb(40, 41, 47);")

        self.verticalLayout_6.addWidget(self.textEdit)

        self.label_19 = QLabel(self.verticalWidget_3)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(0, 20))
        self.label_19.setMaximumSize(QSize(16777215, 10))
        self.label_19.setFont(font1)

        self.verticalLayout_6.addWidget(self.label_19)

        self.lcdNumber_13 = QLCDNumber(self.verticalWidget_3)
        self.lcdNumber_13.setObjectName(u"lcdNumber_13")
        self.lcdNumber_13.setMinimumSize(QSize(0, 40))
        self.lcdNumber_13.setMaximumSize(QSize(16777215, 60))
        font3 = QFont()
        font3.setPointSize(10)
        self.lcdNumber_13.setFont(font3)
        self.lcdNumber_13.setStyleSheet(u"background-color: rgb(45, 45, 45);\n"
"background-color: rgb(49, 50, 56);")

        self.verticalLayout_6.addWidget(self.lcdNumber_13)

        self.pushButton = QPushButton(self.verticalWidget_3)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 40))
        self.pushButton.setMaximumSize(QSize(16777215, 60))

        self.verticalLayout_6.addWidget(self.pushButton)


        self.verticalLayout.addWidget(self.verticalWidget_3)


        self.mainLayout.addWidget(self.batteryVisualizationWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        # MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.satelliteVisualizerLabel.setText(QCoreApplication.translate("MainWindow", u"Satellite Orientation", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Orientation data", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Pitch", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Roll", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Yaw", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Other Parameters", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Angular Velocity", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Orientation", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Battery Parameters", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Voltage", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Charge", None))
        self.label_18.setText("")
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Connection Parameters", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Port", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Baud rate", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        # self.menuIMU.setTitle(QCoreApplication.translate("MainWindow", u"IMU", None))
    # retranslateUi

