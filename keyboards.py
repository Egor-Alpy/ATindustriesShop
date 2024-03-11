from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

cancel_markup = ReplyKeyboardMarkup(resize_keyboard=True)
cancel_markup.add('/cancel')

letswork_markup = ReplyKeyboardMarkup(resize_keyboard=True)
letswork_markup.add('')