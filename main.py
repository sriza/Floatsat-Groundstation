import sys
from PySide6.QtCore import (QRect, QCoreApplication)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenuBar, QMenu)
from PySide6.QtGui import (QAction)
from Views.Summary import Ui_MainWindow
# from Views.Summary_test import Ui_MainWindow
from Views.IMU import IMU_MainWindow
from Views.Telecommand import Telecommand_MainWindow
from Views.Docking import Docking_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "StarStation"
        self.menubarCollection()
        self.summary = Ui_MainWindow()
        self.imu = IMU_MainWindow()
        self.telecommand = Telecommand_MainWindow()
        self.docking = Docking_MainWindow()
        self.summary.setupUi(self)
    
    def menubarCollection(self):
        # set action to menubar buttons
        button_action = QAction(self)
        button_action.triggered.connect(self.show_new_window)
        button_action.setCheckable(True)

        button_action_summary = QAction(self)
        button_action_summary.triggered.connect(self.show_new_window_summary)
        button_action_summary.setCheckable(True)

        button_action_docking = QAction(self)
        button_action_docking.triggered.connect(self.show_new_window_docking)
        button_action_docking.setCheckable(True)

        button_action_telecommand = QAction(self)
        button_action_telecommand.triggered.connect(self.show_new_window_telecommand)
        button_action_telecommand.setCheckable(True)

        # add menu to menubar
        self.menubar = QMenuBar(self)
        self.menubar.addAction(button_action)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 2560, 40))

        self.menuSummary = QMenu(self.menubar)
        self.menuSummary.setObjectName(u"menuSummary")

        self.menuIMU = QMenu(self.menubar)
        self.menuIMU.setObjectName(u"menuIMU")

        self.menuDocking = QMenu(self.menubar)
        self.menuDocking.setObjectName(u"menuDocking")

        self.menuTelecommand = QMenu(self.menubar)
        self.menuTelecommand.setObjectName(u"menuTelecommand")

        # self.menuTesting = QMenu(self.menubar)
        # self.menuTesting.setObjectName(u"menuTelecommand")

        self.setMenuBar(self.menubar)

        self.menubar.addActions([
            self.menuSummary.menuAction(),
            self.menuIMU.menuAction(),
            self.menuDocking.menuAction(),
            self.menuTelecommand.menuAction(),
            # self.menuTesting.menuAction()
        ])

        self.menuSummary.addAction(button_action_summary)
        self.menuIMU.addAction(button_action)
        self.menuDocking.addAction(button_action_docking)
        self.menuTelecommand.addAction(button_action_telecommand)
        # self.menuTesting.addAction(button_action)

        self.menuSummary.setTitle(QCoreApplication.translate("MainWindow", u"Summary", None))
        self.menuIMU.setTitle(QCoreApplication.translate("MainWindow", u"IMU", None))
        self.menuDocking.setTitle(QCoreApplication.translate("MainWindow", u"Docking", None))
        self.menuTelecommand.setTitle(QCoreApplication.translate("MainWindow", u"TeleCommand", None))
        # self.menuTesting.setTitle(QCoreApplication.translate("MainWindow", u"Testing", None))
    
    def show_new_window_summary(self):
        print("clicked")
        self.summary.setupUi(self)

    def show_new_window(self):
        print("clicked")
        self.imu.setupUi(self)
    
    def show_new_window_docking(self):
        print("clicked docking")
        self.docking.setupUi(self)
    
    def show_new_window_telecommand(self):
        print("clicked telecommand")
        self.telecommand.setupUi(self)
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec()