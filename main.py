from aiogram import Dispatcher, executor, Bot, types
import sqlite3 as sq
flag_add = False
flag_delete = False

# создание БД
with sq.connect("shop3_0.db") as con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS users")
    cur.execute("""CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        refer_id TEXT
        )""")
    cur.execute("""CREATE TABLE IF NOT EXISTS software (
    name TEXT PRIMARY KEY,
    description TEXT,
    price REAL
    )""")

    for result in cur:
        print(result)
        print('*')


token = '7147184053:AAH_BIEgqtrQtGtSoJrr3RnTV-j3JWiUhK4'
bot = Bot(token)
dp = Dispatcher(bot)

# список id админов
admin_id = [868320310]

async def on_startup(_):
    print("- - - BOT IS RUNNING - - -")

@dp.message_handler(commands=['start'])
async def startf(message: types.Message):
    await message.answer('<b>Добро пожаловать!</b>', parse_mode='html')

    # добавляем\проверяем пользователя в БД
    user_id = message.from_user.id
    name = message.from_user.first_name
    with sq.connect("shop3_0.db") as con:
        cur = con.cursor()
        cur.execute(f"INSERT INTO users VALUES({user_id}, '{name}', '{message.text[7::]}')")
        print('db-users has been updated')


@dp.message_handler(commands=['addsoft'])
async def addsoftf(message: types.Message):
    if message.from_user.id in admin_id:
        await message.answer('<em>введите параметры нового софта(name, description, price) с разделителем "$"</em>', parse_mode='html')
        global flag_add
        flag_add = True
    else:
        await message.answer('<em>У Вас нет прав на запрашиваемую команду</em>', parse_mode='html')

@dp.message_handler(commands=['deletesoft'])
async def addsoftf(message: types.Message):
    if message.from_user.id in admin_id:
        await message.answer('<em>введите точное название софта</em>', parse_mode='html')
        global flag_delete
        flag_delete = True
    else:
        await message.answer('<em>У Вас нет прав на запрашиваемую команду</em>', parse_mode='html')

@dp.message_handler()
async def main(message: types.Message):
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









if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False, on_startup=on_startup)
