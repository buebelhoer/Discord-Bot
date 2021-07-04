import os
import discord
import random

from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
shitlist = ['Titan','Uebbels Test']
owner = 'Uebbels'
administrators = ['Big-Z-','WiseOwl']

#allows the bot to acess the member list
intents = discord.Intents.default()
intents.members = True

#creates the bot
bot = commands.Bot(command_prefix="!", intents=intents)

master = None


@bot.event
async def on_ready():



    for guild in bot.guilds:
        if guild.name == GUILD:
            break

    #This is my account, for debug purposed
    master = guild.get_member_named(owner)
    await master.create_dm()

    await master.dm_channel.send(f'{bot.user.name} has connected to Discord!')


@bot.event
async def on_error(event, *args, **kwargs):
    await master.dm_channel.send(f'Error! :{args}')

@bot.command()
async def admins(ctx):
    await ctx.send(owner)

    for member in administrators:
        await ctx.send(member)
    await ctx.send("NOTE: Titan is not an admin")

@bot.command()
async def bully(ctx, user = ""):
    if (ctx.author.name != owner and ctx.author.name not in administrators) or user == owner:
        await ctx.send("Nice try lol")
        await master.dm_channel.send(ctx.author.name + " tried to be naughty!")

        return

    #list of naughty words
    insults = ["dumbass", "idiot", "fucker", "cunt","shithead","asshole","whore","slut","bastion main","simp","scrub","poop head (Titan made this one)"]

    #if there is no user specified
    if user == "":
        for member in ctx.guild.members:
            if member != bot.user and member.name != owner:
                await ctx.send(f'{member.name} is a {insults[random.randint(0, len(insults) - 1)]}')
    else:
        userHere = False
        for member in ctx.guild.members:
            if member.name == user:
                userHere = True
                break
        if userHere:
            await ctx.send(f'{user} is a {insults[random.randint(0, len(insults) - 1)]}')
        else:
            await ctx.send("User not found, try not being a dumbass next time!")



bot.run(TOKEN)