from clasescola import Cola
from clasesheaps import HeapMin, HeapMax


def criterio(dato, campo=None):
    dic = {}
    if(hasattr(dato, '__dict__')):
        dic = dato.__dict__
    if(campo is None or campo not in dic):
        return dato
    else:
        return dic[campo]


class nodoArista():
    info, sig, peso = None, None, None
    #? info es el destino


class nodoVertice():
    info, sig, visitado, adyacentes, datos = None, None, False, None, None


class Arista():
    
    def __init__(self):
        self.__inicio = None
        self.__tamanio = 0

    def get_inicio(self):
        return self.__inicio

    def insertar_arista(self, dato, peso, campo=None):
        nodo = nodoArista()
        nodo.info = dato
        nodo.peso = peso

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

    def tamanio(self):
        return self.__tamanio

    def barrido_aristas(self):
        aux = self.__inicio
        while(aux is not None):
            print(aux.info, aux.peso)
            aux = aux.sig
    
    def busqueda_arista(self, buscado, campo=None):
        pos = None
        aux = self.__inicio
        while(aux is not None and pos is None):
            if(criterio(aux.info, campo) == buscado):
                pos = aux
            aux = aux.sig

        return pos

    def eliminar_arista(self, clave, campo=None):
        dato, peso = None, None
        if self.__inicio is not None:
            if(criterio(self.__inicio.info, campo) == clave):
                dato = self.__inicio.info
                peso = self.__inicio.peso
                self.__inicio = self.__inicio.sig
            else:
                anterior = self.__inicio
                actual = self.__inicio.sig
                while(actual is not None and criterio(actual.info, campo) != clave):
                    anterior = anterior.sig
                    actual = actual.sig

                if(actual is not None):
                    dato = actual.info
                    peso = actual.peso
                    anterior.sig = actual.sig
            if dato:
                self.__tamanio -= 1 

        return dato, peso

    def obtener_elemento_arista(self, indice):
        if(indice <= self.__tamanio-1 and indice >= 0):
            aux = self.__inicio
            for i in range(indice):
                aux = aux.sig
            return aux.info            
        else:
            return None


class Grafo():

    def __init__(self, dirigido=True):
        self.__inicio = None
        self.__tamanio = 0
        self.__dirigido = dirigido


    def insertar_vertice(self, dato, campo=None, datos=None):
        nodo = nodoVertice()
        nodo.info = dato
        nodo.datos = datos
        nodo.adyacentes = Arista()

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

    def insertar_arista(self, origen, destino, peso):
        vert_origen = self.busqueda_vertice(origen)
        vert_destino = self.busqueda_vertice(destino)
        if(vert_origen and vert_destino):
            vert_origen.adyacentes.insertar_arista(destino, peso)
            if not self.__dirigido:
                vert_destino.adyacentes.insertar_arista(origen, peso)

    def tamanio(self):
        return self.__tamanio

    def barrido_vertice(self):
        aux = self.__inicio
        while(aux is not None):
            print(aux.info)
            aux = aux.sig
    
    def marcar_no_visitado(self):
        aux = self.__inicio
        while(aux is not None):
            aux.visitado = False
            aux = aux.sig

    # def barrido_lista_lista(self, origen):
    #     self.marcar_no_visitado()
    #     # aux = self.busqueda_vertice(origen)
    #     aux = self.__inicio
    #     while(aux is not None):
    #         print('Vertice:', aux.info)
    #         print('arsitas:')
    #         aux.adyacentes.barrido_aristas()
    #         aux = aux.sig

    def busqueda_vertice(self, buscado, campo=None):
        pos = None
        aux = self.__inicio
        while(aux is not None and pos is None):
            if(criterio(aux.info, campo) == buscado):
                pos = aux
            aux = aux.sig

        return pos

    def barrido_no_visitado(self):
        aux = self.__inicio
        while(aux is not None):
            if not aux.visitado:
                print(aux.info)
            aux = aux.sig
    

    def eliminar_vertice(self, clave, campo=None):
        dato = None
        if self.__inicio is not None:
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

            #! eliminar todas las aristas que apuntan al vertice
            aux = self.__inicio
            while(aux is not None):
                aux.adyacentes.eliminar_arista(clave)
                aux = aux.sig
            
        return dato

    def eliminar_arista(self, origen, destino):
        vert_origen = self.busqueda_vertice(origen)
        valor, peso = None, None
        if vert_origen:
            valor, peso = vert_origen.adyacentes.eliminar_arista(destino)
            if valor:
                vert_destino = self.busqueda_vertice(destino)
                vert_destino.adyacentes.eliminar_arista(origen)

        return peso

    def obtener_elemento_vertice(self, indice):
        if(indice <= self.__tamanio-1 and indice >= 0):
            aux = self.__inicio
            for i in range(indice):
                aux = aux.sig
            return aux.info            
        else:
            return None
    
    def es_adyacente(self, origen, destino):
        resultado = False
        vert_origen = self.busqueda_vertice(origen)
        if vert_origen:
            aux = vert_origen.adyacentes.busqueda_arista(destino)
            if aux:
                resultado = True
        return resultado

    def adyacentes(self, origen):
        vert_origen = self.busqueda_vertice(origen)
        if vert_origen:
            vert_origen.adyacentes.barrido_aristas()

    def existe_paso(self, origen, destino):
        resultado = False
        vert_origen = self.busqueda_vertice(origen)
        if not vert_origen.visitado:
            vert_origen.visitado = True
            print(vert_origen.info)
            adyacentes = vert_origen.adyacentes.get_inicio()
            # resultado = g.es_adyacente(origen, destino)
            while adyacentes is not None and not resultado:
                if adyacentes.info == destino:
                    resultado = True
                else:
                    resultado = self.existe_paso(adyacentes.info, destino)
                adyacentes = adyacentes.sig
        return resultado

    def barrido_profundidad(self, origen):
        vert_origen = self.busqueda_vertice(origen)
        if not vert_origen.visitado:
            print(vert_origen.info)
            vert_origen.visitado = True
            adyacentes = vert_origen.adyacentes.get_inicio()
            while adyacentes is not None:
                self.barrido_profundidad(adyacentes.info)
                adyacentes = adyacentes.sig
    
    def barrido_amplitud(self, origen):
        self.marcar_no_visitado()
        vert_origen = self.busqueda_vertice(origen)
        pendientes = Cola()
        if not vert_origen.visitado:
            vert_origen.visitado = True
            pendientes.arribo(vert_origen)
            while not pendientes.cola_vacia():
                vertice_actual = pendientes.atencion()
                print(vertice_actual.info)
                adyacentes = vertice_actual.adyacentes.get_inicio()
                while adyacentes is not None:
                    adyacente = self.busqueda_vertice(adyacentes.info)
                    if not adyacente.visitado:
                        adyacente.visitado = True
                        pendientes.arribo(adyacente)
                    adyacentes = adyacentes.sig

