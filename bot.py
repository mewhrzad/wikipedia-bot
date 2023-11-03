from text_messages import Message
from inline_query import inline_query
from telegram import Update, __version__ as TG_VER
import os
from dotenv import load_dotenv
load_dotenv("bot_token.env")
TOKEN = os.getenv('BOT_TOKEN')
from telegram import __version_info__

# except ImportError:e
#     __version_info__ = (0, 0, 0, 0, 0)  # type: ignore[assignment]

if __version_info__ < (20, 0, 0, "alpha", 1):
    raise RuntimeError(
        f"This example is not compatible with your current PTB version {TG_VER}. To view the "
        f"{TG_VER} version of this example, "
        f"visit https://docs.python-telegram-bot.org/en/v{TG_VER}/examples.html"
    )
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
    CallbackQueryHandler,
    InlineQueryHandler,
)

async def start(update : Update , context : ContextTypes.DEFAULT_TYPE)->None:
    await update.message.reply_markdown("""سلام به ربات ویکی پدیا خوش اومدی

به 2 روش میتونی اینجا سرچ کنی

1 - ارسال متن سرچ توی چت ربات

2 - تایپ کردن آیدی ربات و Query زدن

`@fawikipedia_bot آدولف`

`@fawikipedia_bot Austrian Painter`

منبع تمامی سرچ ها : wikipedia.org""")


def main() -> None:
    application = (
        Application.builder()
        .token(TOKEN)
        .build()
    )
    application.add_handler(
        MessageHandler(filters.TEXT & ~(filters.COMMAND), Message.Text_Seperation)
    )
    application.add_handler(CommandHandler("start",start))
    application.add_handler(InlineQueryHandler(inline_query))
    application.run_polling()


if __name__ == "__main__":
    main()