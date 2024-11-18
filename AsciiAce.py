import discord
from discord.ext import commands
from discord import app_commands
import pyfiglet
import os
from slash_cmds import all_slash_commands
from docutils.nodes import description

# Initialize the bot with a command prefix
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="+", intents=intents)


# Event: Bot successfully connected to Discord
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(name="ASCII art >_<"))
    await bot.tree.sync()


# ------------------------------
# 3D text convertion
# ------------------------------
@bot.command(name="3d", description='convert the normal text to ASCII styled 3D text')
async def ascii(ctx, text: str):
    try:
        result = pyfiglet.figlet_format(text, font='3-d')
        embed = discord.Embed(
            title="ASCII 3D Text",
            description=f"```{result}```",
            color=discord.Color.dark_blue()
        )
        await ctx.send(embed=embed)

    except Exception as e:
        embed = discord.Embed(
            title="Error",
            description=f"An error occurred: {str(e)}",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)


# ------------------------------
# Slant text convertion
# ------------------------------
@bot.command(name="slant", description="convert the normal text to ASCII styled slant text")
async def slant_text(ctx, text: str):
    try:
        result = pyfiglet.figlet_format(text, font='slant')
        embed = discord.Embed(
            title="ASCII Slant Text",
            description=f"```{result}```",
            color=discord.Color.dark_blue()
        )
        await ctx.send(embed=embed)
    except Exception as e:
        embed = discord.Embed(
            title="Error",
            description=f"An error occurred: {str(e)}",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)


# ------------------------------
# Doom text convertion
# ------------------------------
@bot.command(name="doom", description="convert the normal text to ASCII styled doom text")
async def doom_text(ctx, text: str):
    try:
        result = pyfiglet.figlet_format(text, font='doom')
        embed = discord.Embed(
            title="ASCII Doom Text",
            description=f"```{result}```",
            color=discord.Color.dark_blue()
        )
        await ctx.send(embed=embed)
    except Exception as e:
        embed = discord.Embed(
            title="Error",
            description=f"An error occurred: {str(e)}",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)


# ------------------------------
# Alphabet text convertion
# ------------------------------
@bot.command(name='alphabet', description="convert the normal text to ASCII styled alphabet text")
async def alphabet_text(ctx, text: str):
    try:
        result = pyfiglet.figlet_format(text, font='alphabet')
        embed = discord.Embed(
            title="ASCII Alphabet Text",
            description=f"```{result}```",
            color=discord.Color.dark_blue()
        )
        await ctx.send(embed=embed)
    except Exception as e:
        embed = discord.Embed(
            title="Error",
            description=f"An error occurred: {str(e)}",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)


# ------------------------------
# Banner-3D text convertion
# ------------------------------
@bot.command(name='banner3-d', description="convert the normal text to ASCII styled banner3-D text")
async def banner3d_text(ctx, text: str):
    try:
        result = pyfiglet.figlet_format(text, font='banner3-d')
        embed = discord.Embed(
            title="ASCII Banner3-D Text",
            description=f"```{result}```",
            color=discord.Color.dark_blue()
        )
        await ctx.send(embed=embed)
    except Exception as e:
        embed = discord.Embed(
            title="Error",
            description=f"An error occurred: {str(e)}",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)


# ------------------------------
# Doh text convertion
# ------------------------------
@bot.command(name="doh", description="convert the normal text to ASCII styled doh text")
async def doh_text(ctx, text: str):
    try:
        result = pyfiglet.figlet_format(text, font='doh')
        embed = discord.Embed(
            title="ASCII Doh Text",
            description=f"```{result}```",
            color=discord.Color.dark_blue()
        )
        await ctx.send(embed=embed)
    except Exception as e:
        embed = discord.Embed(
            title="Error",
            description=f"An error occurred: {str(e)}",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)


# ------------------------------
# Isometric1 text convertion
# ------------------------------
@bot.command(name="isometric1", description="convert the normal text to ASCII styled isometric1 text")
async def isometric1_text(ctx, text: str):
    try:
        result = pyfiglet.figlet_format(text, font='isometric1')
        embed = discord.Embed(
            title="ASCII Isometric1 Text",
            description=f"```{result}```",
            color=discord.Color.dark_blue()
        )
        await ctx.send(embed=embed)
    except Exception as e:
        embed = discord.Embed(
            title="Error",
            description=f"An error occurred: {str(e)}",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)


# ------------------------------
# Starwars text convertion
# ------------------------------
@bot.command(name="starwars", description="convert the normal text to ASCII styled starwars text")
async def starwars_text(ctx, text: str):
    try:
        result = pyfiglet.figlet_format(text, font='starwars')
        embed = discord.Embed(
            title="ASCII Starwars Text",
            description=f"```{result}```",
            color=discord.Color.dark_blue()
        )
        await ctx.send(embed=embed)
    except Exception as e:
        embed = discord.Embed(
            title="Error",
            description=f"An error occurred: {str(e)}",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)


