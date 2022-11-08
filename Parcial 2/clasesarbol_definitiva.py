from clasescola import Cola


def nodoArbol():
    nodo = {
        'info': None,
        'datos': None,
        'der': None,
        'izq': None,
        'altura': 0,
        'descripcion': None,
        'capturada' : None
    }
    return nodo


def copiar_nodo(nodo_datos, nodo_copia):
    if nodo_datos:
        nodo_copia['info'] = nodo_datos['info']
        nodo_copia['der'] = nodo_datos['der']
        nodo_copia['izq'] = nodo_datos['izq']
        if 'datos' in nodo_copia:
            nodo_copia['datos'] = nodo_datos['datos']


def insertar_nodo(arbol, dato, datos=None):
    if arbol['info'] is None:
        arbol['info'] = dato
        arbol['datos'] = datos
    elif dato < arbol['info']:
        if arbol['izq'] is None:
            arbol['izq'] = nodoArbol()
        insertar_nodo(arbol['izq'], dato, datos)
    else:
        if arbol['der'] is None:
            arbol['der'] = nodoArbol()
        insertar_nodo(arbol['der'], dato, datos)
    balancear(arbol)
    actualizar_altura(arbol)


def altura(arbol):
    if arbol is None:
        return -1
    else:
        return arbol['altura']


def actualizar_altura(arbol):
    if arbol is not None:
        alt_izq = altura(arbol['izq'])
        alt_der = altura(arbol['der'])
        arbol['altura'] = (alt_izq if alt_izq > alt_der else alt_der) + 1


def rotar_simple(arbol, control):
    aux = nodoArbol()
    if control:
        copiar_nodo(arbol['izq'], aux)
        arbol['izq'] = None
        if(aux['der'] and not arbol['izq']):
            arbol['izq'] = nodoArbol()
        copiar_nodo(aux['der'], arbol['izq'])
        aux['der'] = nodoArbol()
        copiar_nodo(arbol, aux['der'])
    else:
        copiar_nodo(arbol['der'], aux)
        arbol['der'] = None
        if(aux['izq'] and not arbol['der']):
            arbol['der'] = nodoArbol()
        copiar_nodo(aux['izq'], arbol['der'])
        aux['izq'] = nodoArbol()
        copiar_nodo(arbol, aux['izq'])
    arbol.update(aux)
    actualizar_altura(aux['izq'])
    actualizar_altura(aux['der'])
    actualizar_altura(aux)


def rotar_doble(arbol, control):
    if control:
        rotar_simple(arbol['izq'], False)
        rotar_simple(arbol, True)
    else:
        rotar_simple(arbol['der'], True)
        rotar_simple(arbol, False)


def balancear(arbol):
    if arbol is not None:
        if altura(arbol['izq']) - altura(arbol['der']) == 2:
            if(altura(arbol['izq']['izq']) >= altura(arbol['izq']['der'])):
                rotar_simple(arbol, True)
            else:
                rotar_doble(arbol, True)
        elif altura(arbol['der']) - altura(arbol['izq']) == 2:
            if(altura(arbol['der']['der']) >= altura(arbol['der']['izq'])):
                rotar_simple(arbol, False)
            else:
                rotar_doble(arbol, False)


def arbol_vacio(arbol):
    return arbol['info'] is None


def preorden(arbol):
    if(arbol is not None):
        print(arbol['info'], arbol['altura'],
              arbol['izq']['info'] if arbol['izq'] else None,
              arbol['der']['info'] if arbol['der'] else None)
        preorden(arbol['izq'])
        preorden(arbol['der'])


def contar_caracteristica(arbol, categoria, caracteristica):
    contador = 0
    if(arbol is not None):
        if arbol['datos'][categoria] == caracteristica:
            contador += 1
        contador += contar_caracteristica(arbol['izq'])
        contador += contar_caracteristica(arbol['der'])
    return contador

def contar_tipo(arbol, caracteristica):
    contador = 0
    if(arbol is not None):
        if arbol['datos'] == caracteristica:
            contador += 1
        contador += contar_caracteristica(arbol['izq'])
        contador += contar_caracteristica(arbol['der'])
    return contador

def contar_dioses(arbol, diccionario_dioses):
    contador = 0
    if (arbol is not None):
        if(arbol['datos'] is not None) and (arbol['datos'] is not '-'):
            diccionario_dioses[arbol['datos']] += 1

def contar_elementos(arbol):
    contador = 0
    if(arbol is not None):
        contador += 1
        contador += contar_caracteristica(arbol['izq'])
        contador += contar_caracteristica(arbol['der'])
    return contador


