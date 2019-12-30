import socket

class Connection:
    isConnected = False
    ip = ""
    port = -1
    service = None
    def __init__(self,ip,port):
        self.ip = ip
        self.port = port
        self.service = socket.socket()

    def connect(self):
        try:
            self.service.connect((self.ip,self.port))
            self.isConnected = True
        except :
            raise Exception("Error ")

    def send(self,msg):
        if self.isConnected:
            self.service.send(str.encode(msg + '\n'))
    def recv(self):
        result = ""
        if self.isConnected:
             result = self.service.recv(1024)
             result = result.decode("utf-8")
             result = result.strip()
             return result

    def close(self):
        self.service.close()