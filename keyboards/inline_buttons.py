from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

async def start_menu_keyboard():
    markup = InlineKeyboardMarkup()
    questionnaire_button = InlineKeyboardButton(
        "Start Questionnaire",
        callback_data="start_questionnaire"
    )
    markup.add(questionnaire_button)
    return markup

async def start_questionnaire_keyboard(options):
    markup = InlineKeyboardMarkup()
    for option in options:
        button = InlineKeyboardButton(option, callback_data=option.lower())
        markup.add(button)
    return markup
