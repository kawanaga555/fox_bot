import discord
from discord.ext import commands
from core.classes import Cog_Extension

class react(Cog_Extension):
    @commands.command()
    async def 你好(self, ctx):
        await ctx.send('你好')

    @commands.command()  
    async def 安安(self, ctx):
        await ctx.send('安安')

def setup(bot):
    bot.add_cog(react(bot))