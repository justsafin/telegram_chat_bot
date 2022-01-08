from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from conf import bot_token
import os
import logging
import value_evaluating

API_TOKEN = os.getenv("TELEGRAM_API_TOKEN")
bot = Bot(token = API_TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

@dp.inline_handler()
async def inline_handler(query: types.InlineQuery):
    user_id = query.from_user.id
    articles = [types.InlineQueryResultArticle(id = 1,
                                title = 'Check depression level',
                                input_message_content=types.InputTextMessageContent(message_text=value_evaluating.depr_evaluate(user_id))),
                types.InlineQueryResultArticle(id = 2,
                                title = 'Share cock size',
                                input_message_content=types.InputTextMessageContent(message_text=value_evaluating.cock_evaluate(user_id))),
                types.InlineQueryResultArticle(id = 3,
                                title = 'How gay are you',
                                input_message_content=types.InputTextMessageContent(message_text=value_evaluating.gay_rate_evaluate(user_id)))
                ]
    await query.answer(articles, cache_time=1, is_personal=True)

executor.start_polling(dp, skip_updates=True)