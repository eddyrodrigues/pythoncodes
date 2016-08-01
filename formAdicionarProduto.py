# -*- coding: utf-8 -*

#######################       adicionar produto      8################################
from Tkinter import *
import sqlite3
from pydbmodel import *
import formFuncionario
import FetchAllLista



class formAdicionarProduto():
	def __init__(self, master):
		global Jmaster, database #define variaveis global
		database = Model('produtos') #seleciona o banco de dados
		Jmaster = master # Form passado pro parametro
		Jmaster.geometry('250x350') # define o tamanho
		Jmaster.title("Janela para adicionar produto") #define o titulo da janela
 		self.lblAddProd = Label(master, text = 'Adicionando produto').pack() # coloca labels....
 		#label nome do produto
		self.lblNomeProdn = Label(master, text ='Nome do produto:')
		self.lblNomeProdn.pack(side=TOP)
		#edit nome do produto
		self.edNomeProdn = Entry(master,fg='blue')
		self.edNomeProdn.pack(side=TOP)
		#label codigo do produto 
		self.lblCodigoProdn = Label(master, text ='Cod. do produto:')
		self.lblCodigoProdn.pack(side=TOP)
		#edit2 codigo do produto
		self.edCodigoProdn = Entry(master,fg='blue')	
		self.edCodigoProdn.pack(side=TOP)
		#labal 3 validade do produto(em dias)
		self.lblValidadeProdn = Label(master, text ='Validade do produto(em dias):')
		self.lblValidadeProdn.pack(side=TOP)		
		# edit 3 validade em dias
		self.edValidadeProdn = Entry(master,fg='blue')	
		self.edValidadeProdn.pack(side=TOP)
		#labal 4 dia de entrada
		self.lblDiaEntradan = Label(master, text ='Dia de entrada(ex: 27/01 as 17:00):')
		self.lblDiaEntradan.pack(side=TOP)		
		# edit 4 dia de entrada
		self.edDiaEntradan = Entry(master,fg='blue')	
		self.edDiaEntradan.pack(side=TOP)
		self.btLogindn = Button(master, text='Adicionar', fg='black', command=lambda: self.confirma()).pack(side=TOP)
		
	def confirma(self): 
		#cria um dicionario para adicionar ao lados dos itens
		dicio = {'id': '', 'nome': self.edNomeProdn.get(), 'cod': self.edCodigoProdn.get(), 'val': self.edValidadeProdn.get(), 'entrada':self.edDiaEntradan.get()}
		#acessa o pydbmodel diretamente e adiciona o dicionario padrao de produtos o dicionario criado acima.
		database._prop.update(dicio) 
		#salva as alteracoes no banco de dados
		database.persist()
		#fecha a janela
		Jmaster.destroy()
		Jmaster.quit() # sair
		
