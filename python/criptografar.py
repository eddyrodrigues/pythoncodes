def main():
	
	a 	= raw_input()
	a = list(a)
	nova =[]
	for x in a:
		x = chr(ord(x) + 3)
		nova.append(x)
	
	nova.reverse()
	
	string_final = ''.join(nova)
	
	print string_final
	
	return 0

if __name__ == '__main__':
	main()

