import sqlite3 as sq
# создание БД
with sq.connect("shop3_0.db") as con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS software")
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