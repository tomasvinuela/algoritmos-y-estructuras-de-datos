from clasesarbol_definitiva import eliminar_nodo, inorden, nodoArbol, insertar_nodo, inorden_villano, inorden_empieza_con, contar_tipo, crear_bosque, contar_elementos, busqueda, contar_dioses, inorden_caracteristica, inorden_categoria, por_nivel, postorden_caracteristica, busqueda_coincidencia, busqueda_proximidad

# 5. Dado un árbol con los nombre de los superhéroes y villanos de la saga Marvel Cinematic Univer-
# se (MCU), desarrollar un algoritmo que contemple lo siguiente:

# a. además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo boo-
# leano que indica si es un héroe o un villano, True y False respectivamente;
# b. listar los villanos ordenados alfabéticamente;
# c. mostrar todos los superhéroes que empiezan con C;
# d. determinar cuántos superhéroes hay el árbol;
# E. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para
# encontrarlo en el árbol y modificar su nombre;
# f. listar los superhéroes ordenados de manera descendente;
# g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a
# los villanos, luego resolver las siguiente tareas:
#   I. determinar cuántos nodos tiene cada árbol;
#   II. realizar un barrido ordenado alfabéticamente de cada árbol.

arbol_MCU = nodoArbol()

#Punto a:
heroes_y_villanos = [
    ['Capitana Marvel', True],
    ['Hulk', True],
    ['Hawkeye', True],
    ['Black Widow', True],
    ['Hela', False],
    ['Thanos', False],
    ['Ultron', False],
    ['Doctor Strange', True]
 ]

for personaje in heroes_y_villanos:
    insertar_nodo(arbol_MCU, personaje[0], personaje[1])

#Punto b:
inorden_villano(arbol_MCU)

#Punto c:
inorden_empieza_con(arbol_MCU, 'C')

#Punto d:
contar_tipo(arbol_MCU, True)

#Punto e:
strange = busqueda_proximidad(arbol_MCU, 'Doc')
eliminar_nodo(arbol_MCU, strange)
strange['info'] = 'Doctor Strange'
insertar_nodo(arbol_MCU, strange)


#Punto f:
postorden_caracteristica(arbol_MCU, True)


#Punto g:
arbol_MCU_heroes = nodoArbol()
arbol_MCU_villanos = nodoArbol()
crear_bosque(arbol_MCU, arbol_MCU_villanos, arbol_MCU_heroes, True)

#I:
cantidad = contar_elementos(arbol_MCU_heroes)
print('El arbol de heroes tiene ' + cantidad + ' elementos.')
cantidad = contar_elementos(arbol_MCU_villanos)
print('El arbol de villanos tiene ' + cantidad + ' elementos.')

#II:
print()
inorden(arbol_MCU_heroes)
print()
inorden(arbol_MCU_villanos)


# 23. Implementar un algoritmo que permita generar un árbol con los datos de la siguiente tabla y
# resuelva las siguientes consultas:
# a. listado inorden de las criaturas y quienes la derrotaron;
# B. se debe permitir cargar una breve descripción sobre cada criatura;
# c. mostrar toda la información de la criatura Talos;
# D. determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas;
# e. listar las criaturas derrotadas por Heracles;
# f. listar las criaturas que no han sido derrotadas;
# g. además cada nodo debe tener un campo “capturada” que almacenará el nombre del héroe
# o dios que la capturo;
# h. modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de
# Erimanto indicando que Heracles las atrapó;
# i. se debe permitir búsquedas por coincidencia;
# j. eliminar al Basilisco y a las Sirenas;
# k. modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles
# derroto a varias;
# l. modifique el nombre de la criatura Ladón por Dragón Ladón;
# m. realizar un listado por nivel del árbol;
# n. muestre las criaturas capturadas por Heracles.
# 

arbol_criaturas = nodoArbol()

