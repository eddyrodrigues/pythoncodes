# -*- coding: utf-8 -*

##################################3JANELA DE LOGIN8################################

#importação de alguns modulos Tkinter e sqlite3, os principais.
#temos as outras janelas também
from Tkinter import *
import sqlite3
from pydbmodel import * #professor, foi de grande ajuda.
import formFuncionario #usada para abrir a janela de funcionario
import FetchAllLista #modulo criado por mim mesmo para puxar lista de usuarios de outro modo(acabei não usando apos usar o pydbmodel)
import formUsuario #usada para abrir a janela de funcionario
config_sqlite('clientes.db') #configura o banco de dados para cliente.db 
class formLogin(object):
	
	def __init__(self, master):
		global logadocomo #variavel para controle de ambiente onde está logado
		logadocomo = -1 # define como não logado
		global frame # define um frame global para acesso em outros métodos da classe
		#frame = Frame(master)
		#frame.pack()
		#frame.geometry('800x600')
		self.master =master # declara uma variavel da classe com a janela passada por parametro no construtor
		self.lbl = Label(master, text = 'Welcome to the system!') # criar um label como o texto
		self.lbl.pack() #exibe o texto no frame
		#LAbel para para pedido de "please login
		self.plslbl = Label(master, text = 'Please log-in to continue using the system', fg='blue')
		self.plslbl.pack()
		#label usuario
		self.login = Label(master, text ='Usuário')
		self.login.pack(side=TOP)
		#edit usuario
		self.edUsuario = Entry(master,fg='blue')
		self.edUsuario.pack(side=TOP)
		#label senha
		self.senha = Label(master, text ='Senha')
		self.senha.pack(side=TOP)
		#edit2 senha
		self.edSenha = Entry(master,fg='blue',show='*')	
		self.edSenha.pack(side=TOP)
		
		
		#butoes:
		#1 - botao quit
		self.btQuit = Button(master, text='Quit', fg='red', command=lambda: self.sair()).pack()
		
		#2 - botao login
		self.btLogind = Button(master, text='Login', fg='black', command=lambda: self.btLogin()).pack()
		##self.btLogind.pack(side=RIGHT)
		

	def sair(self):
		self.master.destroy() #destroy
		self.master.quit() # e fecha o cliente
		
	def btLogin(self):
		data = Model('clientes') #define o banco de dados que sera usado para pegar as informações
		user =self.edUsuario.get() # pegar o usuario digitado
		passwd = self.edSenha.get() # pega a senha digitada
		list_users = data.select() # gera uma lista de usuarios
		#print list_users printando a lista para conferir(apenas)
		for usr in list_users:  #esse for percorre a lista de usuario e verifica a o login e senha para ver se está correto
			if ( (usr['nome'] == user) & (usr['senha'] == passwd) ):
				print 'Usuario encontrado!'
				if(usr['chave'] == 100): #se a chave por 100 é definido como funcionario
					print 'Entrando como funcionario'
					logadocomo = 0 # 0 para funcionario e 1 para cliente
					self.master.withdraw() # oculta a janela de login
					formFuncionario.formFuncionario(user, passwd) # cria uma instancia da classe formFuncionario que seria a janela de cadastro ou edicao e produtos.
				else: #senao a chave estara definida como qualquer outro....
					print 'Entrando como cliente'
					logadocomo = 1 # 0 para funcionario e 1 para cliente
					self.master.withdraw() # oculta a janela de login
					formUsuario.formUsuario(user, passwd) # cria uma instancia da classe formUsuario que seria a janela de compras
		
		logadocomo = -1		
		
			
			##### o resto não serve para muita coisa, 
			##### apenas foi usado para a meu modulo antigo
			##### visto que o pydbmodel simplificou bastante
			##### essa parte de verificações com o banco de dados.	


"""
	def btLogin(self, frame):
		user =self.edUsuario.get()
		passwd = self.edSenha.get()
		dbUsuarios = FetchAllLista()
		#print dbUsuarios
		if (dbUsuarios == ''):
			return False
		
		for x in dbUsuarios:			
			if((x[1] == user) & (x[2] == passwd)):
				print 'Usuario aceito'
				print 'Logando.....'
				print 'Logado como ',user,'.'
			
				return True
		print 'Nada encontrado no banco de dados'
		
"""		
			
		
		
		


