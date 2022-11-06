from clasesgrafo import Grafo
from random import choice, randint




#Ejercicio 14:
# Implementar sobre un grafo no dirigido los algoritmos necesario para dar solución a las si-
# guientes tareas:

# a. cada vértice representar un ambiente de una casa: cocina, comedor, cochera, quincho,
# baño 1, baño 2, habitación 1, habitación 2, sala de estar, terraza, patio;

# b. cargar al menos tres aristas a cada vértice, y a dos de estas cárguele cinco, el peso de la aris-
# ta es la distancia entre los ambientes, se debe cargar en metros;

# c. obtener el árbol de expansión mínima y determine cuantos metros de cables se necesitan
# para conectar todos los ambientes;

# d. determinar cuál es el camino más corto desde la habitación 1 hasta la sala de estar para
# determinar cuántos metros de cable de red se necesitan para conectar el router con el
# Smart Tv.

casa = Grafo(dirigido=False)

#Punto a:

ambientes = ['cocina', 'comedor', 'cochera', 'quincho', 'baño 1', 'baño 2', 'habitación 1', 'habitación 2', 'sala de estar', 'terraza', 'patio']

for ambiente in ambientes:
    casa.insertar_vertice(ambiente)


#Punto b:

for ambiente in ambientes:
    contador = 0
    while(contador <= 4):
        room = choice(ambientes)
        if(room != ambiente):
            casa.insertar_arista(ambiente, room, randint(1, 99))
            contador += 1

contador = 0
while (contador < 2):
    a = choice(ambientes)
    b = choice(ambientes)
    casa.insertar_arista(a, b, randint(1,99))
    contador += 1

#Punto c:
arbol_minimo = casa.kruskal()
arbol_minimo = arbol_minimo[0].split('-')
print(arbol_minimo)
peso_total = 0
for i in arbol_minimo:
    i = i.split(';')
    peso_total += int(i[2])

print('Los metros de cable necesarios para conectar todos los ambientes son: ' + str(peso_total) + ' metros')
print()

#Punto d:
habitacion_sala = casa.dijkstra('habitación 1')
print(habitacion_sala)
print()
aux, aux_peso = casa.camino_y_peso(habitacion_sala, 'habitacion 1', 'sala de estar')
print('El camino mas corto a la sala de estar es: ' + str(aux['camino']))
print()
print('Los metros de cable de red necesarios son: ' + str(aux_peso) + ' metros')

#Ejercicio 15
# Se requiere implementar un grafo para almacenar las siete maravillas arquitectónicas moder-
# nas y naturales del mundo, para lo cual se deben tener en cuenta las siguientes actividades:

# a. de cada una de las maravillas se conoce su nombre, país de ubicación (puede ser más de
# uno en las naturales) y tipo (natural o arquitectónica);
# b. cada una debe estar relacionada con las otras seis de su tipo, para lo que se debe almacenar
# la distancia que las separa;
# c. hallar el árbol de expansión mínimo de cada tipo de las maravillas;
# d. determinar si existen países que dispongan de maravillas arquitectónicas y naturales;
# e. determinar si algún país tiene más de una maravilla del mismo tipo;
# f. deberá utilizar un grafo no dirigido.

maravillas_varias = [['Piramide de Guiza', 'Egipto', 'Arquitectonica'],
                        ['Jardines colgantes de Babilonia', 'Babilonia', 'Arquitectonica'],
                        ['Templo de Artemisa', 'Grecia', 'Arquitectonica'],
                        ['Estatua de Zeus', 'Olimpia', 'Arquitectonica'],
                        ['Mausoleo de Halicarnaso', 'Turquia', 'Arquitectonica'],
                        ['Coloso de Rodas', 'Rodas', 'Arquitectonica'],
                        ['Faro de Alejandria', 'Alejandria', 'Arquitectonica'],
                        ['Parque Nacional del río subterráneo de Puerto Princesa', 'Filipinas', 'Natural'],
                        ['Montaña de la Mesa', 'Sudáfrica', 'Natural'],
                        ['Cataratas del Iguazú', 'Argentina', 'Natural'],
                        ['Amazonia', 'Bolivia, Brasil, Colombia, Ecuador', 'Natural'],
                        ['Bahía de Ha-Long', 'Vietnam', 'Natural'],
                        ['Isla Jeju', 'Corea del Sur', 'Natural'],
                        ['Parque Nacional de Komodo', 'Indonesia', 'Natural']]

maravillas = Grafo(False)


#Punto a:

for mara in maravillas_varias:
    data = [mara[1], mara[2]]
    maravillas.insertar_vertice(mara[0], datos = data)

#Punto b:

for mara in maravillas_varias:
    for mar in maravillas_varias:
        if (mara[2] == mar[2]):
            maravillas.insertar_arista(mara[0], mar[0], randint(1, 99))

#Punto c:
print()
minimos_naturales = maravillas.kruskal_carac('Natural')
minimos_arquitectonicos = maravillas.kruskal_carac('Arquitectonica')
minimos_naturales = minimos_naturales[0].split('-')
minimos_arquitectonicos = minimos_arquitectonicos[0].split('-')
print('El arbol minimo de las maravillas naturales es: ')
print(minimos_naturales)
print()
print('El arbol minimo de las maravillas arquitectonicas es: ')
print(minimos_arquitectonicos)
print()

#Punto d:
paises_encontrados = []
maravillas.encontrar_paises_dobles(paises_encontrados)
if paises_encontrados:
    print('Los paises que tienen maravillas arquitectonicas y naturales son: ')
    for pais in paises_encontrados:
        print(pais)
else:
    print('No hay paises con maravillas naturales y arquitectonicas')
print()


#Punto e:
paises_naturales = []
paises_arquitectonicos = []
maravillas.encontrar_paises_mas(paises_naturales, paises_arquitectonicos)
if paises_naturales:
    print('Los paises que tienen mas de una maravilla natural son: ')
    for pais in paises_naturales:
        print(pais)
else:
    print('No hay paises con mas de una maravilla natural')

if paises_arquitectonicos:
    print('Los paises que tienen mas de una maravilla arquitectonica son: ')
    for pais in paises_arquitectonicos:
        print(pais)
else:
    print('No hay paises con mas de una maravilla arquitectonica')


