import os
import sys
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, PicklePersistence, CallbackQueryHandler

ACCESS_TOKEN = 'TOKEN'

def start(update, context):
    context.bot.sendMessage(chat_id=update.message.chat_id, text='Здравствуйте')


def reply(update, context):
    context.bot.sendMessage(chat_id=update.message.chat_id, text=update.message.text)


def main():
    pass


if __name__ == '__main__':
    updater = Updater(token=ACCESS_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('info', start))
    dispatcher.add_handler(MessageHandler(Filters.text, reply))
    updater.start_polling()
    logger = logging.getLogger()
    logger.level = logging.DEBUG
    logger.addHandler(logging.StreamHandler(sys.stderr))
