import discord
from discord.ext import commands
import embedlinks
import random
from datetime import datetime
client = commands.Bot(command_prefix = 'y.')

@client.event
async def on_ready():
    print("Bot is ready")


@client.command()
async def pop(ctx):
    choosen_image = random.choice(embedlinks.klinks)
    embed = discord.Embed(color=0xffb694)
    embed.set_image(url=choosen_image)
    embed.set_footer(text =f"Set By: {ctx.author.name}")
    await ctx.send(embed=embed)



@client.command()
async def hello(ctx):
    await ctx.send(f"hello, {ctx.author.mention}")


client.run('ODQxMjcwMjU3NzQyMzgxMDU2.YJkT-w.rVh5TL53rYYfKRN7zEapulgtWBo')
