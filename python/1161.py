def fat(x):
	if x == 0: return 1
	return long(x*fat(x-1))

while 1:
	try:
		fat1,fat2 = raw_input().split( ' ' )
		fat1, fat2 = long(fat1), long(fat2)
		soma1 = long(0); soma1 = fat(fat1)
		soma2 = long(0); soma2 = fat(fat2)
		print soma1 + soma2
		
	except EOFError:
		break
