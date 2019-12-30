
from time import sleep
from threading import Thread
import random
import Configuration
from  Connection import Connection

class stress:
    connections = []
    count = 0
    conf = Configuration.config()

    def __init__(self,conf):
        self.conf = conf
        self.engine()

    def listen(self,conn):
        req = conn.recv()
        if req in self.conf.conditionMessage:
            conn.send(self.conf.conditionMessage[req])

    def iteration(self):
        conn = Connection(self.conf.ip, self.conf.port)
        try:
            conn.connect()
            print("Connected")
        except Exception:
            print("Error to connect")
        conn.send(self.conf.initMessage)
        index = 0
        while conn.isConnected:
            Thread(target=self.listen,args=(conn,)).start()
            if (self.conf.random):
                index = random.randrange(0,len(self.conf.messageList))
            if self.conf.random or index < len(self.conf.messageList) :
                conn.send(self.conf.messageList[index])
                index += 1
            else:
                conn.isConnected = False
                conn.close()
            sleep(1) # add to the config file
        self.connections.append(conn)
        self.count -= 1

    def engine(self):
        while True:
            try:
                if self.count < self.conf.count:
                    Thread(target=self.iteration).start()
                    self.count += 1
                sleep(self.conf.delay)
            except KeyboardInterrupt:
                print("Exiting...")
                for conn in self.connections :
                    conn.close()
                break



if __name__ == '__main__':
        conf = Configuration.loadConfig("stresst.conf")
        stress(conf)