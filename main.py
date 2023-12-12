import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtUiTools import QUiLoader

loader = QUiLoader()

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        btn = QPushButton("Launch dialog")
        btn.pressed.connect(self.launch_dialog)

        self.setCentralWidget(btn)

    def launch_dialog(self):
        
        dialog = loader.load("./summary.ui", None)
        result = dialog.exec()
        result = 1
        if result:
            print("Success!")
        else:
            print("Cancelled.")
            

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()