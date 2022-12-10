import sqlite3
nome = 'sdfsdf'
try:
    banco = sqlite3.connect('pedidos.db')
    cursor = banco.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS teste(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Pizza TEXT NOT NULL,
        Observacao TEXT,
        Rua TEXT,
        Numero INTEGER,
        Bairro TEXT,
        Telefone TEXT,
        Status Text NOT NULL
    )''')
    cursor.execute("INSERT INTO teste VALUES(?, ?, ?, ?, ?, ?, ?, ?);",(None, nome, '', "Dom pedro", 45, 'seila', '5454545', 'Finalizada'))
    banco.commit()
    banco.close()

except sqlite3.Error as erro:
    print(erro)