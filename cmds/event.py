import discord 
from discord.ext import commands
import json

with open('setting.json',mode='r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

class Event(commands.Cog):
    def __init__(self, bot):
        self.bot = bot    
    
    @commands.Cog.listener()
    async def on_member_join(self,member):
        channel = self.bot.get_channel(int(jdata['Welcome_channel']))
        await channel.send(f"{member}加入了大家庭!")

    @commands.Cog.listener()
    async def on_member_remove(self,member):
        channel = self.bot.get_channel(int(jdata['Welcome_channel']))
        await channel.send(f"{member} 的靈壓消失了.....")
            
    @commands.Cog.listener()
    async def on_message(self,msg):
        if msg.content == 'hi bot':
            await msg.channel.send('你好，我是彤彤，請使用_help來查看指令')
        if msg.content == 'KR':
            await msg.channel.send('測試迫害KR')
        if msg.content == 'Kr':
            await msg.channel.send('測試迫害KR')
        if msg.content == 'kr':
            await msg.channel.send('測試迫害KR')
          
    
    @commands.Cog.listener()
    async def on_command_error(self,ctx,error):
        if isinstance(error,commands.errors.MissingRequiredArgument):
            await ctx.send("你什麼參數都不寫是要我怎麼辦呢")
        elif isinstance(error,commands.errors.CommandNotFound):
            await ctx.send("沒有這指令啦，罰你去看_help")
        else:
            await ctx.send("請不要亂寫指令~")
    #@commands.Cog.listener()
    #async def on_message_delete(self,msg):
     #   counter = 1
      #  async for audilog in msg.guild.audit_logs(action=discord.AuditLogAction.message_delete):
       #   if counter == 1:
        #    await msg.channel.send(audilog.user.name)
         #   counter += 1



def setup(bot):
    bot.add_cog(Event(bot))