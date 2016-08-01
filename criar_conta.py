#-*- coding: utf-8 -*-
import sqlite3


conexao = sqlite3.connect('clientes.db')
#definindo iterator de comandos ou sei la o que que seja isso
#básicmante é o que executa comandos
cursor = conexao.cursor()

def criaConta():

	print 'Criando nova conta->'
	nome=raw_input('Nome:')
	senha=raw_input('Senha:')
	idade=input('Idade:')
	cpf=raw_input('CPF:')
	email = raw_input('Email:')
	fone=input('Fone:')
	cidade=raw_input('Cidade:')
	uf=raw_input('Estado[UF]:')
	chave  = input("Digite a chave de acesso do usuario [ func = 100 | cliente = 200 ]:")

	usuario = [(nome, senha, idade, cpf, email, fone, cidade, uf, chave)]

	cursor.executemany("""
	INSERT INTO clientes (nome, senha, idade, cpf, email, fone, cidade, uf, chave)
	VALUES(?,?,?,?,?,?,?,?,?)
	""", usuario)

	conexao.commit()
	print 'Dados registrados com sucesso'
	conexao.close()

criaConta()