def inorden(arbol):
    if(arbol is not None):
        inorden(arbol['izq'])
        print(arbol['info'])
        inorden(arbol['der'])


def contar_nodos(arbol):
    if (arbol is not None):
        if arbol['der']:
            contador = (contador + 1)
            contar_nodos(arbol['der'])
        if arbol['izq']:
            contador = (contador + 1)
            contar_nodos(arbol['izq'])
    return contador

def contar_hojas(arbol):
    if (arbol is not None):
        if(arbol['altura'] == 0):
            contador = (contador + 1)
        else:
            contar_hojas(arbol['der'])
            contar_hojas(arbol['izq'])
    return contador

def identificador_de_nodo(arbol, nodo):
    if (arbol is not None):
        nodo_buscado = busqueda(arbol, nodo)
        if nodo_buscado:
            if(altura(arbol) == nodo_buscado['altura']):
                resultado = 'Raiz'
            if(nodo_buscado['altura'] == 0):
                resultado = 'Hoja'
                if (altura(arbol) == 0):
                    resultado = 'Hoja y Raiz'
            else:
                resultado = 'Intermedio'
            return resultado


def informacion_hojas(arbol):
    if (arbol is not None):
        if(arbol['altura'] == 0):
            print(arbol)
        else:
            informacion_hojas(arbol['der'])
            informacion_hojas(arbol['izq'])


def contar_nodos_siguientes(arbol):
    if (arbol is not None):
        nodos = contar_nodos(arbol)
        print('La cantidad de nodos del arbol ' + arbol['info']+ ' es de ' + nodos)
        contar_nodos_siguientes(arbol['der'])
        contar_nodos_siguientes(arbol['izq'])


def lista_de_arbol(arbol, diccionario):
    if (arbol is not None):
        numero = contar_nodos(arbol)
        diccionario[arbol['info']] = numero
        lista_de_arbol(arbol['der'], diccionario)
        lista_de_arbol(arbol['izq'], diccionario)

def arbol_completo(arbol):
    if (arbol is not None):
        if arbol['der'] and arbol['izq']:
            print('El arbol ' + arbol['info'] + ' esta completo')
        else:
            print('El arbol ' + arbol['info'] + ' no esta completo')
        arbol_completo(arbol['der'])
        arbol_completo(arbol['izq'])


def inorden_villano(arbol):
    if(arbol is not None):
        inorden_villano(arbol['izq'])
        if arbol['datos'] == False:
            print(arbol['info'])
        inorden_villano(arbol['der'])

def inorden_caracteristica(arbol, caracteristica):
    if(arbol is not None):
        inorden_caracteristica(arbol['izq'])
        if caracteristica in arbol['datos']:
            print(arbol['info'])
        inorden_caracteristica(arbol['der'])

def inorden_categoria(arbol, categoria, caracteristica):
    if(arbol is not None):
        inorden_categoria(arbol['izq'])
        if caracteristica in arbol[categoria]:
            print(arbol['info'])
        inorden_categoria(arbol['der'])

def inorden_numeral_menor(arbol, categoria, numero):
    if(arbol is not None):
        inorden_numeral_menor(arbol['izq'], categoria, numero)
        if (arbol['datos'][categoria] < numero):
            print(arbol['info'])
        inorden_numeral_menor(arbol['der'], categoria, numero)

def inorden_numeral_mayor(arbol, categoria, numero):
    if(arbol is not None):
        inorden_numeral_mayor(arbol['izq'], categoria, numero)
        if (arbol['datos'][categoria] > numero):
            print(arbol['info'])
        inorden_numeral_mayor(arbol['der'], categoria, numero)


def inorden_empieza_con(arbol, valor):
    if(arbol is not None):
        inorden_empieza_con(arbol['izq'], valor)
        if arbol['info'].startswith(valor):
            print(arbol['info'])
        inorden_empieza_con(arbol['der'], valor)


def postorden(arbol):
    if(arbol is not None):
        postorden(arbol['der'])
        print(arbol['info'])
        postorden(arbol['izq'])

def postorden_caracteristica(arbol, caracteristica):
    if(arbol is not None) and (caracteristica in arbol['datos']):
        postorden(arbol['der'])
        print(arbol['info'])
        postorden(arbol['izq'])




def busqueda(arbol, clave):
    aux = None
    if arbol is not None and arbol['info'] is not None:
        if arbol['info'] == clave:
            aux = arbol
        elif clave < arbol['info']:
            aux = busqueda(arbol['izq'], clave)
        else:
            aux = busqueda(arbol['der'], clave)
    return aux

