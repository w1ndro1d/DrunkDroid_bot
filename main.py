import os
import discord
from aiohttp import request
from discord import Embed
import requests

from discord.ext import commands
from discord.ext.commands import Bot

drunkdroid = commands.Bot(command_prefix='.')

@drunkdroid.event
async def on_member_join(member,message):
    await member.create_dm()
    await member.dm_channel.send(f'Hi {member.name}, hehe boiiiii')
    await message.channel.send(f'{member} has chosen the life of a Pidit. Very wise decision!')


@drunkdroid.event
async def on_member_remove(member,message):
  await member.create_dm()
  await member.dm_channel.send(f"{member.name}, you left? Well, being a pidit isn't everyone's cup of tea. But once you become a pidit, its a way of life. Don't forget that!")
  await message.channel.send(f'{member} has sadly left the server. We will miss you :/ JK :P')


@drunkdroid.event
async def on_ready():
    print('Logged in as')
    print(drunkdroid.user.name)
    print(drunkdroid.user.id)
    print('------')
    await drunkdroid.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Pidits suffer"))


@drunkdroid.command()
async def ddping(ctx):
  await ctx.send(f'{round(drunkdroid.latency*1000)}ms')


@drunkdroid.command()
async def dogfact(ctx):
  fact_url='https://some-random-api.ml/facts/dog'
  f = requests.get(fact_url).json()
  desc = f['fact']
  embed = discord.Embed(title="Here you go :)", colour=discord.Colour.orange())
  embed.add_field(name="Doggo Fact", value = str(desc))
  await ctx.send(embed=embed)

@drunkdroid.command()
async def dogpic(ctx):
  image_url='https://some-random-api.ml/img/dog'
  img= requests.get(image_url).json()
  embed = discord.Embed(title="Here comes a cute doggo :)", colour=discord.Colour.orange())
  embed.set_image(url=img['link'])
  await ctx.send(embed=embed)



drunkdroid.run(os.environ['token'])
