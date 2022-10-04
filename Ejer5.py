from arbol import (
    altura,
    nodoArbol,
    busqueda,
    insertar_nodo,
    inorden_empieza_con,
    contar_heroes,
    eliminar_nodo,
    inorden,
    postorden,
    postorden_heroes,
    crear_bosque,
    arbol_vacio,
)

arbol = nodoArbol()


heroes = nodoArbol()
villanos = nodoArbol()


lista = [
    ['iron man', False, 1960],
    ['capitana marvel', False, 1890],
    ['thor', False, 1962],
    ['dotor strange', False, 1961],
    ['thanos', True, 1962],
    ['red skull', True, 1963],
    ['capitan america', False, 2000],
]

for nombre, villano, anio_aparicion in lista:
    if villano is True:
        datos = {'nombre': nombre,
                'villano': villano,
                'anio_aparicion': anio_aparicion
                }
        insertar_nodo(villanos, nombre, datos)
    else:
        datos = {'nombre': nombre,
                'villano': villano,
                'anio_aparicion': anio_aparicion
                }
        insertar_nodo(heroes, nombre, datos)

print('---------------Listado de los villanos / B ---------------')

inorden(villanos)

print()

print('---------------Superheroes que empiezan con C / C ---------------')

def inorden_Empieza_C(arbol):
    if(arbol is not None):
        inorden_Empieza_C(arbol['izq'])
        if arbol['info'][0] in ['c','C']:
            print(arbol['info'])
        inorden_Empieza_C(arbol['der'])

inorden_Empieza_C(heroes)

print()

print('---------------Cantidad de superheroes / D ---------------')

def contar_heroes(arbol):
    contador=0
    if(arbol is not None):
        if arbol['datos']['villano'] is False:
            contador += 1
            contador += contar_heroes(arbol['izq'])
            contador += contar_heroes(arbol['der'])
    return(contador)

contar_heroes(heroes)

print()

print('---------------Modificar nombre / E ---------------')

nom = input('ingrese un Superheroe que desea modificar ')
buss = busqueda(heroes, nom)
if buss is not None:
    poss = eliminar_nodo(heroes,nom)
else:
    print('No ha ingresado una Superheroe valido')

if poss:
    nomb = input('Ingrese el nuevo nombre: ')
    insertar_nodo(heroes,nomb)
    print()
    print('El cambio se ha realizado con exito y el nuevo nombre es: ',nomb)
else:
    print()
    print('No se ha encontrado el Superheroe')

print()

print('---------------Listado de los Superheroes descendentes / F ---------------')

def postorden_H(arbol):
    if(arbol is not None):
        postorden_H(arbol['der'])
        print(arbol['info'])
        postorden_H(arbol['izq'])

postorden_H(heroes)

print()

crear_bosque(arbol, heroes, villanos)



