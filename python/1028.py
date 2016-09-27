casos = input()
import time

for caso in range(casos):
	fig_r, fig_v = raw_input().split(' ')
	fig_r, fig_v = int(fig_r), int(fig_v)
	minimo = 0
	menor = None
	if fig_r > fig_v:
		minimo = fig_r
		menor = fig_v
	else:
		menor = fig_r
		minimo = fig_v
		
	while 1:
		
		for i in range(1, minimo):
			if (fig_v  % i == 0 ) and (fig_r  % i== 0):
				minimo = i
			#print i
		break
	
	print minimo
