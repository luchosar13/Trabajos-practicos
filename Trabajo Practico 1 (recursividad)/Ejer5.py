
romanos = {'i':1,'v':5,'x':10,'l':50,'c':100,'d':500,'m':1000}



def NumerosRomanos(roma):
    if(len(roma) == 1):
        return romanos[roma]
    else:
        if(romanos[roma[0]]) >= (romanos[roma[1]]):
            return (romanos[roma[0]]) + NumerosRomanos(roma[1:])
        else:
            return (- romanos[roma[0]]) + NumerosRomanos(roma[1:])


print('El numero convertido es :', NumerosRomanos('xxiv'))


