from aiogram import Dispatcher, executor, Bot, types
import sqlite3 as sq
<<<<<<< HEAD
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Text
=======
>>>>>>> c631c4a65aa87dcba5b00840dae877678861a7d3

from aiogram.dispatcher import FSMContext

<<<<<<< HEAD
import keyboards as kb
import database as db
from config import token, admin_id
from StatesGroups import ClientStatesGroup, DeleteStatesGroup

storage = MemoryStorage()
=======
token = '7147184053:AAH_BIEgqtrQtGtSoJrr3RnTV-j3JWiUhK4'
>>>>>>> c631c4a65aa87dcba5b00840dae877678861a7d3
bot = Bot(token)
dp = Dispatcher(bot=bot,
                storage=storage)


flag_add = False
flag_delete = False

async def on_startup(_):
    print("- - - BOT IS RUNNING - - -")



@dp.message_handler(commands=['start'])
async def startf(message: types.Message):
    await message.answer('<b>Добро пожаловать!</b>',
                         parse_mode='html')
    # добавляем\проверяем пользователя в БД
    user_id = message.from_user.id
    name = message.from_user.first_name
    with sq.connect("shop3_0.db") as con:
        cur = con.cursor()
        cur.execute(f"INSERT INTO users VALUES({user_id}, '{name}', '{message.text[7::]}')")
        print('db-users has been updated')

@dp.message_handler(commands=['cancel'], state="*")
async def cmd_cancel(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await message.answer('Выполнена отмена')
    await state.finish()

@dp.message_handler(commands=['addsoft'], state=None)
async def start_work(message: types.Message):
    if message.from_user.id in admin_id:
        await ClientStatesGroup.name.set()
        await message.answer('Сначала отправь название софта, который хочешь добавить',
                             reply_markup=kb.cancel_markup)
    else:
        await message.reply('У вас нет прав на использование этой команды!')

@dp.message_handler(lambda message: message.text, state=ClientStatesGroup.name)
async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await ClientStatesGroup.next()
    await message.reply('А теперь отправь описание')

@dp.message_handler(state=ClientStatesGroup.desc)
async def load_desc(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['desc'] = message.text
    await ClientStatesGroup.next()
    await message.reply('Теперь отправь цену софта')

@dp.message_handler(state=ClientStatesGroup.price)
async def load_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = int(message.text)
    name = data['name']
    desc = data['desc']
    price = data['price']
    with sq.connect("shop3_0.db") as con:
        cur = con.cursor()
        cur.execute(f"INSERT INTO software VALUES('{name}', '{desc}', {price})")
        print('db-users has been updated')
    await message.reply(f'База Данных была обновлена {name}, {desc}, {price}')
    await state.finish()

@dp.message_handler(commands=['delsoft'], state=None)
async def delete_soft(message: types.Message):
    if message.from_user.id in admin_id:
        await DeleteStatesGroup.namee.set()
        await message.answer('Отправь название софта, который хочешь удалить',
                             reply_markup=kb.cancel_markup)
    else:
        await message.reply('У вас нет прав на использование этой команды!')

@dp.message_handler(lambda message: message.text, state=DeleteStatesGroup.namee)
async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    name = data['name']
    with sq.connect("shop3_0.db") as con:
        cur = con.cursor()
        cur.execute(f"DELETE FROM software WHERE name = '{name}'")
        print('db-users has been updated')
    await state.finish()
    await message.reply('Софт был удален')


@dp.message_handler()
async def main(message: types.Message):
<<<<<<< HEAD
    if __name__ == '__main__':
        await message.reply('Да я тебя отечаю!!!!')

=======
    global flag_add
    global flag_delete

    if message.from_user.id in admin_id and flag_add:
        flag_add = False
        name, description, price = message.text.split('$')
        with sq.connect("shop3_0.db") as con:
            cur = con.cursor()
            cur.execute(f"INSERT INTO software VALUES('{name}', '{description}', {price})")
            print('db-software has been updated')
        await message.answer('db-software has been updated')

    if message.from_user.id in admin_id and flag_delete:
        flag_delete = False
        with sq.connect("shop3_0.db") as con:
            cur = con.cursor()
            cur.execute(f"DELETE FROM software WHERE name = '{message.text}'")
            print('db-software has been updated')
        await message.answer('db-software has been updated')
>>>>>>> c631c4a65aa87dcba5b00840dae877678861a7d3

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False, on_startup=on_startup)


# редактирование БД software
# Обработка несуществующего названия (исключения)