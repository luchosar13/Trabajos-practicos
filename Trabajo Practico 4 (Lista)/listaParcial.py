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
            print(aux.info.nombre,'--',aux.info.maestro,'--',aux.info.colorS,'--',aux.info.especie)
            aux = aux.sig

    def barrido_a(self):
        aux = self.__inicio
        a = 'ahsoka tano'
        b = 'kit fisto'
        while(aux is not None):
            if(aux.info.nombre == a or aux.info.nombre == b):
                print(aux.info.nombre,'--',aux.info.maestro,'--',aux.info.colorS,'--',aux.info.especie)
            aux = aux.sig

    def barrido_b(self):
        aux = self.__inicio
        a = 'padawan'
        b = 'jedi master'
        while(aux is not None):
            if(aux.info.maestro == a or aux.info.nombre == b):
                print(aux.info.nombre)
            aux = aux.sig
        
    def barrido_c(self):
        aux = self.__inicio
        while(aux is not None):
            if('human' in aux.info.especie):
                print(aux.info.nombre,'--',aux.info.maestro,'--',aux.info.colorS,'--',aux.info.especie)
            aux = aux.sig

    def barrido_d(self):
        aux = self.__inicio
        while(aux is not None):
            nombre = None
            nombre = aux.info.nombre
            if(nombre[0] is 'a'):
                print(aux.info.nombre,'--',aux.info.maestro,'--',aux.info.colorS,'--',aux.info.especie)
            aux = aux.sig

    def barrido_e(self):
        aux = self.__inicio
        while(aux is not None):
            sable = None
            sable = aux.info.colorS
            if(len(sable) > 1):
                print(aux.info.nombre,'--',aux.info.maestro,'--',aux.info.colorS,'--',aux.info.especie)
            aux = aux.sig

    def barrido_f(self):
        aux = self.__inicio
        a = 'yellow'
        b = 'purple'
        while(aux is not None):
            color = aux.info.colorS
            if(a in color or b in color):
                print(aux.info.nombre,'--',aux.info.maestro,'--',aux.info.colorS,'--',aux.info.especie)
            aux = aux.sig
    
    def barrido_lista_lista(self):
        aux = self.__inicio
        while(aux is not None):
            print(aux.info)
            print('sublista:')
            aux.sublista.barrido()
            print("-------------------------------")
            # aux1 = aux.sublista.__inicio
            # while(aux1 is not None):
            #     print('  ', aux1.info)
            #     aux1 = aux1.sig

            aux = aux.sig


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
        if dato:
            self.__tamanio -= 1 

        return dato

    def obtener_elemento(self, indice):
        if(indice <= self.__tamanio-1 and indice >= 0):
            aux = self.__inicio
            for i in range(indice):
                aux = aux.sig
            return aux.info            
        else:
            return None

    
    def mayor_de_lista(self, campo):
        mayor = self.__inicio
        aux = self.__inicio
        while(aux is not None):
            if(criterio(aux.info, campo) > criterio(mayor.info, campo)):
                mayor = aux
            aux = aux.sig
        return mayor