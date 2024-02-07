import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtOpenGL import *
from PySide6.QtOpenGLWidgets import *
from math import cos, radians, tan, pi, sin

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
        self.mocksatAngle = 0
        self.floatsatAngle = 0
        # scene.setSceneRect(-300, -200, 600, 400)
        
        # self.painter.begin(self)

    def paintEvent(self,e):
        print("updating paint event")
        self.painter = QPainter(self)
        self.brush = QBrush()
        self.brush.setColor(QColor('black'))

        self.drawMockSat()
        self.drawFloatSat()

        
        self.painter.end()
    
    def drawMockSat(self):
        painter = self.painter
        painter.drawRect(150,150,75,10)
        painter.drawRect(150,150, -75,10)
        rect = QRect(150,100,100,100)
        center_rect = rect.center()
        print(center_rect.x, center_rect.y)

        trans = QTransform()
        trans.translate(199,149)
        trans.rotate(self.mocksatAngle)
        trans.translate(-199,-149)
        painter.setTransform(trans)
        painter.drawRect(150,100,100,100)
        painter.resetTransform()

    # def updatePainter(self):
    #     self.angle+=1
    #     if self.angle >= 360:
    #         self.angle = 0
    #     self.update()
        

    def drawFloatSat(self):
        painter = self.painter
        painter.setBrush(Qt.black)
        painter.setOpacity(12)

        floatrect = QRect()
        trans = QTransform()
        # trans.translate(125,100)
        trans.rotate(self.floatsatAngle)
        trans.translate(-125,-100)
        painter.setTransform(trans)
        painter.drawRect(350,100, 100,100)
        painter.resetTransform()

def updateSat():
    window.mocksatAngle +=5
    window.floatsatAngle +=15
    window.update()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RotatingCirclesAnimation()
    window.show()
    updatePaint = QTimer()

    updatePaint.setInterval(100)
    updatePaint.timeout.connect(updateSat)
    updatePaint.start()


    # window.update()
    sys.exit(app.exec())
