import random
from discord.ext import commands

corelist1 = ["crunches ", "side crunches ", "sec plank "]
corelist2 = ["each side russian twists", "sec hollow hold", "Glut bridges", "mountain climbers"]
corelist3 = ["V sits", "side planks", "Hollow rock"]

leglist1 = ["calf raises", "sec mountain climbers", "sec Wall sit"]
leglist2 = ["squats", "lunges", "Leg raises"]
leglist3 = ["Dumbbell squats", "Dumbbell lunges", "Dumbbell Side lunge"]

armslist1 = ["sec planks", "shoulder shrugs"]
armslist2 = ["curls", "overhead press", "rows"]
armslist3 = ["raises", "lateral raises", "push ups"]

cardiolist1 = ["sec of jog in place", "jumping jacks", "sec of side steps"]
cardiolist2 = ["sec mountain climbers", "sec flutter kicks", " secs of high knees"]
cardiolist3 = ["sec Side mountain climbers", "jump squats", "Burpee"]


class Fittness(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # excise fittness commands

    # the commands for the bot to output out a random workout set
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"bot is ready!\n")
        print(f"fitness is ready! \n")

    @commands.command()
    async def core(self, exc):
        core1 = random.choice(corelist1)  # chooses a random work from a list
        core2 = random.choice(corelist2)  # chooses a random work from a list
        core3 = random.choice(corelist3)  # chooses a random work from a list
        coreset1 = random.randint(40, 50)  # chooses a random number
        coreset2 = random.randint(15, 25)  # chooses a random number
        coreset3 = random.randint(10, 15)  # chooses a random number
        await exc.send(
            str(coreset1) + " " + core1 + ", " + str(coreset2) + " " + core2 + ", " + str(coreset3) + " " + core3)

    # Above is the making of the workout sentence you most turn number into string using the str() command

    @commands.command()
    async def leg(self, exl):
        legs1 = random.choice(leglist1)
        legs2 = random.choice(leglist2)
        legs3 = random.choice(leglist3)
        legset1 = random.randint(25, 30)
        legset2 = random.randint(10, 15)
        legset3 = random.randint(5, 10)
        await exl.send(
            str(legset1) + " " + legs1 + ", " + str(legset2) + " " + legs2 + ", " + str(legset3) + " " + legs3)

    @commands.command()
    async def arm(self, exa):
        arms1 = random.choice(armslist1)
        arms2 = random.choice(armslist2)
        arms3 = random.choice(armslist3)
        armset1 = random.randint(20, 25)
        armset2 = random.randint(10, 15)
        armset3 = random.randint(5, 10)
        await exa.send(
            str(armset1) + " " + arms1 + ", " + str(armset2) + " " + arms2 + ", " + str(armset3) + " " + arms3)

    @commands.command()
    async def cardio(self, exc):
        cardio1 = random.choice(cardiolist1)
        cardio2 = random.choice(cardiolist2)
        cardio3 = random.choice(cardiolist3)
        cardioset1 = random.randint(40, 50)
        cardioset2 = random.randint(15, 25)
        cardioset3 = random.randint(10, 15)
        await exc.send(
            str(cardioset1) + " " + cardio1 + ", " + str(cardioset2) + " " + cardio2 + ", " + str(cardioset3) + " " +
            cardio3)

    # excise fittness commands


async def setup(bot):
    await bot.add_cog(Fittness(bot))
