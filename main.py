import games.source_eniges as se
import games.minecraft as mc
import json
from fastapi import FastAPI

app = FastAPI()

games = {
    "minecraft_java": mc.MinecraftJava,
    "csgo": se.SourcesEngines,
    "css": se.SourcesEngines,
    "cs16": se.SourcesEngines,
}


@app.get("/status", tags=["status"])
async def root(ip: str, port: str = None, game: str = None):
    if game is None:
        return {"error": "game is not specified"}
    if game not in games:
        return {"error": "game is not supported"}

    game = games[game](ip, port)
    return game.getInfo()



