#https://www.geeksforgeeks.org/create-a-telegram-bot-using-python/

from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

updater = Updater("5577790947:AAElSajx49QK1Tayyq9ZWVLQbNwLyTSjXHM",
				use_context=True)


def start(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Welcome to rufus10 bot, the king of LN Markets trading bots.")

def help(update: Update, context: CallbackContext):
    update.message.reply_text("This bot uses Trading View technical indicators to get a buy, sell or neutral recommendantion on XBTUSD")

def twitter_url(update: Update, context: CallbackContext):
	update.message.reply_text("https://twitter.com/LNMarkets")


def telegram_url(update: Update, context: CallbackContext):
	update.message.reply_text("https://t.me/lnmarkets")

def unknown_text(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Sorry I can't recognize you , you said '%s'" % update.message.text)

def unknown(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Sorry '%s' is not a valid command" % update.message.text)





updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('twitter', twitter_url))
updater.dispatcher.add_handler(CommandHandler('telegram', telegram_url))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
# Filters out unknown commands
updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))

# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

updater.start_polling()

