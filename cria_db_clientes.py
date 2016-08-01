import sqlite3

conexao = sqlite3.connect('clientes.db')
#definindo o cursor
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE clientes (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        senha TEXT NOT NULL,
	idade INTEGER,
        cpf VARCHAR(11) NOT NULL,
        email TEXT NOT NULL,
        fone TEXT,
        cidade TEXT,
        uf VARCHAR(2) NOT NULL,
        chave INTEGER NOT NULL
);
""")

print 'Tabela criada com sucesso'

conexao.close()
