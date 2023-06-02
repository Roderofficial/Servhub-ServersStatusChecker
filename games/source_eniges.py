import json
from dataclasses import dataclass
import a2s


class SourcesEngines:

    def __init__(self, ip, port="27015"):
        self.ip = ip
        self.port = port
        self.data = {
            "response_status": 0,  # 0 = ERROR, 1 = SIMPLE, 2 = FULL
            "ip": self.ip,  # IP address of the server
            "port": self.port,  # Port of the server
            "players": 0,  # Number of players online
            "max_players": 0,  # Maximum number of players
            "name": None,

            "extra": {

            }  # Extra information
        }


    def getInfo(self):
        srv = a2s.info((self.ip, int(self.port)))
        info = srv

        print(info, info.server_name)

        if info is None:
            self.data["response_status"] = 0
            return self.data

        self.data["response_status"] = 1
        self.data["name"] = info.server_name
        self.data["players"] = info.player_count
        self.data["max_players"] = info.max_players
        self.data["extra"]["map"] = info.map_name if hasattr(info, 'map_name') else None
        self.data["extra"]["keywords"] = info.keywords if hasattr(info, 'keywords') else None
        self.data["extra"]["bots"] = info.bot_count if hasattr(info, 'bot_count') else None
        self.data["extra"]["vac"] = info.vac_enabled if hasattr(info, 'vac_enabled') else None
        self.data["extra"]["password"] = info.password_protected if hasattr(info, 'password_protected') else None

        try:
            players = a2s.players((self.ip, int(self.port)))
            self.data["extra"]["players"] = players
        except Exception as e:
            pass

        return self.data
