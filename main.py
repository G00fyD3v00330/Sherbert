import os

os.system('pip install nextcord')
## installing thing because fuck replit download thing

import nextcord
import json
import typing
discord = nextcord
from nextcord.ext import commands
from nextcord.utils import get

intents = nextcord.Intents.default()
intents.message_content = True
import random
from googletrans import Translator
import asyncio

t = Translator()


def generateUwU(input_text):
  length = len(input_text)
  output_text = ''
  for i in range(length):
    current_char = input_text[i]
    previous_char = '&# 092;&# 048;'
    if i > 0:
      previous_char = input_text[i - 1]
    if current_char == 'L' or current_char == 'R':
      output_text += 'W'
    elif current_char == 'l' or current_char == 'r':
      output_text += 'w'
    elif current_char == 'O' or current_char == 'o':
      if previous_char == 'N' or previous_char == 'n' or previous_char == 'M' or previous_char == 'm':
        output_text += "yo"
      else:
        output_text += current_char
    else:
      output_text += current_char
  return output_text


activity = nextcord.Game('with your kidney')

from flask import Flask
from threading import Thread

app = Flask("")


@app.route("/")
def index():
  return "<h1>Bot is running</h1>"


Thread(target=app.run, args=("0.0.0.0", 8080)).start()

## bot appears
client = commands.Bot(intents=intents,
                      activity=activity,
                      owner_id=941785334667169842,
                      command_prefix='>')
## reading settings (only IDs, other programs will prob request things themselves)
ReactingCh = None
SendingCh = None
with open('SettingsAndThings.json', 'r') as settings:
  realdata = json.load(settings)
  for i in realdata:
    if i == "EmojiChannel":
      ReactingCh = i
    if i == "StarboardCh":
      SendingCh = i


@client.event
async def on_ready():
  print('Bot activated')


staremoji = "⭐"


@client.event
async def on_raw_reaction_add(payload):
  if payload.channel_id == ReactingCh:
    if payload.emoji.name == staremoji:
      channel = client.get_channel(payload.channel_id)
      message = await channel.fetch_message(payload.message_id)
      reaction = get(message.reactions, emoji=payload.emoji.name)
      if reaction and reaction.count > 1:
        ctx = client.get_channel(SendingCh)
        msg = message
        embedsContent = []
        if msg.attachments:
          for i in msg.attachments:
            file = await i.to_file()
            list.append(embedsContent, file)
        if embedsContent == []:
          await ctx.send(f'{msg.author}:{msg.content}')
        else:
          await ctx.send(f'{msg.author}:{msg.content}', files=embedsContent)


@client.event
async def on_message(message):
  if message.content.startswith('ok' or 'Ok' or 'OK'):
    await message.add_reaction('🥵')
  elif message.content.startswith('rug dog'):
    await message.add_reaction('<:rugdog:1097010090436989060>')
  elif message.content.startswith('oh no'):
    await message.add_reaction('<:ohno:1097009850506031254>')
  elif message.content.startswith('Sherbert DEBUG!'):
    await message.add_reaction(staremoji)


@client.slash_command(description='only for gods')
async def say(ctx, arg):
  if ctx.user.id == 941785334667169842 or 919466550040330351:
    await ctx.send(arg)
  else:
    await ctx.send('access denied.')


@client.slash_command(description='get banned')
async def fakeban(ctx, user: discord.Member = None, reason=None):
  if user == None:
    user = ctx.user
  elif reason == None:
    reason = 'No Reason'
  elif user == None and reason == None:
    reason = 'No Reason'
    user = ctx.user
  embed = discord.Embed(title=f"{user} got banned!",
                        description="haha yes",
                        color=0xff0000)
  embed.set_author(name=ctx.user)
  embed.set_thumbnail(
    url=
    "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fdoy2mn9upadnk.cloudfront.net%2Fuploads%2Fdefault%2Foptimized%2F4X%2Fa%2F6%2Fc%2Fa6cfbd21ce606aacca5d1e0956a78f527cdc7f57_2_1000x1000.png&f=1&nofb=1"
  )
  embed.add_field(name="Information",
                  value=f"*ID:{user.id}* || __***Reason: {reason}***__",
                  inline=True)
  embed.set_footer(text="that's fake ban jk")
  await ctx.send(embed=embed)


