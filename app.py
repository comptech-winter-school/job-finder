import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, PicklePersistence, CallbackQueryHandler
from api.handlers import get_k_items, get_full_job_text, start_and_info

if __name__ == '__main__':
    ACCESS_TOKEN = os.environ['JOB_FINDER_TOKEN']
    updater = Updater(token=ACCESS_TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler(['start', 'info'], start_and_info))
    dispatcher.add_handler(CallbackQueryHandler(get_full_job_text))
    dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), get_k_items
                                          ))
    dispatcher.add_handler(MessageHandler(Filters.document, get_k_items))


    updater.start_polling()
