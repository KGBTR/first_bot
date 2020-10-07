import discord
from discord.ext import commands
import random
import os

from discord.ext.commands.core import has_permissions

intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix = '-', intents = intents)

@client.event
async def on_ready():
    print("Bot is ready.")

@client.command(aliases = ["8ball", "8b"]) #all of this strings can be used to invoke the below function(_8ball)
async def _8ball(ctx, *, question): #it can now take multiple arguments 
    responses = ["It is certain.",
                "It is decidedly so.",
                "Without a doubt.",
                "Yes - definitely.",
                "You may rely on it.",
                "As I see it, yes.",
                "Most likely.",
                "Outlook good.",
                "Yes.",
                "Signs point to yes.",
                "Reply hazy, try again.",
                "Ask again later.",
                "Better not tell you now.",
                "Cannot predict now.",
                "Concentrate and ask again.",
                "Don't count on it.",
                "My reply is no.",
                "My sources say no.",
                "Outlook not so good.",
                "Very doubtful."]

    await ctx.send(f"Question: {question}\nAnswer: {random.choice(responses)}")

@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount = 5):
    if (amount <= 0):
        await ctx.send("Nice try.")
    else:
        await ctx.channel.purge(limit = amount + 1)

@client.command(aliases = ["dick", "yarrak", "pp"])
async def penis(ctx, member : discord.Member=None):
    if (member == None):
        await ctx.send(f"{ctx.message.author.mention}'s' penis:\n8{random.randint(0,11) * '='}D")

    else:
        await ctx.send(f"{member.mention}'s penis:\n8{random.randint(0,11) * '='}D")

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f"Kicked {member.mention}")

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f"Banned {member.mention}")

@client.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans() #guild means server
    member_name, member_discriminator = member.split("#") #for example, member_name = forthus member_discriminator = #1907

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"Unbanned {user.mention}")
            return

@client.command()
async def load(ctx, extension): #it is going to load our extension
    client.load_extension(f"cogs.{extension}")

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")

for filename in os.listdir("./cogs"): #it is going to go through all the files in this cogs folder and check if there is a py file, if there is load it like a cog
    if filename.endswith("py"):
        client.load_extension(f"cogs.{filename[:-3]}")

client.run(os.environ["DISCORD_TOKEN"])
