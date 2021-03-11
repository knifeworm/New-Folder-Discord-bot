import discord
from discord.ext import commands, tasks
from secret import TOKEN
from secret import PREFIX

bot = commands.Bot(command_prefix = PREFIX)

@bot.event
async def on_ready():
    print("New Folder is online!")


bot.run(TOKEN)