from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inlinekeyboardbuttons.callback_datas.callback import yangikurs_callback
from loader import bot, dp, db


@dp.message_handler(text="Mening ma'lumotlarim ❗")
async def malumotlar(message: types.Message):
    user = db.select_user(id=message.chat.id)
    await bot.send_message(message.chat.id, text=f"""Bu sizning malumotlaringiz:
Sizning ism familiyangiz: {user[1]}
Sizning yashash joyingiz: {user[2]}
Sizning kursning o'qish turingiz: {user[3]}
Sizning telefon raqamingiz: {user[5]}""")


@dp.message_handler(text="Mening kurslarim ❗")
async def kurslar(message: types.Message):
    await bot.send_message(message.chat.id, "Sizning kurslaringgiz")
    user = db.select_user(id=message.chat.id)
    c0 = str()
    s0 = str(user[4])
    n0 = 0
    while not (n0 == -1):
        r0 = len(s0)
        n0 = s0.find("$", 0, r0)
        if n0 != -1:
            c0 += "\n" + s0[:n0]
            s0 = s0[n0 + 1: r0]
            print("Birinchi cccc: ", c0)
        else:
            c0 += "\n" + s0[0:]
            print("ikkinchi cccc:", c0)

    await bot.send_message(message.chat.id, f"Bu sizning yozilgan kurslaringiz:{c0}")


@dp.message_handler(text="Yangi kursga yozilish ❗")
async def yangikurs(message: types.Message):
    await message.answer("Yangi kursga yozilish")
    user = db.select_user(id=message.chat.id)
    await message.answer(f"Siz yozilgan kurlar:{user[4]}")
    s = str(user[4])
    a = list()
    z = ("front_end", "back_end", "python_basic", "c#_basic")
    n = 0
    while not (n == -1):
        r = len(s)
        n = s.find("$", 0, r)
        if n != -1:
            a.append(s[0:n])
            s = s[n + 1:r]

    a.append(s)
    b = ""
    c = 0
    for i in z:
        c = c + 1
        if not (i in a):
            b = b + '\n' + str(c) + ")" + i

    courseinbut0 = InlineKeyboardButton(text="1.",
                                        callback_data=yangikurs_callback.new(yangikurs_callback_name="front_end"))
    courseinbut1 = InlineKeyboardButton(text="2.",
                                        callback_data=yangikurs_callback.new(yangikurs_callback_name="back_end"))
    courseinbut2 = InlineKeyboardButton(text="3.",
                                        callback_data=yangikurs_callback.new(
                                            yangikurs_callback_name="python_basic"))
    courseinbut3 = InlineKeyboardButton(text="4.",
                                        callback_data=yangikurs_callback.new(yangikurs_callback_name="c#_basic"))

    courseinbutpack = InlineKeyboardMarkup(row_width=2)

    if not ("front_end" in a):
        courseinbutpack.add(courseinbut0)

    if not ("back_end" in a):
        courseinbutpack.add(courseinbut1)

    if not ("python_basic" in a):
        courseinbutpack.add(courseinbut2)

    if not ("c#_basic" in a):
        courseinbutpack.add(courseinbut3)

    await message.answer(f"Siz azo bo'lmagan kurslar:{b}", reply_markup=courseinbutpack)


@dp.callback_query_handler(
    yangikurs_callback.filter(yangikurs_callback_name=("front_end", "back_end", "python_basic", "c#_basic")))
async def kurs_qoshish(call: types.CallbackQuery, callback_data: dict):
    kurs_name = callback_data.get("yangikurs_callback_name")
    user = db.select_user(id=call.message.chat.id)
    if kurs_name == "front_end":
        kurs_name0 = user[4] + "$" + kurs_name
        print(kurs_name0)

        db.update_coursegroup(coursegroup=kurs_name0, id=call.message.chat.id)
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                    text="Siz Front End kursiga yozildingiz❗❗❗")

    if kurs_name == "back_end":
        kurs_name0 = user[4] + "$" + kurs_name
        db.update_coursegroup(coursegroup=kurs_name0, id=call.message.chat.id)
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                    text="Siz Back End kursiga yozildingiz❗❗❗")

    if kurs_name == "python_basic":
        kurs_name0 = user[4] + "$" + kurs_name
        db.update_coursegroup(coursegroup=kurs_name0, id=call.message.chat.id)
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                    text="Siz Python basic kursiga yozildingiz❗❗❗")

    if kurs_name == "c#_basic":
        kurs_name0 = user[4] + "$" + kurs_name
        db.update_coursegroup(coursegroup=kurs_name0, id=call.message.chat.id)
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                    text="Siz C# basic kursiga yozildingiz❗❗❗")
