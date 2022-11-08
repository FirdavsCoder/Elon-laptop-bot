from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

check = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text = "Yuborish"),
            KeyboardButton(text = "Rad qilish")
        ]
    ],
    resize_keyboard=True
)




check_admin  =ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text = "Kanalga joylash"),
            KeyboardButton(text = "Yaroqsiz elon")
        ]
    ],
    resize_keyboard=True
)