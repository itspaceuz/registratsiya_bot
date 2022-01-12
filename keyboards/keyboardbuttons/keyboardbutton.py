from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

welcome0 = KeyboardButton("Kurslar ❗")
# welcome1 = KeyboardButton("Yana kursga yozilish ❗")
welcomepack = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(welcome0)
# welcomepack.add(welcome1)
keyphone = KeyboardButton(text="Telefon raqamni berish", request_contact=True)
keyphonepast = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(keyphone)
yangikurs = KeyboardButton(text="Yangi kurs qo'shish")
yangikurspast = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(yangikurs)

menu0 = KeyboardButton(text="Mening ma'lumotlarim ❗")
menu1 = KeyboardButton(text="Mening kurslarim ❗")
menu2 = KeyboardButton(text="Yangi kursga yozilish ❗")
menupast = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(menu0)
menupast.add(menu1)
menupast.add(menu2)
