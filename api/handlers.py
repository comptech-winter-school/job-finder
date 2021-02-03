import logging
import sys
import time
from models import BaselineIndexer, FaissIndexer
from telegram import ReplyKeyboardMarkup, KeyboardButton
from models import RandomEmbedder
import pandas as pd
from .model_controller import get_answer

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
    STATE = 0


def enter_the_text(update, context):
    global STATE
    context.bot.sendMessage(chat_id=update.message.chat_id, text='Введите текст')
    logger.debug(update.message.text)
    STATE = 1


def make_decision(update, context):
    keyboard = ReplyKeyboardMarkup([[KeyboardButton(text='Вакансия'), KeyboardButton(text='Резюме')]],
                                   resize_keyboard=True)
    context.bot.sendMessage(chat_id=update.message.chat_id, reply_markup=keyboard, text='Ваш выбор?')


def get_k_items(update, context):
    global STATE
    if STATE:
        jobs = get_answer(update.message.text)
        for elem in jobs:
            context.bot.sendMessage(chat_id=update.message.chat_id,
                                    text=elem)
            time.sleep(2)
        STATE = 0
    else:
        pass
