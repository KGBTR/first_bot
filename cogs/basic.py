from discord.ext import commands

class Basic(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Events

    @commands.Cog.listener()
    async def on_member_join(self, member):
        if (self.client.guild.name == "Bot Testing"):
            channel = self.client.get_channel(763690414615560212)
            await channel.send(f"{member.mention} has joined the server!")
    
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        if (self.client.guild.name == "Bot Testing"):
            channel = self.client.get_channel(763690414615560212)
            await channel.send(f"{member.mention} has left the server!")

    # Commands

    @commands.command(name="ping", description="shows bot's latency", aliases=["p"])
    async def ping(self, ctx):
        msg = await ctx.send(content = "Pinging.....")
        await msg.edit(content = f"Ping is {round(self.client.latency * 1000)}ms")

def setup(client):
    client.add_cog(Basic(client))