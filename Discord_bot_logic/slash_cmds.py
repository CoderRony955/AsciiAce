import discord
from Cython.Compiler.Options import embed
from discord.ext import commands
from discord import app_commands
import logging
import pyfiglet
from docutils.nodes import description

# Initialize the bot with a command prefix
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="+", intents=intents)

logging.basicConfig(level=logging.INFO,
                    format='(%(asctime)s): %(message)s - %(levelname)s - %(filename)s : %(process)s',
                    filename='AsciiAce_dc_bot.log',
                    filemode='w')

logger = logging.getLogger(__name__)


@bot.event
async def on_ready():
    await bot.tree.sync()


def all_slash_commands(bot):
    @bot.tree.command(name="3d", description='convert the normal text to ASCII styled 3D text')
    async def ascii(interaction: discord.Interaction, text: str):
        if text is None:
            embed = discord.Embed(
                title="Error",
                description="Please provide some text to convert.",
                color=discord.Color.red()
            )
            await interaction.response.send_message(embed=embed)
            logger.error('An error occurred: User does not provide some text to convert.')

        else:
            try:
                result = pyfiglet.figlet_format(text, font='3-d')
                embed = discord.Embed(
                    title="ASCII 3D Text",
                    description=f"```{result}```",
                    color=discord.Color.dark_blue()
                )
                await interaction.response.send_message(embed=embed)
                logger.info(f'Successfully converted {text} normal text to 3D ASCII Text')

            except discord.DiscordException as e:
                embed = discord.Embed(
                    title="Error ;-;",
                    description=f"It seems like something went wrong {str(e)}",
                    color=discord.Color.red()
                )
                logging.error(f'It seems like something went wrong {e}')
                await interaction.response.send_message(embed=embed)
            finally:
                logging.info('command executed')

    # ------------------------------
    # Slant text convertion
    # ------------------------------
    @bot.tree.command(name="slant", description="convert the normal text to ASCII styled slant text")
    async def slant_text(interaction: discord.Interaction, text: str):
        if text is None:
            embed = discord.Embed(
                title="Error",
                description="Please provide some text to convert.",
                color=discord.Color.red()
            )
            await interaction.response.send_message(embed=embed)
            logger.error('An error occurred: user does not provide a any text to convert in ASCII slant format')
        else:
            try:
                result = pyfiglet.figlet_format(text, font='slant')
                embed = discord.Embed(
                    title="ASCII Slant Text",
                    description=f"```{result}```",
                    color=discord.Color.dark_blue()
                )
                await interaction.response.send_message(embed=embed)
                logger.info(f'Successfully converted {text} normal text to ASCII slant')
            except discord.DiscordException as e:
                embed = discord.Embed(
                    title="Error ;-;",
                    description=f"An error occurred: {str(e)}",
                    color=discord.Color.red()
                )
                await interaction.response.send_message(embed=embed)
                logger.error(f'An error occurred: {e}')
            finally:
                logging.info('command executed')

    # ------------------------------
    # Doom text convertion
    # ------------------------------
    @bot.tree.command(name="doom", description="convert the normal text to ASCII styled doom text")
    async def doom_text(interaction: discord.Interaction, text: str):
        if text is None:
            embed = discord.Embed(
                title="Error",
                description="Please provide some text to convert.",
                color=discord.Color.red()
            )
            await interaction.response.send_message(embed=embed)
            logger.error('An error occurred: user does not provide a any text to convert in ASCII doom format')
        else:

            try:
                result = pyfiglet.figlet_format(text, font='doom')
                embed = discord.Embed(
                    title="ASCII Doom Text",
                    description=f"```{result}```",
                    color=discord.Color.dark_blue()
                )
                await interaction.response.send_message(embed=embed)
                logger.info(f'Successfully converted {text} normal text to ASCII doom')
            except discord.DiscordException as e:
                embed = discord.Embed(
                    title="Error ;-;",
                    description=f"An error occurred: {str(e)}",
                    color=discord.Color.red()
                )
                await interaction.response.send_message(embed=embed)
                logger.error(f'An error occurred: {e}')
            finally:
                logging.info('command executed')

    # ------------------------------
    # Alphabet text convertion
    # ------------------------------
    @bot.tree.command(name='alphabet', description="convert the normal text to ASCII styled alphabet text")
    async def alphabet_text(interaction: discord.Interaction, text: str):
        if text is None:
            embed = discord.Embed(
                title="Error",
                description="Please provide some text to convert.",
                color=discord.Color.red()
            )
            await interaction.response.send_message(embed=embed)
            logger.error('An error occurred: user does not provide a any text to convert in ASCII alphabet format')
        else:

            try:
                result = pyfiglet.figlet_format(text, font='alphabet')
                embed = discord.Embed(
                    title="ASCII Alphabet Text",
                    description=f"```{result}```",
                    color=discord.Color.dark_blue()
                )
                await interaction.response.send_message(embed=embed)
                logger.info(f'Successfully converted {text} normal text to ASCII alphabet')
            except discord.DiscordException as e:
                embed = discord.Embed(
                    title="Error ;-;",
                    description=f"An error occurred: {str(e)}",
                    color=discord.Color.red()
                )
                await interaction.response.send_message(embed=embed)
                logger.error(f'An error occurred: {e}')
            finally:
                logging.info('command executed')

    # ------------------------------
    # Banner-3D text convertion
    # ------------------------------
    @bot.tree.command(name='banner3-d', description="convert the normal text to ASCII styled banner3-D text")
    async def banner3d_text(interaction: discord.Interaction, text: str):
        if text is None:
            embed = discord.Embed(
                title="Error",
                description="Please provide some text to convert.",
                color=discord.Color.red()
            )
            await interaction.response.send_message(embed=embed)
            logger.error('An error occurred: user does not provide a any text to convert in ASCII banner3-d format')
        else:

            try:
                result = pyfiglet.figlet_format(text, font='banner3-d')
                embed = discord.Embed(
                    title="ASCII Banner3-D Text",
                    description=f"```{result}```",
                    color=discord.Color.dark_blue()
                )
                await interaction.response.send_message(embed=embed)
                logger.info(f'Successfully converted {text} normal text to ASCII banner3-d')
            except discord.DiscordException as e:
                embed = discord.Embed(
                    title="Error ;-;",
                    description=f"An error occurred: {str(e)}",
                    color=discord.Color.red()
                )
                await interaction.response.send_message(embed=embed)
                logger.error(f'An error occurred: {e}')
            finally:
                logging.info('command executed')

    # ------------------------------
    # Doh text convertion
    # ------------------------------
    @bot.tree.command(name="doh", description="convert the normal text to ASCII styled doh text")
    async def doh_text(interaction: discord.Interaction, text: str):
        if text is None:
            embed = discord.Embed(
                title="Error",
                description="Please provide some text to convert.",
                color=discord.Color.red()
            )
            await interaction.response.send_message(embed=embed)
            logger.error('An error occurred: user does not provide a any text to convert in ASCII doh format')
        else:

            try:
                result = pyfiglet.figlet_format(text, font='doh')
                embed = discord.Embed(
                    title="ASCII Doh Text",
                    description=f"```{result}```",
                    color=discord.Color.dark_blue()
                )
                await interaction.response.send_message(embed=embed)
                logger.info(f'Successfully converted {text} normal text to ASCII doh')
            except discord.DiscordException as e:
                embed = discord.Embed(
                    title="Error ;-;",
                    description=f"An error occurred: {str(e)}",
                    color=discord.Color.red()
                )
                await interaction.response.send_message(embed=embed)
                logger.error(f'An error occurred: {e}')
            finally:
                logging.info('command executed')

    # ------------------------------
    # Isometric1 text convertion
    # ------------------------------
    @bot.tree.command(name="isometric1", description="convert the normal text to ASCII styled isometric1 text")
    async def isometric1_text(interaction: discord.Interaction, text: str):
        if text is None:
            embed = discord.Embed(
                title="Error",
                description="Please provide some text to convert.",
                color=discord.Color.red()
            )
            await interaction.response.send_message(embed=embed)
            logger.error('An error occurred: user does not provide a any text to convert in ASCII isometric1 format')
        else:

            try:
                result = pyfiglet.figlet_format(text, font='isometric1')
                embed = discord.Embed(
                    title="ASCII Isometric1 Text",
                    description=f"```{result}```",
                    color=discord.Color.dark_blue()
                )
                await interaction.response.send_message(embed=embed)
                logger.info(f'Successfully converted {text} normal text to ASCII isometric1')
            except discord.DiscordException as e:
                embed = discord.Embed(
                    title="Error ;-;",
                    description=f"An error occurred: {str(e)}",
                    color=discord.Color.red()
                )
                await interaction.response.send_message(embed=embed)
                logger.error(f'An error occurred: {e}')
            finally:
                logging.info('command executed')

    # ------------------------------
    # Starwars text convertion
    # ------------------------------
    @bot.tree.command(name="starwars", description="convert the normal text to ASCII styled starwars text")
    async def starwars_text(interaction: discord.Interaction, text: str):
        if text is None:
            embed = discord.Embed(
                title="Error",
                description="Please provide some text to convert.",
                color=discord.Color.red()
            )
            await interaction.response.send_message(embed=embed)
            logger.error('An error occurred: user does not provide a any text to convert in ASCII starwars format')
        else:

            try:
                result = pyfiglet.figlet_format(text, font='starwars')
                embed = discord.Embed(
                    title="ASCII Starwars Text",
                    description=f"```{result}```",
                    color=discord.Color.dark_blue()
                )
                await interaction.response.send_message(embed=embed)
                logger.info(f'Successfully converted {text} normal text to ASCII starwars')
            except discord.DiscordException as e:
                embed = discord.Embed(
                    title="Error ;-;",
                    description=f"An error occurred: {str(e)}",
                    color=discord.Color.red()
                )
                await interaction.response.send_message(embed=embed)
                logger.error(f'An error occurred: {e}')
            finally:
                logging.info('command executed')

    # ------------------------------
    # Block text convertion
    # ------------------------------
    @bot.tree.command(name="block", description="convert the normal text to ASCII styled block text")
    async def block_text(interaction: discord.Interaction, text: str):
        if text is None:
            embed = discord.Embed(
                title="Error",
                description="Please provide some text to convert.",
                color=discord.Color.red()
            )
            await interaction.response.send_message(embed=embed)
            logger.error('An error occurred: user does not provide a any text to convert in ASCII block format')
        else:

            try:
                result = pyfiglet.figlet_format(text, font='block')
                embed = discord.Embed(
                    title="ASCII Block Text",
                    description=f"```{result}```",
                    color=discord.Color.dark_blue()
                )
                await interaction.response.send_message(embed=embed)
                logger.info(f'Successfully converted {text} normal text to ASCII block')
            except discord.DiscordException as e:
                embed = discord.Embed(
                    title="Error ;-;",
                    description=f"An error occurred: {str(e)}",
                    color=discord.Color.red()
                )
                await interaction.response.send_message(embed=embed)
                logger.error(f'An error occurred: {e}')
            finally:
                logging.info('command executed')

    # ------------------------------
    # Digital text convertion
    # ------------------------------
    @bot.tree.command(name="digital", description="convert the normal text to ASCII styled digital text")
    async def digital_text(interaction: discord.Interaction, text: str):
        if text is None:
            embed = discord.Embed(
                title="Error",
                description="Please provide some text to convert.",
                color=discord.Color.red()
            )
            await interaction.response.send_message(embed=embed)
            logger.error('An error occurred: user does not provide a any text to convert in ASCII digital format')
        else:

            try:
                result = pyfiglet.figlet_format(text, font='digital')
                embed = discord.Embed(
                    title="ASCII Digital Text",
                    description=f"```{result}```",
                    color=discord.Color.dark_blue()
                )
                await interaction.response.send_message(embed=embed)
                logger.info(f'Successfully converted {text} normal text to ASCII digital')
            except discord.DiscordException as e:
                embed = discord.Embed(
                    title="Error ;-;",
                    description=f"An error occurred: {str(e)}",
                    color=discord.Color.red()
                )
                await interaction.response.send_message(embed=embed)
                logger.error(f'An error occurred: {e}')
            finally:
                logging.info('command executed')

    # ------------------------------
    # Shadow text convertion
    # ------------------------------
    @bot.tree.command(name="shadow", description="convert the normal text to ASCII styled shadow text")
    async def shadow_text(interaction: discord.Interaction, text: str):
        if text is None:
            embed = discord.Embed(
                title="Error",
                description="Please provide some text to convert.",
                color=discord.Color.red()
            )
            await interaction.response.send_message(embed=embed)
            logger.error('An error occurred: user does not provide a any text to convert in ASCII shadow format')
        else:

            try:
                result = pyfiglet.figlet_format(text, font='shadow')
                embed = discord.Embed(
                    title="ASCII Shadow Text",
                    description=f"```{result}```",
                    color=discord.Color.dark_blue()
                )
                await interaction.response.send_message(embed=embed)
                logger.info(f'Successfully converted {text} normal text to ASCII shadow')
            except discord.DiscordException as e:
                embed = discord.Embed(
                    title="Error ;-;",
                    description=f"An error occurred: {str(e)}",
                    color=discord.Color.red()
                )
                await interaction.response.send_message(embed=embed)
                logger.error(f'An error occurred: {e}')
            finally:
                logging.info('command executed')

    # ------------------------------
    # Speed text convertion
    # ------------------------------
    @bot.tree.command(name="speed", description="convert the normal text to ASCII styled speed text")
    async def speed_text(interaction: discord.Interaction, text: str):
        if text is None:
            embed = discord.Embed(
                title="Error",
                description="Please provide some text to convert.",
                color=discord.Color.red()
            )
            await interaction.response.send_message(embed=embed)
            logger.error('An error occurred: user does not provide a any text to convert in ASCII speed format')
        else:

            try:
                result = pyfiglet.figlet_format(text, font='speed')
                embed = discord.Embed(
                    title="ASCII Speed Text",
                    description=f"```{result}```",
                    color=discord.Color.dark_blue()
                )
                await interaction.response.send_message(embed=embed)
                logger.info(f'Successfully converted {text} normal text to ASCII speed')
            except  discord.DiscordException as e:
                embed = discord.Embed(
                    title="Error ;-;",
                    description=f"An error occurred: {str(e)}",
                    color=discord.Color.red()
                )
                await interaction.response.send_message(embed=embed)
                logger.error(f'An error occurred: {e}')
            finally:
                logging.info('command executed')

    # ------------------------------
    # Epic text convertion
    # ------------------------------
    @bot.tree.command(name="epic", description="convert the normal text to ASCII styled epic text")
    async def epic_text(interaction: discord.Interaction, text: str):
        if text is None:
            embed = discord.Embed(
                title="Error",
                description="Please provide some text to convert.",
                color=discord.Color.red()
            )
            await interaction.response.send_message(embed=embed)
            logger.error('An error occurred: user does not provide a any text to convert in ASCII epic format')
        else:

            try:
                result = pyfiglet.figlet_format(text, font='epic')
                embed = discord.Embed(
                    title="ASCII Epic Text",
                    description=f"```{result}```",
                    color=discord.Color.dark_blue()
                )
                await interaction.response.send_message(embed=embed)
                logger.info(f'Successfully converted {text} normal text to ASCII epic')
            except discord.DiscordException as e:
                embed = discord.Embed(
                    title="Error ;-;",
                    description=f"An error occurred: {str(e)}",
                    color=discord.Color.red()
                )
                await interaction.response.send_message(embed=embed)
                logger.error(f'An error occurred: {e}')
            finally:
                logging.info('command executed')

    # ------------------------------
    # Rectangles text convertion
    # ------------------------------
    @bot.tree.command(name="rectangles", description="convert the normal text to ASCII styled rectangles text")
    async def rectangles_text(interaction: discord.Interaction, text: str):
        if text is None:
            embed = discord.Embed(
                title="Error",
                description="Please provide some text to convert.",
                color=discord.Color.red()
            )
            await interaction.response.send_message(embed=embed)
            logger.error('An error occurred: user does not provide a any text to convert in ASCII rectangles format')
        else:

            try:
                result = pyfiglet.figlet_format(text, font='rectangles')
                embed = discord.Embed(
                    title="ASCII Rectangles Text",
                    description=f"```{result}```",
                    color=discord.Color.dark_blue()
                )
                await interaction.response.send_message(embed=embed)
                logger.info(f'Successfully converted {text} normal text to ASCII rectangles')
            except discord.DiscordException as e:
                embed = discord.Embed(
                    title="Error ;-;",
                    description=f"An error occurred: {str(e)}",
                    color=discord.Color.red()
                )
                await interaction.response.send_message(embed=embed)
                logger.error(f'An error occurred: {e}')
            finally:
                logging.info('command executed')

    # ------------------------------
    # Cosmic text convertion
    # ------------------------------
    # @bot.tree.command(name="cosmic", description="convert the normal text to ASCII styled cosmic text")
    # async def cosmic_text(interaction: discord.Interaction, text: str):
    #     try:
    #         result = pyfiglet.figlet_format(text, font='cosmic')
    #         embed = discord.Embed(
    #             title="ASCII Cosmic Text",
    #             description=f"{result}",
    #             color=discord.Color.dark_blue()
    #         )
    #         await interaction.response.send_message(embed=embed)
    #     except Exception as e:
    #         embed = discord.Embed(
    #             title="Error",
    #             description=f"An error occurred: {str(e)}",
    #             color=discord.Color.red()
    #         )
    #         await interaction.response.send_message(embed=embed)

    @bot.tree.command(name="bothelp", description="know about the bot")
    async def hel_cmd(interaction: discord.Interaction):
        help_desc = """
          **What bot does?**
          AsciiAce bot designed to convert the normal text to ASCII Text. Transform plain text into eye-catching ASCII Text in a variety of styles, perfect for adding flair to your messages and making your server more fun.

          **Available commands?**
           The default prefix for AsciiAce bot is `_`
           Use `_command_name yourtext` e.g. `_slant Hello` 

          Type ```/``` to see all available commands, each and every command perform best operation to convert the normal text to beautiful **ASCII** Text :)

          Bot invite: [AsciiAce invite](https://discord.com/oauth2/authorize?client_id=1300315132873801728)

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
        await interaction.response.send_message(embed=embed)
        logger.info('User used help command')

    @bot.tree.command(name='invite', description='get the bot invite link')
    async def invite_(interaction: discord.Interaction):
        embed = discord.Embed(
            title="AsciiAce invite",
            description="[Invite to your server](https://discord.com/oauth2/authorize?client_id=1300315132873801728)",
            color=discord.Color.dark_blue()
        )
        bot_avatar = bot.user.avatar.url if bot.user.avatar else bot.user.default_avatar.url
        embed.set_thumbnail(url=bot_avatar)
        await interaction.response.send_message(embed=embed)

    @bot.tree.command(name='ping', description='check bot latency')
    async def ping(interaction: discord.Interaction):
        await interaction.response.send_message(f'Pong! {round(bot.latency * 1000)}ms')

    # @bot.event
    # async def on_command_error(ctx, error):
    #     if isinstance(error, commands.CommandNotFound):
    #         await ctx.send("Sorry, I don't recognize that command.")
    #     else:
    #         await ctx.send("An error occurred while processing your command.")
