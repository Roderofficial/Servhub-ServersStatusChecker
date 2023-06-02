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
            "ip": self.ip,  # IP address of the server
            "port": self.port,  # Port of the server
            "players": 0,  # Number of players online
            "max_players": 0,  # Maximum number of players
            "name": None,

            "extra": {
                "version": None,  # Version of the server
                "ping": None,  # Ping of the server
                "plugins": None,  # List of plugins
                "map": None,  # Map of the server
                "favicon": None,  # Favicon of the server
                "hostname": None,  # Hostname of the server
            } # Extra information
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
            print(status)

            self.data["response_status"] = 1
            self.data['extra']['version'] = status['version']['name'] if 'version' in status else None
            self.data['name']= self.getDescription(status['description']) if 'description' in status else None
            self.data['players'] = status['players']['online'] if 'players' in status else None
            self.data['max_players'] = status['players']['max'] if 'players' in status else None
            self.data['extra']['ping'] = int(round(server.ping(),0))
            self.data['extra']['favicon'] = status['favicon'] if 'favicon' in status else None



        except Exception as e:
            print(e, "Error while getting the server status")
            return self.data

        try:

            query = server.query().raw
            self.data["response_status"] = 2
            self.data['extra']['hostname'] = query['hostname'] if 'hostname' in query else None
            self.data['extra']['map'] = query['map'] if 'map' in query else None
            self.data['extra']['plugins'] = query['plugins'] if 'plugins' in query else None

        except Exception as e:
            print(e, "Error while getting the server query")

        return self.data


    def getDescription(self, description):
        print(description)
        if(description['text']):
            return description['text']

        if(description['extra']):
            text = ""
            for i in description['extra']:
                text += i['text']

            return text
