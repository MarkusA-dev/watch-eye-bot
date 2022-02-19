import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='? ')

@bot.event
async def on_ready():
    print(f"The bot has logged in as {bot.user.name, bot.user.id}")

@bot.command()
async def ping(ctx):
    await ctx.send("hey")


bot.run('token')