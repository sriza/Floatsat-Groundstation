import sys
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtGui import QPainter, QColor
from PySide6.QtCore import Qt, QTimer


class RotatingCircle(QWidget):
    def __init__(self):
        super().__init__()

        self.angle = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateAnimation)
        self.timer.start(50)  # Adjust the timer interval for speed

        self.setWindowTitle('Rotating Circle')
        self.setGeometry(100, 100, 400, 400)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(Qt.blue)

        width = self.width()
        height = self.height()
        size = min(width, height) * 0.8
        x = (width - size) / 2
        y = (height - size) / 2

        painter.translate(width / 2, height / 2)
        painter.rotate(self.angle)
        # painter.translate(-width / 2, -height / 2)
        painter.drawRect(x, y, size/2, size/2)

    def updateAnimation(self):
        self.angle += 1
        if self.angle >= 360:
            self.angle = 0
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RotatingCircle()
    window.show()
    sys.exit(app.exec_())