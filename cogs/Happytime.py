import asyncio
import requests
from discord.ext import commands, tasks
import PrivateInfo


class Happy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"bot is ready!\n")
        print("Happytimes is ready!\n")
        self.catoclock.start()
        self.dogoclock.start()
        self.quoteoclock.start()

    @commands.command(brief="random cat image", description="get a random cat image from api")
    async def get_cat(self, gci):
        url = f"https://api.thecatapi.com/v1/images/search?api_key={PrivateInfo.Cat_and_Dog_API}"
        r = requests.get(url)
        json_data = r.json()
        await gci.send(json_data[0]['url'])

    @commands.command(brief="random dog image", description="get a random dog image from api")
    async def get_dog(self, gdi):
        url = f"https://api.thedogapi.com/v1/images/search?api_key={PrivateInfo.Cat_and_Dog_API}"
        r = requests.get(url)
        json_data = r.json()
        await gdi.send(json_data[0]['url'])

    @commands.command(brief="random motivational quote", description="get a random quote from a api")
    async def get_quote(self, ggq):
        url = "https://zenquotes.io/api/quotes/"
        r = requests.get(url)
        json_data = r.json()
        await ggq.send(f"\U00002B50Quote\U00002B50:\n"
                       f"\"{json_data[0]['q']}\"\n"
                       f"by {json_data[0]['a']}\n")

    @commands.command(brief="stop cat post", description="stops the cat pic posting if there is a issue")
    @commands.has_role(PrivateInfo.Admin_role)
    async def stop_cat(self, sci):
        self.catoclock.stop()
        await sci.send("cat posting stopped")

    @commands.command(brief="stop dog post", description="stops the dog pic posting if there is a issue")
    @commands.has_role(PrivateInfo.Admin_role)
    async def stop_dog(self, sdi):
        self.dogoclock.stop()
        await sdi.send("dog posting stopped")

    @commands.command(brief="stop quote post", description="stops the quote posting if there is a issue")
    @commands.has_role(PrivateInfo.Admin_role)
    async def stop_quote(self, sqi):
        self.catoclock.stop()
        await sqi.send("quote posting stopped")

    @commands.command(brief="start cat post", description="starts the cat pic posting if there is a issue")
    @commands.has_role(PrivateInfo.Admin_role)
    async def start_cat(self, sci):
        self.catoclock.start()
        await sci.send("cat posting started")

    @commands.command(brief="start dog post", description="starts the dog pic posting if there is a issue")
    @commands.has_role(PrivateInfo.Admin_role)
    async def start_dog(self, sdi):
        self.dogoclock.start()
        await sdi.send("dog posting started")

    @commands.command(brief="start quote post", description="starts the quote posting if there is a issue")
    @commands.has_role(PrivateInfo.Admin_role)
    async def start_quote(self, sdi):
        self.quoteoclock.start()
        await sdi.send("quote posting started")

    @tasks.loop(minutes=30)
    async def dogoclock(self):
        url = f"https://api.thedogapi.com/v1/images/search?api_key={PrivateInfo.Cat_and_Dog_API}"
        r = requests.get(url)
        try:
            json_data = r.json()
            channel = self.bot.get_channel(PrivateInfo.Happy_channel)
            await channel.send(json_data[0]['url'])
        except:
            print("no info")

    @tasks.loop(minutes=30)
    async def catoclock(self):
        await asyncio.sleep(10)
        url = f"https://api.thecatapi.com/v1/images/search?api_key={PrivateInfo.Cat_and_Dog_API}"
        r = requests.get(url)
        try:
            json_data = r.json()
            channel = self.bot.get_channel(PrivateInfo.Happy_channel)
            await channel.send(json_data[0]['url'])
        except:
            print("no info")

    @tasks.loop(hours=12)
    async def quoteoclock(self):
        url = f"https://zenquotes.io/api/quotes/"
        r = requests.get(url)
        try:
            json_data = r.json()
            channel = self.bot.get_channel(PrivateInfo.Happy_channel)
            await channel.send(f"\U00002B50Quote\U00002B50:\n"
                               f"\"{json_data[0]['q']}\"\n"
                               f"by {json_data[0]['a']}\n")
        except:
            print("no info")


async def setup(bot):
    await bot.add_cog(Happy(bot))
