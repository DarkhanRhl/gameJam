from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor
from threading import Thread

class Network(DatagramProtocol):  

    def __init__(self, callback):
        # print('INIT')
        reactor.listenUDP(8000, self)
        thread = Thread(target=reactor.run, args=(False,))
        thread.daemon = True
        thread.start()
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
