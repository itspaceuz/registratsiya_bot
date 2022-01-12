from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from keyboards.inlinekeyboardbuttons.callback_datas.callback import course_callback, course_sing

cancelbutton = InlineKeyboardButton(text="orqaga", callback_data=course_callback.new("cancel"))

courseinbut0 = InlineKeyboardButton(text="1.", callback_data=course_callback.new(course_name="front_end"))
courseinbut1 = InlineKeyboardButton(text="2.", callback_data=course_callback.new(course_name="back_end"))
courseinbut2 = InlineKeyboardButton(text="3.", callback_data=course_callback.new(course_name="python_basic"))
courseinbut3 = InlineKeyboardButton(text="4.", callback_data=course_callback.new(course_name="c#_basic"))
courseinbutpack = InlineKeyboardMarkup(row_width=2).add(courseinbut0, courseinbut1)
courseinbutpack.add(courseinbut2, courseinbut3)

course_sing = InlineKeyboardButton(text="Kursga yozilish",
                                   callback_data=course_sing.new(course_sing_name="course_sing_name"))
course_singpack = InlineKeyboardMarkup(row_width=1).add(course_sing)
course_singpack.add(cancelbutton)
