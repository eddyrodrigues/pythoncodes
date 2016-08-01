# -*- coding: utf-8 -*


#modulos importados normalmente....


from Tkinter import *
from pydbmodel import *
import sqlite3
import formLogin
import FetchAllLista # caso eu queria usar FetchAllLista(nome do banco de dados.db, tipo('clientes' ou 'produtos')
import formEditarProduto
#config_sqlite('produtos.db')
import formAdicionarProduto

class formFuncionario():
	def __init__(self, usuario, senha):
			global data # variavel global para gerenciamento do banco de dados
			self.usuario = usuario # criar variavel da classe, usuario
			self.senha = senha # criar variavel da classe, senha
			master = Tk() # cria um janela funcionario 
			master.title("Janela do funcionario") #define o titulo dessa janela
			master.geometry('375x285') # define o tamnho da janela
			myList = Listbox(master) # cria uma lista (que sera adicionado os itens do banco de dados
			data = Model('produtos') # seleciona o banco de dados
			self.lblProds = Label(master, text="Produtos existentes:") # cria um label para informar que sao os produtos que estao no estoque
			self.lblProds.pack() # gera o botao(visivelmente)
			
			self.carrega_mylist(myList) # carrega_mylist é uma função que adiciona, os itens que estão no banco de dados
										# produtos, à listbox criada logo acima.
			myList.pack() # mostra a lista
			#botao de adicionar produto
			self.btAdicionar = Button(master, text="Adicionar produto", command=lambda: self.adicionar_produto(myList)).pack(side=TOP)
			# botao de editar produto
			self.btEditar = Button(master, text='Editar produto', command= lambda:self.editar_produto(myList.get(myList.curselection()[0]), myList)).pack(side=TOP)
			# botao para remocao do produto
			self.btRemover = Button(master, text='Remover produto', command = lambda: self.remover_produto(myList.get(myList.curselection()[0]), myList)).pack(side=TOP)
			#botao para sair do programa
			self.btExit = Button(master, text='Sair', command=lambda: self.sair(master)).pack(side=TOP)
			# funcao loop para eventos do frame principal
			master.mainloop()
			
			
	def sair(self, master): #fecha o programa
		meu = master
		meu.destroy()
		meu.quit()
	
		
		
	def carrega_mylist(self, lists): 
		lists.delete(0, lists.size()) # deleta todos os itens antigos
		prods = data.select() # seleciona todo o banco de dados, ou seja, todos os itens 
		#print 'lista de produtos'
		#print prods
		for prod in prods: # adiciona todos os itens a listbox
			lists.insert(prod['id'], str(prod['nome']))		
			
			
			
	def editar_produto(self, produto, lists):
	#eu recebo a variavel lists( que é a lista la de cima) para que eu posso atualizar a lista de acordo com o banco de dados
		self.__nomeproduto = produto #nome do produto selecionado.
 		#print self.__nomeproduto
		lista_produtos = data.select() #novamente seleciona todos o sprodutos do banco de dados
		self.id_real = 0 #id real para identificar ele no banco de dados com seu respectivo id( do banco de dados )
		#print self.__nomeproduto
		##imprimi e forma de lista o que representa o produto selecionado
		for prod in lista_produtos: # esse for faz a verificacao do nome do produto e depois retorna o id do mesmo
			if(prod['nome'] == self.__nomeproduto): 
				self.id_real = prod['id']
				break
		mainEdit = Tk() # cria uma nova janele
		formEditarProduto.formEditarProduto(self.id_real, mainEdit) #passa essa nova janela e o id real do produto, no banco de dados, para o formEditar, que faz a edição do produto	
		
		
		
		#print 'recarregando lista de produtos'
		self.carrega_mylist(lists) #recarrega a lista de produtos.


	def remover_produto(self, produto, lists):
		#eu recebo a variavel lists( que é a lista la de cima) para que eu posso atualizar a lista de acordo com o banco de dados
		self.__nomeproduto = produto #nome do produto de acordo com o selecionado na listbox
		#print self.__nomeproduto
		lista_produtos = data.select() #pega todos os produtos do banco de dados
		self.id_real = 0 # define um id 0 para usar logo apos
		#print self.__nomeproduto 
		##imprimi e forma de lista o que representa o produto selecionado
		for prod in lista_produtos:
			if(prod['nome'] == self.__nomeproduto): # faz a verificação para todos os proutos da lista de produtos
													# se for o mesmo nome ele define o id_real = ao id no banco de dados
				self.id_real = prod['id'] #atribui
				break # breka
		data.load(self.id_real) # carrega produto de acordo com o id retornado
		data.delete(self.id_real) # deleta o produto
		data.persist() # salva as modificações no banco de dados
		self.carrega_mylist(lists) # recarrega a lista de produtos e acordo com o banco de dados.
		
			
			
	def adicionar_produto(self, mylist):		 # adicionar produto
		mainADD = Tk() #cria uma janela que adiciona o produto
		formAdicionarProduto.formAdicionarProduto(mainADD) #instancia
		
		mainADD.mainloop() #deixa o loop dela
		
		#print 'recarregando lista de produtos'
		self.carrega_mylist(mylist) # carrega a lista novamente ( acho que não necessitaria aqui, mas tudo bem ).
