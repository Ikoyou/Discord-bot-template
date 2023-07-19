import random

import discord
import pyrandmeme
from discord.ext import commands, tasks
from pyrandmeme import *
import PrivateInfo
import CursedUwU
import booru


class Common(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # @tasks.loop(minutes=30)
    # async def meme_clock(self):
    #     try:
    #         channel = self.bot.get_channel(PrivateInfo.meme_channel)
    #         await channel.send(embed=await pyrandmeme())
    #     except IndexError:
    #         channel = self.bot.get_channel(PrivateInfo.meme_channel)
    #         await channel.send(f"sowwy we thewe was a fucky wucky pwease stowp awnd stawt the meme-posting. "
    #                            f"uwu cawn duwu thiws by using the stopmeme awnd startmeme commands.")

    @commands.command(brief="This is to stop the auto meme posting", description="This is to stop the auto "
                                                                                 "meme posting")
    async def stopmeme(self, srr):
        self.meme_clock.cancel()
        await srr.send("posting stopped!")

    @commands.command(brief="This is to start the auto meme posting", description="This is to start the auto meme "
                                                                                  "posting")
    async def startmeme(self, srr):
        self.meme_clock.start()
        await srr.send("posting started!")

    @commands.command(brief="This is to pause the auto meme posting", description="This is to pause the auto meme")
    async def pausememe(self, srr):
        self.meme_clock.stop()
        await srr.send("posting paused!")

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"bot is ready!\n")
        print("common is ready!\n")
        self.meme_clock.start()

    @commands.command(brief="Test command", description="Test command")
    async def hello(self, ctx):
        await ctx.send(f"Hello it is working now")

    @commands.command(brief="Rules for the Nsfw commands", description="Rules for the Nsfw commands")
    async def nsfw_rules(self, rul):
        await rul.send(f"if you want to do a search you need to type * and say together followed by a space then your "
                       f"search tag, if you search tag has more than one word in it you need to put _ in the emtpy "
                       f"spaces otherwise it will only search the first word. ex: fire emblem would be fire_emblem "
                       f"as a tag.")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send(f"incorrect command!")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        if "uwu" in message.content and "*" not in message.content:
            user_message = str(message.content)
            cursed = CursedUwU.english_to_uwu_converter(user_message)
            channel = message.channel
            cursed = cursed.replace("uwu", "")
            print(cursed)
            await channel.send(cursed)

    @commands.command(brief="Flip a coin", description=" Get a heads or tails")
    async def coinflip(self, cin):
        coin = random.randint(1, 2)
        emojitails = self.bot.get_emoji(1120774674813558896)
        emojiheads = self.bot.get_emoji(1120773115912405132)
        if coin == 1:
            await cin.send(f"Heads {str(emojiheads)}")
        else:
            await cin.send(f"Tails {str(emojitails)}")

    @commands.command(brief="roll dice", description="Roll dice and you cand add a number to replace the max")
    async def roll(self, drc, num=6):
        dice = random.randint(1, int(num))
        await drc.send(f"You Rolled: {str(dice)}")

    @commands.command(brief="Roll two dice", description="Roll two dice and you cand add a number to replace the max")
    async def doubleroll(self, ddr, num=6):
        dice1 = random.randint(1, int(num))
        dice2 = random.randint(1, int(num))
        if dice1 == dice2:
            await ddr.send(f"Double! You Rolled: {str(dice1)} And {str(dice2)}")
        else:
            await ddr.send(f"You Rolled: {str(dice1)} And {str(dice2)}")

    @commands.command(brief="Butthurt form", description="Give a image of the butthurt form")
    async def butthurt(self, mbh):
        await mbh.send("https://cdn.discordapp.com/attachments/95213694820028416/1121467811349413988/image0.png")

    @commands.command(brief="call up memes in a specfic channel", description="call up memes in a specfic channel")
    async def meme(self, mme):
        if mme.channel.id == PrivateInfo.meme_channel:
            await mme.send(embed=await pyrandmeme())
        else:
            await mme.send(" wrong channel")

    @commands.command(brief="sparten navy seal copy pasta", description="sparten navy seal copy pasta")
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

    @commands.command(brief="Personal help command", description="Custom help command")
    async def help_commands(self, ctx):
        helptext = "```"
        for command in self.bot.commands:
            helptext += f"{command}\n"
        helptext += "```"
        await ctx.send(f"if you want to use any of the commands need to type * and then the command that you want to "
                       f"use, some commands can be used to search so if you want to do that then you need to add a "
                       f"space then you can add your search tag, if you search tag has more than one word in it you "
                       f"need to put _ in the emtpy spaces otherwise it will only search the first word. ex: fire  "
                       f"emblem would be fire_emblem as a tag. Below is a List of our commands: \n{helptext}")


async def setup(bot):
    await bot.add_cog(Common(bot))
