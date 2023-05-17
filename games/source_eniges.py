import json
from dataclasses import dataclass
from sourceserver.sourceserver import SourceServer
class SourcesEngines:

    def __init__(self, ip, port = "27015"):
        self.ip = ip
        self.port = port
        self.data = {
            "response_status": 0,  # 0 = ERROR, 1 = SIMPLE, 2 = FULL
            "app_name": "csgo",  # Name of the application
            "name": None,  # Hostname of the server
            "map": None,  # Message of the day
            "ip": self.ip,  # IP address of the server
            "port": self.port,  # Port of the server
            "players": None,  # Number of players online
            "max_players": None,  # Maximum number of players
            "keywords": None,  # Keywords
            "vac": None,  # VAC
            "visibility": None,  # Visibility
            "server_type" : None, # Server type
            "extra": None  # Extra information
        }

        self.app_id_list = {
            "csgo": 730,
            "css": 240,
            "cs16": 10
        }

    def ipConbine(self):
        return self.ip+":"+self.port

    def getInfo(self):
        srv = SourceServer(self.ipConbine())
        info = srv.info
        players = srv.getPlayers()
        print(info, players)
        return {
            info, players
        }


