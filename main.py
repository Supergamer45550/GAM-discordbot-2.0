import discord
from discord.ext import commands


intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
intents.members = True
intents.bans = True
intents.guilds = True
intents.guild_messages = True



bot = commands.Bot(command_prefix='!', intents=intents)
client = discord.Bot(command_prefix='', intents=intents)

@bot.event
async def on_ready():
    print("Hello World")


bot.load_extension("commands.test") 
bot.run("")