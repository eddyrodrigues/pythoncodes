while 1:
	try:
		entrada = raw_input().split(' ')
	except:
		break
	a,b = entrada[0], entrada[1]
	a,b = list(a), list(b)
	if len(b) < len(a):
		b = [0]*(abs(len(a) - len(b))) + b
	else:
		a = [0]*(abs(len(a) - len(b))) + a
		
	if a[0] == '0' and b[0] == '0': break
	carry = 0
	for i in range(len(b)-1,-1,-1):
		try:
			#print a[i],b[i]
			if int(a[i]) + int(b[i]) >= 10:
				carry +=1
		except:
			pass
	if carry == 0: print 'No carry operation.'
	elif carry == 1: print carry, 'carry operation.'
	else: print carry, 'carry operations.'
	
