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
async def pizza(ctx):
    await ctx.send("Pizza")
    
@client.command()
async def testPoll
    
    channel = message.channel
    choices = {"🇦": "Solos",
               "🇧": "Duos",
               "🇨": "Squads"}

    vote = discord.Embed(title="**[POLL]**", description=" ", color=0x00ff00)
    value = "\n".join("- {} {}".format(*item) for item in choices.items()) 
    vote.add_field(name="Please vote for the match type:", value=value, inline=True)

    message_1 = await client.send_message(channel, embed=vote)

    for choice in choices:
        await client.add_reaction(message_1, choice)

    await aynsio.sleep(60)  # wait for one minute
    message_1 = await client.get_message(channel, message_1.id)


    counts = {react.emoji: react.count for react in message_1.reactions}
    winner = max(choices, key=counts.get)

    await client.send_message(channel, "{} is the winner".format(choices[winner]))

# client.run(TOKEN)
