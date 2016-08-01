import sqlite3

conexao = sqlite3.connect('clientes.db')
#definindo o cursor
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE produtos (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        cod TEXT NOT NULL,
	val INTEGER NOT NULL,
	entrada TEXT NOT NULL
);
""")

print 'Tabela criada com sucesso'

conexao.close()
