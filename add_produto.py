#-*- coding: utf-8 -*-
import sqlite3


conexao = sqlite3.connect('clientes.db')
#definindo iterator de comandos ou sei la o que que seja isso
#básicmante é o que executa comandos
cursor = conexao.cursor()

def addProduto():

	print 'Informações do produto'
	nome=raw_input('NOME:')
	cod=raw_input('CODIGO DO PRODUTO:')
	val=input('VALIDADE(EM DIAS):')
	entrada = raw_input('DIA/MES de entrada')
	

	produto = [(nome, cod, val, entrada)]

	cursor.executemany("""
	INSERT INTO produtos (nome, cod, val, entrada)
	VALUES(?,?,?,?)
	""", produto)

	conexao.commit()
	print 'Dados registrados com sucesso'
	conexao.close()

addProduto()
