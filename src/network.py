from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor
from threading import Thread

class Network(DatagramProtocol):  

    def __init__(self, callback):
        reactor.listenUDP(8000, self)
        thread = Thread(target=reactor.run, args=(False,))
        thread.daemon = True
        thread.start()
        self.callback = callback

    def startProtocol(self):
        self.transport.connect('192.168.43.202', 8000)
    
    def sendDatagram(self, datagram):
        self.transport.write(datagram.encode())

    def datagramReceived(self, datagram, host):
        self.callback(datagram.decode())
