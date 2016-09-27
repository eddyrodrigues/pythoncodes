while 1:
	try:
		entrada = raw_input()
		if "x" in entrada:
			print int(entrada, 16)
		elif '-' in entrada:
			break
		else:
			print str(hex(int(entrada))).upper().replace('X','x')
	except:
		break
