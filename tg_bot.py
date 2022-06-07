# https://docs.python-telegram-bot.org/en/v20.0a0/
# https://github.com/python-telegram-bot/v13.x-wiki/wiki
# https://github.com/python-telegram-bot/v13.x-wiki/wiki/Introduction-to-the-API


#Link to the bot: https://telegram.me/rufus10bot
#TOKEN = '5577790947:AAElSajx49QK1Tayyq9ZWVLQbNwLyTSjXHM'



# import telegram

# bot = telegram.Bot(token=TOKEN)

# print(bot.get_me())

# updates = bot.get_updates()

# print(updates[0], updates[1])

import logging
from telegram import Update
from telegram.ext import Updater, CallbackContext, CommandHandler
from telegram.ext import MessageHandler, Filters

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

TOKEN = '5577790947:AAElSajx49QK1Tayyq9ZWVLQbNwLyTSjXHM'

updater = Updater(token=TOKEN)

dispatcher = updater.dispatcher


def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

start_handler = CommandHandler('start', start)

#as soon as you add new handlers to dispatcher, they are in effect
dispatcher.add_handler(start_handler)

#start the bot
updater.start_polling()


def echo(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)

dispatcher.add_handler(echo_handler)

def caps(update: Update, context: CallbackContext):
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

caps_handler = CommandHandler('caps', caps)
dispatcher.add_handler(caps_handler)

from telegram import InlineQueryResultArticle, InputTextMessageContent

def inline_caps(update: Update, context: CallbackContext):
    query = update.inline_query.query
    if not query:
        return
    results = []
    results.append(
        InlineQueryResultArticle(
            id=query.upper(),
            title='Caps',
            input_message_content=InputTextMessageContent(query.upper())
        )
    )
    context.bot.answer_inline_query(update.inline_query.id, results)

from telegram.ext import InlineQueryHandler
inline_caps_handler = InlineQueryHandler(inline_caps)
dispatcher.add_handler(inline_caps_handler)

def unknown(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")

unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)

updater.idle()

updater.stop()

