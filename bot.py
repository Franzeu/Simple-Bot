import discord
import random
from discord.ext import commands, tasks
from itertools import cycle

client = commands.Bot(command_prefix = "!")
token = 'NzM5ODk5NDM0MzQyNjc4NTg5.XyhLCw.EdIppNOheFppTCTwdz4UvXGc1XE' #Insert your Discord Token here
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
async def clearall(ctx):
    await ctx.channel.purge(limit = 10000)

#Clear command error handling if there is a missing argument
@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("**Please specify an amount of messages to delete.**")

#Rock-Paper-Scissor command
@client.command()
async def rps(ctx, choice : str):
    responses = ["Rock", "Paper", "Scissors"]
    set = random.choice(responses)
    if choice in responses:
        await ctx.send("**Rock, Paper, Scissors, SHOOT!**")
        if choice == set:
            await ctx.send(f"I picked **{set}**. This is a draw! :hushed:")
        else:
            if choice == 'Rock':
                if set == 'Paper':
                    await ctx.send(f"I picked **{set}**. You lose! :sweat_smile:")
                if set == 'Scissors':
                    await ctx.send(f"I picked **{set}**. You Win! :smiley:")
            elif choice == 'Paper':
                if set == 'Scissors':
                    await ctx.send(f"I picked **{set}**. You lose! :sweat_smile:")
                if set == 'Rock':
                    await ctx.send(f"I picked **{set}**. You Win! :smiley:")
            elif choice == 'Scissors':
                if set == 'Rock':
                    await ctx.send(f"I picked **{set}**. You lose! :sweat_smile:")
                if set == 'Paper':
                    await ctx.send(f"I picked **{set}**. You Win! :smiley:")
    else:
        await ctx.send(f"Unknown Argument. Please check spelling.")

#Rock-Paper Scissor error handling if there is a missing argument
@rps.error
async def rps_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("**Please input a response of either Rock, Paper, or Scissors.**")

#Ping Command
@client.command()
async def ping(ctx):
    await ctx.send(f'Your latency is: **{round(client.latency * 1000)}**ms')

#Member join notification
@client.event
async def on_member_join(member):
    print(f'{member} has joined the server.')

#Member leave notification
@client.event
async def on_member_remove(member):
    print(f'{member} has left the server.')

#Coin flip command
@client.command()
async def coinflip(ctx):
    responses = ['Heads','Tails']
    await ctx.send(f"{random.choice(responses)}")

#Kick command
@client.command()
async def kick(ctx, member : discord.Member, *, reason = None):
    await member.kick(reason = reason)
    await ctx.send(f'**Kicked** {member.mention}')

#Ban command
@client.command()
async def ban(ctx, member : discord.Member, *, reason = None):
    await member.ban(reason = reason)
    await ctx.send(f'**Banned** {member.mention}')

#Error handling if a command is misspelled or a unknown command is used, [not working!]
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("**Invalid command used.**")

client.run(token)