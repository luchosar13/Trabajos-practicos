from pila import Pila

def criterio(dato, campo=None):
    dic = {}
    if(hasattr(dato, '__dict__')):
        dic = dato.__dict__
    if(campo is None or campo not in dic):
        return dato
    else:
        return dic[campo]

class nodoLista():
    info, sig = None, None


class Lista():

    def __init__(self):
        self.__inicio = None
        self.__tamanio = 0


    def insertar(self, dato, campo=None):
        nodo = nodoLista()
        nodo.info = dato

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

    def barrido_fechas(self):
        pila1 = Pila()
        pila2 = Pila()
        aux = self.__inicio
        while(aux is not None):
            if(aux.info.fechaEstimada == aux.info.fechaEfectiva):
                pila1.apilar(aux.info.actividad)
            elif(aux.info.fechaEstimada != aux.info.fechaEfectiva):
                pila2.apilar(aux.info.actividad)
            aux = aux.sig
        print('Las actividades que se entregaron a tiempo fueron: ')
        while(not pila1.pila_vacia()):
            print(pila1.desapilar())
        print('Las actividades que se entregaron fuera de tiempo fueron: ')
        while(not pila2.pila_vacia()):
            print(pila2.desapilar())
        
    
    
    def barrido_actividades(self):
        a = str(input('Ingrese la persona que desea saber que actividades realiza: '))
        pila3 = Pila()
        aux = self.__inicio
        while(aux is not None):
            if(aux.info.personaCargo == a):
                pila3.apilar(aux.info.actividad)
            aux = aux.sig

        print('Las actividades realizadas por ',a,' son: ')
        while(not pila3.pila_vacia()):
            print(pila3.desapilar())

    def barrido_promedioTareas(self):
        a = 0
        b = 0
        aux = self.__inicio
        while(aux is not None):
            if(aux.info.tiempoEjecucion > 0):
                a += 1
                b += aux.info.tiempoEjecucion
            aux = aux.sig
        print('El tiempo promedio de ejecucion de los procesos es de: ', b/a ,'días.')

    def barrido_costo(self):
        a = 0
        aux = self.__inicio
        while(aux is not None):
            if(aux.info.costo > 0):
                a += aux.info.costo
            aux = aux.sig
        print('El costo total del proyecto es de: $',a)

    def barrido_anio(self):
        aux = self.__inicio
        anio = str(input('Ingrese anio en el que desea filtrar las peliculas: '))
        while(aux is not None):
            if(aux.info.anioEstreno == anio):
                print(aux.info.nombre)
            aux = aux.sig

    def barrido_recaudo(self):
        aux = self.__inicio
        a = 0
        b = ''
        while(aux is not None):
            if(aux.info.recaudacion > a):
                a = aux.info.recaudacion
                b = aux.info.nombre
            aux = aux.sig
        
        print('La pelicula que mas recaudó fue',b,'con $',a)

    def barrido_valoracion(self):
        aux = self.__inicio
        a = 0
        aN = ''
        b = 0
        bN = ''
        while(aux is not None):
            if(aux.info.valoracion > a):
                a = aux.info.valoracion
                aN = aux.info.nombre
            elif(aux.info.valoracion == a):
                b = aux.info.valoracion
                bN = aux.info.nombre
            aux = aux.sig

        if(a and b):
            print('Las peliculas con mayor valoración son :')
            print(aN,'con valoración',a)
            print(bN,'con valoración',b)
        elif(a):
            print('La pelicula con mayor valoración es :')
            print(aN,'con valoración',a)
        
        

    def barrido_tailandia(self):
        aux = self.__inicio
        while(aux is not None):
            if('Tailandia' in aux.info.destino):
                print('La empresa',aux.info.empresa,'tiene un vuelo a Tailandia con la distancia de',aux.info.kms,'kilometros')
            aux = aux.sig
    
    def barrido_vendervuelo(self):
        vuelo = int(input('Ingrese el vuelo en el que desea comprar un pasaje: '))
        clase = str(input('Ingrese la clase en la que desea viajar: '))
        aux = self.__inicio
        while(aux is not None):
            if(aux.info.numeroVuelo == vuelo):
                if(clase == 'turista'):
                    aux.info.turista += 1
                    break
                elif(clase == 'primera'):
                    aux.info.primera += 1
                    break
            aux = aux.sig
        print('Usted ha comprado un pasaje en el vuelo',aux.info.numeroVuelo,'con clase',clase,'.')
        print('Actualización del vuelo: ',aux.info.empresa,'--',aux.info.numeroVuelo,'--',aux.info.turista,'--',aux.info.primera,'--',aux.info.fechaS)

    totalKms = 0
    totalTurista = 0
    totalPrimera = 0
    total = 0
    def barrido_totalRecaudado(self):
        aux = self.__inicio
        while(aux is not None):
            if(aux.info.turista > 0 or aux.info.primera > 0):
                kmsTurista = 75 * aux.info.kms
                kmsPrimera = 203 * aux.info.kms
                totalTurista = aux.info.turista * kmsTurista
                totalPrimera = aux.info.primera * kmsPrimera
                total = totalTurista + totalPrimera
                print('El total recaudado en el vuelo',aux.info.numeroVuelo,'es de : ', '$',total)
            aux = aux.sig

    def barrido_turista(self):
        aux = self.__inicio
        while(aux is not None):
            if(aux.info.turista > 0):
                print(aux.info.empresa,'--',aux.info.numeroVuelo,'--',aux.info.cantAsientos,'--',aux.info.fechaS,'--',aux.info.destino,'--',aux.info.kms,'--',aux.info.turista,'--',aux.info.primera)
                #print(aux.info.empresa,'--',aux.info.numeroVuelo,'--',aux.info.cantAsientos,'--',aux.info.fechaS)
                #print('Empresa del vuelo: ',aux.info.empresa)
                #print('Numero de vuelo: ',aux.info.numeroVuelo,),'/Numero de vuelo:',aux.info.numeroVuelo,'--',aux.info.cantAsientos,'--',aux.info.cantAsientos,'--',aux.info.fechaS)
            aux = aux.sig
        
    def barrido_Fecha(self):
        aux = self.__inicio
        fecha = str(input('Ingrese la fecha del vuelo que desea buscar la informacion :'))
        while(aux is not None):
            if(aux.info.fechaS == fecha):
                print('Empresa del vuelo: ',aux.info.empresa)
                print('Numero de vuelo: ',aux.info.numeroVuelo)
                print('Cantidad de asientos :',aux.info.cantAsientos)
                print('Destino: ', aux.info.destino)
                print('Distancia del viaje en kilometros: ',aux.info.kms)
            aux = aux.sig
    
    def barrido_armadura_traje(self):
        aux = self.__inicio
        while(aux is not None):
            if('traje' in aux.info.bio or 'armadura' in aux.info.bio):
                print(aux.info)
            aux = aux.sig

    def barrido_1963(self):
        aux = self.__inicio
        while(aux is not None):
            if(aux.info.anio < 1963):
                print(aux.info)
            aux = aux.sig
    
    def barrido_comienza_con(self, iniciales=[]):
        aux = self.__inicio
        while(aux is not None):
            if(aux.info.nombre[0] in iniciales):
                print(aux.info)
            aux = aux.sig

    def busqueda(self, buscado, campo=None):
        pos = None
        aux = self.__inicio
        while(aux is not None and pos is None):
            if(criterio(aux.info, campo) == buscado):
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

    def eliminar_vuelo(self, clave, campo=None):
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


