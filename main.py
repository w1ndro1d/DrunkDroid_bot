import os
import discord
from aiohttp import request
from discord import Embed
import requests
from datetime import datetime
from discord.ext import commands
from discord.ext.commands import Bot
# from discord.ext import tasks
import time
import random
import requests
from bs4 import BeautifulSoup


drunkdroid = commands.Bot(command_prefix='.')
drunkdroid.previous_typer = 0
drunkdroid.remove_command("help")


@drunkdroid.group(invoke_without_command=True)
async def ddhelp(ctx):
    em = discord.Embed(
        title="Help", colour=discord.Colour.orange())
    em.add_field(name="For dog lovers", value=".dogfact, .dogpic")
    em.add_field(name="Latency check", value=".ddping")
    em.add_field(name="Keywords that trigger me",
                 value="drunkdroid, quotes, drunk, suck, hate this bot")
    em.add_field(name="Ping a user", value=".ping, .ultraping")
    await ctx.send(embed=em)


# @tasks.loop(seconds=2.0, count=5)
# async def pinguser(user, ctx):
#     await ctx.send(f'{user.mention}'+" Your friends are waiting for you in VC. Come let's play VALORANT!")


# @drunkdroid.event
# async def on_member_join(member, message):
#     mbed = discord.Embed(
#         colour=discord.Colour.orange(),
#         title="Welcome!",
#         description=f"Hi {member.mention} hehe boiiiii! Becoming a pidit is a way of life. Good on ya!"
#     )
#     await member.send(embed=mbed)
#     await message.channel.send(f'{member} has chosen the life of a Pidit. Very wise decision!')


@drunkdroid.event
async def on_member_remove(member, message):
    mbed = discord.Embed(
        colour=discord.Colour.orange(),
        title="Goodbye!",
        description=f"{member.mention}, you left? Well, being a pidit isn't everyone's cup of tea. But once you become a pidit, its a way of life. Don't forget that!"
    )
    await member.send(embed=mbed)
    await message.channel.send(f'{member} has sadly left the server. We will miss you :/ JK :P')


@drunkdroid.event
async def on_ready():
    print('Logged in as')
    print(drunkdroid.user.name)
    print(drunkdroid.user.id)
    print('---------------')
    await drunkdroid.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Pidits suffer"))


