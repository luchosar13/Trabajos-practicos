
from re import A, M


def criterio(dato, campo=None):
    dic = {}
    if(hasattr(dato, '__dict__')):
        dic = dato.__dict__
    if(campo is None or campo not in dic):
        return dato
    else:
        return dic[campo]


class nodoLista():
    info, sig, sublista = None, None, None


class Lista():

    def __init__(self):
        self.__inicio = None
        self.__tamanio = 0


    def insertar(self, dato, campo=None):
        nodo = nodoLista()
        nodo.info = dato
        nodo.sublista = Lista()

        if(self.__inicio is None or criterio(nodo.info, campo) < criterio(self.__inicio.info, campo)):
            nodo.sig = self.__inicio
            self.__inicio = nodo
        else:
            anterior = self.__inicio
            actual = self.__inicio.sig
            while(actual is not None and criterio(nodo.info, campo) > criterio(actual.info, campo)):
                anterior = anterior.sig
                actual = actual.sig

            nodo.sig = actual
            anterior.sig = nodo

        self.__tamanio += 1

    def lista_vacia(self):
        return self.__inicio is None

    def tamanio(self):
        return self.__tamanio

    def barrido(self):
        aux = self.__inicio
        while(aux is not None):
            print(aux.info)
            aux = aux.sig

    def barrido_pokemoness(self):
        aux = self.__inicio
        while(aux is not None):
            print(aux.info.nombreP,'--',aux.info.nivel,'--',aux.info.tipo,'--',aux.info.subtipo)
            aux = aux.sig

    def barrido_mayor_79(self):
        aux = self.__inicio
        print('Los entrenadores que tienen porcentaje mayor a 79 en batallas ganadas son: ')
        while(aux is not None):
            total = aux.info.batallas_ganadas + aux.info.batallas_perdidas
            porcen = (aux.info.batallas_ganadas * 100) / total
            if(porcen > 79):
                print(aux.info.nombre)
            aux = aux.sig

    def barrido_pokemoness(self):
        aux = self.__inicio
        while(aux is not None):
            print(aux.info.nombreP,'--',aux.info.nivel,'--',aux.info.tipo,'--',aux.info.subtipo)
            aux = aux.sig

    def barrido_pokemonesss(self):
        aux = self.__inicio
        while(aux is not None):
            if(aux.info.tipo in ['fuego','planta']):
                print(aux.info.nombreP,'--',aux.info.nivel,'--',aux.info.tipo,'--',aux.info.subtipo)
            aux = aux.sig

    def barrido_lista_lista1(self):
        aux = self.__inicio
        while(aux is not None):
            print('El entrenador es el',aux.info.nombre,'y sus pokemones que son de tipo fuego o planta son: ')
            aux.sublista.barrido_pokemonesss()
            aux = aux.sig

    def barrido_pokemones_promedio(self):
        aux = self.__inicio
        a = 0
        b = 0
        while(aux is not None):
            if(aux.info.nivel):
                a += 1
                b += aux.info.nivel
            aux = aux.sig
        
        print(b/a)

    def barrido_pokemones_repetidos(self):
        aux = self.__inicio
        a = ''
        b = ''
        while(aux is not None):
            if(aux.info.nombre):
                a = aux.info.nombre
            if(aux.info.nombre == b):
                b = aux.info.nombre
            aux = aux.sig

            if(b):
                print(b)
    
    def barrido_lista_lista_pok_repetidos(self):
        aux = self.__inicio
        vec = []
        while(aux is not None):
            print('El entrenador',aux.info.nombre,'tiene el siguiente pokemon repetido: ')
            aux2 = aux.sublista.__inicio
            while(aux2 is not None):
                if(aux2.info.nombreP in vec):
                    print(aux2.info.nombreP)
                    break
                else:
                    vec.append(aux2.info.nombreP)
                aux2 = aux2.sig
            aux = aux.sig


    def barrido_lista_lista3(self, pok):
        aux = self.__inicio
        cont = 0
        while(aux is not None):
            po = None
            po = aux.sublista.busqueda2(pok , 'nombreP')
            if(po):
                cont += 1
            aux = aux.sig

        print('Los entrenadores con el pokemon',pok,'son: ',cont)

    def barrido_lista_lista2(self):
        aux = self.__inicio
        while(aux is not None):
            print('El entrenador es el',aux.info.nombre,'y el promedio de nivel de sus pokemones es: ')
            aux.sublista.barrido_pokemones_promedio()
            aux = aux.sig
    
    def barrido_lista_lista(self):
        aux = self.__inicio
        while(aux is not None):
            print('El entrenador es: ',aux.info.nombre,'y su sublista es: ')
            aux.sublista.barrido_pokemoness()
            aux = aux.sig

    
    def barrido_armadura_traje(self):
        aux = self.__inicio
        while(aux is not None):
            if('traje' in aux.info.bio or 'armadura' in aux.info.bio):
                print(aux.info)
            aux = aux.sig

    def barrido_pokemones(self):
        aux = self.__inicio
        while(aux is not None):
            print(aux.info.nombreP,'--',aux.info.nivel,'--',aux.info.tipo,'--',aux.info.subtipo)
            aux = aux.sig

    def barrido_entrenadormastres(self):
        aux = self.__inicio
        while(aux is not None):
            if(aux.info.torneos_ganados > 3):
                print(aux.info.nombre)
            aux = aux.sig

    def barrido_jedi_master(self):
        aux = self.__inicio
        while(aux is not None):
            if('yoda' in aux.info.maestro or 'luke skywalker' in aux.info.maestro):
                print(aux.info)
            aux = aux.sig

    def barrido_comienza_con(self, iniciales=[]):
        aux = self.__inicio
        while(aux is not None):
            if(aux.info.nombre[0] in iniciales):
                print(aux.info)
            aux = aux.sig

    def busqueda2(self, buscado, campo=None):
        pos = None
        aux = self.__inicio
        while(aux is not None and pos is None):
            if(criterio(aux.info.nombreP, campo) == buscado):
                pos = aux
            aux = aux.sig

        return pos

    def busqueda(self, buscado, campo=None):
        pos = None
        aux = self.__inicio
        while(aux is not None and pos is None):
            if(criterio(aux.info.nombre, campo) == buscado):
                pos = aux
            aux = aux.sig

        return pos

    def eliminar(self, clave, campo=None):
        dato = None
        if(criterio(self.__inicio.info, campo) == clave):
            dato = self.__inicio.info
            self.__inicio = self.__inicio.sig
        else:
            anterior = self.__inicio
            actual = self.__inicio.sig
            while(actual is not None and criterio(actual.info, campo) != clave):
                anterior = anterior.sig
                actual = actual.sig

            if(actual is not None):
                dato = actual.info
                anterior.sig = actual.sig

        return dato

    def obtener_elemento(self, indice):
        if(indice <= self.__tamanio-1 and indice >= 0):
            aux = self.__inicio
            for i in range(indice):
                aux = aux.sig
            return aux.info            
        else:
            return None

    def contar_por_casa(self):
        marvel, dc = 0, 0

        aux = self.__inicio
        while(aux is not None):
            if(aux.info.casa.capitalize() == 'Marvel'):
                marvel += 1
            if(aux.info.casa.capitalize() == 'Dc'):
                dc += 1
            aux = aux.sig

        return marvel, dc

    def mayor_de_lista(self):
        aux = self.__inicio
        mayor = 0
        while(aux is not None):
            if(aux.info.torneos_ganados > mayor):
                mayor = aux.info.torneos_ganados
                entre = aux.info.nombre
            aux = aux.sig

        print(entre)

    def mayor_pokemonNivel(self):
        mayor = 0
        aux = self.__inicio
        while(aux is not None):
            if(aux.info.sublista.nivel > mayor):
                mayor = aux.info.sublista.nivel
                poke = aux.info.sublista.nombreP
            aux = aux.sig

        print(poke)

    def mayor_de_lista(self, campo):
        mayor = self.__inicio
        aux = self.__inicio
        while(aux is not None):
            if(criterio(aux.info, campo) > criterio(mayor.info, campo)):
                mayor = aux.info
                break
            aux = aux.sig
        return mayor