#Devuelve el camino mas corto entre 2 vertices
    def dijkstra(self, origen):
        from math import inf
        # self.marcar_no_visitado()
        no_visitado = HeapMin()
        camino = {}

        aux = self.__inicio
        while aux is not None:
            if aux.info == origen:
                no_visitado.agregar([aux, None], 0)
            else:
                no_visitado.agregar([aux, None], inf)
            aux = aux.sig

        while no_visitado.tamanio > 0:
            elemento, peso = no_visitado.quitar()
            vertice, previo = elemento[0], elemento[1]
            camino[vertice.info] = {'previo': previo, 'peso': peso}
            adyacentes = vertice.adyacentes.get_inicio()
            while adyacentes is not None:
                buscado = no_visitado.buscar(adyacentes.info)
                if buscado:
                    if no_visitado.vector[buscado][1] > peso + adyacentes.peso:
                        no_visitado.vector[buscado][1] = peso + adyacentes.peso
                        no_visitado.vector[buscado][0][1] = vertice.info
                        no_visitado.flotar(buscado)
                adyacentes = adyacentes.sig
        return camino

#Kruskal devuelve el arbol de expansion minimo
    def kruskal(self):
        def buscar_en_bosque(bosque, buscado):
            for arbol in bosque:
                if buscado in arbol:
                    return arbol

        bosque = []
        aristas = HeapMin()
        aux = self.__inicio
        while aux is not None:
            bosque.append(str(aux.info))
            adyacentes = aux.adyacentes.get_inicio()
            while adyacentes is not None:
                aristas.arribo([aux.info, adyacentes.info], adyacentes.peso)
                adyacentes = adyacentes.sig
            aux = aux.sig

        while len(bosque) > 1 and aristas.tamanio > 0:
            arista, peso = aristas.quitar()
            # print(bosque)
            # print(arista[0])
            # print(arista[1])
            origen = buscar_en_bosque(bosque, arista[0])
            destino = buscar_en_bosque(bosque, arista[1])
            # print(origen, destino, 'posiciones')
            if origen is not None and destino is not None:
                if origen != destino:
                    # print(arista[0], origen)
                    # print(arista[1], destino)
                    bosque.remove(origen)
                    bosque.remove(destino)
                    if ';' not in origen and ';' not in destino:
                        bosque.append(f'{origen};{destino};{peso}')
                    elif ';' in origen and ';' not in destino:
                        bosque.append(origen+f'-{arista[0]};{destino};{peso}')
                    elif ';' not in origen and ';' in destino:
                        bosque.append(destino+f'-{origen};{arista[1]};{peso}')
                    else:
                        bosque.append(origen+'-'+destino+f'-{arista[0]};{arista[1]};{peso}')

            # print(bosque)
            # a = input()
        return bosque


    def camino(self, resultados, origen, destino):
        camino_mas_corto = {'camino': [],
                            'costo': None}
        if destino in resultados:
            vert_destino = resultados[destino]
            camino_mas_corto['costo'] = vert_destino['peso']
            camino_mas_corto['camino'].append(destino)
            while vert_destino['previo'] is not None:
                camino_mas_corto['camino'].append(vert_destino['previo'])
                vert_destino = resultados[vert_destino['previo']]
            camino_mas_corto['camino'].reverse()

        
        return camino_mas_corto

    def camino_y_peso(self, resultados, origen, destino):
        contador_peso = 0
        camino_mas_corto = {'camino': [],
                            'costo': None}
        if destino in resultados:
            vert_destino = resultados[destino]
            camino_mas_corto['costo'] = vert_destino['peso']
            camino_mas_corto['camino'].append(destino)
            while vert_destino['previo'] is not None:
                contador_peso += int(vert_destino['peso'])
                camino_mas_corto['camino'].append(vert_destino['previo'])
                vert_destino = resultados[vert_destino['previo']]
            camino_mas_corto['camino'].reverse()

        
        return camino_mas_corto, contador_peso

    def kruskal_carac(self, carac):
        def buscar_en_bosque(bosque, buscado):
            for arbol in bosque:
                if buscado in arbol:
                    return arbol

        bosque = []
        aristas = HeapMin()
        aux = self.__inicio
        while aux is not None:
            if (carac in aux.datos):
                bosque.append(str(aux.info))
                adyacentes = aux.adyacentes.get_inicio()
                while adyacentes is not None:
                    aristas.arribo([aux.info, adyacentes.info], adyacentes.peso)
                    adyacentes = adyacentes.sig
            aux = aux.sig

        while len(bosque) > 1 and aristas.tamanio > 0:
            arista, peso = aristas.quitar()
            origen = buscar_en_bosque(bosque, arista[0])
            destino = buscar_en_bosque(bosque, arista[1])
            if origen is not None and destino is not None:
                if origen != destino:
                    bosque.remove(origen)
                    bosque.remove(destino)
                    if ';' not in origen and ';' not in destino:
                        bosque.append(f'{origen};{destino};{peso}')
                    elif ';' in origen and ';' not in destino:
                        bosque.append(origen+f'-{arista[0]};{destino};{peso}')
                    elif ';' not in origen and ';' in destino:
                        bosque.append(destino+f'-{origen};{arista[1]};{peso}')
                    else:
                        bosque.append(origen+'-'+destino+f'-{arista[0]};{arista[1]};{peso}')

        return bosque


    def encontrar_paises_dobles(self, almacenador_paises):
        aux = self.__inicio
        almacenador_naturales = []
        almacenador_arquitectonicas= []
        while(aux is not None):
            if ('Natur' in aux.datos[1]):
                data = aux.datos[0]
                data = data.split(',')
                for d in data:
                    almacenador_naturales.append(d)
            if ('Arqui' in aux.datos[1]):
                data = aux.datos[0]
                data = data.split(',')
                for d in data:
                    almacenador_arquitectonicas.append(d)
            aux = aux.sig
        for natural in almacenador_naturales:
            if natural in almacenador_arquitectonicas:
                almacenador_paises.append(natural)
        return almacenador_paises


    def encontrar_paises_mas(self, almacenador_n, almacenador_a):
        aux = self.__inicio
        almacenador_naturales = []
        almacenador_arquitectonicas= []
        while(aux is not None):
            if ('Natur' in aux.datos[1]):
                data = aux.datos[0]
                data = data.split(',')
                for d in data:
                    almacenador_naturales.append(d)
            if ('Arqui' in aux.datos[1]):
                data = aux.datos[0]
                data = data.split(',')
                for d in data:
                    almacenador_arquitectonicas.append(d)
            aux = aux.sig
        for pais in almacenador_naturales:
            contador = 0
            for p in almacenador_naturales:
                if (pais in p) or (p in pais):
                    contador += 1
            if (contador >= 2):
                almacenador_n.append(pais)
        for pais in almacenador_arquitectonicas:
            contador = 0
            for p in almacenador_arquitectonicas:
                if (pais in p) or (p in pais):
                    contador += 1
            if (contador >= 2):
                almacenador_a.append(pais)
        
        return almacenador_a, almacenador_n