from aiogram import types

from keyboards.keyboardbuttons import keyboardbutton
from loader import bot, dp


@dp.message_handler(commands="start")
async def send_welcome(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text="<s>Welcome</s>", parse_mode=types.ParseMode.HTML)
    await message.answer(
        f"Assalomu aleykum {message.from_user.first_name}, Bu bot <b>IT-SPACE</b> maktab inovatsion kurslariga yozilishingiz mumkin",
        parse_mode="HTML", reply_markup=keyboardbutton.welcomepack)


@dp.message_handler(commands="menu")
async def menu(message: types.Message):
    await bot.send_message(message.chat.id, "Bu botning menyusi", reply_markup=keyboardbutton.menupast)
