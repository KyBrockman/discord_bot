import discord

import random
from discord.ext import commands


client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print('bot is ready.')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency*1000)} ms')
    
@client.command(aliases = ['8ball'])
async def _8ball(ctx, *, question):
    responses = ['It is certain.',
                 'Without a doubt',
                 'reply hazy try again',
                 'better not tell you now'
                 'my reply is no.',
                 'my sources say no']
    await ctx.send(f'Question: {question} \n Awnswer: {random.choice(responses)}')
    
    
client.run('NjgxOTczNTI5OTM5NjczMTQ4.XmlEfw.OGGXZMG4iQh31Y03YI5bs2RkZG0')