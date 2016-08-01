import sqlite3

#######################Pega todos os usuarios e senhas do banco de dados#############################
def FetchAllLista(banco, tipo):
   #conexao com o banco de dados
	conexao = sqlite3.connect(banco)

	cursor = conexao.cursor()
	if tipo == 'clientes':	
		cursor.execute("""
		SELECT * FROM clientes;
		""")
	if tipo == 'produtos':
		cursor.execute("""
		SELECT * FROM produtos;
		""")
		
	return cursor.fetchall()
####################################################################################################

