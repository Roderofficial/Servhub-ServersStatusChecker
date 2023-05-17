import json
from dataclasses import dataclass

import mcstatus


class MinecraftJava:
    def __init__(self, ip, port = None):
        self = self
        self.name = "Minecraft"
        self.ip = ip  # IP address of the server
        self.port = port  # Port of the server
        self.data = {
            "response_status": 0,  # 0 = ERROR, 1 = SIMPLE, 2 = FULL
            "app_name": "minecraft_java",  # Name of the application
            "hostname": None,  # Hostname of the server
            "motd": None,  # Message of the day
            "ip": self.ip,  # IP address of the server
            "port": self.port,  # Port of the server
            "players": None,  # Number of players online
            "max_players": None,  # Maximum number of players
            "version": None,  # Version of the server
            "ping": None,  # Ping of the server
            "plugins": None,  # List of plugins
            "map": None,  # Map of the server
            "favicon": None,  # Favicon of the server
            "extra": None  # Extra information
        }


    def adress_conbine(self):
        if self.port is None:
            return self.ip
        else:
            return self.ip + ":" + self.port

    def getInfo(self): # Get information about the server
        print('getting info')
        try:
            print(self.adress_conbine())
            server = mcstatus.JavaServer.lookup(self.adress_conbine())
        except Exception as e:
            print(e, "Error while connecting to the server")
            return self.data

        try:
            status = server.status().raw

            self.data["response_status"] = 1
            self.data['version'] = status['version']['name'] if 'version' in status else None
            self.data['motd'] = status['description']['text'] if 'description' in status else None
            self.data['players'] = status['players']['online'] if 'players' in status else None
            self.data['max_players'] = status['players']['max'] if 'players' in status else None
            self.data['ping'] = int(round(server.ping(),0))
            self.data['favicon'] = status['favicon'] if 'favicon' in status else None



        except Exception as e:
            print(e, "Error while getting the server status")
            return None

        try:

            query = server.query().raw
            self.data["response_status"] = 2
            self.data['hostname'] = query['hostname'] if 'hostname' in query else None
            self.data['map'] = query['map'] if 'map' in query else None
            self.data['plugins'] = query['plugins'] if 'plugins' in query else None

        except Exception as e:
            print(e, "Error while getting the server query")

        return self.data
