
class Configuration:

    worgHeaderException = Exception("invalid file  header")
    invalidConfigException = Exception("invalid configuration")

    class config:
        #connection
        ip = None
        port = None
        #iterations
        count = None
        delay = None
        #messages
        initMessage = None
        conditionMessage = dict()
        messageList = list()
        orderMesage = list()


    def loadConfig(self,fileName):
        finalConfig = self.config()
        configFile = open(fileName,'r')
        configLines = configFile.readlines()
        configLines = [l.strip() for l in configLines]
        protoConfig = dict()
        if configLines[0] != "[stresst config]": raise self.worgHeaderException()
        #connection n iterations
        for l in configLines:
            if l == "": continue
            if l[0] == '#' or l[0] == '[': continue
            a,b = l.split(": ")
            if  a == "if":
                req,res = b.split(" then ")
                finalConfig.conditionMessage[req] = res
            else:
                try:
                    setattr(finalConfig,a,b)
                except Exception:
                    continue

        checkNulls = finalConfig.ip != None and finalConfig.port != None and finalConfig.count != None and finalConfig.delay != None and finalConfig.initMessage != None
        if not checkNulls:
            raise

        return finalConfig


