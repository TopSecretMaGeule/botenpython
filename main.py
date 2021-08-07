import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio

PREFIX = (".")
bot = commands.Bot(command_prefix=PREFIX, description='Hey')

@bot.event
async def on_ready():
    activity = discord.Game(name="Dév des autres bots")
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print("Bot est prêt!")


bot.run('ODQ1NTk5Nzg5NDE1OTIzNzEy.YKjULA.CmVnXOT2MZBs7haYwmDiVq_zGu0')