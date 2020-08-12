import discord
import random
from discord.ext import commands, tasks
from itertools import cycle

client = commands.Bot(command_prefix = "!")
token = 'token' #Insert your Discord Token here
status = cycle(['with python :)', 'around my code :D'])

@client.event 
async def on_ready():
    change_status.start()
    print('Bot is online.')

@tasks.loop(seconds = 900)
async def change_status():
    await client.change_presence(activity = discord.Game(next(status))) 

#Clear command - deletes specified amount of messages
@client.command()
async def clear(ctx, amount : int):
    await ctx.channel.purge(limit = amount)

#Clear command - deletes 10000 messages
@client.command()
async def clearAll(ctx):
    await ctx.channel.purge(limit = 10000)

#Clear command error handling
@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("**Please specify an amount of messages to delete.**")

@client.command()
async def rps(ctx, choice : str):
    responses = ["Rock", "Paper", "Scissors"]
    set = random.choice(responses)
    if choice in responses:
        await ctx.send("**Rock, Paper, Scissors, SHOOT!**")
        if choice == set:
            await ctx.send(f"**I picked __{set}__. This is a draw! :D**")
        else:
            if choice == 'Rock':
                if set == 'Paper':
                    await ctx.send(f"**I picked __{set}__. You lose! :(**")
                if set == 'Scissors':
                    await ctx.send(f"**I picked __{set}__. You Win! :)**")
            if choice == 'Paper':
                if set == 'Scissors':
                    await ctx.send(f"**I picked __{set}__. You lose! :(**")
                if set == 'Rock':
                    await ctx.send(f"**I picked __{set}__. You Win! :)**")
            if choice == 'Scissors':
                if set == 'Rock':
                    await ctx.send(f"**I picked __{set}__. You lose! :(**")
                if set == 'Paper':
                    await ctx.send(f"**I picked __{set}__. You Win! :)**")
    else:
        await ctx.send(f"**Unknown Argument. Please Capitalize the first letter.**")

@rps.error
async def rps_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("**Please input a response of either Rock, Paper, or Scissors.**")

#Error handling
@client.event
async def error_command(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("**Invalid command used.")

client.run(token)