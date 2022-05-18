from pila import Pila

class Pelicula():
    personajes, peliculas = None,None

personajes = ['Thor','Iron Man','Black Widow','Captain America','Black Panther','Groot','Rocket Raccoon']
peliculas = ['7','4','5','6','1','1','5']

pila1 = Pila()
pila2 = Pila()

print('-----Los datos de los personajes son: -----')
i = 0
for i in range(len(personajes)):
    dato = Pelicula()
    dato.personajes = personajes[i]
    dato.peliculas = peliculas[i]
    print('')
    print('Nombre: ',dato.personajes,'/ Apariciones en peliculas de Marvel: ',dato.peliculas)
    pila1.apilar(dato)

personaje = str(input('Ingrese el personaje a buscar posicion: '))
cimaC = 1 
print('------------------------------------------------')
while(not pila1.pila_vacia()):
    dato = pila1.desapilar()
    cadena = dato.personajes
    #A
    if(cadena != personaje):
        cimaC += 1
    else:
        print(personaje,'esta en la posicion ',cimaC)
    #B
    if(dato.peliculas > '5'):
        print('el personaje ',dato.personajes,' supera las 5 apariciones en peliculas de Marvel con ',dato.peliculas,' recurrencias.')
    #C
    if(dato.personajes == 'Black Widow'):
        contC = dato.peliculas
    #D
    if(cadena[0] == 'C' or cadena[0] == 'D' or cadena[0] == 'G'):
        pila2.apilar(dato.personajes)
    
print('------------------------PUNTO C------------------------')
print('Los personajes que empiezan con las letras "C", "D" o "G" son: ')
while(not pila2.pila_vacia()):
    print(pila2.desapilar())

print('------------------------PUNTO D------------------------')
print('El personaje Black Widow aparece en ',contC,' peliculas.')
print('-------------------------------------------------------')






