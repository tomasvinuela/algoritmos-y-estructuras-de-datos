
from lzma import CHECK_ID_MAX
from random import randint


class nodoPila():
    info, sig = None, None

class Pila():
    def __init__(self):
        self.__tamanio = 0
        self.__cima = None
    
    def tamanio(self):
        return self.__tamanio
    
    def apilar(self, dato):
        nodo = nodoPila()
        nodo.info = dato
        if(self.__cima is None):
            self.__cima = nodo
        else:
            nodo.sig = self.__cima
            self.__cima = nodo
        self.__tamanio += 1
    
    def desapilar(self):
        dato = self.__cima.info
        self.__cima = self.__cima.sig
        self.__tamanio -= 1
        return dato

    def cima(self):
        return self.__cima.info
    
    def pila_vacia(self):
        return self.__cima is None

