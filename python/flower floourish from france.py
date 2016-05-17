#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
	
	a = raw_input()
	while (a != '*'):
		a = a.lower()
		a = a.split(' ')
		inicial = a[0][0]
		ok = True
		for x in a:
			if(x[0] == inicial):
				ok = True
			else:
				ok = False
				print 'N'
				break
	
		if ok == True:
			print 'Y'
		
		
		
		
		a = raw_input()
		
	
	
	return 0

if __name__ == '__main__':
	main()

