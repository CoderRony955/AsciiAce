from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import pyfiglet


# ----------------------------------
# 3d text conversion
# ----------------------------------
async def three_d(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = ' '.join(context.args)

    if not text:
        await update.message.reply_text("Please provide some text to convert to ASCII art.")
        return

    try:
        result = pyfiglet.figlet_format(text, font='doh')
        await update.message.reply_text(f"```\n{result}\n```", parse_mode='Markdown')
    except Exception as e:
        await update.message.reply_text(f"An error occurred: {str(e)}")


# ----------------------------------
# Slant text conversion
# ----------------------------------
async def slant(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = ' '.join(context.args)
    if not text:
        await update.message.reply_text("Please provide some text to convert to ASCII art.")
        return
    try:
        result = pyfiglet.figlet_format(text, font='slant')
        await update.message.reply_text(f"```\n{result}\n```", parse_mode='Markdown')
    except Exception as e:
        await update.message.reply_text(f"An error occurred: {str(e)}")


# ----------------------------------
# Doom text conversion
# ----------------------------------
async def doom(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = ' '.join(context.args)

    if not text:
        await  update.message.reply_text("Please provide some text to convert to ASCII art.")
    try:
        result = pyfiglet.figlet_format(text, font='doom')
        await update.message.reply_text(f"```\n{result}\n```", parse_mode='Markdown')
    except Exception as e:
        await update.message.reply_text(f"An error occurred: {str(e)}")


# ----------------------------------
# Alphabet text conversion
# ----------------------------------
async def alphabet(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = ' '.join(context.args)
    if not text:
        await update.message.reply_text("Please provide some text to convert to ASCII art.")

    try:
        result = pyfiglet.figlet_format(text, font='alphabet')
        await update.message.reply_text(f"```\n{result}\n```", parse_mode='Markdown')
    except Exception as e:
        await update.message.reply_text(f"An error occurred: {str(e)}")


# ----------------------------------
# banner text conversion
# ----------------------------------
async def banner(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = ' '.join(context.args)
    if not text:
        await update.message.reply_text("Please provide some text to convert to ASCII art.")
    try:
        result = pyfiglet.figlet_format(text, font='banner3-d')
        await update.message.reply_text(f"```\n{result}\n```", parse_mode='Markdown')
    except Exception as e:
        await update.message.reply_text(f"An error occurred: {str(e)}")


# ----------------------------------
# doh text conversion
# ----------------------------------
async def doh(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = ' '.join(context.args)
    if not text:
        await update.message.reply_text("Please provide some text to convert to ASCII art.")

    try:
        result = pyfiglet.figlet_format(text, font='doh')
        await update.message.reply_text(f"```\n{result}\n```", parse_mode='Markdown')
    except Exception as e:
        await update.message.reply_text(f"An error occurred: {str(e)}")


# ----------------------------------
# isometric1 text conversion
# ----------------------------------
async def isometric(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = ' '.join(context.args)
    if not text:
        await update.message.reply_text("Please provide some text to convert to ASCII art.")

    try:
        result = pyfiglet.figlet_format(text, font='isometric1')
        await update.message.reply_text(f"```\n{result}\n```", parse_mode='Markdown')
    except Exception as e:
        await update.message.reply_text(f"An error occurred: {str(e)}")


# Define a handler to echo any message the user sends
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(update.message.text)


# ----------------------------------
# starwars text conversion
# ----------------------------------
async def starwars(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = ' '.join(context.args)
    if not text:
        await update.message.reply_text("Please provide some text to convert to ASCII art.")

    try:
        result = pyfiglet.figlet_format(text, font='starwars')
        await update.message.reply_text(f"```\n{result}\n```", parse_mode='Markdown')
    except Exception as e:
        await update.message.reply_text(f"An error occurred: {str(e)}")


# ----------------------------------
# block text conversion
# ----------------------------------
async def block(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = ' '.join(context.args)
    if not text:
        await update.message.reply_text("Please provide some text to convert to ASCII art.")

    try:
        result = pyfiglet.figlet_format(text, font='block')
        await update.message.reply_text(f"```\n{result}\n```", parse_mode='Markdown')
    except Exception as e:
        await update.message.reply_text(f"An error occurred: {str(e)}")


# ----------------------------------
# digital text conversion
# ----------------------------------
async def digital(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = ' '.join(context.args)
    if not text:
        await update.message.reply_text("Please provide some text to convert to ASCII art.")

    try:
        result = pyfiglet.figlet_format(text, font='digital')
        await update.message.reply_text(f"```\n{result}\n```", parse_mode='Markdown')
    except Exception as e:
        await update.message.reply_text(f"An error occurred: {str(e)}")


# ----------------------------------
# shadow text conversion
# ----------------------------------
async def shadow(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = ' '.join(context.args)
    if not text:
        await update.message.reply_text("Please provide some text to convert to ASCII art.")

    try:
        result = pyfiglet.figlet_format(text, font='shadow')
        await update.message.reply_text(f"```\n{result}\n```", parse_mode='Markdown')
    except Exception as e:
        await update.message.reply_text(f"An error occurred: {str(e)}")


# ----------------------------------
# speed text conversion
# ----------------------------------
async def speed(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = ' '.join(context.args)
    if not text:
        await update.message.reply_text("Please provide some text to convert to ASCII art.")

    try:
        result = pyfiglet.figlet_format(text, font='speed')
        await update.message.reply_text(f"```\n{result}\n```", parse_mode='Markdown')
    except Exception as e:
        await update.message.reply_text(f"An error occurred: {str(e)}")


# ----------------------------------
# epic text conversion
# ----------------------------------
async def epic(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = ' '.join(context.args)
    if not text:
        await update.message.reply_text("Please provide some text to convert to ASCII art.")

    try:
        result = pyfiglet.figlet_format(text, font='epic')
        await update.message.reply_text(f"```\n{result}\n```", parse_mode='Markdown')
    except Exception as e:
        await update.message.reply_text(f"An error occurred: {str(e)}")


# ----------------------------------
# rectangles text conversion
# ----------------------------------
async def rectangles(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = ' '.join(context.args)
    if not text:
        await update.message.reply_text("Please provide some text to convert to ASCII art.")

    try:
        result = pyfiglet.figlet_format(text, font='rectangles')
        await update.message.reply_text(f"```\n{result}\n```", parse_mode='Markdown')
    except Exception as e:
        await update.message.reply_text(f"An error occurred: {str(e)}")


# ----------------------------------
# cosmic text conversion
# ----------------------------------
async def cosmic_text(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = ' '.join(context.args)
    if not text:
        await update.message.reply_text("Please provide some text to convert to ASCII art.")

    try:
        result = pyfiglet.figlet_format(text, font='cosmic')
        await update.message.reply_text(f"```\n{result}\n```", parse_mode='Markdown')
    except Exception as e:
        await update.message.reply_text(f"An error occurred: {str(e)}")
