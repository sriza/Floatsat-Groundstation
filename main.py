import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from Views.Summary import Ui_MainWindow
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QMainWindow()
    summary = Ui_MainWindow()
    summary.setupUi(w)
    w.show()
    app.exec()