import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random

class Main(Cog_Extension):
    @commands.command()  
    async def 來抽卡(self, ctx, a: int, b: float, c: int, d: int):
        if a > 0 and a <= 3 and b > 0 and b <= 100 and c > 0 and c <= 5000 and d > 0 and d <= 1000 :
            sum = 0
            b = b/100
            pool = ['other','PU1','PU2','PU3']
            if a == 1:
                weights = [1-b,b,0,0]
            elif a == 2:
                weights = [1-b*2,b,b,0]
            elif a == 3:
                weights = [1-b*3,b,b,b]

            for person in range(c):
                count = [0,0,0,0]
                cards = random.choices(pool,weights,k=d)
                for card in cards:
                    if card == 'PU1':
                        count[1] += 1
                    elif card == 'PU2':
                        count[2] += 1
                    elif card == 'PU3':
                        count[3] += 1
                    else :
                        count[0] += 1
                if 0 not in count[1:a+1]:
                    sum = sum + 1

            await ctx.send(f'{a}Pick up，每一Pick up都是{b*100}%的機率下，{c}人去抽{d}連抽的情況下。\n有{sum}人成功抽齊了，佔總體{round(sum/c*100, 1)}%。')
        else :
            await ctx.send('參數錯誤')

def setup(bot):
    bot.add_cog(Main(bot))