from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from all_funcs import (
    three_d,
    slant,
    doom,
    alphabet,
    doh,
    epic,
    speed,
    cosmic_text,
    block,
    digital,
    shadow,
    isometric,
    starwars,
    rectangles,
    banner,
    echo)

#-------------------------------------------------------------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Hey there! I'm, ASCIIACE. Bot which converts text to ASCII art. So what are you waiting for? let's create ASCII art!")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("""
    What bot does?
    AsciiAce bot designed to convert the normal text to ASCII Text. Transform plain text into eye-catching ASCII Text in a variety of styles, perfect for adding flair to your messages and making your server more fun.
    
    Available commands?
    Type / to see all available commands, each and every command perform best operation to convert the normal text to beautiful ASCII Text :)
    
    |A|s|c|i|i|A|c|e|
    +-+-+-+-+-+-+-+-+
    
    """)


# ********************************************************************************************************************************


# Main function to start the bot
def main():
    app = ApplicationBuilder().token("BOT_TOKEN").build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("3d", three_d))
    app.add_handler(CommandHandler("slant", slant))
    app.add_handler(CommandHandler("doom", doom))
    app.add_handler(CommandHandler("alphabet", alphabet))
    app.add_handler(CommandHandler("banner", banner))
    app.add_handler(CommandHandler("doh", doh))
    app.add_handler(CommandHandler("isometric1", isometric))
    app.add_handler(CommandHandler("starwars", starwars))
    app.add_handler(CommandHandler("block", block))
    app.add_handler(CommandHandler("digital", digital))
    app.add_handler(CommandHandler("shadow", shadow))
    app.add_handler(CommandHandler("speed", speed))
    app.add_handler(CommandHandler("epic", epic))
    app.add_handler(CommandHandler("rectangles", rectangles))
    app.add_handler(CommandHandler("cosmic", cosmic_text))

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    app.run_polling()


if __name__ == "__main__":
    main()
