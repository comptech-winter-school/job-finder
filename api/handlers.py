import logging
import sys
from api.model_controller import get_answer
from telegram import InlineKeyboardMarkup
from telegram import InlineKeyboardButton
from datetime import datetime
from scripts.text_utils import get_text_from_file


logger = logging.getLogger('BOT')

logger.level = logging.DEBUG
logger.addHandler(logging.StreamHandler(sys.stderr))
fh = logging.FileHandler('BOX.log')
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)

JOBS_QUANTITY = 5


# start -> make_decision -> enter_the_text -> indexing

def start(update, context):
    context.bot.sendMessage(chat_id=update.message.chat_id,
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
    if update.message.attachments:
        file= update.message.attachments[0]
        resume_path= f'data/output/bot_resumes/{file.filename}'
        file.save_to_dir(resume_path)
        text_resume = get_text_from_file(resume_path)
    else:   
        text_resume = update.message.text
    text_jobs, date_jobs = get_answer(text_resume, JOBS_QUANTITY)
    buttons = [[[InlineKeyboardButton('Подробнее', callback_data=f's{i}')]] for i in
               range(JOBS_QUANTITY)]  # create button 'Подробнее' for each job
    cut_text_jobs = ['\n'.join(elem.split('\n')[:6]) for elem in text_jobs]
    context.user_data['user_id'] = update.message.chat_id
    for full_job, cut_job, button, date in zip(text_jobs, cut_text_jobs, buttons, date_jobs):
        update.message.reply_text(
            '\n' + f'{datetime.utcfromtimestamp(float(date)).strftime("%Y-%m-%d")}' + '\n' + f'{cut_job}',
            reply_markup=InlineKeyboardMarkup(button))
        context.user_data[button[0][0].callback_data] = full_job
    logger.debug(update.message)


def get_full_job_text(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=context.user_data[str(query.data)])
    logger.debug(update.message)
