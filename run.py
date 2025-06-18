import discord
import os
import json

# Erst Umgebungsvariablen versuchen (für Docker), sonst /data/options.json (für Home Assistant Add-on)
TOKEN = os.environ.get("TOKEN") or os.environ.get("token")
CHANNEL_ID = os.environ.get("CHANNEL_ID") or os.environ.get("channel_id")

if not TOKEN or not CHANNEL_ID:
    try:
        with open("/data/options.json") as f:
            options = json.load(f)
        TOKEN = TOKEN or options.get("token")
        CHANNEL_ID = CHANNEL_ID or options.get("channel_id")
    except Exception as e:
        print("Fehler beim Lesen der Add-on-Konfiguration:", e)

if not TOKEN:
    raise ValueError("Discord TOKEN ist nicht gesetzt! Bitte in der Add-on-Konfiguration eintragen.")
if not CHANNEL_ID:
    raise ValueError("Discord CHANNEL_ID ist nicht gesetzt! Bitte in der Add-on-Konfiguration eintragen.")
CHANNEL_ID = int(CHANNEL_ID)

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Bot ist eingeloggt als {self.user}')
        channel = self.get_channel(CHANNEL_ID)
        if channel:
            await channel.send('Hello, World!')
        else:
            print(f"Kanal mit ID {CHANNEL_ID} nicht gefunden.")
        await self.close()

intents = discord.Intents.default()
client = MyClient(intents=intents)
client.run(TOKEN)
