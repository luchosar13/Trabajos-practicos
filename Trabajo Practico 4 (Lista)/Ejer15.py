from random import randint,choice
from lista import Lista
from lista2 import Lista

class Entrenador:
    nombre, torneos_ganados, batallas_perdidas, batallas_ganadas = None, None, None, None
    #def __init__(self, nombre, torneos_ganados, batallas_perdidas, batallas_ganadas):
    #    self.nombre = nombre
    #    self.torneos_ganados = torneos_ganados
    #    self.batallas_perdidas = batallas_perdidas
    #    self.batallas_ganadas = batallas_ganadas

class Pokemon():
    nombreP, nivel, tipo, subtipo = None, None, None, None

#Entrenadores
nombre = ['uno','dos','tres']
torneos_ganados = [2,10,6]
batallas_perdidas = [23,10,16]
batallas_ganadas = [40,63,59]
#Pokemones
nombreP = ['pkm1','pkm2','pkm3']
nivel = [2,1,5]
tipo = ['fuego','tierra','planta']
subtipo = ['lucha','dragon','normal']

lista_entrenadores = Lista()

for i in range (len(nombre)):
    dato = Entrenador()
    dato.nombre = nombre[i]
    dato.torneos_ganados = torneos_ganados[i]
    dato.batallas_perdidas = batallas_perdidas[i]
    dato.batallas_ganadas = batallas_ganadas[i]
    #print(dato.nombre,'--',dato.torneos_ganados,'--',dato.batallas_perdidas,'--',dato.batallas_ganadas)
    lista_entrenadores.insertar(dato, campo = 'nombre')

for i in range (len(nombre)):
    pos = lista_entrenadores.busqueda(nombre[i], campo = 'nombre')
    for j in range(randint(1, 5)):
        indice = randint(0, 2)
        pokemon = Pokemon()
        pokemon.nombreP = choice(nombreP)
        pokemon.nivel = choice(nivel)
        pokemon.tipo = choice(tipo)
        pokemon.subtipo = choice(subtipo)
        pos.sublista.insertar(pokemon, campo = 'nombreP')

lista_entrenadores.barrido_lista_lista()

#!A
print('---------------------------------------------------')
entrenador = str(input('Ingrese el entrenador: '))
pos = lista_entrenadores.busqueda(entrenador, 'nombre')
if(pos):
    print('El entrenador',entrenador,'tiene',pos.sublista.tamanio(),'pokemons.')
else:
    print('El entrenador',entrenador,'no se encuentra en la lista.')
#!B
print('---------------------------------------------------')
print('Los entrenadores con mas de tres torneos ganados son: ')
lista_entrenadores.barrido_entrenadormastres()
#!C
print('---------------------------------------------------')
mayor_entrenador = lista_entrenadores.mayor_de_lista('torneos_ganados')
mayor_pokemon = mayor_entrenador.sublista.mayor_de_lista('nivel')
print('El entrenador con mas torneos ganados es ', mayor_entrenador.info.nombre,'y su pokemon de mayor nivel es: ', mayor_pokemon.info.nombreP)
#!D
print('---------------------------------------------------')
entrenadorr = str(input('Ingrese el entrenador que quiere mostrar sus pokemones: '))
entrena = lista_entrenadores.busqueda(entrenadorr, 'nombre')
print('Los pokemones del entrenador',entrenadorr,'son: ')
entrena.sublista.barrido_pokemones()
#!E
print('---------------------------------------------------')
lista_entrenadores.barrido_mayor_79()
#!F
print('---------------------------------------------------')
lista_entrenadores.barrido_lista_lista1()
#!G
print('---------------------------------------------------')
lista_entrenadores.barrido_lista_lista2()
#!H
print('---------------------------------------------------')
pok = str(input('Ingrese el pokemon que desea analizar: '))
lista_entrenadores.barrido_lista_lista3(pok)
#!I
print('---------------------------------------------------')
lista_entrenadores.barrido_lista_lista_pok_repetidos()

