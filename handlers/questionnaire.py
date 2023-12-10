import sqlite3

from aiogram import types, Dispatcher
from config import bot
from keyboards import inline_buttons

questions = {
    "Mercedes or BMW": ["Mercedes", "BMW"],
    "Android or Ios": ["Android", "Ios"],
    "Samsung or Xiaomi": ["Samsung", "Xiaomi"]
}


async def start_questionnaire_call(call: types.CallbackQuery):
    for question, options in questions.items():
        await bot.send_message(
            chat_id=call.from_user.id,
            text=question,
            reply_markup=await inline_buttons.start_questionnaire_keyboard(options)
        )
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Mercedes or BMW",
        reply_markup=await inline_buttons.start_questionnaire_keyboard()
    )
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Android or Ios",
        reply_markup=await inline_buttons.start_questionnaire_keyboard()
    )
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Samsung or Xiaomi",
        reply_markup=await inline_buttons.start_questionnaire_keyboard()
    )

async def mercedes_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Mercedes is a good car",
    )

async def bmw_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="BMW is normal car",
    )


async def android_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Good taste"
    )

async def ios_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="The perfect taste"
    )


async def samsung_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Worthy"
    )

async def xiaomi_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Such a thing"
    )


def register_questionnaire_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(start_questionnaire_call,
                                       lambda call: call.data == "start_questionnaire")
    dp.register_callback_query_handler(mercedes_call,
                                       lambda call: call.data == "mercedes")
    dp.register_callback_query_handler(bmw_call,
                                       lambda call: call.data == "bmw")
    dp.register_callback_query_handler(android_call,
                                       lambda call: call.data == "android")
    dp.register_callback_query_handler(ios_call,
                                       lambda call: call.data == "ios")
    dp.register_callback_query_handler(samsung_call,
                                       lambda call: call.data == "samsung")
    dp.register_callback_query_handler(xiaomi_call,
                                       lambda call: call.data == "xiaomi")
