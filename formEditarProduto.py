# -*- coding: utf-8 -*

##################################3JANELA DE LOGIN8################################
from Tkinter import *
import sqlite3
from pydbmodel import *
import formFuncionario
import FetchAllLista

class formEditarProduto(object):
	
	def __init__(self, idproduto, master):
		global database
		self.idproduto = idproduto
		
		global Jmaster
		Jmaster = master
		database = Model('produtos')
		master.geometry('250x350')
		Jmaster.title('Janela de edição')
		self.lbl = Label(master, text = 'Edição do produto')
		self.lbl.pack()
		#label nome do produto
		self.lblNomeProd = Label(master, text ='Nome do produto:')
		self.lblNomeProd.pack(side=TOP)
		#edit nome do produto
		self.edNomeProd = Entry(master,fg='blue')
		self.edNomeProd.pack(side=TOP)
		#label codigo do produto 
		self.lblCodigoProd = Label(master, text ='Cod. do produto:')
		self.lblCodigoProd.pack(side=TOP)
		#edit2 codigo do produto
		self.edCodigoProd = Entry(master,fg='blue')	
		self.edCodigoProd.pack(side=TOP)
		#labal 3 validade do produto(em dias)
		self.lblValidadeProd = Label(master, text ='Validade do produto(em dias):')
		self.lblValidadeProd.pack(side=TOP)		
		# edit 3 validade em dias
		self.edValidadeProd = Entry(master,fg='blue')	
		self.edValidadeProd.pack(side=TOP)
		#labal 4 dia de entrada
		self.lblDiaEntrada = Label(master, text ='Dia de entrada(ex: 27/01 as 17:00):')
		self.lblDiaEntrada.pack(side=TOP)		
		# edit 4 dia de entrada
		self.edDiaEntrada = Entry(master,fg='blue')	
		self.edDiaEntrada.pack(side=TOP)
				
		
		#butoes:
		#1 - botao quit
		#self.btQuit = Button(master, text='Quit', fg='red', command=lambda: Jmaster.destroy()).pack()
		
		#2 - botao login
		self.btLogind = Button(master, text='Confirmar', fg='black', command=lambda: self.confirmar()).pack()
		##self.btLogind.pack(side=RIGHT)	
		Jmaster.mainloop()	
		
		
	def confirmar(self):
		if( (self.edNomeProd.get() != '' ) | ( self.edCodigoProd.get() != '' ) | ( self.edValidadeProd.get() != '' ) | ( self.edDiaEntrada.get() != '' )   ):
			produtos_in_db = database.select()
			#usando o for para verificar se existe um produto de mesmo nome
			achou = False
			for prod in produtos_in_db:
				if(achou == 1): break
				nome_atual = self.edNomeProd.get()
				nome_atual = nome_atual.lower()
				if( prod['nome'].lower() == nome_atual ):
					achou = True
				
			if( achou == 1 ):
				lblEncontrado = Label(Jmaster, text = 'Parece que o produto já foi cadastrado', fg='red').pack()
			
			if( achou == 0):			
				database.load(self.idproduto) #carrega todas as informações do produto
				#seta todas as novas informações(atualiza de acordo com os edits) 
				database.set('nome', self.edNomeProd.get())
				database.set('cod', self.edCodigoProd.get())
				database.set('val', self.edValidadeProd.get())
				database.set('entrada', self.edDiaEntrada.get())
				database.persist() #salva os dados
				
				Jmaster.destroy()
				Jmaster.quit()
		Jmaster.destroy()
		Jmaster.quit()
#formEditarProduto()

