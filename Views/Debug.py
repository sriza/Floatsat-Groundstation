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

class Debug_MainWindow(object):
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
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
    # retranslateUi
        
    def createDebugList(self, data):
        max_height = 1200
        max_width = 800
        # keep track of the length of table
        segment_width = max_width/5-20
        data_height = 15
        i = 0

        for topic in data:
            topicName = topic
            topicData = data[topicName]["data"]
            topicLeft = 10+ segment_width*i
            topicTop = 20
            j =0 
            #create topic header

            for key in data.keys():
                self.pitch_label = QLabel(self.frame)
                self.pitch_label.setObjectName(u"label_4")
                self.pitch_label.setGeometry(QRect(topicLeft, topicTop, 50, 20))
                # self.pitch_label.setFont(font1)
                # create data key label
                # create data value label
                print(key, topicData[key])
        # keep track of both the top and left value
        # update the top and left on each data addition
        # restart from last value if the (count of terms* height) is smaller than remaining height

        self.label = QLabel()
    
    def updateTrigger(self):
        pass
        
    
    def updateData(self, data):
        try:
            print("update data")

        except Exception as ex:
            print("exception docking update:", ex)

