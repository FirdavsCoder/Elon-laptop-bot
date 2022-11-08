from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from data.config import ADMINS
from loader import dp,db, bot
from keyboards.default.pc_elon import menu

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):

        
    try:
        if db.check_user(id=message.from_user.id):
            await message.answer(text=f"Assalomu aleykum {message.from_user.full_name}!", reply_markup=menu)
        else:
            await message.answer(text=f"Assalomu aleykum {message.from_user.full_name}!\nXush kelibsiz!", reply_markup=menu)
            count = db.count_users()[0]
            matn = f"{message.from_user.get_mention()} bazaga qo'shildi!\nBazada {count} ta foydalanuvchi bor!"
            await bot.send_message(
                chat_id=1849953640,
                text=f"Yangi foydalanuvchi: {message.from_user.get_mention()} @{message.from_user.username}\n{matn}"
            )
            db.add_user(id=message.from_user.id, 
            name=message.from_user.full_name, 
            )
    except Exception as ex:
        await dp.bot.send_message(chat_id=1849953640, text=f"🤖Log: {ex}")
        