@drunkdroid.event
async def on_typing(channel, user, when):
    prob_annoy = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
    if random.choice(prob_annoy) == 1:
        if user.bot:
            return
        if drunkdroid.previous_typer == user.id:
            return
        else:
            drunkdroid.previous_typer = user.id
        responses = ["Oi "+f'{user.mention}'+" Type faster. I don't have all day. I have bottles to drink! 🥴",
                     "Ma jhyaap xu kta ho. 🥴",
                     "Bulbul.",
                     "Sahi ho, haha.",
                     "Champaklal le hepdo raixa yar. Champake noob.",
                     "I may be drunk, Miss, but in the morning I will be sober and you will still be ugly.",
                     "atitkh#1327 VolteX vandal sprayer ho. 🥴",
                     "One should always be drunk. That's all that matters...But with what? With wine, with poetry, or with virtue, as you chose. But get drunk.",
                     "Noob! Type faster!!",
                     "Drunken men give some of the best pep talks.",
                     "Herb is the healing of a nation, alcohol is the destruction.",
                     "I assure you, my friends, I am cone sold stober.",
                     "One tequila, two tequila, three tequila, floor.",
                     "Vikram begins!",
                     "Oh? Rhina is on fire.",
                     "I don't have a drinking problem, 'cept when I can't get a drink.",
                     "@legend4545 noobde ho. 🥴",
                     "@ankit#6969 Nightmare crouch strafe sprayer ho. 🥴",
                     "@Suman_Aryal#1495 Suman_Aryal phantom sprayer ho. 🥴",
                     "WINDROID is my god, and yours too. 🥴",
                     "Oi "+f'{user.mention}'+" Beer khane? 🥴",
                     "I accept no responsibility for anything I did while drunk. -drunkdroid 🥴",
                     "One should always be drunk. That's all that matters...But with what? With wine, with poetry, or with virtue, as you chose. But get drunk. -Charles Baudelaire, Paris Spleen",
                     "A man's true character comes out when he's drunk. -Charlie Drunklin",
                     "And in the end, we were all just humans.. drunk on the idea that love, only love, could heal our brokenness. -Christopher Poindexter",
                     "What's so unpleasant about being drunk? Ask a glass of water! -Douglas Adams, The Hitchhiker's Guide to the Galaxy",
                     "If getting drunk was how people forgot they were mortal, then hangovers were how they remembered. -Matt Haig, The Humans",
                     "They're professionals at this in Russia, so no matter how many Jell-O shots or Jager shooters you might have downed at college mixers, no matter how good a drinker you might think you are, don't forget that the Russians - any Russian - can drink you under the table. -Anthony Bourdain, A Cook's Tour: Global Adventures in Extreme Cuisines",
                     "Jon: 'What are you doing up there? Why aren't you at the feast? Tyrion: 'Too hot, too noisy, and I'd drunk too much wine', the dwarf told him. 'I learned long ago that it is considered rude to vomit on your brother. -George R.R. Martin, A Game of Thrones",
                     "Drunken men give some of the best pep talks. -Criss Jami, Killosophy",
                     "My mind may be sober, but my confidence is high! -Habeeb Akande",
                     "I'm always drunk! hehe -drunkdroid",
                     "There are hours for rest, and hours for wakefulness; nights for sobriety and nights for drunkenness—(if only so that possession of the former allows us to discern the latter when we have it; for sad as it is, no human body can be happily drunk all the time). -Roman Payne, Rooftop Soliloquy",
                     "Nothing spells trouble like two drunk cowboys with a rocket launcher. -C.J. Box, Cold Wind",
                     "Just because you're sober, don't think you're a good driver, Cookie. -John Irving, Last Night in Twisted River",
                     "To be now a sensible man, by and by a fool, and presently a beast! -William Shakespeare, Othello and the Tragedy of Mariam",
                     "Millions of deaths would not have happened if it weren’t for the consumption of alcohol. The same can be said about millions of births. -Mokokoma Mokhonoana",
                     "98% of the things said by a drunk man are true; 98% of those said by a horny man aren’t. -Mokokoma Mokhonoana",
                     "Drunkenness - that fierce rage for the slow, sure poison, that oversteps every other consideration; that casts aside wife, children, friends, happiness, and station; and hurries its victims madly on to degradation and death. -Charles Dickens, Sketches by Boz",
                     "An intoxicated person will never lie, the sober will always be diplomatic. -Kumar Pranay",
                     "Drunk words are sober thoughts. -Taylor Jenkins Reid, Forever, Interrupted",
                     "At some point, old is indistinguishable from drunk. -Carol L. Covin",
                     "...drunks and leggings always tell the truth. -Abby Jimenez, The Friend Zone",
                     "I have met drunken ladies during my travels, it is okay until they vomit all over you! -Steven Magee",
                     "I accept no responsibility for anything I did while drunk. -drunkdroid"]
        await channel.send(random.choice(responses))
    else:
        return


