import discord
from discord.ext import commands
from os import environ

client = commands.Bot(
    command_prefix="-",
    description="forthus' first bot",
    owner_id=289832224512016396,
    case_insensitive=True,
    intents = discord.Intents(messages=True, reactions=True, members=True, guilds=True, presences=True)
)

cogs = ["cogs.fun", "cogs.basic", "cogs.moderator"]

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game("-help"))
    print(f"Logged in as {client.user.name} - {client.user.id}")
    for cog in cogs:
        client.load_extension(cog)
    return

client.run(environ["DISCORD_TOKEN"])