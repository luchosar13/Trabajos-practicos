from cola import Cola
from random import randint

class Turnos():
    letra, numero = None, None


cola1 = Cola()
cola2 = Cola()
cola3 = Cola()
cola4 = Cola()
cola5 = Cola()

print('--------------------Cola inicial de turnos-----------------------')
for i in range(20):
    dato = Turnos()
    dato.letra = chr(randint(65,71))
    dato.numero = int(randint(0,100))
    print(dato.letra,dato.numero)
    cola1.arribo(dato)

while(not cola1.cola_vacia()):
    dato = cola1.atencion()
    
    if(dato.letra in ['A','C','F']):
        cola2.arribo(dato)
    else:
        cola3.arribo(dato)

print('--------------------------------------------------------------')
colaMayor1 = 0
colaMayor2 = 0
if(cola2.tamanio() > cola3.tamanio()):
    print('La cola 2 tiene mayor cantidad de turnos')
    colaMayor1 = 1
else:
    print('La cola 3 tiene mayor cantidad de turnos')
    colaMayor2 = 1

contA = 0
contC = 0
contF = 0
while(not cola2.cola_vacia()):
    dato = cola2.atencion()
    cola4.arribo(dato)
    if(colaMayor1 == 1):
        if(dato.letra is 'A'):
            contA += 1
        elif(dato.letra is 'C'):
            contC += 1
        elif(dato.letra is 'F'):
            contF += 1

if(contA > contC and contA > contF):
    print('La letra que mas aparece en la cola mayor es la A con',contA,'apariciones.')
elif(contC > contA and contC > contF):
    print('La letra que mas aparece en la cola mayor es la C con',contC,'apariciones.')
elif(contF > contA and contF > contC):
    print('La letra que mas aparece en la cola mayor es la F con',contF,'apariciones.')

contB = 0
contD = 0
contE = 0
while(not cola3.cola_vacia()):
    dato = cola3.atencion()
    cola5.arribo(dato)
    if(colaMayor2 == 1):
        if(dato.letra is 'B'):
            contB += 1
        elif(dato.letra is 'D'):
            contD += 1
        elif(dato.letra is 'E'):
            contE += 1

if(contB > contD and contB > contE):
    print('La letra que mas aparece en la cola mayor es la B con',contB,'apariciones.')
elif(contD > contB and contD > contE):
    print('La letra que mas aparece en la cola mayor es la D con',contD,'apariciones.')
elif(contE > contB and contE > contD):
    print('La letra que mas aparece en la cola mayor es la E con',contE,'apariciones.')

print('--------------------------------------------------------------')
print('Los turnos con numeros mayores a 56 de la cola menor son: ')
if(colaMayor1 == 0):
    while(not cola4.cola_vacia()):
        dato = cola4.atencion()
        if(dato.numero > 56):
            print(dato.letra,dato.numero)

if(colaMayor2 == 0):
    while(not cola5.cola_vacia()):
        dato = cola5.atencion()
        if(dato.numero > 56):
            print(dato.letra,dato.numero)


        









