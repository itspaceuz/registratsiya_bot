import sqlite3

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inlinekeyboardbuttons.callback_datas.callback import yangikurs_callback
from data.config import ADMIN_ID
from keyboards.inlinekeyboardbuttons import inlinekeyboardbutton
from keyboards.inlinekeyboardbuttons.callback_datas import callback
from loader import bot, dp, db
from keyboards.keyboardbuttons import keyboardbutton
from states.state import Registrator

KurslarArr = {"1": "Front-End", "2": "Python Back-End", "3": "C# Back-End", "4": "Python Telegram Bot",
              "5": "PHP Telegram Bot"}


@dp.message_handler(text="Kurslar ❗")
async def course(message: types.message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=f"1)Front-End\n2)Back-End\n3)Python basic\n4)C# basic",
                           reply_markup=inlinekeyboardbutton.courseinbutpack)


@dp.callback_query_handler(
    callback.course_callback.filter(course_name=("front_end", "back_end", "python_basic", "c#_basic")))
async def course_name(call: types.CallbackQuery, callback_data: dict):
    global course_name
    course_name = callback_data.get("course_name")
    if course_name == "front_end":
        # Bu oldingi xabarni udalit qiladi
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                   text="Siz Front End kursini tanladingiz:\n1-bo'lim:\nHTML\nCSS\nJS\n2-bo'lim\nReactJS",
                                   reply_markup=inlinekeyboardbutton.course_singpack)


    elif course_name == "back_end":
        await call.message.answer(
            text="Siz Back End kursini tanladingiz:\n1-bo'lim\nJS\nSQL\n2-bo'lim\nPostergsql\nSQLite",
            reply_markup=inlinekeyboardbutton.course_singpack)

    elif course_name == "python_basic":
        await call.message.answer(
            text="Siz Python basic kursini tanladingiz:"
                 "\n1-bo'lim\nAlgoritmlar\nKirish\n2-bo'lim\nFunksiyalar\nTayyor programma",
            reply_markup=inlinekeyboardbutton.course_singpack)

    elif course_name == "c#_basic":
        await call.message.answer(
            text="Siz C# basic kursini tanladingiz:"
                 "\n1-bo'lim\nAlgoritmlar\nKirish\n2-bo'lim\nFunksiyalar\nTayyor programma",
            reply_markup=inlinekeyboardbutton.course_singpack)

    # await call.message.answer("Siz")


# @dp.callback_query_handler(callback.course_callback)


@dp.callback_query_handler(callback.course_sing.filter(course_sing_name="course_sing_name"))
async def course_sing(call: types.CallbackQuery, state: FSMContext):
    if course_name == "front_end":
        course_group1 = course_name
        await state.update_data(course_group=course_group1)

        await call.message.answer(
            text="Siz Front End kursiga yozilyapsiz.\nRo'yxatdan o'tish uchun ism familiyangizni yozing:")
        await Registrator.all_name.set()

    elif course_name == "back_end":
        course_group1 = course_name
        await state.update_data(course_group=course_group1)

        await call.message.answer(
            text="Siz Back End kursiga yozilyapsiz.\nRo'yxatdan o'tish uchun ism familiyangizni yozing:")
        await Registrator.all_name.set()

    elif course_name == "python_basic":
        course_group1 = course_name
        await state.update_data(course_group=course_group1)

        await call.message.answer(
            text="Siz Python basic kursiga yozilyapsiz.\nRo'yxatdan o'tish uchun ism familiyangizni yozing:")
        await Registrator.all_name.set()

    elif course_name == "c#_basic":
        course_group1 = course_name
        await state.update_data(course_group=course_group1)

        await call.message.answer(
            text="Siz C# basic kursiga yozilyapsiz.\nRo'yxatdan o'tish uchun ism familiyangizni yozing:")
        await Registrator.all_name.set()


@dp.message_handler(state=Registrator.all_name)
async def all_name_def(message: types.Message, state: FSMContext):
    all_name1 = message.text
    await state.update_data(all_name=all_name1)

    await bot.send_message(message.chat.id, "Yashash viloyatingizni yozing:")
    await Registrator.area_name.set()


