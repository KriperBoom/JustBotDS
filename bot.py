import os
import discord
from discord import app_commands

TOKEN = os.getenv("TOKEN")

class MyClient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.none())
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()

client = MyClient()

@client.tree.command(name="ping", description="Проверка бота")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("pong!")

client.run(TOKEN)
