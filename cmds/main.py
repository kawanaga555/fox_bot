import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random

class Main(Cog_Extension):
    @commands.command()  
    async def 來抽卡(self, ctx, pickup: int, Probability: float, people: int, times: int):
        if pickup > 0 and pickup <= 3 and Probability > 0 and Probability <= 100 and people > 0 and people <= 5000 and times > 0 and times <= 1000 :
            sum = 0
            Probability = Probability/100
            pool = ['other','PU1','PU2','PU3']
            if pickup == 1:
                weights = [1-Probability,Probability,0,0]
            elif pickup == 2:
                weights = [1-Probability*2,Probability,Probability,0]
            else :
                weights = [1-Probability*3,Probability,Probability,Probability]

            for person in range(people):
                count = [0,0,0,0]
                cards = random.choices(pool, weights, k=times)
                for card in cards:
                    if card == 'other':
                        count[0] += 1
                    elif card == 'PU1':
                        count[1] += 1
                    elif card == 'PU2':
                        count[2] += 1
                    elif card == 'PU3':
                        count[3] += 1
                        
                if 0 not in count[1:pickup+1]:
                    sum = sum + 1

            await ctx.send(f'{pickup}Pick up，每一Pick up都是{Probability*100}%的機率下，{people}人去抽{times}連抽的情況下。\n\
有{sum}人成功抽齊了，佔總體{round(sum/people*100, 1)}%。')
        else :
            await ctx.send('參數錯誤')

def setup(bot):
    bot.add_cog(Main(bot))