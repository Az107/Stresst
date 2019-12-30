

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
    messageDelay
    conditionMessage = dict()
    messageList = list()
    random = False


def loadConfig(fileName):
    finalConfig = config()
    configFile = open(fileName,'r')
    configLines = configFile.readlines()
    configLines = [l.strip() for l in configLines]
    protoConfig = dict()
    if configLines[0] != "[stresst config]": raise worgHeaderException()
    #connection n iterations
    for l in configLines:
        if l == "": continue
        if l[0] == '#' or l[0] == '[': continue
        a,b = l.split(": ")
        if  a == "if":
            req,res = b.split(" then ")
            req = req.strip('"')
            res = res.strip('"')
            finalConfig.conditionMessage[req] = res
        elif a == "messages":
            messages = b.replace('"','').split(',')
            finalConfig.messageList = messages
        elif a == "random":
            if b == "True":
                finalConfig.random = True
            elif b == "False":
                finalConfig.random = False
        else:
            try:
                if b[0] == '"':
                    b = b.strip('"')
                    setattr(finalConfig,a,b)
                else:
                    setattr(finalConfig, a, int(b))
            except Exception:
                continue

    checkNulls = finalConfig.ip != None and finalConfig.port != None and finalConfig.count != None and finalConfig.delay != None and finalConfig.initMessage != None
    if not checkNulls:
        raise invalidConfigException()

    return finalConfig


