from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor

class Network(DatagramProtocol):  

    def __init__(self, callback):
        # print('INIT')
        self.callback = callback

    def startProtocol(self):
        # print('START')
        self.transport.connect('127.0.0.1', 8000)
    
    def sendDatagram(self, datagram):
        # print('SEND')
        self.transport.write(datagram.encode())

    def datagramReceived(self, datagram, host):
        # print('RECEIVE')
        self.callback(datagram.decode())
