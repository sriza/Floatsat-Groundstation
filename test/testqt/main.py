from PySide6.QtWidgets import QApplication, QWidget, QPushButton

import sys
import rodos
import struct

app = QApplication(sys.argv)

window = QWidget()
PORT = 65435


window.setWindowTitle("Python app!")

button = QPushButton()
button.setText("Press Me")

myTopic1 = rodos.Topic(1234)
myTopic2 = rodos.Topic(1001)
cnt = 1

sendMe = struct.pack("20sIddd", b"HALLO", cnt, 65, 65, 65)
print(struct)
print(myTopic1)
myTopic1.publish(sendMe)


# requires udp port as parameter to initialize the udp link interface
linkIF = rodos.LinkinterfaceUDP(PORT)
# print("the link interface is:")

# communication occurs through gateway for link interface
# gateway = rodos.Gateway(linkIF)
# print(gateway)


# creating network message for communication
# message = rodos.NetworkMessage()

# gateway.sendNetworkMessage(message)


# window.setCentralWidget(button)
window.show()

app.exec()