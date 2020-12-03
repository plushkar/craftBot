# bot.py
import os

import discord
import random
from dotenv import load_dotenv
from discord.ext import commands

client = commands.Bot('!')


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.command()
async def test(ctx):
    await ctx.send("Test")


@client.command()
async def craft(ctx):
    await ctx.send('Craft Bot')


@client.command()
async def coinflip(ctx):
    num = random.random()
    if num < 0.5:
        await ctx.send('Heads')
    else:
        await ctx.send('Tails')


@client.command()
async def poll(ctx):
    upvote = '<:upvote:778439419014152193>'
    downvote = '<:downvote:778439419010613249>'

    await ctx.message.add_reaction(upvote)
    await ctx.message.add_reaction(downvote)

@client.command()
async def pizza(ctx)
    await ctx.send("Pizza")

# client.run(TOKEN)
