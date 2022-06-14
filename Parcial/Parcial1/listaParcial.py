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

    def barrido_alertas(self):
        aux = self.__inicio
        while(aux is not None):
            print(aux.info.time,'--',aux.info.zona_code,'--',aux.info.dino_number,'--',aux.info.alert_level)
            aux = aux.sig

    def barrido_alertas_zona_code(self):
        aux = self.__inicio
        while(aux is not None):
            if(aux.info.zona_code in ['WYG075','SXH966','LYF010']):
                print('El elemento eliminado es :', aux.info.zona_code)
                aux.eliminar_zona(aux.info.zona_code, 'zona_code')
            aux = aux.sig


    def barrido_alertas2(self):
        aux = self.__inicio
        while(aux is not None):
            print(aux.info.time,'--',aux.info.zona_code,'--',aux.info.dino_number,'--',aux.info.alert_level,'--',aux.info.nombre_dino,'--',aux.info.tipo)
            aux = aux.sig

    def barrido_alertas3(self):
        aux = self.__inicio
        while(aux is not None):
            if((aux.info.nombre_dino in ['Tyrannosaurus Rex','Spinosaurus','Giganotosaurus']) and (aux.info.alert_level not in ['low','medium'])):
                print(aux.info.time,'--',aux.info.zona_code,'--',aux.info.dino_number,'--',aux.info.alert_level,'--',aux.info.nombre_dino,'--',aux.info.tipo)
            aux = aux.sig

    def barrido_alertas4(self):
        aux = self.__inicio
        while(aux is not None):
            if(aux.info.nombre_dino in ['Raptors (Dromaeosauridae)','Carnotaurus']):
                print(aux.info.time,'--',aux.info.zona_code,'--',aux.info.dino_number,'--',aux.info.alert_level,'--',aux.info.nombre_dino,'--',aux.info.tipo)
            aux = aux.sig
            
    def barrido_alertas5(self):
        aux = self.__inicio
        print('Las zonas donde se encuentra el Compsognathus son :')
        while(aux is not None):
            if(aux.info.nombre_dino == 'Compsognathus'):
                print(aux.info.zona_code)
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

    def busqueda_dino(self, buscado, campo=None):
        pos = None
        aux = self.__inicio
        while(aux is not None and pos is None):
            if(criterio(aux.info, campo) == buscado):
                pos = aux
            aux = aux.sig

        return pos

    def busqueda_number(self, buscado, campo=None):
        pos = None
        aux = self.__inicio
        while(aux is not None and pos is None):
            if(criterio(aux.info.number, campo) == buscado):
                pos = aux
            aux = aux.sig

        return pos

    def busqueda(self, buscado, campo=None):
        pos = None
        aux = self.__inicio
        while(aux is not None and pos is None):
            if(criterio(aux.info.zona_code, campo) == buscado):
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

    def eliminar_zone(self, clave, campo=None):
        dato = None
        if(criterio(self.__inicio.info, campo) == clave):
            dato = self.__inicio.info
            self.__inicio = self.__inicio.sig
        else:
            anterior = self.__inicio
            actual = self.__inicio.sig
            while(actual is not None and criterio(actual.info.zona_code, campo) != clave):
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

    def mayor_de_lista_alertas(self, campo):
        mayor = self.__inicio
        aux = self.__inicio
        while(aux is not None):
            if(criterio(aux.info.time, campo) > criterio(mayor.info.time, campo)):
                mayor = aux
            aux = aux.sig
        return mayor