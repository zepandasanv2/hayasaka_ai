import discord
from discord.ext import commands
from dotenv import load_dotenv
from datetime import datetime
import os
import random
from pathlib import Path  # Pour gérer les chemins de fichiers

# Chargement des variables d'environnement
load_dotenv()
TOKEN = os.getenv('TOKEN')

# Configuration des intents
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.presences = True

# Initialisation du bot
bot = commands.Bot(command_prefix="!", intents=intents)

# Chemin vers le dossier des médias
MEDIA_DIR = Path("media")

@bot.event
async def on_ready():
    """Log entry"""
    print(f"Connecté en tant que {bot.user}")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="your messages with love ❤️"))


@bot.event
async def on_message(message):
    # Ignore les messages du bot pour éviter les boucles
    if message.author == bot.user:
        return

    # Répondre aux mentions
    if bot.user in message.mentions:
        gif_path = MEDIA_DIR / "mention.gif"
        if gif_path.exists():
            with open(gif_path, 'rb') as gif_file:
                await message.channel.send(file=discord.File(gif_file, "mention.gif"))
        else:
            print(f"Fichier introuvable : {gif_path}")

    if "sisi" in message.content.lower():
        sisi_gif_path = MEDIA_DIR / "sisi.gif"  # Remplace "sisi.gif" par le nom de ton GIF
        if sisi_gif_path.exists():
            with open(sisi_gif_path, 'rb') as sisi_gif_file:
                await message.channel.send(file=discord.File(sisi_gif_file, "sisi.gif"))
        else:
            print(f"Fichier GIF introuvable : {sisi_gif_path}")
    # Vérifie si le message se termine par "quoi" ou "koi" (en ignorant la ponctuation)
    content_lower = message.content.lower().strip()
    # Supprime les ponctuations à la fin du message
    while content_lower and content_lower[-1] in "?!.,;:":
        content_lower = content_lower[:-1]

    if content_lower.endswith("quoi") or content_lower.endswith("koi"):
        await message.channel.send("Feur")
    elif content_lower.endswith("oui"):
        await message.channel.send("Stiti")

    # Permet aux autres commandes de fonctionner
    await bot.process_commands(message)

@bot.command(name="ohayo")
async def ohayo(ctx):
    """Ohayo username"""
    await ctx.send(f"Ohayo {ctx.author.mention} !")


@bot.command(name="command")
async def help_command(ctx):
    help_message = (
        "**Commandes disponibles :**\n\n"
        "`!ohayo` : Salue l'utilisateur avec 'Ohayo'\n"
        "`!time` : Affiche l'heure actuelle\n"
        "`!ask [question]` : Pose une question à la boule magique\n"
        "`!avatar [@utilisateur]` : Affiche l'avatar d'un utilisateur\n"
        "`!command` : Affiche cette liste de commandes\n\n"
        "**Réactions automatiques :**\n"
        "- Mentionnez le bot pour une réponse spéciale\n"
        "- Écrivez 'sisi' pour une réaction\n"
        "- Les messages se terminant par 'quoi' ou 'koi' reçoivent 'Feur'\n"
        "- Les messages se terminant par 'oui' reçoivent 'Stiti'\n"
    )
    await ctx.send(help_message)

@bot.command(name="time")
async def getTime(ctx):
    time = datetime.now()
    stringTime=time.strftime("%H:%M:%S")
    await ctx.send(stringTime)

@bot.command(name="ask")
async def eight_ball(ctx, *, question: str):
    """Répond à une question de manière aléatoire."""
    responses = [
        "Oui, sans aucun doute.",
        "Non, pas du tout.",
        "Peut-être bien que oui...",
        "C’est certain !",
        "Très probablement.",
        "Demande plus tard.",
        "Mieux vaut ne pas te le dire maintenant.",
        "Les perspectives ne sont pas bonnes.",
        "Concentre-toi et repose ta question.",
    ]
    response = random.choice(responses)
    await ctx.send(f"**{ctx.author.display_name}** a demandé : *{question}*\n**Réponse :** {response}")

@bot.command(name="avatar")
async def avatar(ctx, member: discord.Member = None):
    """Affiche l'avatar d'un utilisateur."""
    # Si aucun utilisateur n'est mentionné, on prend l'auteur du message
    if member is None:
        member = ctx.author

    # Récupère l'URL de l'avatar de l'utilisateur
    avatar_url = member.avatar.url if member.avatar else member.default_avatar.url

    # Crée un embed pour afficher l'avatar de manière élégante
    embed = discord.Embed(
        title=f"Avatar de {member.display_name}",
        color=discord.Color.blue()
    )
    embed.set_image(url=avatar_url)

    await ctx.send(embed=embed)



if __name__ == "__main__":
    bot.run(TOKEN)
