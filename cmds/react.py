import discord 
from discord.ext import commands
import random
import json


with open('setting.json',mode='r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

class React(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 

    @commands.command()
    async def picu(self,ctx):
      random_pic = random.choice(jdata['pic'])
      pic = discord.File(random_pic)
      await ctx.send(File = pic)

    @commands.command()
    async def web(self,ctx):
        random_pic = random.choice(jdata['url_pic'])
        await ctx.send(random_pic)

def setup(bot):
    bot.add_cog(React(bot))