@dp.message_handler(state=Registrator.area_name)
async def area_name_def(message: types.Message, state: FSMContext):
    area_name1 = message.text
    await state.update_data(area_name=area_name1)

    await bot.send_message(message.chat.id, "O'qish turini tanlang:(online, ofline)")
    await Registrator.course_type.set()


@dp.message_handler(state=Registrator.course_type)
async def course_type_def(message: types.Message, state: FSMContext):
    course_type1 = message.text
    await state.update_data(course_type=course_type1)

    await bot.send_message(message.chat.id, "Telefon raqamingizni Berish uchun tugmani bosing",
                           reply_markup=keyboardbutton.keyphonepast)
    await Registrator.phone_number.set()


@dp.message_handler(state=Registrator.phone_number, content_types=types.ContentTypes.CONTACT)
async def phone_number(message: types.Message, state: FSMContext):
    phone_number1 = message.contact.phone_number
    await state.update_data(phone_number=phone_number1)
    data = await state.get_data()

    try:
        user_id = message.chat.id
        all_name = data.get("all_name")
        area_name = data.get("area_name")
        course_type = data.get("course_type")
        course_group = data.get("course_group")
        phone_number = data.get("phone_number")

        await bot.send_message(chat_id=ADMIN_ID, text=f"""IT-space
Ismi familiyasi: {all_name}
Yashash joyi: {area_name}
Kursning o'qish turi: {course_type}
Kursning nomi: {course_group}
Telefon raqami: {phone_number}""")
        db.add_user(id=user_id, allname=all_name, areaname=area_name, coursetype=course_type, coursegroup=course_group,
                    phonenumber=phone_number)
        await bot.send_message(message.chat.id, "Siz bilan 36 soat ichida bog'lanishadi")
    except sqlite3.IntegrityError as err:
        await bot.send_message(message.chat.id, "xatolik")
    await state.finish()


@dp.message_handler(text="Yangi kurs qo'shish")
async def yangikurs(message: types.message):
    user = db.select_user(id=message.chat.id)
    print(user)
    s = str(user[4])
    a = []
    z = ("front_end", "back_end", "python_basic", "c#_basic")
    await bot.send_message(message.chat.id, text=f"siz azo bo'lgan kurslar\n{s}")
    n = 0
    while not (n == -1):
        n = s.find("\n", 0, len(s))
        # print(n)
        if n != -1:
            a.append(s[0:n])
            print(a)
            s = s[n + 1:len(s)]
            print(s)
    a.append(s)
    print(a)
    b = ""
    c = 0
    for i in z:
        c = c + 1
        if not (i in a):
            b = b + '\n' + str(c) + ")" + i
    print(f"siz azo bo'lmagan kurslar{b}")
    await bot.send_message(message.chat.id, f"siz azo bo'lmagan kurslar{b}")
    courseinbut0 = InlineKeyboardButton(text="1.",
                                        callback_data=yangikurs_callback.new(yangikurs_callback_name="front_end"))
    courseinbut1 = InlineKeyboardButton(text="2.",
                                        callback_data=yangikurs_callback.new(yangikurs_callback_name="back_end"))
    courseinbut2 = InlineKeyboardButton(text="3.",
                                        callback_data=yangikurs_callback.new(yangikurs_callback_name="python_basic"))
    courseinbut3 = InlineKeyboardButton(text="4.",
                                        callback_data=yangikurs_callback.new(yangikurs_callback_name="c#_basic"))

    courseinbutpack = InlineKeyboardMarkup(row_width=2)

    if not (s == "front_end"):
        courseinbutpack.add(courseinbut0)

    if not (s == "back_end"):
        courseinbutpack.add(courseinbut1)

    if not (s == "python_basic"):
        courseinbutpack.add(courseinbut2)

    if not (s == "c#_basic"):
        courseinbutpack.add(courseinbut3)

    await bot.send_message(message.chat.id, f"siz azo bo'lmagan kurslar{b}", reply_markup=courseinbutpack)
