
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import os
import requests
from PIL import Image, ImageFont, ImageDraw
import io
from discord.utils import get
import json

# functions


token = open("token.txt", "r").readline()
prefix = "!"
intents = discord.Intents.all()
Bot = commands.Bot(command_prefix= "!", intents=intents)

players = {}

# commands

@Bot.event
async def on_ready():
    print("Bot started")
    await Bot.change_presence(status=discord.Status.idle, activity=discord.Game("VILNOYS"))



@Bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: discord.Member, *,reason=None):
    await user.ban(reason=reason)
    embedd = discord.Embed(
        title = 'Ban',
        description = 'He\her has been banned!',
        color= discord.Color.red()
    )
    embedd.set_footer(text = "Bots for examples.")
    await ctx.send(embed=embedd)

@Bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member, *,reason=None):
    await user.kick(reason=reason)
    embedd = discord.Embed(
        title = 'kick',
        description = 'his(her) has been kicked.',
        color= discord.Color.red()
    )

    await ctx.send(embed=embedd)



@Bot.command()
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount)
    embedd = discord.Embed(
        title = 'Clear',
        description = 'Needed count messages has been cleared',
        color= discord.Color.green()
    )
    await ctx.send(embed=embedd)


Bot.run(token)
