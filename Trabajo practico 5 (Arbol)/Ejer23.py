from arbol import (
    busqueda,
    nodoArbol,
    insertar_nodo,
    inorden_empieza_con,
    contar_heroes,
    eliminar_nodo,
    inorden,
    postorden_heroes,
    crear_bosque,
    arbol_vacio,
    por_nivel,
)

ArbolCriaturas = nodoArbol()
ArbolDerrotados = nodoArbol()

lista = [
    ['Ceto','-','',''],
    ['Tifón','Zeus','',''],
    ['Equidna','Argos Panoptes','',''],
    ['Dino','-','',''],
    ['Toro de Creta','Teseo','',''],
    ['jabalí de Calidón','Atalanta','',''],
    ['Pefredo','-','',''],
    ['Basilisco','-','',''],
    ['Carcinos','-','',''],
    ['Aves del Estinfalo','-','',''],
    ['Enio','-','',''],
    ['Gerión','Heracles','',''],
    ['Sirenas','-','',''],
    ['Ladón','Heracles','','']
]

for criaturas, derrotadoPor, descrip, capturado in lista:
    datos = {'criaturas': criaturas,
             'derrotadoPor': derrotadoPor,
             'descrip' : descrip,
             'capturado' : capturado
             }
    insertar_nodo(ArbolCriaturas, criaturas, datos)
    insertar_nodo(ArbolDerrotados,derrotadoPor,datos)

print('---------------Listado de las criaturas / A ---------------')
def inorden_Cr(arbol):
    if(arbol is not None):
        inorden_Cr(arbol['izq'])
        print(arbol['info'],arbol['datos']['derrotadoPor'])
        inorden_Cr(arbol['der'])

inorden_Cr(ArbolCriaturas)

print()

print('---------------Agregar descripción / B ---------------')

pos2 = input('ingrese criatura que desea agregarle una descripción ')
pos3 = busqueda(ArbolCriaturas,pos2)
if pos3:
    pos4 = input('Ingrese la descripción que quiere agregarle: ')
    pos3['datos']['descrip'] = pos4

def inorden_(arbol):
    if(arbol is not None):
        inorden_(arbol['izq'])
        if arbol['info']:
            print(arbol['datos']['criaturas'],arbol['datos']['derrotadoPor'],arbol['datos']['descrip'])
        inorden_(arbol['der'])

inorden_(ArbolCriaturas)

print('---------------Información de la criatura Talos / C ---------------')
def inorden_Talos(arbol):
    if(arbol is not None):
        inorden_Talos(arbol['izq'])
        if arbol['info'] == 'Equidna':
            print(arbol['datos']['criaturas'],arbol['datos']['derrotadoPor'])
        inorden_Talos(arbol['der'])

inorden_Talos(ArbolCriaturas)

print()

print('---------------Criaturas derrotadas por Heracles / E ---------------')
def inorden_H(arbol):
    if(arbol is not None):
        inorden_H(arbol['izq'])
        if arbol['datos']['derrotadoPor'] == 'Heracles':
            print(arbol['datos']['criaturas'])
        inorden_H(arbol['der'])

inorden_H(ArbolCriaturas)

print()

print('---------------Criaturas que no fueron derrotadas / F ---------------')
def inorden_NoD(arbol):
    if(arbol is not None):
        inorden_NoD(arbol['izq'])
        if arbol['datos']['derrotadoPor'] == '-':
            print(arbol['datos']['criaturas'])
        inorden_NoD(arbol['der'])

inorden_NoD(ArbolCriaturas)

print()

print()

print('---------------Criaturas capturada por Heracles / H ---------------')
def inorden_cap(arbol):
    if(arbol is not None):
        inorden_cap(arbol['izq'])
        if arbol['info'] in ['Dino','Toro de Creta','Cierva Cerinea','Jabalí de Erimanto']:
            arbol['datos']['capturado'] = 'Heracles'
            print(arbol['info'],arbol['datos']['derrotadoPor'],arbol['datos']['descrip'],arbol['datos']['capturado'])
        inorden_cap(arbol['der'])

inorden_cap(ArbolCriaturas)

print()

print('---------------Listado por nivel del arbol de criaturas / M---------------')

por_nivel(ArbolCriaturas)

print()

print('---------------Eliminar a Basilisco y a Sirenas / J ---------------')

valor1 = eliminar_nodo(ArbolCriaturas,'Basilisco')
if valor1:
    print('Basilisco a sido eliminado')
else:
    print('Basilisco no se ha encontrado en el arbol')
print()
valor2 = eliminar_nodo(ArbolCriaturas,'Sirenas')
if valor2:
    print('Las Sirenas han sido eliminadas')
else:
    print('Las Sirenas no se han encontrado en el arbol')

print()

print('---------------Modificar nombre / L ---------------')

nom = input('ingrese criatura que desea modificar ')
poss = eliminar_nodo(ArbolCriaturas,nom)
if poss:
    nomb = input('Ingrese el nuevo nombre: ')
    insertar_nodo(ArbolCriaturas,nomb)
    print('El cambio se ha realizado con exito')
else:
    print('No se ha encontrado la criatura')

print()

print('---------------Modificar Aves del Estinfalo / K ---------------')

posi = busqueda(ArbolCriaturas,'Aves del Estinfalo')
if posi:
    posi['datos']['derrotadoPor'] = 'Heracles'
    print('La modificación se ha realizado con exito')


def inorden_ca(arbol):
    if(arbol is not None):
        inorden_ca(arbol['izq'])
        if arbol['info']:
            print(arbol['info'],arbol['datos']['derrotadoPor'],arbol['datos']['descrip'],arbol['datos']['capturado'])
        inorden_ca(arbol['der'])

#inorden_ca(ArbolCriaturas)

print('---------------Busqueda por coincidencia / I ---------------')

def inorden_coin(arbol, coin):
    if(arbol is not None):
        inorden_coin(arbol['izq'], coin)
        if [coin] in [arbol['info']]:
            print(arbol['info'])
        inorden_coin(arbol['der'], coin)

coin = str(input('Ingrese lo que quiere buscar: '))
inorden_coin(ArbolCriaturas, coin)

print()
