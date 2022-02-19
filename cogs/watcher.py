import discord
from discord.ext import commands


class watcher(commands.Cog):
    def __init__(self, bot):
        self.client = bot

    @commands.command()
    async def repeat(self, ctx, *, rep):
        await ctx.send(rep)

    
def setup(bot):
    bot.add_cog(watcher(bot))
