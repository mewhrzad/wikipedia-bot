from .wiki import search
from telegram import Update,__version__ as TG_VER
from telegram.ext import ContextTypes


class Message:
    async def Text_Seperation(
        update: Update, context: ContextTypes.DEFAULT_TYPE
    ) -> None:
        try:
            result = await search(update.message.text)
            data = result[0]
            description = data[2].replace("None","")
            await update.message.reply_text(f"{data[0]}\n\n{description}\n\nمنبع : {data[3]}")
        except:
            await update.message.reply_text("نتیجه ای یافت نشد",reply_to_message_id=update.message.id)