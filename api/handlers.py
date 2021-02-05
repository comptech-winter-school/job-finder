import logging
import sys
import time
from telegram import ReplyKeyboardMarkup, KeyboardButton
from api.model_controller import get_answer
from api.inline_buttons import buttons
from telegram import InlineKeyboardMarkup

logger = logging.getLogger('BOT')

logger.level = logging.DEBUG
logger.addHandler(logging.StreamHandler(sys.stderr))
fh = logging.FileHandler('BOX.log')
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)


# start -> make_decision -> enter_the_text -> indexing

def start(update, context):
    hello = context.bot.sendMessage(chat_id=update.message.chat_id,
                                    text='Здравствуйте!\n'
                                         'Введите текст :)')
    logger.debug(update.message)


# def enter_the_text(update, context):
#     text_resume = update.message.text
#     logger.debug(update.message.text)


# def make_decision(update, context):
#     keyboard = ReplyKeyboardMarkup([[KeyboardButton(text='Вакансия'), KeyboardButton(text='Резюме')]],
#                                    resize_keyboard=True)
#     context.bot.sendMessage(chat_id=update.message.chat_id, reply_markup=keyboard, text='Ваш выбор?')


def get_k_items(update, context):
    text_resume = update.message.text
    text_jobs, date_jobs = get_answer(text_resume)
    cut_text_jobs = ['\n'.join(elem.split('\n')[:6]) for elem in text_jobs]
    context.bot_data['user_id'] = update.message.chat_id
    for full_job, cut_job, button in zip(text_jobs, cut_text_jobs, buttons):
        update.message.reply_text(cut_job, reply_markup=InlineKeyboardMarkup(button))
        context.user_data[button[0][0].callback_data] = full_job
    logger.debug(update.message)


def get_full_job_text(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=context.user_data[str(query.data)])
    logger.debug(update.message)
