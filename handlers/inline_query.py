from uuid import uuid4
from telegram import InlineQueryResultArticle, InputTextMessageContent, __version__ as TG_VER, Update
from telegram.ext import ContextTypes
from .wiki import search

async def inline_query(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.inline_query.query
    if not query:
        return
    results = await search(query)
    output = []
    for data in results:
        output.append(
            InlineQueryResultArticle(
                id=str(uuid4()),
                title=data[0],
                input_message_content=InputTextMessageContent(
                    message_text=f"{data[0]} : {data[3]}"
                ),
                description=data[2],
                thumbnail_url=data[1],
            )
        )
    await update.inline_query.answer(output)