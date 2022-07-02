
from ctypes import sizeof


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
    
    def barrido_armadura_traje(self):
        aux = self.__inicio
        while(aux is not None):
            if('traje' in aux.info.bio or 'armadura' in aux.info.bio):
                print(aux.info)
            aux = aux.sig

    def barrido_anterior_1963(self):
        aux = self.__inicio
        while(aux is not None):
            if(aux.info.aparicion < 1963):
                print(aux.info)
            aux = aux.sig
    
    def barrido_jedi_master(self):
        aux = self.__inicio
        while(aux is not None):
            if('yoda' in aux.info.maestro or 'luke skywalker' in aux.info.maestro):
                print(aux.info)
            aux = aux.sig

    def barrido_mas_de_uno(self):
        aux = self.__inicio
        while(aux is not None):
            if(sizeof(aux.info.sable) > 1):
                print(aux.info)
            aux = aux.sig

    def barrido_por_anio(self, anio):
        aux = self.__inicio
        while(aux is not None):
            if(aux.info.anio == anio):
                print(aux.info)
            aux = aux.sig

    def barrido_violeta_amarillo(self):
        aux = self.__inicio
        while(aux is not None):
            if('violeta' in aux.info.sable or 'amarillo' in aux.info.sable):
                print(aux.info)
            aux = aux.sig

    def barrido_padawans(self):
        aux = self.__inicio
        while(aux is not None):
            if('Qui-Gon Jin' in aux.info.maestro or 'Mace Windu' in aux.info.maestro):
                print(aux.info.nombre)
            aux = aux.sig

    def barrido_comienza_con(self, iniciales=[]):
        aux = self.__inicio
        while(aux is not None):
            if(aux.info.nombre[0] in iniciales):
                print(aux.info)
            aux = aux.sig
    
    def barrido_torneos_ganadas(self):
        aux = self.__inicio
        while(aux is not None):
            if(aux.info.torneos > 3):
                print(aux.info)
            aux = aux.sig
    

    def barrido_tipo_subtipo(self):
        aux = self.__inicio
        while(aux is not None):
            if(aux.sublista.busqueda('fuego', 'tipo') and aux.sublista.busqueda('planta', 'subtipo')) or (aux.sublista.busqueda('agua', 'tipo') and aux.sublista.busqueda('volador', 'subtipo')):
                print(aux.info)
            aux = aux.sig

    def barriduo_segun_nombres(self, nombre_buscado):
        aux = self.__inicio
        while(aux is not None):
            if(aux.sublista.busqueda(nombre_buscado, 'nombre')):
               print(aux.info)
            aux = aux.sig

    def barriduo_de_repetidos(self):
        aux = self.__inicio
        while(aux is not None):
            if(aux.sublista.busqueda('fuego', 'tipo') and aux.sublista.busqueda('planta', 'subtipo')) or (aux.sublista.busqueda('agua', 'tipo') and aux.sublista.busqueda('volador', 'subtipo')):
                print(aux.info)
            aux = aux.sig

    def barrido_YODA_LUKE(self):
        aux = self.__inicio
        while(aux is not None):
            if('Yoda' in aux.info.maestro or 'Luke Skywalker' in aux.info.maestro):
                print(aux.info)
            aux = aux.sig

    def barrido_por_especie(self):
        aux = self.__inicio
        while(aux is not None):
            if('humana' in aux.info.especie or 'twilek' in aux.info.especie):
                print(aux.info)
            aux = aux.sig

    def contador_de_entrenadores(self, poke_busca):
        aux = self.__inicio
        contador = 0
        while(aux is not None):
            if(aux.sublista.busqueda(poke_busca, 'nombre')):
                contador += 1
            aux = aux.sig
        return contador


    def comparador(pokemones, numero, total):
        pokemon = pokemones.obtener_elemento(numero)
        resultado = 0
        while(total != numero):
            auxiliar = pokemones.obtener_elemento(total)
            if(auxiliar == pokemon):
                resultado = 1
                return resultado
            total = (total - 1)

    def pokemon_repetido(self):
        aux = self.__inicio
        while(aux is not None):
            veces = aux.sublista.tamanio()
            for i in range(veces):
                repite = aux.sublista.comparador(i, veces)
            if (repite == 1):
                print(aux.info)
            aux = aux.sig

    
    def mayor_de_lista(self, campo):
        aux = self.__inicio
        mayor = self.__inicio.info
        while(aux is not None):
            if(criterio(aux.info, campo) > criterio(mayor, campo)):
                mayor = aux.info
            aux = aux.sig
        return mayor

    def barriduo_segun_resenia(self, resenia):
        aux = self.__inicio
        while(aux is not None):
            if(aux.info.valoracion() == resenia):
               print(aux.info)
            aux = aux.sig

    def nivel_promedio(self):
        aux = self.__inicio
        promedio = 0
        contador = 0
        while(aux is not None):
            promedio += aux.nivel
            contador += 1
            aux = aux.sig
        promedio = (promedio / contador)
        return promedio


    def barrido_pocentaje_79(self):
        aux = self.__inicio
        while(aux is not None):
            porcentaje = (aux.info.ganadas + aux.info.perdidas)
            if((aux.info.ganadas / porcentaje) >= 0.79):
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

