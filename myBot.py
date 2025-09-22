import discord
from discord.ext import commands
from dotenv import load_dotenv  # Pour charger les variables d'environnement
import os                      # Pour accéder aux variables d'environnement

# Charger les variables depuis le fichier .env
load_dotenv()

# Récupérer le token
TOKEN = os.getenv('TOKEN')

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
        await message.channel.send("Réel")

    
    await bot.process_commands(message)


bot.run(TOKEN)