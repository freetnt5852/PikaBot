import discord
from discord.ext import commands
import os
import sys

bot = commands.Bot(command_prefix="+", description="This is an example bot", owner_id=279974491071709194)

@bot.event
async def on_ready():
    print("Bot is online!")
    
@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong! {bot.ws.latency* 1000:.4f} ms")
    
@bot.command()
async def say(ctx, *, msg: str):
    await ctx.message.delete()
    await ctx.send(msg)
    
bot.run(os.environ.get("TOKEN"))
