import discord
import os

# Kompatibel für Home Assistant (klein) und Docker (groß)
TOKEN = os.environ.get("TOKEN") or os.environ.get("token")
CHANNEL_ID = int(os.environ.get("CHANNEL_ID") or os.environ.get("channel_id"))

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
