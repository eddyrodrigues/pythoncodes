def rafa(x,y):
        return float (((3*x)**2) + y**2)
def beto(x,y):
        return float(2*(x**2)+ (5*y)**2)
def carlos(x,y):
        return float(-100*x + y**3)

casos = input()
for caso in range(casos):
        a,b = raw_input().split(' ')
        a,b = int(a), int(b)
        ganhador = []
        ganhador.append(rafa(a,b))
        ganhador.append(beto(a,b))
        ganhador.append(carlos(a,b))
        ganhou = ganhador.index(max(ganhador))

        if ( ganhou == 0 ):
                print 'Rafael ganhou'
        elif ganhou == 1:
                print 'Beto ganhou'
        else:
                print 'Carlos ganhou'
