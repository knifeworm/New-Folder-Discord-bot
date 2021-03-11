import discord
from discord.ext import commands, tasks
from secret import TOKEN
from secret import PREFIX
import os

bot = commands.Bot(command_prefix = PREFIX)

@bot.event
async def on_ready():
    print("New Folder is online!")


@bot.command()
@commands.has_guild_permissions(administrator=True)
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')
    await ctx.send(f":white_check_mark: Cog {extension} has been loaded!")

@bot.command()
@commands.has_guild_permissions(administrator=True)
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    await ctx.send(f":white_check_mark: Cog {extension} has been unloaded!")

@bot.command()
@commands.has_guild_permissions(administrator=True)
async def reload(ctx, extension):
    bot.load_extension(f'cogs.{extension}')
    await ctx.send(f":white_check_mark: Cog {extension} has been reloaded!")

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')
        print("Cogs have been loaded!")

bot.run(TOKEN)