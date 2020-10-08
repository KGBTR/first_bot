import discord
from discord.ext import commands
from discord.ext.commands.core import has_permissions

class Moderator(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name="clear", description="clears amount of x messages", usage="<amount>")
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount = 5):
        if (amount <= 0):
            await ctx.send(f"Nice try!")
        else:
            await ctx.channel.purge(limit = amount+1)
    
    @commands.command(name="kick", description="kicks mentioned user", aliases=["kick"],usage="@user <reason(optional)>")
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f"Kicked {member.mention}")

    @commands.command(name="ban", description="bans mentioned user", usage="@user <reason(optional)>")
    @commands.has_permissions(ban_members=True)
    async def kick(self, ctx, member : discord.Member, *, reason):
        await member.ban(reason=reason)
        await ctx.send(f"Banned {member.mention}!")

    @commands.command(name="unban", description="unbans given user(with )", usage="user's discord full discord name  <reason(optional)>")
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.Member, *, reason):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split("#")

        for ban_entry in banned_users:
            user = ban_entry.user

            if(user.name, user.discriminator == member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f"Unbanned {user.mention}!")
                return
    
def setup(client):
    client.add_cog(Moderator(client))