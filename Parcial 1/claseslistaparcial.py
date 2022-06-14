
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
    
    def barrido_lista_lista(self):
        aux = self.__inicio
        while(aux is not None):
            print(aux.info)
            print('sublista:')
            aux.sublista.barrido()

            aux = aux.sig
    
    def barrido_segun_palabra(self, palabra):
        aux = self.__inicio
        while(aux is not None):
            if(palabra in aux.info.dato):
                print(aux.info)
            aux = aux.sig

    def barrido_segun_dino(self, palabra):
        aux = self.__inicio
        while(aux is not None):
            if(palabra in aux.info.name):
                print(aux.info)
            aux = aux.sig

    def barrido_segun_dino(self, palabra):
        aux = self.__inicio
        while(aux is not None):
            if(palabra in aux.info.name):
                print(aux.info.zona)
            aux = aux.sig

    def barrido_segun_menor(self, numero):
        aux = self.__inicio
        while(aux is not None):
            if(aux.info.dato < numero):
                print(aux.info)
            aux = aux.sig
    
    def barrido_segun_mayor(self, numero):
        aux = self.__inicio
        while(aux is not None):
            if(aux.info.dato > numero):
                print(aux.info)
            aux = aux.sig

    def barrido_comienza_con(self, letra):
        aux = self.__inicio
        while(aux is not None):
            if(aux.info.dato[0] in letra):
                print(aux.info)
            aux = aux.sig

    def barriduo_sublista_barrido(self):
        aux = self.__inicio
        while(aux is not None):
            aux.sublista.barrido()
            aux = aux.sig
    
    def mayor_de_lista(self, campo):
        aux = self.__inicio
        mayor = self.__inicio.info
        while(aux is not None):
            if(criterio(aux.info, campo) > criterio(mayor, campo)):
                mayor = aux.info
            aux = aux.sig
        return mayor

    def barrido_pocentaje(self, porciento):
        aux = self.__inicio
        while(aux is not None):
            porcentaje = (aux.info.dato1 + aux.info.dato2)
            if((aux.info.dato / porcentaje) >= porciento):
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

    def contar_segun_dato(self, dato):
        contador = 0

        aux = self.__inicio
        while(aux is not None):
            if(aux.info.dato == dato):
                contador += 1
            aux = aux.sig

        return contador

