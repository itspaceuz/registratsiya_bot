from aiogram import types

from loader import dp


@dp.message_handler(commands="start")
async def tony(message: types.Message):
    await message.answer(" ")
    