import logging
import asyncio
import booru
from discord.ext import commands, tasks
from rule34Py import rule34Py
import PrivateInfo
import datetime
import random
import json
from booru import Konachan

exclude = [
    "female",
    "-male/male",
    "-gay",
    "-gore",
    "-vore",
    "-watersports",
    "-scat",
    "-horsecock",
    "-futanari",
    "-monsterification",
    "-identity_death",
    "-muscle_growth",
    "-transformation",
    "-breast_expansion",
    "-furry",
    "-lip_expansion",
    "-yiff",
    "-young",
    "-canine",
    "-scalie",
    "-reptile",
    "-pokemon",
    "-cyborg",
    "-leporid",
    "-diaper",
    "-toddler",
    "-baby",
    "-birth",
    "-pregnant",
    "-bbw",
    "-fart",
    "-my_little_pony",
    "-friendship_is_magic",
    "-hasbro",
    "-tentacle",
    "-smell",
    "-minecraft",
    "-abuse",
    "-roblox",
    "-inflation",
    "-eye_penetration",
    "-feral",
    "-giantess",
    "-hanged",
    "-autoerotic_asphyxiation",
    "-video",
    "-decapitation",
    "-ero_guro",
    "-necrophilia",
    "-asphyxiation",
    "-rape"]

exclude_vid = [
    "female",
    "animated",
    "-male/male",
    "-gay",
    "-gore",
    "-vore",
    "-watersports",
    "-scat",
    "-horsecock",
    "-futanari",
    "-monsterification",
    "-identity_death",
    "-muscle_growth",
    "-transformation",
    "-breast_expansion",
    "-furry",
    "-lip_expansion",
    "-yiff",
    "-young",
    "-canine",
    "-scalie",
    "-reptile",
    "-pokemon",
    "-cyborg",
    "-leporid",
    "-diaper",
    "-toddler",
    "-baby",
    "-birth",
    "-pregnant",
    "-bbw",
    "-fart",
    "-my_little_pony",
    "-friendship_is_magic",
    "-hasbro",
    "-tentacle",
    "-smell",
    "-minecraft",
    "-abuse",
    "-roblox",
    "-inflation",
    "-eye_penetration",
    "-feral",
    "-giantess",
    "-hanged",
    "-autoerotic_asphyxiation",
    "-large_filesize",
    "-extremely_large_filesize",
    "-very_high_resolution",
    "-decapitation",
    "-ero_guro",
    "-necrophilia",
    "-asphyxiation",
    "-rape"]

r34Py = rule34Py()
channel = PrivateInfo.nsfw_channel


