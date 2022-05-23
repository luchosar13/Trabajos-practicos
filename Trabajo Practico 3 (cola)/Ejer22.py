from cola import Cola

class Peliculas():
    nombrePersonaje, nombreHeroe, sexo = None, None, None

nombrePersonaje = ['Tony Stark','Steve Rogers','Natasha Romanoff','Scott Lang','Carol Danvers','Peter Benjamin Parker']
nombreHeroe = ['Iron Man','Capitan America','Black Winter','Ant-Man','Capitana Marvel','Spider Man']
sexo = ['M','M','F','M','F','M']

cola1 = Cola()
cola2 = Cola()
cola3 = Cola()
cola4 = Cola()
cola5 = Cola()

print('--------------------Cola inicial de personajes-----------------------')
for i in range(len(nombrePersonaje)):
    dato = Peliculas()
    dato.nombrePersonaje = nombrePersonaje[i]
    dato.nombreHeroe = nombreHeroe[i]
    dato.sexo = sexo[i]
    print('Personaje: ',dato.nombrePersonaje,'-- Superheroe: ',dato.nombreHeroe,'-- Sexo: ',dato.sexo)
    cola1.arribo(dato)

print('--------------------------------------------------------------')

while(not cola1.cola_vacia()):
    dato = cola1.atencion()
    cadena1 = dato.nombrePersonaje
    cadena2 = dato.nombreHeroe
    #A
    if(dato.nombreHeroe == 'Capitana Marvel'):
        nombreCapitana = dato.nombrePersonaje
    #B
    if(dato.sexo == 'F'):
        cola2.arribo(dato.nombrePersonaje)
    #C
    if(dato.sexo == 'M'):
        cola3.arribo(dato.nombrePersonaje)
    #D
    if(dato.nombrePersonaje == 'Scott Lang'):
        nombreScott = dato.nombreHeroe
    #E
    if(cadena1[0] is 'S'):
        cola4.arribo(dato.nombrePersonaje)

    if(cadena2[0] is 'S'):
        cola5.arribo(dato.nombreHeroe)
    #F
    if(dato.nombrePersonaje == 'Carol Danvers'):
        print('Carol Danvers se encuentra en la cola y su nombre de superheroe es',dato.nombreHeroe)

print('')

print('------------------------PUNTO A------------------------')
print('El nombre de la superheroe Capitana Marvel es', nombreCapitana)
print('------------------------PUNTO B------------------------')
print('Los superheroes femeninos son: ')
while(not cola2.cola_vacia()):
    print(cola2.atencion())
print('------------------------PUNTO C------------------------')
print('Los superheroes masculinos son: ')
while(not cola3.cola_vacia()):
    print(cola3.atencion())
print('------------------------PUNTO D------------------------')
print('El nombre de superheroe del personaje Scott Lang es',nombreScott)
print('------------------------PUNTO E------------------------')
print('Los personajes que empiezan con la letra "S" son :')
while(not cola4.cola_vacia()):
    print(cola4.atencion())
print('')
print('Los superheroes que empiezan con la letra "S" son :')
while(not cola5.cola_vacia()):
    print(cola5.atencion())


    

    


