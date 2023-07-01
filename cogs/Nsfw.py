from discord.ext import commands, tasks
from rule34Py import rule34Py
import PrivateInfo

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
    "-video"]

r34Py = rule34Py()
channel = PrivateInfo.nsfw_channel


class Nsfw(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @tasks.loop(minutes=10.0)
    async def rule34clock(self):
        channel1 = self.bot.get_channel(channel)
        result_random = r34Py.random_post(exclude)
        await channel1.send(result_random.image)

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"bot is ready!\n")
        self.rule34clock.start()
        print(f"Nsfw is ready! \n")

    # nsfw commands
    #   to search for a tag on rule 34
    @commands.command()
    async def say(self, rhs, lookup):
        list1 = [lookup]
        list2 = exclude
        list3 = list1 + list2
        result_random = r34Py.random_post(list3)
        await rhs.send(result_random.image)

    # responds to errors when someone puts in a bad tags

    @say.error
    async def info_error(self, rhs, error):
        if isinstance(error, commands.CommandInvokeError):
            await rhs.send("the tag that you search is not available or you need to put _ in all of the empty " +
                           "spaces of you search tag ex: fire emblem will need to be fire_emblem.")

    # looks for video
    @commands.command()
    async def vid(self, vhs, lookup):
        list1 = [lookup]
        list2 = exclude
        list3 = list1 + list2
        result_random = r34Py.random_post(list3)
        await vhs.send(result_random.video)

    # Vaporeon copy-pasta but you can replace the name height and weight with a different value

    @commands.command()
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

    @commands.command()
    async def supersay(self, rss, lookup1="female", lookup2="breasts", lookup3="1girls"):
        list1 = [lookup1, lookup2, lookup3]
        list2 = exclude
        list3 = list1 + list2
        result_random = r34Py.random_post(list3)
        await rss.send(result_random.image)

    # responds to errors when someone puts in a bad tags

    @supersay.error
    async def info_error(self, rss, error):
        if isinstance(error, commands.CommandInvokeError):
            await rss.send("the tag that you search is not available or you need to put _ in all of the empty " +
                           "spaces of you search tag ex: fire emblem will need to be fire_emblem.")

    # start r34 autobot in case it stops
    @commands.command()
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

    @commands.command()
    async def r34(self, rhx):
        result_random = r34Py.random_post(exclude)
        await rhx.send(result_random.image)

    # send a random image to output in your Nsfw channel from rule 34

    # nsfw commands


async def setup(bot):
    await bot.add_cog(Nsfw(bot))
