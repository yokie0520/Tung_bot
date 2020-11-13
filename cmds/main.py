import discord 
from discord.ext import commands
import random
class Main(commands.Cog):
    def __init__(self, bot):
        self.bot = bot    
        
    @commands.command()
    async def ping(self,ctx):
        await ctx.send(f"{round(self.bot.latency*1000)}(ms)")

    @commands.command()
    async def  say(self,ctx,*,msg):
        await ctx.message.delete()
        await ctx.send(msg)
  
    @commands.command()
    async def rand_squad(self,ctx):
      online = []
      for member in ctx.guild.members:
        if str(member.status) == 'online' and member.bot == False:
          online.append(member.name)

      random_online = random.sample(online,k=20)

      for squad in range(5):
          a = random.sample(random_online,k=4)
          await ctx.send(f"{squad+1}小隊"+str(a))
          for name in a:
            random_online.remove(name)
    
    @commands.command()
    @commands.is_owner()
    async def clean(self,ctx,num:int):
        await ctx.channel.purge(limit=num+1)
    


    

def setup(bot):
    bot.add_cog(Main(bot))
