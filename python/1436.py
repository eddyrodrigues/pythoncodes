#!/usr/bin/env python

casos = input()

for caso in range(casos):
	fl = raw_input().split(' ')
	fl = [ int(c) for c in fl]
	fl = fl[1:]
	print 'Case ' + str(caso+1) + ':', fl[len(fl)/2]

