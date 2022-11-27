import sqlite3

try:
    banco = sqlite3.connect('pedidos.db')
    cursor = banco.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS teste(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NAME TEXT NOT NULL
    )''')
    cursor.execute("INSERT INTO teste VALUES(?, ?);",(None, "Jihad"))
    banco.commit()
    banco.close()

except sqlite3.Error as erro:
    print(erro)