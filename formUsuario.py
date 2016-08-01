# -*- coding: utf-8 -*

from Tkinter import *
from pydbmodel import *
import sqlite3
import formCarrinho
import formLogin
import FetchAllLista # caso eu queria usar FetchAllLista(nome do banco de dados.db, tipo('clientes' ou 'produtos')
import formEditarProduto
import formAdicionarProduto



carro_aberto = False # define se o carrinho esta aberto ou nao
mainCarrinho = Tk() #cria a janela do carrinho
listCarrinho = Listbox(mainCarrinho) #cria a listabox do carrinho com os itens que serao adicionados
carrinho = formCarrinho.formCarrinho(mainCarrinho,listCarrinho) #instancia o formCarrinho para ser editado abaixo na parte de adicionar produto


class formUsuario():
	
	#mainCarrinho.title('Carrinho:')

	#mainCarrinho.mainloop()
	def __init__(self, usuario, senha):
		self.usuario = usuario # usuario e senha
		self.senha = senha ##
		master = Tk() # cria uma janela
		master.title("Shop") # define o titulo
		master.geometry('375x285') #tamanho
		myList = Listbox(master) #uma listbox padrao de produtos que estao no banco de dados
		data = Model('produtos') #seleciona o banco de dados
		self.lblProdutoToSale = Label(master, text="Produtos disponiveis para compra").pack() # label
		self.carrega_mylist(myList) # carrega a lista atual com os produtos do banco de dados
		myList.pack() # gera a lista(exibi na tela)
		#botao de adicionar ao carrinho
		self.btAddCarinho = Button(master, text="Adicionar ao carrinho", command=lambda: self.addProduto(myList.get(myList.curselection()[0]))).pack(side=TOP)
		#botao de sair do usuario
		self.btExitUsuario = Button(master, text='Sair', command=lambda: self.sair(master)).pack(side=TOP)
		#loop do master.
		master.mainloop()
		
		
	#funcao para sair do programa	
	def sair(self, master):
		meu = master
		meu.destroy()
		meu.quit()
	#funcao que carrega os produtos do banco de dados
	#ja foi comentado em outras classes.
	#verificar classe formFuncionario para ver comentarios. obrigado.
	def carrega_mylist(self, lists):
		lists.delete(0, lists.size())
		data = Model('produtos')
		prods = data.select()
		#print 'lista de produtos'
		#print prods
		for prod in prods:	
			lists.insert(prod['id'], str(prod['nome']) )		
			
	#retorna o id, do banco de dados, de acordo com o nome passado
	def idProd(self, nome):
		data = Model('produtos')
		lista = data.select()
		self.id_prod = 0
		for prod in lista:
			if (prod['nome'] == nome):
				self.id_prod = prod['id']
		return self.id_prod
	#metodo addProduto no qual adiciona o produto ao carrinho de compras	
	def addProduto(self, produto_nome):
		global carrinho, listCarrinho 
		data = Model('produtos') 
		lista_produtos = data.select()
		preco = 0.00
		for prod in lista_produtos: #usei o cod como preço do produto
			if((prod['id']) == (self.idProd(produto_nome))):
				preco = float(prod['cod'])
				
		if(carrinho.getCarroAberto() == False):	 # se o carrinho estiver fechado	
			carrinho.mostraCarrinho() # acessa a funcao no modulo formCarrinho para abrir o carrinho;
			carrinho.setCarroAberto(True)			#seta o carrinho como aberto
			carrinho.addCarrinho(int(self.idProd(produto_nome)),str(produto_nome), listCarrinho) #passa o nome e id do produto
			carrinho.addTotal(preco) # e adiciona o preco ao total a pagaR(uma variavel dentro do carrinho a principio)
		else:# se o carrinho estiver aberto ele apenas adiciona ao carrinho e adiciona ao total a pagar.
			carrinho.addCarrinho(self.idProd(produto_nome),produto_nome, listCarrinho)
			carrinho.addTotal(preco)
		#print 'produto adicionado no carrinho'
		#print total_a_pagar 
		#print 'carrinho aberto ? ', carro_aberto
