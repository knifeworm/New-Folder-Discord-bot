import discord
from discord.ext import commands

class moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            em = discord.Embed(title="Missing Perms")
            em.add_field(name="", value=":x: You don't have permission to run this command! :x:")
            await ctx.send(embed=em)
        if isinstance(error, commands.MissingRequiredArgument):
            em = discord.Embed(title="Missing argument")
            em.add_field(name="", value=":x: The command you have run requires arguments do n!help <command> to see how the command should be ran! :x:")
            await ctx.send(embed=em)
        else:
            await ctx.send(error)

    @commands.command()
    @commands.has_guild_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        embed = discord.Embed(title = "Ban")
        embed.add_field(name = "Member Banned", value = f'{member}', inline=False)
        embed.add_field(name = "Staff Member", value = f'{ctx.author}', inline=False)
        embed.add_field(name = "Reason", value = f'{reason}', inline=False)
        await ctx.send(embed = embed)
        mem = discord.Embed(title = "Ban")
        mem.add_field(name = "Staff Member", value = f'{ctx.author}', inline=False)
        mem.add_field(name = "Reason", value = f'{reason}', inline=False)
        mem.add_field(name = "Server", value = f'{ctx.guild.name}', inline=False)
        await member.send(embed = mem)
        await member.ban(reason = reason)
    @commands.command()
    @commands.has_guild_permissions(kick_members=True)
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        embed = discord.Embed(title = "Kick")
        embed.add_field(name = "Member Kicked", value = f'{member}', inline=False)
        embed.add_field(name = "Staff Member", value = f'{ctx.author}', inline=False)
        embed.add_field(name = "Reason", value = f'{reason}', inline=False)
        await ctx.send(embed = embed)
        mem = discord.Embed(title= "Kick")
        mem.add_field(name = "Staff Member", value = f'{ctx.author}', inline=False)
        mem.add_field(name = "Reason", value = f'{reason}', inline=False)
        mem.add_field(name = "Server", value = f'{ctx.guild.name}', inline=False)
        await member.send(embed = mem)
        await member.kick(reason = reason)
def setup(bot):
    bot.add_cog(moderation(bot))