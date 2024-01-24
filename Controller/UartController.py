import rodos

class UartController:

    UART_PORT = "COM3"
    BAUDRATE = 115200

    def __init__(self, uart_port = UART_PORT, baudrate = BAUDRATE):
        self.liUart = rodos.linkinterfaceUART(uart_port, baudrate)
        self.gateway = rodos.Gateway(self.liUart)
        self.initializeTopic()
        self.publisherTopic()
        self.subscriberTopic()
        # self.gateway = rodos.Gateway(self.liUart)


    def initializeTopic(self):
        self.imuTopic = rodos.Topic(40)
        self.imuTopic = rodos.Topic(40)
        self.telecommandTopic = rodos.Topic(50)
        self.telecommandEchoTopic = rodos.Topic(60)

    def publisherTopic(self):

        pass

    def subscriberTopic(self):
        pass


    def storeData():





