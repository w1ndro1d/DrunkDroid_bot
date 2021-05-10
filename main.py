import os
import discord
from aiohttp import request
from discord import Embed

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
  image_url='https://some-random-api.ml/img/dog'

  async with request("GET",image_url) as response:
    if response.status==200:
      data=await response.json()
      image_link=data['link']
    else:
      image_link=None

  async with request("GET",fact_url) as response:
    if response.status==200:
      data=await response.json()
      embed=Embed(title="Random doggo fact",description=data['fact'],colour=ctx.author.colour)
      if(image_link is not None):
        embed.set_image(url=image_link)
      await ctx.send(embed)
    else:
      await ctx.send(f'The API returned a {response.status} status.')




drunkdroid.run(os.environ['token'])
