import socket

class connection:
    isConnected = False
    ip = ""
    port = -1
    service = None
    def __init__(self,ip,port):
        self.ip = ip
        self.port = 0
        self.service = socket.socket()

    def connect(self):
        try:
            self.service.connect((self.ip,self.port))
        except :
            raise Exception("Error ")

    def send(self,msg):
        if self.isConnected:
            self.service.send(str.encode(msg))
    def recv(self):
        result = ""
        if self.isConnected:
             result = self.service.recv(1024)
             result = result.decode("utf-8")
             return result

