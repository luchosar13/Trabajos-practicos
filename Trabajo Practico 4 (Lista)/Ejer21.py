from lista import Lista
from pila import Pila

class Peliculas():
    nombre, valoracion, anioEstreno, recaudacion = None, None, None, None

nombre = ['Harry Potter I','Top Gun','Inglourious Basterds','Titanic','Pirates Of The Caribbean I']
valoracion = [10,7,8,10,9]
anioEstreno = ['1997','1986','2009','1997','2003']
recaudacion = [87000000,75000000,237000000,53000000,654000000]


lista1 = Lista()
pila1 = Pila()

i = 0
for i in range(len(nombre)):
    dato = Peliculas()
    dato.nombre = nombre[i]
    dato.valoracion = valoracion[i]
    dato.anioEstreno = anioEstreno[i]
    dato.recaudacion = recaudacion[i]
    print(dato.nombre,'--',dato.valoracion,'--',dato.anioEstreno,'--',dato.recaudacion)
    lista1.insertar(dato,campo= 'nombre')

print('------------------Peliculas filtradas por anio de estreno------------------')
# !A
lista1.barrido_anio()
print('------------------Pelicula con mas recaudación------------------')
# !B
lista1.barrido_recaudo()
print('------------------Peliculas con mayor valoracion------------------')
# !C
lista1.barrido_valoracion()
