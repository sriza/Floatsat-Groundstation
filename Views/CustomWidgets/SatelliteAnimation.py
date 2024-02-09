import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtOpenGL import *
from PySide6.QtOpenGLWidgets import *
from math import cos, radians, tan, pi, sin

class SatelliteAnimation(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setGeometry(100, 100, 600, 400)

        # mocksatData
        self.mocksatVelocity = 0
        self.mocksatAngle = 0
        self.mocksatDistance = 0

        # floatsat data
        self.floatsatAngle = 0
        self.armTranslate = 0
        self.armExtension = 0

        # scaling factor for animation, based on actual satellite arm width
        self.satArmLength = 100 #10 cm = 100 mm , this is only the length of extension that can be made
        self.armWidth = 140 # this is length of full arm
        self.scalingFactor = (self.armWidth/2)/(self.satArmLength)

        # floatsat pos x, y
        self.pos_x = 350
        self.pos_y = 150

        # satellite height and width
        self.sat_width = 100
        self.sat_height = 100

        # docking hand width and height
        self.hand_width = 10
        self.hand_height = 30

        # setting satellite animation background white
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.white)        
        self.setPalette(p)
        self.setAutoFillBackground(True)
        

    def paintEvent(self,e):
        print("updating paint event")
        self.painter = QPainter(self)
        self.brush = QBrush()
        self.brush.setColor(QColor('black'))

        if self.mocksatDistance:
            self.drawMockSat()

        self.drawFloatSat()
        self.painter.end()
    
    def drawFloatSat(self):
      # floatsat pos x, y
        pos_x = self.pos_x
        pos_y = self.pos_y

        # satellite height and width
        sat_width = self.sat_width 
        sat_height = self.sat_height

        painter = self.painter
        trans = QTransform()
        trans.translate(pos_x+sat_height/2,pos_y+sat_width/2)
        trans.rotate(self.floatsatAngle)
        trans.translate(-(pos_x+sat_height/2),-(pos_y+sat_width/2))
        painter.setTransform(trans)
        painter.setBrush(Qt.black)
        painter.setOpacity(.20)
        
        # arms
        arm_width = 140
        arm_height = 10

        #hand
        hand_width = self.hand_width
        hand_height = self.hand_height

        # scale translation of arm in real sat to animation 
        print("arm Translate:",self.armTranslate)
        self.armTranslate *=self.scalingFactor
        print("arm Translate:",self.armTranslate)
        print("-----------------------------------------------------")

        # if translation is greater or equal to armtranslate, reset translation to arm width
        # limiting condition
        # some snapping motion seen because of this.. need to test in real life
        if arm_width/2 < self.armTranslate:
            print("arm_width:" , arm_width/2)
            self.armTranslate = arm_width/2

        # self.prevArmTranslate = self.armTranslate

        arm1_x = (pos_x+23)+self.armTranslate-arm_width/2
        arm1_y = pos_y+50
        arm1_handx = arm1_x+arm_width
        arm1_handy = arm1_y-10

        arm2_x = (pos_x+23)-self.armTranslate+arm_width/2
        arm2_y = pos_y+50
        arm2_handx = arm2_x-arm_width-10
        arm2_handy = arm2_y-10
      
        painter.drawRect(arm1_x,arm1_y, arm_width,arm_height)
        painter.drawRect(arm1_handx,arm1_handy, hand_width, hand_height)

        painter.drawRect(arm2_x,arm2_y, -arm_width,arm_height)
        painter.drawRect(arm2_handx,arm2_handy, hand_width, hand_height)

        # floatsat
        rect = QRect(pos_x,pos_y,sat_width,sat_height)
        path = QPainterPath()
        radius = 90
        path.moveTo(rect.topLeft())
        path.arcTo(rect.left()-radius/2, rect.top(), radius, radius+20, 90, radius*2)
        path.arcTo(rect.left(), rect.top(), radius, radius+20, -90, radius*2)
        path.closeSubpath()
        painter.drawPath(path)

        painter.resetTransform()

    # draw mocksat
    def drawMockSat(self):
        # self.mocksatAngle = self.mocksatVeloc
        self.mocksatAngle = self.mocksatAngle*360/3.14
        sat_width = self.sat_width
        sat_height = self.sat_height
        armFactor = self.hand_width*2
        pos_x = self.pos_x - self.mocksatDistance* self.scalingFactor- armFactor- sat_width
        pos_y = self.pos_y

        painter = self.painter
        trans = QTransform()
        trans.translate(pos_x+sat_height/2,pos_y+sat_width/2)
        print("mocksatangle:", self.mocksatAngle)
        trans.rotate(self.mocksatAngle)
        trans.translate(-(pos_x+sat_height/2),-(pos_y+sat_width/2))
        painter.setTransform(trans)

        painter.setBrush(Qt.black)
        painter.setOpacity(.20)

        # mocksat
        trans = QTransform()
        rect = QRect(pos_x,pos_y,sat_width,sat_height)
        path = QPainterPath()
        radius = 90
        path.moveTo(rect.topLeft())
        path.arcTo(rect.left()-radius/2, rect.top(), radius, radius+20, 90, radius*2)
        path.arcTo(rect.left(), rect.top(), radius, radius+20, -90, radius*2)
        path.closeSubpath()

        # docking port
        docking_port_x = pos_x-60
        docking_port_y = pos_y+43

        arm_width = self.hand_width
        arm_height = self.hand_height
      
        painter.drawRect(docking_port_x,docking_port_y, arm_width,arm_height)
        # painter.drawRect(docking_port_handx,docking_port_handy, 10, 30)

        painter.drawPath(path)
        painter.resetTransform()

# def updateSat():
    # data regarding docking

    # window.mocksatAngle +=0.5
    # window.floatsatAngle +=0.15
    # window.armTranslate+=.1
    # window.update()

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = RotatingCirclesAnimation()
#     window.show()
#     updatePaint = QTimer()

#     updatePaint.setInterval(100)
#     updatePaint.timeout.connect(updateSat)
#     updatePaint.start()


#     # window.update()
#     sys.exit(app.exec())
