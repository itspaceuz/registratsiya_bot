from aiogram.dispatcher.filters.state import State, StatesGroup


class Registrator(StatesGroup):
    all_name = State()
    area_name = State()
    course_type = State()
    course_group = State()
    phone_number = State()


