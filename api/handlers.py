import logging
import sys
from models import BaselineIndexer, FaissIndexer
from models import RandomEmbedder

logger = logging.getLogger()
logger.level = logging.DEBUG
logger.addHandler(logging.StreamHandler(sys.stderr))
STATE = 0


# start -> make_decision -> enter_the_text -> indexing

def start(update, context):
    context.bot.sendMessage(chat_id=update.message.chat_id,
                            text='Здравствуйте!\n'
                                 'Для выбора режима работы нажмите вакансия или резюме')
    make_decision(update, context)
    logger.debug(update.message)


def enter_the_text(update, context):
    global STATE
    context.bot.sendMessage(chat_id=update.message.chat_id, text='Введите текст')
    logger.debug(update.message.text)
    STATE = 1


def make_decision(update, context):
    from telegram import ReplyKeyboardMarkup, KeyboardButton
    keyboard = ReplyKeyboardMarkup([[KeyboardButton(text='Вакансия'), KeyboardButton(text='Резюме')]],
                                   resize_keyboard=True)
    context.bot.sendMessage(chat_id=update.message.chat_id, reply_markup=keyboard, text='Ваш выбор?')


def get_k_items(update, context):
    global STATE
    if STATE == 1:
        indexer = FaissIndexer(RandomEmbedder())
        indexer.build(update.message.text.split(' '))
        context.bot.sendMessage(chat_id=update.message.chat_id,
                                text=str(indexer.get_nearest_k(update.message.text)))
    else:
        pass
