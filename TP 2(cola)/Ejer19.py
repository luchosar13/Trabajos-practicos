from pila import Pila

class Pelicula():
    titulo, estudio, anioEstreno = None, None, None

#dic = {'titulo':'nada','estudio':'nada','anioEstreno':'nada'}

titulo = ['El Hobbit','Vengadores: Infinity War','Ouija','Jurassic World','Doctor Strange']
estudio = ['Warner Bros', 'Marvel Studios','Universal Studios','Universal Pictures','Marvel Studios']
anioEstreno = ['2014', '2018','2014','2015','2016']

pila1 = Pila()
pila2 = Pila()
pila3 = Pila()

i = 0
for i in range(len(titulo)):
    dato = Pelicula()
    dato.titulo = titulo[i]
    dato.estudio = estudio[i]
    dato.anioEstreno = anioEstreno[i]
    #dic = {'titulo':titulo[i],'estudio':estudio[i],'anioEstreno':anioEstreno[i]}
    print('Titulo: ',dato.titulo,'--Estudio cinematografico: ',dato.estudio,'--Anio de estreno: ',dato.anioEstreno)
    pila1.apilar(dato)

cont = 0
while(not pila1.pila_vacia()):
    dato = pila1.desapilar()
    #A
    if(dato.anioEstreno == '2014'):
        pila2.apilar(dato.titulo)
    #B
    if(dato.anioEstreno == '2018'):
        cont += 1
    #C
    if(dato.estudio == 'Marvel Studios' and dato.anioEstreno == '2016'):
        pila3.apilar(dato.titulo)

print('----------------------------------------------------------------------')
print('Las peliculas estrenadas en el anio 2014 fueron: ')
while (not pila2.pila_vacia()):
    print(pila2.desapilar())
print('')
print('La cantidad de peliculas estrenadas en el anio 2018 son: ', cont)
print('')
print('Las peliculas que fueron producidas por Marvel Studios en 2016 son: ')
while(not pila3.pila_vacia()):
    print(pila3.desapilar())
print('----------------------------------------------------------------------')






    


