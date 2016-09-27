#!/usr/bin/env python

casos = input()
for caso in range(casos):
	a = long(input())
	qnt_ = 2
	i = a**0.5
	for k in range(2, int(i+1)):
		if a % k == 0:
			qnt_ +=1
			break
		
	if qnt_ == 3:
		print 'Not prime'
	else: print 'Prime'
