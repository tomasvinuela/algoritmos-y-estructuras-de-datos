from clasesgrafo import Grafo
from clasesarbol_definitiva import nodoArbol, insertar_nodo, por_nivel, busqueda, eliminar_nodo, inorden_numeral_mayor, inorden_numeral_menor, identificador_de_nodo
from random import choice, randint, random

# 1 - Desarrollar un algoritmo que permita implementar un árbol como índice para hacer consultas de personajes
# de la saga de Star Wars, de los cuales se sabe su nombre, altura y peso. Además deberá contemplar los
# siguientes requerimientos (debe cargar al menos 20 personajes):
# a. se debe poder cargar un nuevo personaje, modificarlo (cualquiera de sus campos) y darlo de baja;
# b. mostrar toda la información de Yoda, Mandalorian y Luke Skywalker
# c. mostrar un listado ordenado alfabéticamente de los personajes que miden menos de 0.9 metro;
# d. mostrar un listado ordenado alfabéticamente de los personajes que pesan mas de 75 kilos;
# e. mostrar un listado por nivel de los personajes del árbol;
# f. determinar si Grogu esta en el árbol y responder lo siguiente:
#       mostrar toda su información;
#       en que tipo de nodo esta (hoja, intermedio o raíz);
#       que altura tiene el nodo dentro del árbol.

personajes = ['Luke Skywalker', 'Darth Vader', 'Yoda', 'Boba Fett', 'C3PO', 'Leia', 'Rey', 'Kylo Ren', 'Chewbacca', 'Han Solo', 'R2D2', 'Obi-Wan kenobi', 'BB8', 'Quigon jin', 'Quinlan vos', 'Eeth koth', 'Shaak ti', 'Pablo jill', 'Imagun di', 'Ord enisence', 'Mandalorian', 'Grofu']

arbol_star_wars = nodoArbol()

for personaje in personajes:
    data = {'peso' : randint(1,99), 'altura' : (random() * randint(0, 5))}
    insertar_nodo(arbol_star_wars, personaje, data)

#Punto a: cargar un personaje cualquiera, cambiarle algo y eliminarlo.

insertar_nodo(arbol_star_wars, 'Randio', {'peso' : 88, 'altura' : 1.9} )
aux = busqueda(arbol_star_wars, 'Randio')
aux['peso'] = 44
eliminar_nodo(arbol_star_wars,'Randio')


#Punto b: mostrar a Yoda, Mandalorian y Luke Skywalker
print('Mostrar a Yoda, Mandalorian y Luke Skywalker')
mostrar = ['Yoda', 'Mandalorian', 'Luke Skywalker']
for b in mostrar:
    auxilia = busqueda(arbol_star_wars, b)
    if auxilia:
        print(auxilia['info'])
        print(auxilia['datos'])
        print()
    else:
        print(b + ' no se encuentra en el arbol')
        print()
print()

#Punto c: Listar alfabeticamente (inorden) a los personajes menores a 0.9 metros
print('Orden alfabetico de los menores a 0.9 metros: ')
inorden_numeral_menor(arbol_star_wars, 'altura', 0.9)
print()

#Punto d: Listar alfabeticamente (inorden) a los personajes mayor a 75 kilos
print('Orden alfabetico de los que pesan menos de 75 kilos: ')
inorden_numeral_mayor(arbol_star_wars, 'peso', 77)
print()

#Punto e: Listado por nivel.
print('Listado por nivel: ')
por_nivel(arbol_star_wars)
print()

#Punto f: Buscar a Grofu y, si se encuentra, mostrarlo, mostrar su tipo de nodo (Hoja, intermedio, raiz) y mostrar su altura en el arbol (todo se puede deducir a base de la altura)
auxiliar = busqueda(arbol_star_wars, 'Grofu')
tipo_nodo = identificador_de_nodo(arbol_star_wars, 'Grofu')
if auxiliar:
    print('Los datos de Grofu son: ')
    print(auxiliar)
    print('Es un nodo del tipo: ' + tipo_nodo)
    print('Su altura en el arbol es de: ' + str(auxiliar['altura']))
else:
    print('Grofu no se encuentra en el arbol')

print()



# 2 - Dado un grafo no dirigido con personajes de la saga Star Wars, implementar los algoritmos necesarios
# para resolver las siguientes tareas:
# a. cada vértice debe almacenar el nombre de un personaje, las aristas representan la cantidad de episodios
# en los que aparecieron juntos ambos personajes que se relacionan;
# b. hallar el árbol de expansión mínimo desde el vértice que contiene a C-3PO, Yoda y la princesa Leia;
# c. determinar cuales personajes comparten con otro dos episodios o mas (mostrar el par de pesonajes);
# d. cargue al menos los siguientes personajes: Luke Skywalker, Darth Vader, Yoda, Boba Fett, C-3PO, Leia, Rey, Kylo Ren, Chewbacca, Han Solo, R2-D2, Obi-Wan kenobi; BB-8;
# e. determinar que personaje es el que a compartido episodio con la mayor cantidad del resto de los personajes.

grafo_star_wars = Grafo(dirigido = False)

#Punto a y d: Cargar los vertices y aristas y utilizar si o si los personajes indicados en d.
for i in personajes:
    grafo_star_wars.insertar_vertice(i)

for i in personajes:
    for h in personajes:
        if(i != h):
            grafo_star_wars.insertar_arista(i, h, randint(1, 10))

#Punto b: Arbol de expansion minimo a partir C-3PO, Yoda y Leia (dijkstra)
cepo = grafo_star_wars.dijkstra('C3PO')
print(cepo)
print()
yoda = grafo_star_wars.dijkstra('Yoda')
print(yoda)
print()
leia = grafo_star_wars.dijkstra('Leia')
print(leia)
print()


#Punto c: Mostrar los personajes que compartan mas de 2 episodios (sus aristas pesen mas de 2)
ya_mostrados = grafo_star_wars.barrido_parejas_jedi(2)
print()

#Punto e: Determinar el personaje que compartio mayor cantidad de episodios con los demas.
totales = {}
for par in ya_mostrados:
    per_1 = str(par[0])
    per_2 = str(par[1])
    if per_1 in totales:
        totales[per_1] += 1
    else:
        totales[per_1] = 1
    if per_2 in totales:
        totales[per_2] += 1
    else:
        totales[per_2] = 1

for i in totales:
    print(i, totales[i])


mas_compartido = ['', 0]
for total in totales:
    if (totales[total] > mas_compartido[1]):
        mas_compartido[1] = totales[total]
        mas_compartido[0] = total

print('El personaje que mas episodios comparte con los demas es: ' + mas_compartido[0] + ', con un total de: ' + str(mas_compartido[1]))

