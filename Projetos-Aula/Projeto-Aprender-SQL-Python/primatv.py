import sqlite3

banco = sqlite3.connect('banco.db')

cursor = banco.cursor()

res = cursor.execute("SELECT name FROM sqlite_master")

res.fetchone()