# ------------------------------
# Block text convertion
# ------------------------------
@bot.command(name="block", description="convert the normal text to ASCII styled block text")
async def block_text(ctx, text: str):
    try:
        result = pyfiglet.figlet_format(text, font='block')
        embed = discord.Embed(
            title="ASCII Block Text",
            description=f"```{result}```",
            color=discord.Color.dark_blue()
        )
        await ctx.send(embed=embed)
    except Exception as e:
        embed = discord.Embed(
            title="Error",
            description=f"An error occurred: {str(e)}",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)


# ------------------------------
# Digital text convertion
# ------------------------------
@bot.command(name="digital", description="convert the normal text to ASCII styled digital text")
async def digital_text(ctx, text: str):
    try:
        result = pyfiglet.figlet_format(text, font='digital')
        embed = discord.Embed(
            title="ASCII Digital Text",
            description=f"```{result}```",
            color=discord.Color.dark_blue()
        )
        await ctx.send(embed=embed)
    except Exception as e:
        embed = discord.Embed(
            title="Error",
            description=f"An error occurred: {str(e)}",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)


# ------------------------------
# Shadow text convertion
# ------------------------------
@bot.command(name="shadow", description="convert the normal text to ASCII styled shadow text")
async def shadow_text(ctx, text: str):
    try:
        result = pyfiglet.figlet_format(text, font='shadow')
        embed = discord.Embed(
            title="ASCII Shadow Text",
            description=f"```{result}```",
            color=discord.Color.dark_blue()
        )
        await ctx.send(embed=embed)
    except Exception as e:
        embed = discord.Embed(
            title="Error",
            description=f"An error occurred: {str(e)}",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)


# ------------------------------
# Speed text convertion
# ------------------------------
@bot.command(name="speed", description="convert the normal text to ASCII styled speed text")
async def speed_text(ctx, text: str):
    try:
        result = pyfiglet.figlet_format(text, font='speed')
        embed = discord.Embed(
            title="ASCII Speed Text",
            description=f"```{result}```",
            color=discord.Color.dark_blue()
        )
        await ctx.send(embed=embed)
    except Exception as e:
        embed = discord.Embed(
            title="Error",
            description=f"An error occurred: {str(e)}",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)


# ------------------------------
# Epic text convertion
# ------------------------------
@bot.command(name="epic", description="convert the normal text to ASCII styled epic text")
async def epic_text(ctx, text: str):
    try:
        result = pyfiglet.figlet_format(text, font='epic')
        embed = discord.Embed(
            title="ASCII Epic Text",
            description=f"```{result}```",
            color=discord.Color.dark_blue()
        )
        await ctx.send(embed=embed)
    except Exception as e:
        embed = discord.Embed(
            title="Error",
            description=f"An error occurred: {str(e)}",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)


# ------------------------------
# Rectangles text convertion
# ------------------------------
@bot.command(name="rectangles", description="convert the normal text to ASCII styled rectangles text")
async def rectangles_text(ctx, text: str):
    try:
        result = pyfiglet.figlet_format(text, font='rectangles')
        embed = discord.Embed(
            title="ASCII Rectangles Text",
            description=f"```{result}```",
            color=discord.Color.dark_blue()
        )
        await ctx.send(embed=embed)
    except Exception as e:
        embed = discord.Embed(
            title="Error",
            description=f"An error occurred: {str(e)}",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)


# ------------------------------
# Cosmic text convertion
# ------------------------------
# @bot.command(name="cosmic", description="convert the normal text to ASCII styled cosmic text")
# async def cosmic_text(ctx, text: str):
#     try:
#         result = pyfiglet.figlet_format(text, font='cosmic')
#         embed = discord.Embed(
#             title="ASCII Cosmic Text",
#             description=f"{result}",
#             color=discord.Color.dark_blue()
#         )
#         await ctx.send(embed=embed)
#     except Exception as e:
#         embed = discord.Embed(
#             title="Error",
#             description=f"An error occurred: {str(e)}",
#             color=discord.Color.red()
#         )
#         await ctx.send(embed=embed)


# --------------------------------------
# help command
# -------------------------------------
@bot.command(name="bothelp", description="know about the bot and see all available commands")
async def hel_cmd(ctx):
    help_desc = """
    **What bot does?**
    AsciiAce bot designed to convert the normal text to ASCII Text. Transform plain text into eye-catching ASCII Text in a variety of styles, perfect for adding flair to your messages and making your server more fun.
    
    **Available commands?**
    Type ```/``` to see all available commands, each and every command perform best operation to convert the normal text to beautiful **ASCII** Text :)
    
    |A|s|c|i|i|A|c|e|
    +-+-+-+-+-+-+-+-+
    
    
    """
    bot_avatar_url = bot.user.avatar.url if bot.user.avatar else bot.user.default_avatar.url
    embed = discord.Embed(
        title="AsciiAce bot help",
        description=help_desc,
        color=discord.Color.darker_gray()
    )
    embed.set_thumbnail(url=bot_avatar_url)
    embed.set_footer(text=f"{bot.user.name}", icon_url=bot_avatar_url)
    await ctx.send(embed=embed)


all_slash_commands(bot)


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(
            description=f"Sorry, I don't recognize that command :(",
            color=discord.Color.red()
        )
        await ctx.semd(embed=embed)
    else:
        embed = discord.Embed(
            description="An error occurred while processing your command.",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)


# Start the bot with your token
bot.run("BOT_TOKEN")