class Nsfw(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @tasks.loop(minutes=10.0)
    async def rule34clock(self):
        channel1 = self.bot.get_channel(channel)
        result_random = r34Py.random_post(exclude)
        time = datetime.datetime.now()
        await channel1.send(result_random.image)
        logging.basicConfig(filename='taginfo.log', level=logging.INFO)
        logging.info(f'{time} {result_random.tags}')
        print(f"{time} {result_random.tags}")

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"bot is ready!\n")
        self.rule34clock.start()
        print(f"Nsfw is ready! \n")
        self.nsfwlitclock.start()

    # nsfw commands
    #   to search for a tag on rule 34
    @commands.command(brief="search a r34 tag", description="search a r34 tag excluding a list of tags")
    @commands.has_role(PrivateInfo.Nsfw_role)
    async def say(self, rhs, lookup):
        list1 = [lookup]
        list2 = exclude
        list3 = list1 + list2
        result_random = r34Py.random_post(list3)
        if rhs.channel.id == PrivateInfo.nsfw_channel:
            await rhs.send(result_random.image)
        else:
            await rhs.send(" wrong channel")

    # responds to errors when someone puts in a bad tags

    @say.error
    async def info_error(self, rhs, error):
        if isinstance(error, commands.CommandInvokeError):
            await rhs.send("the tag that you search is not available or you need to put _ in all of the empty " +
                           "spaces of you search tag ex: fire emblem will need to be fire_emblem.")

    # looks for video
    @commands.command(brief="search a r34 video", description="search a r34 vid excluding a list of tags")
    @commands.has_role(PrivateInfo.Nsfw_role)
    async def vid(self, vhs, lookup="female"):
        list1 = [lookup]
        list2 = exclude_vid
        list3 = list1 + list2
        result_random = r34Py.random_post(list3)
        if vhs.channel.id == PrivateInfo.nsfw_channel:
            await vhs.send(result_random.video)
        else:
            await vhs.send(" wrong channel")

    @tasks.loop(minutes=15)
    async def nsfwlitclock(self):
        kone = Konachan()
        img = await kone.search_image(query="breasts", block="loli", limit=500)
        new1 = img.replace('[', '')
        new2 = new1.replace(']', '')
        new3 = new2.replace('\"', '')
        final_list = list(new3.split(','))
        random_img = random.choice(final_list)
        channel_lit = self.bot.get_channel(PrivateInfo.nsfw_channel2)
        await channel_lit.send(random_img)

    # Vaporeon copy-pasta but you can replace the name height and weight with a different value

    @commands.command(brief="Vaporeon copy pasta", description="Vaporeon copy pasta you can change name height and "
                                                               "weight")
    async def breed(self, rsb, name="Vaporeon", hei="3”03’", wei="63.9"):
        await rsb.send(
            f"Hey guys, did you know that in terms of male human and female Pokémon breeding, {name} is the "
            f"most compatible Pokémon for humans? Not only are they in the field egg group, which is mostly "
            f"comprised of mammals, {name} are an average of {hei} tall and {wei}  pounds, this means they’re"
            f" large enough to be able handle human dicks, and with their impressive Base Stats for HP and "
            f"access to Acid Armor, you can be rough with one. Due to their mostly water based biology, "
            f"there’s no doubt in my mind that an aroused  {name} would be incredibly wet, so wet that you "
            f"could easily have sex with one for hours without getting sore. They can also learn the moves "
            f"Attract, Baby-Doll Eyes, Captivate, Charm, and Tail Whip, along with not having fur to hide "
            f"nipples, so it’d be incredibly easy for one to get you in the mood. With their abilities Water "
            f"Absorb and Hydration, they can easily recover from fatigue with enough water. No other Pokémon "
            f"comes close to this level of compatibility. Also, fun fact, if you pull out enough, you can make "
            f"your {name} turn white. {name} is literally built for human dick. Ungodly defense stat+high "
            f"HP pool+Acid Armor means it can take cock all day, all shapes and sizes and still come for more")

    # do up to a 3 tag search
    @commands.command(brief="Stop r34 autopost", description="Stop r34 autopost dont if issue happen")
    @commands.has_role(PrivateInfo.Admin_role)
    async def stopnsfw(self, srr):
        self.rule34clock.cancel()
        await srr.send("posting stopped!")

    @commands.command(brief="Start r34 autopost", description="Start r34 autopost dont if issue happen")
    @commands.has_role(PrivateInfo.Admin_role)
    async def startnsfw(self, srr):
        self.rule34clock.start()
        await srr.send("posting started!")

    @commands.command(brief="Pause r34 autopost", description="Pause r34 autopost dont if issue happen")
    @commands.has_role(PrivateInfo.Admin_role)
    async def pausensfw(self, srr):
        self.rule34clock.stop()
        await srr.send("posting paused!")

    @commands.command(brief="search 3 r34 tags", description="search 3 r34 tags with a excluded list")
    @commands.has_role(PrivateInfo.Nsfw_role)
    async def supersay(self, rss, lookup1="female", lookup2="breasts", lookup3="1girls"):
        list1 = [lookup1, lookup2, lookup3]
        list2 = exclude
        list3 = list1 + list2
        result_random = r34Py.random_post(list3)
        if rss.channel.id == PrivateInfo.nsfw_channel:
            await rss.send(result_random.image)
        else:
            await rss.send(" wrong channel")

    # responds to errors when someone puts in a bad tags

    @supersay.error
    async def info_error(self, rss, error):
        if isinstance(error, commands.CommandInvokeError):
            await rss.send("the tag that you search is not available or you need to put _ in all of the empty " +
                           "spaces of you search tag ex: fire emblem will need to be fire_emblem.")

    # start r34 autobot in case it stops
    @commands.command(brief="restart r34 autopost", description="restart r34 autopost dont if issue happen")
    @commands.has_role(PrivateInfo.Admin_role)
    async def restartnsfw(self, rrs):
        self.rule34clock.start()
        await rrs.send("task restarted.")

    # responds to errors when someone puts in a bad tags

    @vid.error
    async def info_error(self, vhs, error):
        if isinstance(error, commands.CommandInvokeError):
            await vhs.send("the tag that you search is not available or you need to put _ in all of the empty " +
                           "spaces of you search tag ex: fire emblem will need to be fire_emblem.")

    # random rule 34 search

    @commands.command(brief="Random r34 image", description="random r34 image only do able in r34 channel")
    @commands.has_role(PrivateInfo.Nsfw_role)
    async def r34(self, rhx):
        result_random = r34Py.random_post(exclude)
        if rhx.channel.id == PrivateInfo.nsfw_channel:
            await rhx.send(result_random.image)
        else:
            await rhx.send(" wrong channel")

    # send a random image to output in your Nsfw channel from rule 34

    # nsfw commands
    @commands.command(brief="Search tag for Konachan ", description="Search tag for Konachan.")
    @commands.has_role(PrivateInfo.Nsfw_role)
    async def ksearch(self, krs, lookup="breasts"):
        kone = Konachan()
        img = await kone.search_image(query=lookup, block="loli", limit=500)
        new1 = img.replace('[', '')
        new2 = new1.replace(']', '')
        new3 = new2.replace('\"', '')
        final_list = list(new3.split(','))
        random_img = random.choice(final_list)
        if krs.channel.id == PrivateInfo.nsfw_channel2:
            await krs.send(random_img)
        else:
            await krs.send(" wrong channel")


async def setup(bot):
    await bot.add_cog(Nsfw(bot))
