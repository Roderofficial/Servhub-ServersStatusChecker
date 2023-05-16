import json

from sourceserver.sourceserver import SourceServer
class SourcesEngines:

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def getInfo(self):
        srv = SourceServer("51.83.169.118:27015")
        info = srv.info
        players = srv.getPlayers()
        print(info, players)
        return