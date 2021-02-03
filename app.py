import os
import sys
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, PicklePersistence, CallbackQueryHandler
from api import start, enter_the_text



if __name__ == '__main__':
    ACCESS_TOKEN = '1662109088:AAE0QtQTQNBnzgWMueHwnKtZ6w8STAlMkK8'
    updater = Updater(token=ACCESS_TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('info', start))
    dispatcher.add_handler(MessageHandler(Filters.text('Вакансия'), enter_the_text))
    # dispatcher.add_handler(CommandHandler('get', ))
    updater.start_polling()
