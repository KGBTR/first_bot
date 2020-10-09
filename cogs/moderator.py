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
    
def setup(client):
    client.add_cog(Moderator(client))