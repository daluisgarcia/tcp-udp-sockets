import os
from datetime import datetime

class LogWritter:
    def writeProtocolLog(self, userName, content, ipAddress, protocol, error = False):
        fileName = os.path.abspath(__file__).replace('LogWritter.py', '') + userName + '-' + protocol + '-' + datetime.now().isoformat().replace(':', '+') + '.log'
        fileContent = content + ' - ' + datetime.now().isoformat() + ' - ' + ipAddress + ' - ' + protocol
        f = open(fileName, "a")
        f.write(fileContent)
        f.close()