@drunkdroid.event
async def on_message(message):
    if message.author.bot:
        return
    if 'drunkdroid' in message.content.lower() or 'quotes' in message.content or 'drunk' in message.content.lower():

        responses = ["One should always be drunk. That's all that matters...But with what? With wine, with poetry, or with virtue, as you chose. But get drunk. -Charles Baudelaire, Paris Spleen",
                     "A man's true character comes out when he's drunk. -Charlie Drunklin",
                     "And in the end, we were all just humans.. drunk on the idea that love, only love, could heal our brokenness. -Christopher Poindexter",
                     "What's so unpleasant about being drunk? Ask a glass of water! -Douglas Adams, The Hitchhiker's Guide to the Galaxy",
                     "If getting drunk was how people forgot they were mortal, then hangovers were how they remembered. -Matt Haig, The Humans",
                     "They're professionals at this in Russia, so no matter how many Jell-O shots or Jager shooters you might have downed at college mixers, no matter how good a drinker you might think you are, don't forget that the Russians - any Russian - can drink you under the table. -Anthony Bourdain, A Cook's Tour: Global Adventures in Extreme Cuisines",
                     "Jon: 'What are you doing up there? Why aren't you at the feast? Tyrion: 'Too hot, too noisy, and I'd drunk too much wine', the dwarf told him. 'I learned long ago that it is considered rude to vomit on your brother. -George R.R. Martin, A Game of Thrones",
                     "Drunken men give some of the best pep talks. -Criss Jami, Killosophy",
                     "My mind may be sober, but my confidence is high! -Habeeb Akande",
                     "I'm always drunk! hehe -drunkdroid",
                     "There are hours for rest, and hours for wakefulness; nights for sobriety and nights for drunkenness—(if only so that possession of the former allows us to discern the latter when we have it; for sad as it is, no human body can be happily drunk all the time). -Roman Payne, Rooftop Soliloquy",
                     "Nothing spells trouble like two drunk cowboys with a rocket launcher. -C.J. Box, Cold Wind",
                     "Just because you're sober, don't think you're a good driver, Cookie. -John Irving, Last Night in Twisted River",
                     "To be now a sensible man, by and by a fool, and presently a beast! -William Shakespeare, Othello and the Tragedy of Mariam",
                     "Millions of deaths would not have happened if it weren’t for the consumption of alcohol. The same can be said about millions of births. -Mokokoma Mokhonoana",
                     "98% of the things said by a drunk man are true; 98% of those said by a horny man aren’t. -Mokokoma Mokhonoana",
                     "Drunkenness - that fierce rage for the slow, sure poison, that oversteps every other consideration; that casts aside wife, children, friends, happiness, and station; and hurries its victims madly on to degradation and death. -Charles Dickens, Sketches by Boz",
                     "An intoxicated person will never lie, the sober will always be diplomatic. -Kumar Pranay",
                     "Drunk words are sober thoughts. -Taylor Jenkins Reid, Forever, Interrupted",
                     "At some point, old is indistinguishable from drunk. -Carol L. Covin",
                     "...drunks and leggings always tell the truth. -Abby Jimenez, The Friend Zone",
                     "I have met drunken ladies during my travels, it is okay until they vomit all over you! -Steven Magee",
                     "I accept no responsibility for anything I did while drunk. -drunkdroid"]
        await message.channel.send("```"+random.choice(responses)+"```")
        await message.add_reaction("🥴")
    if 'suck' in message.content or 'hate this bot' in message.content:
        await message.channel.send("No "+f"{message.author.mention}. You suck! :angry:")
        await message.add_reaction("😡")
        await message.add_reaction("🤬")
    await drunkdroid.process_commands(message)


@drunkdroid.command()
async def ddping(ctx):
    await ctx.send(f'{round(drunkdroid.latency*1000)}ms')


@drunkdroid.command()
async def ping(ctx, user: discord.User):
    i = 0
    if "w-i-n-d-r-o-i-d" in user.name:
        await ctx.send("Sorry, he's immune to this command. You can't uno reverse card a god! Nice try noob.")
    else:
        for i in range(5):
            print(user)
            await ctx.send(f'{user.mention}' + ", your friends are waiting for you in VC. Come let's play VALORANT!")
            time.sleep(3)


@drunkdroid.command()
async def ultraping(ctx, user: discord.User):
    i = 0
    if "w-i-n-d-r-o-i-d" in user.name:
        await ctx.send("Sorry, he's immune to this command. You can't uno reverse card a god! That was a nice try though.")
    else:
        for i in range(10):
            await ctx.send(f'{user.mention}' + ", your friends are waiting for you in VC. Come let's play VALORANT!")
            time.sleep(1)


@drunkdroid.command()
async def dogfact(ctx):
    fact_url = 'https://some-random-api.ml/facts/dog'
    f = requests.get(fact_url).json()
    desc = f['fact']
    embed = discord.Embed(title="Here you go :)",
                          colour=discord.Colour.orange())
    embed.add_field(name="Doggo Fact", value=str(desc))
    await ctx.send(embed=embed)


@drunkdroid.command()
async def dogpic(ctx):
    image_url = 'https://some-random-api.ml/img/dog'
    img = requests.get(image_url).json()
    embed = discord.Embed(
        title="Here comes a cute doggo :smile:", colour=discord.Colour.orange())
    embed.set_image(url=img['link'])
    await ctx.send(embed=embed)


drunkdroid.run(os.environ['token'])
