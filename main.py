import discord
import time
import random
from bot_logic import rzut_moneta
from discord.ext import commands


# Zmienna intencje przechowuje uprawnienia bota
intents = discord.Intents.default()
# Włączanie uprawnienia do czytania wiadomości
intents.message_content = True
# Tworzenie bota w zmiennej klienta i przekazanie mu uprawnień
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')

@bot.command()
async def cześć(ctx):
    await ctx.send(f'Cześć, jestem bot{bot.user}!')

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))

@bot.command()
async def pa(ctx):
    await ctx.send(f'Do widzenia')
@bot.command()
async def rzut(ctx):
    await ctx.send(f'Zgadnij co wypadnie? ...')
    time.sleep(1)
    await ctx.send(f'...')    
    time.sleep(1)
    await ctx.send(f'...')
    time.sleep(1)
    await ctx.send(f'...')
    await ctx.send(f'Wynik: ' + rzut_moneta() + '!')      

bot.run("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx") 
