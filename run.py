import discord
import os

TOKEN = os.environ["TOKEN"]
CHANNEL_ID = int(os.environ["CHANNEL_ID"])

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
