import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='.', intents=intents)

#Login message
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

#Play the silver case
@client.command()
async def tsc(ctx):
    await ctx.send("Play this shit. NOW!\nSteam: <https://store.steampowered.com/app/476650/The_Silver_Case/>\nSwitch: <https://www.nintendo.co.uk/Games/Nintendo-Switch-games/The-Silver-Case-2425-1993621.html>\nPlayStation: <https://store.playstation.com/en-gb/product/EP1063-CUSA07272_00-THESILVERCASEPS4>")

#KTP playguide
@client.command()
async def ktp(ctx):
    await ctx.send("Kill The Past play guide here: https://discord.com/channels/567851899395506195/567860616992260116/1102264462855131247")

#ID hiding/handling
id_file = open("id.txt", "r")
id = id_file.read()

client.run(id)