import json

import mcstatus
class Minecraft:
    def __init__(self,ip,port):
        self = self
        self.name = "Minecraft"
        self.ip = ip # IP address of the server
        self.port = port # Port of the server


    def getInfo(self):
         server = mcstatus.JavaServer.lookup(self.ip+":"+self.port)
         status = server.status()
         query = server.query()
         print(query.raw)
         return status
