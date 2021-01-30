import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, PicklePersistence, CallbackQueryHandler

ACCESS_TOKEN = os.environ['JOB_FINDER_TOKEN']


def start(update, context):
    return "Hello"


def reply(update, context):
    return "not implemented yet"


def main():
    pass


if __name__ == '__main__':
    updater = Updater(token=ACCESS_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('info', start))
    dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), reply))
    updater.start_polling()
