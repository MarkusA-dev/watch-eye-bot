import discord
import os
from discord.ext import commands
import jsonhandler

bot = commands.Bot(command_prefix='?')

@bot.event
async def on_ready():
    print(f"The bot has logged in as {bot.user.name, bot.user.id}")
    

@bot.command()
async def datastruct(ctx):
    await ctx.send(jsonhandler.data)

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')

@bot.command()
async def reload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    bot.load_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run('token')