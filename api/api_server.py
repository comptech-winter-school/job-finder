import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, PicklePersistence, CallbackQueryHandler

ACCESS_TOKEN = '1662109088:AAE0QtQTQNBnzgWMueHwnKtZ6w8STAlMkK8'


def start(update, context):
    updater.bot.sendMessage(chat_id=update.message.chat_id, text='Здравствуйте')




def reply(update, context):
    updater.bot.sendMessage(chat_id=update.message.chat_id, text='test')


def main():
    pass


if __name__ == '__main__':
    updater = Updater(token=ACCESS_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('info', start))
    dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), reply))
    updater.start_polling()
