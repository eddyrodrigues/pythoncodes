casos = input()

for caso in range(casos):
	a  = float(input())
	dias = 0
	while a >= 1.00:
		a /= 2
		dias += 1
	if dias > 1:
		print dias, 'dias'
