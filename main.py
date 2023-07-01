import os
import random
from discord.ext import commands, tasks
from rule34Py import rule34Py
import pyrandmeme
from pyrandmeme import *
import PrivateInfo
import json
import requests
from bs4 import BeautifulSoup
import asyncio

# turn intents.all into a variable intents are permissions that you need to check off on your discord dev page
intents = discord.Intents.all()
# the variable with the bot command symbol and the declared intents
bot = commands.Bot(command_prefix='*', intents=intents)


async def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')


async def main():
    await load()
    await bot.start(PrivateInfo.Token)


asyncio.run(main())
