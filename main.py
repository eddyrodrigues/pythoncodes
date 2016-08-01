#!/usr/bin/env python
# -*- coding: utf-8 -*

##Estou trabalhando com a hipótese de que os produtos não tenha uma quantia definida, ou seja ilimitada(a quantia de produtos)



from Tkinter import *
import sqlite3
import formLogin



def main():
	main = Tk()						#cria a janela principal para ser passada por parametro
	mainJ = formLogin.formLogin(main) #criar uma janela com estilo formLogin
	main.title('Log-in') #define o titulo
	main.geometry('400x200') #define a altura e a largura da janela
	logadocomo = formLogin.logadocomo
	main.mainloop()
	return 0

if __name__ == '__main__':
	main()




