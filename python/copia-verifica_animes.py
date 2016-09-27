#!/usr/bin/env python

import os, time, sys, urllib

def verifica_animes(listao):
	site = urllib.urlopen("http://animeai.net")
	conteudo = str(site.read()).lower()
	conteudo = conteudo[conteudo.index("telinhas"):conteudo.index("paginacao")]
	for i in listao:
		if i in conteudo:
			print i, 'encontrado algo'
		else:
			print 'nada encontrado para', i

	
def main():
	while 1:
		verifica_animes(sys.argv[1:])
		time.sleep(30)
	return 0

main()
	
