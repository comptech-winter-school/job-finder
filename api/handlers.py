import logging
import sys
from models import BaselineIndexer, FaissIndexer
from models import RandomEmbedder

logger = logging.getLogger()
logger.level = logging.DEBUG
logger.addHandler(logging.StreamHandler(sys.stderr))


# start -> make_decision -> enter_the_text -> indexing

def start(update, context):
    context.bot.sendMessage(chat_id=update.message.chat_id,
                            text='Здравствуйте!\n'
                                 'Для выбора режима работы нажмите вакансия или резюме')
    make_decision(update, context)
    logger.debug(update.message)


def enter_the_text(update, context):
    context.bot.sendMessage(chat_id=update.message.chat_id, text='Сделайте выбор')
    indexing(update, context)
    logger.debug(update.message)


def indexing(update, context):
    context.bot.sendMessage(chat_id=update.message.chat_id,
                            text=BaselineIndexer(RandomEmbedder).get_nearest_k(update.message.text))
    logger.debug(update.message)


def make_decision(update, context):
    from telegram import ReplyKeyboardMarkup, KeyboardButton
    keyboard = ReplyKeyboardMarkup([[KeyboardButton(text='Вакансия'), KeyboardButton(text='Резюме')]],
                                   resize_keyboard=True)
    context.bot.sendMessage(chat_id=update.message.chat_id, reply_markup=keyboard, text='Ваш выбор?')
