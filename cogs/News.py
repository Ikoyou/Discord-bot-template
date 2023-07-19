import requests
from requests_cache import CachedSession
import PrivateInfo
from discord.ext import commands, tasks
import asyncio


class News(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"bot is ready!\n")
        print("News is ready!\n")
        self.news_clock.start()
        self.tech_news_clock.start()

    @commands.command(brief="Get top headline from BBC", description="Get top headline from BBC")
    async def get_news(self, ctx):
        Url = f'https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey={PrivateInfo.News_API_Key}'
        session = CachedSession(
            cache_name='./Newscache/lastchecked',
            expire_after=600
        )
        rep = session.get(Url)
        try:
            json_data = rep.json()
            await ctx.send(f"World Top Headlines: \n"
                           f"{json_data['articles'][0]['title']}\n"
                           f"{json_data['articles'][0]['url']}\n"
                           f"{json_data['articles'][0]['description']}\n \n")
            await ctx.send(f"{json_data['articles'][1]['title']}\n"
                           f"{json_data['articles'][1]['url']}\n"
                           f"{json_data['articles'][1]['description']}\n \n")
            await ctx.send(f"{json_data['articles'][2]['title']}\n"
                           f"{json_data['articles'][2]['url']}\n"
                           f"{json_data['articles'][2]['description']}\n \n")
            await ctx.send(f"{json_data['articles'][3]['title']}\n"
                           f"{json_data['articles'][3]['url']}\n"
                           f"{json_data['articles'][3]['description']}\n \n")
            await ctx.send(f"{json_data['articles'][4]['title']}\n"
                           f"{json_data['articles'][4]['url']}\n"
                           f"{json_data['articles'][4]['description']}\n \n")
        except:
            print("no info")

    @tasks.loop(hours=12)
    async def news_clock(self):
        url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={PrivateInfo.News_API_Key}'

        rep = requests.get(url)
        try:
            channel = self.bot.get_channel(PrivateInfo.News_channel)
            json_data = rep.json()
            await channel.send(f"World Top Headlines: \n"
                               f"{json_data['articles'][0]['title']}\n"
                               f"{json_data['articles'][0]['url']}\n"
                               f"{json_data['articles'][0]['description']}\n \n")
            await channel.send(f"{json_data['articles'][1]['title']}\n"
                               f"{json_data['articles'][1]['url']}\n"
                               f"{json_data['articles'][1]['description']}\n \n")
            await channel.send(f"{json_data['articles'][2]['title']}\n"
                               f"{json_data['articles'][2]['url']}\n"
                               f"{json_data['articles'][2]['description']}\n \n")
            await channel.send(f"{json_data['articles'][3]['title']}\n"
                               f"{json_data['articles'][3]['url']}\n"
                               f"{json_data['articles'][3]['description']}\n \n")
            await channel.send(f"{json_data['articles'][4]['title']}\n"
                               f"{json_data['articles'][4]['url']}\n"
                               f"{json_data['articles'][4]['description']}\n \n")
        except:
            print("no info")

    @tasks.loop(hours=8)
    async def tech_news_clock(self):
        await asyncio.sleep(10)
        url = f'https://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey={PrivateInfo.News_API_Key}'
        rep = requests.get(url)
        try:
            channel = self.bot.get_channel(PrivateInfo.News_channel)
            json_data = rep.json()
            await channel.send(f"Tech Top Headlines: \n"
                               f"{json_data['articles'][0]['title']}\n"
                               f"{json_data['articles'][0]['url']}\n"
                               f"{json_data['articles'][0]['description']}\n \n")
            await channel.send(f"{json_data['articles'][1]['title']}\n"
                               f"{json_data['articles'][1]['url']}\n"
                               f"{json_data['articles'][1]['description']}\n \n")
            await channel.send(f"{json_data['articles'][2]['title']}\n"
                               f"{json_data['articles'][2]['url']}\n"
                               f"{json_data['articles'][2]['description']}\n \n")
            await channel.send(f"{json_data['articles'][3]['title']}\n"
                               f"{json_data['articles'][3]['url']}\n"
                               f"{json_data['articles'][3]['description']}\n \n")
            await channel.send(f"{json_data['articles'][4]['title']}\n"
                               f"{json_data['articles'][4]['url']}\n"
                               f"{json_data['articles'][4]['description']}\n \n")
        except:
            print("no info")


async def setup(bot):
    await bot.add_cog(News(bot))
