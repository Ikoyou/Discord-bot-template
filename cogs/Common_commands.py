import random
import pyrandmeme
import requests
from bs4 import BeautifulSoup
from discord.ext import commands, tasks
from pyrandmeme import *
import PrivateInfo


class Common(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @tasks.loop(minutes=30)
    async def meme_clock(self):
        try:
            channel = self.bot.get_channel(PrivateInfo.meme_channel)
            await channel.send(embed=await pyrandmeme())
        except IndexError:
            channel = self.bot.get_channel(PrivateInfo.meme_channel)
            await channel.send("UWU We made a fucky Wucky!")
            self.meme_clock.start()

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"bot is ready!\n")
        print("common is ready!\n")
        self.meme_clock.start()

    @commands.command()
    async def hello(self, ctx):
        await ctx.send(f"hello it is working now")

    @commands.command()
    async def rules(self, rul):
        await rul.send(f"if you want to do a search you need to type * and say together followed by a space then your "
                       f"search tag, if you search tag has more than one word in it you need to put _ in the emtpy "
                       f"spaces otherwise it will only search the first word. ex: fire emblem would be fire_emblem "
                       f"as a tag.")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send(f"incorrect command!")

    @commands.command()
    async def coinflip(self, cin):
        coin = random.randint(1, 2)
        emojitails = self.bot.get_emoji(0)  # put your own emoji ID here
        emojiheads = self.bot.get_emoji(0)  # put your own emoji ID here
        if coin == 1:
            await cin.send(f"Heads {str(emojiheads)}")
        else:
            await cin.send(f"Tails {str(emojitails)}")

    @commands.command()
    async def roll(self, drc, num=6):
        dice = random.randint(1, int(num))
        await drc.send(f"You Rolled: {str(dice)}")

    @commands.command()
    async def doubleroll(self, ddr, num=6):
        dice1 = random.randint(1, int(num))
        dice2 = random.randint(1, int(num))
        if dice1 == dice2:
            await ddr.send(f"Double! You Rolled: {str(dice1)} And {str(dice2)}")
        else:
            await ddr.send(f"You Rolled: {str(dice1)} And {str(dice2)}")

    @commands.command()
    async def weather(self, wwc, x="new york"):
        location = f"Weather in {x} now"
        url = f"https://www.google.com/search?q={location}"

        req = requests.get(url)
        soup = BeautifulSoup(req.text, "html.parser")

        current_weather = soup.find("div", class_="BNeawe").text

        await wwc.send(f"Your weather: {current_weather}")

    @commands.command()
    async def butthurt(self, mbh):
        await mbh.send("https://imgur.com/gallery/q9rABvt")

    @commands.command()
    async def meme(self, mme):
        await mme.send(embed=await pyrandmeme())

    @commands.command()
    async def bitch(self, mbi):
        await mbi.send("What the fuck did you just fucking say about me, you little bitch? I'll have you know "
                       "I graduated top of my class in the Spartan Forces, and I've been involved in numerous "
                       "secret raids on Covenant forces, and I have over 300 confirmed Brute Chieftain "
                       "assassinations. I am trained in gorilla warfare and I'm the top sniper in the entire "
                       "UNSC Special Forces. You are nothing to me but just another target. I will wipe you "
                       "the fuck out with precision the likes of which has never been seen before in this sector,"
                       " mark my fucking words. You think you can get away with saying that shit to me over "
                       "Battlenet? Think again, fucker. As we speak I am contacting my secret network of ONI spies "
                       "across space and your location is being traced right now so you better prepare for the storm, "
                       "maggot. The storm that wipes out the pathetic little thing you call your life. You're fucking "
                       "dead, split-chin. I can be anywhere, anytime, and I can kill you in over seven hundred ways, "
                       "and that's just with my bare hands. Not only am I extensively trained in unarmed combat, "
                       "but I have access to the entire arsenal of the United Nations Space Corps and I will use it "
                       "to its full extent to wipe your miserable ass out of this universe, you squid-head. "
                       "If only you could have known what unholy retribution your little clever comment "
                       "was about to bring down upon you, maybe you would have held your jaw. But you couldn't, "
                       "you didn't, and now you're paying the price, you goddamn split-lip. I will rain lead all over "
                       "you and you will drown in it. You're fucking dead, hinge-head.")

    @tasks.loop(minutes=30)
    async def meme_clock(self):
        try:
            channel = self.bot.get_channel(PrivateInfo.meme_channel)
            await channel.send(embed=await pyrandmeme())
        except IndexError:
            channel = self.bot.get_channel(PrivateInfo.meme_channel)
            await channel.send("UWU We made a fucky Wucky!")
            self.meme_clock.start()


async def setup(bot):
    await bot.add_cog(Common(bot))
