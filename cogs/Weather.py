import datetime as dt
import requests
from bs4 import BeautifulSoup
from discord.ext import commands

import PrivateInfo


def kel_to_cel(kelvin):
    cel = kelvin - 273.15
    return cel


def meters_per_second_to_miles_per_hour(mps):
    mph = mps * 2.237
    return mph


def kel_to_far(kelvin):
    far = (kelvin - 273.15) * (9 / 5) + 32
    return far


class Weather(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"bot is ready!\n")
        print("Weather is ready!\n")

    @commands.command(brief="Google weather search", description="search google for the weather of the location you "
                                                                 "want")
    async def gweather(self, gwc, x="new york"):
        location = f"Weather in {x} now"
        url = f"https://www.google.com/search?q={location}"
        req = requests.get(url)
        soup = BeautifulSoup(req.text, "html.parser")
        current_weather = soup.find("div", class_="BNeawe").text
        await gwc.send(f"Your weather: {current_weather}")

    @commands.command(brief="Open weather search", description="search open weather for detail info")
    async def weather(self, wwc, x="new york"):
        base_url = "https://api.openweathermap.org/data/2.5/weather?appid="
        key = PrivateInfo.Weather_token
        url = f"{base_url}{key}&q={x}"
        respond = requests.get(url).json()
        kel = respond['main']['temp']
        far = kel_to_far(kel)
        cel = kel_to_cel(kel)
        feels_like = respond['main']['feels_like']
        feels_like_far = kel_to_far(feels_like)
        feels_like_cel = kel_to_cel(feels_like)
        humidity = respond['main']['humidity']
        description = respond['weather'][0]['description']
        time_rise = dt.datetime.utcfromtimestamp(respond['sys']['sunrise'] + respond['timezone'])
        time_set = dt.datetime.utcfromtimestamp(respond['sys']['sunset'] + respond['timezone'])
        wind_speed = meters_per_second_to_miles_per_hour(respond['wind']['speed'])
        await wwc.send(f"Temp in {x} is: {far: .2f}F or {cel: .2f}C \n It feels like: {feels_like_far: .2f}F or "
                       f"{feels_like_cel: .2f}C\n"
                       f"The humidity is: {humidity}%\n The wind speed: {wind_speed:.2f}Mph \n "
                       f"The Status is: {description}\n"
                       f"Sunrise and sunset: {time_rise} rise and {time_set} set\n")


async def setup(bot):
    await bot.add_cog(Weather(bot))