def busqueda_padre(arbol, clave):
    aux = None
    padre = None
    if arbol is not None and arbol['info'] is not None:
        if arbol['info'] == clave:
            aux = arbol
        elif clave < arbol['info']:
            aux = busqueda_padre(arbol['izq'], clave)
        else:
            aux = busqueda_padre(arbol['der'], clave)
    return aux



def busqueda_coincidencia(arbol, clave):
    aux = None
    print('Las coincidencias encontradas fueron: ')
    if arbol is not None and arbol['info'] is not None:
        if clave in arbol['info']:
            print(arbol)
        elif clave < arbol['info']:
            busqueda(arbol['izq'], clave)
        else:
            busqueda(arbol['der'], clave)
    return aux



def busqueda_proximidad(arbol, clave):
    aux = None
    if arbol is not None and arbol['info'] is not None:
        if arbol['info'].startswith(clave):
            aux = arbol
        elif clave < arbol['info']:
            aux = busqueda(arbol['izq'], clave)
        else:
            aux = busqueda(arbol['der'], clave)
    return aux


def reemplazar(arbol, anterior=None, primero=None):
    info, datos = None, None
    if arbol['der'] is None:
        info, datos = arbol['info'], arbol['datos']
        if anterior:
            anterior['der'] = arbol['izq']
        else:
            primero['izq'] = arbol['izq']
    else:
        info, datos = reemplazar(arbol['der'], anterior=arbol)
    return info, datos


def eliminar_nodo(arbol, clave, previo=None, hijo=None):
    x, datos = None, None
    if arbol['info'] is not None:
        if arbol['izq'] and clave < arbol['info']:
            x, datos = eliminar_nodo(arbol['izq'], clave, arbol, 'izq')
        elif arbol['der'] and clave > arbol['info']:
            x, datos = eliminar_nodo(arbol['der'], clave, arbol, 'der')
        elif arbol['info'] == clave:
            x = arbol['info']
            datos = arbol['datos']
            if arbol['izq'] is None and arbol['der'] is not None:
                copiar_nodo(arbol['der'], arbol)
            elif arbol['der'] is None and arbol['izq'] is not None:
                copiar_nodo(arbol['izq'], arbol)
            elif arbol['izq'] is None and arbol['der'] is None:
                if previo is None:
                    arbol['info'] = None
                    arbol['datos'] = None
                else:
                    previo[hijo] = None
            else:
                info, datos = reemplazar(arbol['izq'], primero=arbol)
                arbol['info'] = info
                arbol['datos'] = datos
        actualizar_altura(arbol)
        balancear(arbol)

    return x, datos



def por_nivel(arbol):
    pendientes = Cola()
    pendientes.arribo(arbol)
    while not pendientes.cola_vacia():
        nodo = pendientes.atencion()
        print(nodo['info'], nodo['izq']['info'] if nodo['izq'] else None, nodo['der']['info'] if nodo['der'] else None)
        if nodo['izq']:
            pendientes.arribo(nodo['izq'])
        if nodo['der']:
            pendientes.arribo(nodo['der'])


def crear_bosque_categ(arbol, bosque1, bosque2, categ, valor_categ):
    if(arbol is not None):
        crear_bosque_categ(arbol['izq'], bosque1, bosque2, categ, valor_categ)
        if arbol['datos'][categ] == valor_categ:
            insertar_nodo(bosque2, arbol['info'])
        else:
            insertar_nodo(bosque1, arbol['info'])
        crear_bosque_categ(arbol['der'], bosque1, bosque2, categ, valor_categ)

def crear_bosque(arbol, bosque1, bosque2, valor_categ):
    if(arbol is not None):
        crear_bosque(arbol['izq'], bosque1, bosque2, valor_categ)
        if arbol['datos'] == valor_categ:
            insertar_nodo(bosque2, arbol['info'])
        else:
            insertar_nodo(bosque1, arbol['info'])
        crear_bosque(arbol['der'], bosque1, bosque2, valor_categ)

def crear_bosque_comienzo(arbol, bosque, cantidad_niveles):
    cantidad_niveles = (cantidad_niveles - 1)
    if(arbol is not None) and (cantidad_niveles != -1):
        insertar_nodo(bosque, arbol['info'])
        crear_bosque_comienzo(arbol['izq'], bosque, cantidad_niveles)
        crear_bosque_comienzo(arbol['der'], bosque, cantidad_niveles)