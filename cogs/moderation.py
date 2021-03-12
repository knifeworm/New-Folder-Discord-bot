import discord
from discord.ext import commands

class moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            em = discord.Embed(title="Missing Perms")
            em.add_field(name="Error!", value=":x: You don't have permission to run this command! :x:")
            await ctx.send(embed=em)
        if isinstance(error, commands.MissingRequiredArgument):
            em = discord.Embed(title="Missing argument")
            em.add_field(name="Error!", value=":x: The command you have run requires arguments do n!help <command> to see how the command should be ran! :x:")
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

    @commands.command()
    @commands.has_guild_permissions(mute_members=True)
    async def mute(self, ctx, member : discord.Member, *, reason=None):
        role = discord.utils.get(ctx.guild.roles, name="Muted")

        if role is None:

            await ctx.send("Creating role!")
            create_role = await ctx.guild.create_role(name="Muted", reason = "Created for muted command! New Folder Bot")
            await ctx.sen("Setting permissions!")

            for channel in ctx.guild.channels:
                role_channel = discord.utils.get(ctx.guild.roles, name="Muted")
                await channel.set_permissions(role_channel, speak=False, send_messages=False, read_message_history=True, read_messages=True)
                await ctx.send("Permissions set!")
                await ctx.send("Muteing!")
                await member.add_roles(role_channel)
                embed = discord.Embed(title = "Mute")
                embed.add_field(name = "Member Muted", value=f"{member}", inline=False)
                embed.add_field(name = "Staff Member", value=f"{ctx.author}", inline=False)
                embed.add_field(name = "Reason", value=f"{reason}", inline=False)
                await ctx.send(embed = embed)
                mem = discord.Embed(title = "Mute")
                mem.add_field(name = "Staff Member", value=f"{ctx.author}", inline=False)
                mem.add_field(name = "Reason", value=f"{reason}", inline=False)
                mem.add_field(name = "Server", value=f"{ctx.guild.name}", inline=False)
                await member.send(embed = mem)
        else:
            role_channell = discord.utils.get(ctx.guild.roles, name="Muted")
            await member.add_roles(role_channell)
            embed = discord.Embed(title = "Mute")
            embed.add_field(name = "Member Muted", value=f"{member}", inline=False)
            embed.add_field(name = "Staff Member", value=f"{ctx.author}", inline=False)
            embed.add_field(name = "Reason", value=f"{reason}", inline=False)
            await ctx.send(embed = embed)
            mem = discord.Embed(title = "Mute")
            mem.add_field(name = "Staff Member", value=f"{ctx.author}", inline=False)
            mem.add_field(name = "Reason", value=f"{reason}", inline=False)
            mem.add_field(name = "Server", value=f"{ctx.guild.name}", inline=False)
            await member.send(embed = mem)

    @commands.command()
    @commands.has_guild_permissions(mute_members=True)
    async def unmute(self, ctx, member : discord.Member):
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        if role in member.roles:
            await member.remove_roles(role)
            embed = discord.Embed(title = "Unmute")
            embed.add_field(name = "Member Unmuted", value=f"{member}", inline=False)
            embed.add_field(name = "Staff Member", value=f"{ctx.author}", inline=False)
            embed.add_field(name = "Reason", value=f"{reason}", inline=False)
            await ctx.send(embed = embed)
            mem = discord.Embed(title="Unmute")
            mem.add_field(name = "Staff Member", value=f"{ctx.author}", inline=False)
            mem.add_field(name = "Reason", value=f"{reason}", inline=False)
            mem.add_field(name = "Server", value=f"{ctx.guild.name}", inline=False)
            await member.send(embed = mem)
        else:
            await ctx.send(f":x: The member {member} is not muted! :x:")


def setup(bot):
    bot.add_cog(moderation(bot))