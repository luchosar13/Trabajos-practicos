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
    por_nivel,
)

arbol = nodoArbol()

lista = [['yoda',0.7,30],
        ['mandalorian',1.7,100],
        ['luke skywalker',1.87,96],
        ['grogu',0.8,67],
        ['obi wan',1.50,56],
        ['darth vader',1.93,110],
        ['mace windu',1.25,58],
        ['plo koon',1.52,73],
        ['yaddle',0.60,40],
        ['kit fisto',1.68,79]
        ]

for nombre, medida, peso in lista:
        datos = {'nombre': nombre,
                'medida': medida,
                'peso': peso
                }
        insertar_nodo(arbol, nombre, datos)

print('-------------------Punto A-------------------')
bus = input('Ingrese Jedi que desea eliminar: ')
eliminar_nodo(arbol, bus)
pos = input('ingrese Jedi que desea modificar: ')
pos1 = busqueda(arbol,pos)
cambio = input('Ingrese que dato desea modificar: ')
if pos1:
    pos2 = input('Ingrese el nuevo dato que desea modificarle: ')
    pos1['datos'][cambio] = pos2

def inorden_jedis(arbol):
    if(arbol is not None):
        inorden_jedis(arbol['izq'])
        if arbol['info']:
            print(arbol['info'],arbol['datos']['peso'],arbol['datos']['medida'])
        inorden_jedis(arbol['der'])

inorden_jedis(arbol)
buss = input('Desea agregar un nuevo Jedi: ')
if buss == 'si':
    dato_nombre = input('Ingrese su nombre: ')
    dato_medida = input('ingrese su medida: ')
    dato_peso = input('Ingrese su peso: ')
    insertar_nodo(arbol, dato_nombre, datos=[dato_medida,dato_peso])

print('')

print('-------------------Punto B-------------------')

def inorden_jedis(arbol):
    if(arbol is not None):
        inorden_jedis(arbol['izq'])
        if arbol['info']:
            print(arbol['info'],arbol['datos']['peso'],arbol['datos']['medida'])
        inorden_jedis(arbol['der'])

inorden_jedis(arbol)

print('')

print('-------------------Punto C-------------------')

print('Los Jedis que miden menos de 0.9 metros son: ')
def inorden_jedis_medida(arbol):
    if(arbol is not None):
        inorden_jedis_medida(arbol['izq'])
        if arbol['datos']['medida'] < 0.9:
            print(arbol['info'])
        inorden_jedis_medida(arbol['der'])

inorden_jedis_medida(arbol)

print('')

print('-------------------Punto D-------------------')

print('Los Jedis que pesan mas de 75 kg son: ')
def inorden_jedis_peso(arbol):
    if(arbol is not None):
        inorden_jedis_peso(arbol['izq'])
        if arbol['datos']['peso'] > 75:
            print(arbol['info'])
        inorden_jedis_peso(arbol['der'])

inorden_jedis_peso(arbol)

print('')
print('-------------------Punto E-------------------')

print('Barrido por nivel de los Jedis')
print('')
por_nivel(arbol)

print('')

print('-------------------Punto F-------------------')
buscar_grogu = busqueda(arbol, 'grogu')
if buscar_grogu:
    print('Se ha encontrado a Grogu y sus datos son: ')
    print(buscar_grogu['info'], buscar_grogu['datos']['medida'], buscar_grogu['datos']['peso'])