@client.slash_command(description='why i created this? i dont know')
async def dice(ctx):
  await ctx.send(f'dice says: {random.randint(1, 6)}')


@client.slash_command(description='tbh useless feature')
async def uwutranslate(ctx, text=None):
  if text == None:
    await ctx.send(generateUwU('hey, you need to write text first'))
  else:
    await ctx.send(generateUwU(text))


@client.slash_command(description='tbh useless feature')
async def hack(ctx,
               user: discord.Member = None,
               localIP="153.23.34.321",
               localhacksettings="-s"):
  if user == None:
    await ctx.send("ayo dude, write user first, goofy")
  else:
    msg = await ctx.send(
      f'Welcome to the Sherbert Hacking Program. Hacking Settings: {localhacksettings}'
    )
    await asyncio.sleep(1)
    await msg.edit(f"Chosen Target: {user}. Hack starts in next 1 second")
    await asyncio.sleep(1)
    await msg.edit(f"Connecting to the VM - {localIP}. . .")
    await asyncio.sleep(1)
    await msg.edit("Scanning for the open ports...")
    await asyncio.sleep(1)
    await msg.edit("Open ports has been detected - 22, 21, 25. Cracking in...")
    await asyncio.sleep(1)
    await msg.edit("Loading passwords...")
    await asyncio.sleep(1)
    possiblepass = {
      'IEatKids', "ISleep", "Sherbert", "password", "123412341234"
    }
    await msg.edit(
      f"Passwords found! Discord_Password: {possiblepass[random.randint(0, 5)]}"
    )
    await asyncio.sleep(1)
    await msg.edit(f"All passwords info has been sent to {ctx.user}")
    await asyncio.sleep(1)
    await msg.edit(
      "Scanning for strange files... ``(Search_Settings: SearchingFor: {kids, kids, kids})``"
    )
    await asyncio.sleep(1)
    await msg.edit("194,503 strange files found. Reporting  FBI")
    await asyncio.sleep(1)
    if localhacksettings == "-sherbert":
      await asyncio.sleep(1)
      await msg.edit(
        "Sherbert setting detected. Uploading 100,303,205,303 pictures of sherbert (EST WEIGHT OF FILES: 2,5 TB)..."
      )
      await asyncio.sleep(2)
      await msg.edit("Upload complete.")
      await asyncio.sleep(1)
    await msg.edit("Selling information to the government...")
    await asyncio.sleep(2)
    await msg.edit("Disconnecting...")
    await asyncio.sleep(1)
    await msg.edit(f"{user} has been hacked successfully!")


# Settings for Starboard Feature


@client.slash_command(description='Sets channel for reacts for StarBoard Feature (owner only)')
async def setreactchannel(ctx, channel: discord.TextChannel = None):
  if ctx.author.id == 941785334667169842:
    if channel == None:
      await ctx.send('dude this channel does not exist bruh')
    else:
      with open('SettingsAndThings.json') as settingFile:
        loadData = json.load(settingFile)
        for i in loadData:
          if i == "EmojiChannel":
            i = channel.id
            break
        json.dump(settingFile, loadData)
  else:
    await ctx.send('You are not my father')

@client.slash_command(description='Sets channel for StarBoard Feature (owner only)')
async def setstarboard(ctx, channel: discord.TextChannel = None):
  if ctx.author.id == 941785334667169842:
    if channel == None:
      await ctx.send('dude this channel does not exist bruh')
    else:
      with open('SettingsAndThings.json') as settingFile:
        loadData = json.load(settingFile)
        for i in loadData:
          if i == "StarboardCh":
            i = channel.id
            break
        json.dump(settingFile, loadData)
  else:
    await ctx.send('You are not my father')

# end of settings for starboard

token = os.environ.get("DISCORD_TOKEN")
client.run(token)
