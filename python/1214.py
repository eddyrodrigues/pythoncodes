casos = input()

for caso in range(casos):
	entradas = raw_input().split(' ')
	entradas = [float(c) for c in entradas]
	soma = float(sum(entradas[1:]))
	media = float(float(soma)/float(entradas[0]))
	total = float(0)
	for medias in entradas[1:]:
		if medias > media:
	#		print medias 
			total += 1
	print  '%.3lf%%' % ( float((total*100)/entradas[0]) )
