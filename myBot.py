import discord
from discord.ext import commands
from dotenv import load_dotenv
from datetime import datetime
import os
from pathlib import Path  # Pour gérer les chemins de fichiers

# Chargement des variables d'environnement
load_dotenv()
TOKEN = os.getenv('TOKEN')

# Configuration des intents
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True

# Initialisation du bot
bot = commands.Bot(command_prefix="!", intents=intents)

# Chemin vers le dossier des médias
MEDIA_DIR = Path("media")

@bot.event
async def on_ready():
    """Log entry"""
    print(f"Connecté en tant que {bot.user}")

@bot.event
async def on_message(message):
    # Ignore loop
    if message.author == bot.user:
        return

    # Répondre aux mentions
    if bot.user in message.mentions:
        gif_path = MEDIA_DIR / "mention.gif"
        if gif_path.exists():  # Vérifie que le fichier existe
            with open(gif_path, 'rb') as gif_file:
                await message.channel.send(file=discord.File(gif_file, "mention.gif"))
        else:
            print(f"Fichier introuvable : {gif_path}")

    await bot.process_commands(message)

@bot.command(name="ohayo")
async def ohayo(ctx):
    """Ohayo username"""
    await ctx.send(f"Ohayo {ctx.author.mention} !")


@bot.command(name="command")
async def help_command(ctx):
    help_message = (
        "**Commandes disponibles :**\n"
        "`!ohayo` : Ohayo username.\n"
    )
    await ctx.send(help_message)

@bot.command(name="time")
async def getTime(ctx):
    time = datetime.now()
    stringTime=time.strftime("%H:%M:%S")
    await ctx.send(stringTime)



if __name__ == "__main__":
    bot.run(TOKEN)
