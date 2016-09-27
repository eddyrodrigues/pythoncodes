while 1:
	try:
		h,o = raw_input().split(' ')
		h,o = long(h), long(o)
		print abs(h-o)
		
	except:
		break
