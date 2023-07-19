import json
import random

from discord.ext import commands


class Food(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"bot is ready!\n")
        print(f"Food is ready! \n")

    @commands.command(brief="Gives a random recipe", description="Gives a random recipe out of 1600+ chooses")
    async def recipe(self, rrr):
        with open('recipes.json') as raw_data:
            load_data = raw_data.read()
            new_data = json.loads(str(load_data))
            random_data = random.choice(new_data)
            await rrr.send(f"Name: {random_data['Name']}\nurl: {random_data['url']}"
                           f"\nIngredients: {str(random_data['Ingredients'])}"
                           f"\nInstructions: {str(random_data['Method'])}")
            raw_data.close()

    @commands.command(brief="Pick a random food", description="Pick a random food from a list of food")
    async def food(self, frr):
        fileobj = open("food.txt")
        lines = []
        for line in fileobj:
            lines.append(line.strip())
        food_choose = random.choice(lines)
        await frr.send("You may like: " + str(food_choose))
        fileobj.close()


async def setup(bot):
    await bot.add_cog(Food(bot))
