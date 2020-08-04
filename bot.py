import discord
from discord.ext import commands, tasks
from itertools import cycle

client = commands.Bot(command_prefix = "!")
token = 'NzM5ODk5NDM0MzQyNjc4NTg5.XyhLCw.Kem86_GfLO5ag_Wpx_YdumDb50k'
status = cycle(['with python :)', 'around my code :D'])

@client.event 
async def on_ready():
    change_status.start()
    print('Bot is online.')

@tasks.loop(seconds = 900)
async def change_status():
    await client.change_presence(activity = discord.Game(next(status))) 

client.run(token)