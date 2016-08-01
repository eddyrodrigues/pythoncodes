# -*- coding: utf-8 -*

from Tkinter import *
import sqlite3
from pydbmodel import *
import FetchAllLista
import formUsuario
import formLogin
 
#config_sqlite('clientes.db')
class formCarrinho(object):
	def __init__(self, master, mylist):
		global MyList
		self.master = master
		self.carro_aberto = False
		mylist.pack()
		MyList = mylist
		self.total_a_pagar = 0.00
		master.title('Seu carrinho de compras')
		master.withdraw() 

		#frame = Frame(master)
		#frame.pack()
		#frame.geometry('800x600')
		self.lbl = Label(master, text = 'Carrinho de compras!')
		self.lbl.pack()
		#LAbel para para pedido de "please login
		self.lblAviso1 = Label(master, text = 'Produtos atualmente no seu carrinho', fg='blue').pack()
		#label usuario
		self.lblAviso2 = Label(master, text ='obs: para manter os produtos no carrinho não feche está janela!!!').pack(side=TOP)		
		self.lblTotalAPagar = Label(master, text = str('Total a pagar: ' + str(self.total_a_pagar) + ' RS'))
		self.lblTotalAPagar.pack(side=LEFT)
		#butoes:
		#1 - botao confirmar compra
		#self.btConfirmarCompra = Button(master, text='Quit', fg='green', command=lambda: self.confirmarCompra()).pack()
		
		#2 - botao fechar carrinho
		#self.btFecharCarrinho = Button(master, text='Login', fg='black', command=lambda: self.btLogin()).pack()
		

	def btfecharCarrinho(self):
		self.total_a_pagar = 0.00
		self.carrinho_aberto = False
		self.master.destroy()
		self.master.quit()
	
	def addCarrinho(self, idprod, nome, lists):
		#global listCarrinho
		global MyList
		MyList.insert(idprod, nome)
	
	def removerDoCarrinho(self):
		listCarrinho.delete(self.listCarrinho.curselection()[0])
	
	def limparCarrinho(self):
		listCarrinho.delete(0, self.listCarrinho.size())
		self.btFecharCarrinho()
	
	def mostraCarrinho(self):
		global mainCarrinho,listCarrinho,carro_aberto
		carro_aberto = True
		self.master.deiconify()
	
	def addTotal(self, qnt):
		self.total_a_pagar += qnt
		
		self.lblTotalAPagar.config(text = str('Total a pagar: ' + str(self.total_a_pagar) + ' RS'))
	
	def btConfirmarCompra(self):
		data = Model('produtos')
		list_users = data.select()
		print list_users	
		
	def getCarroAberto(self):
		return self.carro_aberto
	def setCarroAberto(self, boo):
		self.carro_aberto = boo
"""	def atualizaLista(self, mlist, id_produto):
		prods = data.select()
		print 'Lista de produtos atuaias no banco de dados'
		print prods
		for prod in prods:
			mylist.insert(prod['id'], str(prod['nome']))
"""
	
	
