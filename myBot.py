import discord
from discord.ext import commands
from dotenv import load_dotenv
from datetime import datetime
import os
import sqlite3
import random
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

def get_random_opening():
    conn = sqlite3.connect("anime.db")
    cur = conn.cursor()
    cur.execute("""
        SELECT a.titre, o.numero, o.titre, o.artiste, o.link_url
        FROM opening o
        JOIN anime a ON a.id = o.anime_id
        ORDER BY RANDOM()
        LIMIT 1
    """)
    result = cur.fetchone()
    conn.close()
    return result

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

@bot.command(name="random_opening")
async def opening(ctx):
    data = get_random_opening()
    if data:
        anime, numero, chanson, artiste, url = data
        embed = discord.Embed(
            title=f"🎵 {anime} {numero}",
            description=f"**{chanson}** par *{artiste}*\n{url}",
            color=discord.Color.purple()
        )
        await ctx.send(embed=embed)
    else:
        await ctx.send("Aucun opening trouvé dans la base de données.")

@bot.command(name="random_anime")
async def anime(ctx):
    conn = sqlite3.connect("anime.db")
    cur = conn.cursor()
    cur.execute("SELECT id, titre, saison, episodes, studio FROM anime WHERE titre LIKE ?", (f"%{titre}%",))
    result = cur.fetchone()
    conn.close()

    if result:
        id_, titre, saison, episodes, studio = result
        embed = discord.Embed(
            title=f"{titre}",
            description=f"Saison: {saison}\nEpisodes: {episodes}\nStudio: {studio}",
            color=discord.Color.blue()
        )
        await ctx.send(embed=embed)
    else:
        await ctx.send(f"Aucun animé trouvé contenant « {titre} »")

if __name__ == "__main__":
    bot.run(TOKEN)
