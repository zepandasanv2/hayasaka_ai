import discord
from discord.ext import commands 

# token 
TOKEN = #tbd

# intents
intents = discord.Intents.default()
intents.message_content = True  
intents.guilds = True 

# bot creation 
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"connected as {bot.user}")

@bot.event
async def on_message(message):
    # avoid loop
    if message.author == bot.user:
        return

    # Check if mentionned
    if bot.user in message.mentions:
        await message.channel.send("réel")

    
    await bot.process_commands(message)


bot.run(TOKEN)