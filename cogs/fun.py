import discord
from discord.ext import commands
from random import randint

class Fun(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Events

    @commands.Cog.listener() #this is our function decorator for within a cog
    async def on_message(self, message):
        try:
            if [i for i in ["hmm", "acaba", "düşünüyorum", "dusunuyorum"] if i in message.content]:
                await message.add_reaction("🤔")
            if [i for i in ["🥴", "Woozy", "woozy"]if i in message.content]:
                await message.add_reaction("🥴")
            if message.content == "sa":
                await message.channel.send("cami mi lan burası orospu çocuğu")
            if [i for i in ["gercek mi", "gerçek mi", "gercekmi", "gerçekmi"] if i in message.content]:
                await message.channel.send("amına kodumun çocuğu gerizekalı amcık sence Hulk gerçek olabilir mi?")
        except:
            return
    
    # Commands

    @commands.command(name="penis", description="how big pp", aliases=["pp", "dick", "yarrak"])
    async def penis(self, ctx, member : discord.Member=None):
        if (member == None):
            await ctx.send(f"{ctx.message.author.mention}'s penis:\n8{randint(0,11) * '='}D")
        else:
            await ctx.send(f"{member.mention}'s penis:\n8{randint(0,11) * '='}D")
    
def setup(client):
    client.add_cog(Fun(client))
    # Adds the Fun commands to the bot
    # Note: The "setup" function has to be there in every cog file