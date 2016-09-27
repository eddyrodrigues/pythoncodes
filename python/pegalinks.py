#!/usr/bin/env python
# coding: utf-8

from HTMLParser import HTMLParser
import sys, os
import urllib2

class myHTMLp(HTMLParser):
	pegos = []
	pegar = False
	def handle_starttag(self, tag, attr):
		if tag == 'a' or tag == 'p':
			pegar = True
			nome = 'sem nome'
			link = ''
			for l, m in attr:
				if l == 'href':
					link = m
				if l == 'title' or l == 'name':
					nome = m
			if len(nome) == 0 or len(link) == 0: return
			self.pegos.append([nome,link])

	def handle_data(self, data):
		print data
		try:
			if pegar:
				self.pegos[len(self.pegos)-1].append(data)
				pegar = False
				return
			else:
				return
		except:
			pass
	def print_links(self):
		for nome in self.pegos:
			print nome


web = urllib2.urlopen(raw_input("website> "))
content = web.read()

myHTML = myHTMLp()

myHTML.feed(content)
myHTML.print_links()
myHTML.close()


