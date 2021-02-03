import os
import sys
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, PicklePersistence, CallbackQueryHandler
from api import start, enter_the_text, get_k_items

if __name__ == '__main__':
    ACCESS_TOKEN = os.environ['TOKEN']
    updater = Updater(token=ACCESS_TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('info', start))
    dispatcher.add_handler(MessageHandler(Filters.text('Вакансия'), enter_the_text))
    dispatcher.add_handler(MessageHandler(Filters.text, get_k_items))

    updater.start_polling()