tabla_criaturas = [ ['Ceto', '-'],
['Tifón','Zeus'],
['Equidna','Argos Panoptes'],
['Dino','-'],
['Pefredo','-'],
['Enio','-'],
['Escila','-'],
['Caribdis','-'],
['Euríale','-'],
['Esteno','-'],
['Medusa','Perseo'],
['Ladón','Heracles'],
['Águila del Cáucaso','-'],
['Quimera','Belerofonte'],
['Hidra de Lerna','Heracles'],
['León de Nemea','Heracles'],
['Esfinge','Edipo'],
['Dragón de la Cólquida','-'],
['Cerbero','-'],
['Cerda de Cromión','Teseo'],
['Ortro','Heracles'],
['Toro de Creta','Teseo'],
['Jabalí de Calidón','Atalanta'],
['Carcinos','-'],
['Gerión','Heracles'],
['Cloto','-'],
['Láquesis','-'],
['Átropos','-'],
['Minotauro de Creta','Teseo'],
['Harpías','-'],
['Argos Panoptes','Hermes'],
['Aves del Estinfalo','-'],
['Talos','Medea'],
['Sirenas','-'],
['Pitón','Apolo'],
['Cierva de Cerinea','-'],
['Basilisco','-'],
['Jabalí de Erimanto','-']

]

for criatura in tabla_criaturas:
    insertar_nodo(arbol_criaturas, criatura[0], criatura[1])

#Punto a:
inorden(arbol_criaturas)

#Punto b:
#Realizado dentro de clasesarbol (ver nodoArbol)

#Punto c:
talos = busqueda(arbol_criaturas, 'Talos')
print(talos)
print('Nombre de la criatura: ' + talos['info'] + '. Derrotada por: ' + talos['datos'])

#Punto d:
derrotas_dioses = {}
contar_dioses(arbol_criaturas, derrotas_dioses)

primero = [ ' ', 0]
segundo = [ ' ', 0]
tercero = [ ' ', 0]
for dios in derrotas_dioses:
    if derrotas_dioses[dios] > derrotas_dioses[primero[1]]:
        primero[1] = derrotas_dioses[dios]
        primero[0] = dios

for dios in derrotas_dioses:
    if (derrotas_dioses[dios] > segundo[1]) and (derrotas_dioses[dios] < primero[1]):
        segundo[1] = derrotas_dioses[dios]
        segundo[0] = dios

for dios in derrotas_dioses:
    if (derrotas_dioses[dios] > tercero[1]) and (derrotas_dioses[dios] < segundo[1]):
        tercero[1] = derrotas_dioses[dios]
        tercero[0] = dios

print('Los 3 héroes o dioses que derrotaron mayor cantidad de criaturas fueron: ')
print(primero[0] + ', quien derroto a ' + primero[1] + ' criaturas')
print(segundo[0] + ', quien derroto a ' + segundo[1] + ' criaturas')
print(tercero[0] + ', quien derroto a ' + tercero[1] + ' criaturas')

#Punto e:
inorden_caracteristica(arbol_criaturas, 'Heracles')

#Punto f:
inorden_caracteristica(arbol_criaturas, '-')

#Punto g:
#Realizado dentro de clasesarbol (ver nodoArbol)

#Punto h:
capturadas = ['Cerbero', 'Toro de Creta', 'Cierva Cerinea', 'Jabalí de Erimanto']
for captura in capturadas:
    auxilia = busqueda(arbol_criaturas, captura)
    auxilia['capturada'] = 'Heracles'

#Punto i:
#Realizado en clasesarbol (busqueda_coincidencia)

#Punto j:
eliminar_nodo(arbol_criaturas, 'Basilisco')
eliminar_nodo(arbol_criaturas, 'Sirenas')

#Punto k:
auxilia = busqueda(arbol_criaturas, 'Aves del Estínfalo')
auxilia['datos'] = 'Hercules (varias)'


#Punto l:
auxilia = busqueda(arbol_criaturas, 'Ladón')
auxilia['info'] = 'Dragón Ladón'

#Punto m:
por_nivel(arbol_criaturas)

#Punto n:
inorden_categoria(arbol_criaturas, 'capturada', 'Heracles')