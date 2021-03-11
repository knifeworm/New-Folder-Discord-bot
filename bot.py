import discord
from discord.ext import commands, tasks

bot = commands.Bot(command_prefix = "n!")

@bot.event
async def on_ready():
    print("New Folder is online!")