# cadena = 'hola'
# cadena.startswith('C')
# print(cadena[0])

# class Persona:

#     def __init__(self, apellido, nombre, dni):
#         self.apellido = apellido
#         self.nombre = nombre
#         self.dni = dni
#         self.telefono = None
    
#     def __str__(self):
#         return f"{self.apellido} {self.nombre}, {self.dni}"



# p = Persona('A', 'A', 3)
# num = 45
# cadena = 'hola'
# print(criterio(p, 'mail'))
# print(criterio(p, 'apellido'))
# print(criterio(num))
# print(criterio(num, 'tel'))
# print(criterio(cadena, 'mail'))
# print(criterio(cadena))


# l = Lista()

# l.insertar(Persona('A', 'A', 7), 'nombre')
# l.insertar(Persona('C', 'C', 2), 'nombre')
# l.insertar(Persona('A', 'A', 11), 'nombre')
# l.insertar(Persona('B', 'Z', 1), 'nombre')
# l.insertar(Persona('B', 'H', 10), 'nombre')
# l.insertar(Persona('B', 'X', 4), 'nombre')

# Persona dni = 5 nombre = G




# l.eliminar('A', 'nombre')
# l.insertar(11)
# l.insertar(8)
# l.insertar(9)
# l.insertar(10)
# l.insertar(5)

# print(l.obtener_elemento(0))
# print(l.obtener_elemento(-2))
# print(l.obtener_elemento(5))
# print(l.obtener_elemento(8))

# pos = l.eliminar(8)
# if pos is not None:
#     l.insertar(18)


# print(l.eliminar(5))
# print(l.eliminar(7))
# print(l.eliminar(10))


# l.barrido()

# print(l.busqueda(7).info)
# print(l.busqueda(2))


# vocales = ['A', 'E',.....]

# for vocal in vocale:
#     aux = l.eliminar(vocal)
#     while(aux is not None):
#         aux = l.eliminar(vocal)

