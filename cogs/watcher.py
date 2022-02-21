import discord
from discord.ext import commands


class watcher(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def repeat(self, ctx, *, rep):
        await ctx.send(rep)

    @commands.Cog.listener('on_message')
    async def msg_ev(ctx, message):
        if message.author.bot == False:
            str = f"{message.author} sent message: {message.content}"
            await message.channel.send(str)
    
def setup(bot):
    bot.add_cog(watcher(bot))
