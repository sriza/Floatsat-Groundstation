import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtOpenGL import *
from PySide6.QtOpenGLWidgets import *
# import sys
# from PySide6.QtWidgets import QApplication, QGraphicsScene, QGraphicsView, QGraphicsEllipseItem
# from PySide6.QtCore import Qt, QRectF, QPointF, QPropertyAnimation

# class CircleItem(QGraphicsEllipseItem):
#     def __init__(self, radius, color, parent=None):
#         super().__init__(parent)
#         self.setRect(-radius, -radius, 2 * radius, 2 * radius)
#         self.setBrush(color)

#         self.animation = QPropertyAnimation(self, b'rotation')
        # self.animation.setDuration(2000)
        # self.animation.setStartValue(0)
        # self.animation.setEndValue(360)
        # self.animation.setLoopCount(-1)

class RotatingCirclesAnimation(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setGeometry(100, 100, 600, 400)
        # scene.setSceneRect(-300, -200, 600, 400)
        
        # self.painter.begin(self)

    def paintEvent(self,e):
        print("updating paint event")
        self.painter = QPainter(self)
        self.brush = QBrush()
        self.brush.setColor(QColor('black'))
        # self.brush.setTextureImage()
        # rect = QRect(0, 0, painter.device().width(), painter.device().height())
        # painter.fillRect(rect, brush)
        # painter = QPainter(self)

        self.drawMockSat()
        self.drawFloatSat()

        
        self.painter.end()
    
    def drawMockSat(self):
        painter = self.painter
        # painter.setBrush(Qt.black)
        # QIma
        # self.brush.se
        # painter.drawImage(150,150, QImage("../../Assets/mocksat.jpeg"),5,5,-5,-5, QImage::Format_Grayscale8)
        # painter.setBackground(QBrush.setTextureImage(QImage("../../Assets/mocksat.jpeg")))
        # painter.drawRect(150,150,75,10)
        painter.drawRect(150,150,75,10)
        painter.drawRect(150,150, -75,10)

        painter.setBrush(Qt.blue)
        # polygon = QPolygon([QPoint(10,20), QPoint(20,20), QPoint(40,20), QPoint(10,30), QPoint(10,20)])
        # polygon.
        # painter.drawEllipse(150,100, 100,100)
        # painter.drawPolygon(polygon, Qt.OddEvenFill)
        painter.drawRect(150,100,100,100)

    def drawFloatSat(self):
        painter = self.painter
        painter.setBrush(Qt.black)
        painter.setOpacity(12)
        painter.drawEllipse(350,100, 100,100)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RotatingCirclesAnimation()
    window.show()
    updatePaint = QTimer()

    updatePaint.setInterval()


    window.update()
    sys.exit(app.exec())
