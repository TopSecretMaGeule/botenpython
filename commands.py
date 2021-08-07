import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = ".")

@bot.command()
async def report(ctx):
    await ctx.send("**Commande en développement**!")

@bot.command()
async def serverInfo(ctx):
	server = ctx.guild
	numberOfTextChannels = len(server.text_channels)
	numberOfVoiceChannels = len(server.voice_channels)
	serverDescription = server.description
	numberOfPerson = server.member_count
	serverName = server.name
	message = f"Le serveur **{serverName}** 🤖 contient ***{numberOfPerson}*** personnes ! \nLa description du serveur est ***{serverDescription}***. \nCe serveur possède ***{numberOfTextChannels}*** salons écrit et ***{numberOfVoiceChannels}*** salon vocaux."
	await ctx.send(message)

bot.run("ODQ1NTk5Nzg5NDE1OTIzNzEy.YKjULA.CmVnXOT2MZBs7haYwmDiVq_zGu0")