import discord 
from discord.ext import commands

import json
import os
import random
import keep_alive

intents = discord.Intents.all()

with open('setting.json',mode='r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

bot = commands.Bot(command_prefix='_',intents=intents )

@bot.event
async def on_ready():
    print(">>bot is online<<")




@bot.command()
@commands.is_owner()
async def load(ctx, extension):
    bot.load_extension(f'cmds.{extension}')
    await ctx.send(f"loaded {extension} done.")

@bot.command()
@commands.is_owner()
async def unload(ctx, extension):
    bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f"unloaded {extension} done.")

@bot.command()
@commands.is_owner()
async def reload(ctx, extension):
    bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f"reloaded {extension} done.")

for Filename in os.listdir('./cmds'):
    if Filename.endswith('.py') and not(Filename.startswith('__')):
        bot.load_extension(f'cmds.{Filename[:-3]}')

if __name__ == "__main__":
  keep_alive.keep_alive()
  bot.run(jdata['TOKEN'])