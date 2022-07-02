from claseslista2 import Lista
from random import randint, choice

#Ejercicios a entregar de la guía de lista del libro: 15, 21 y 22.


#Ejercicio 15
# Se cuenta con una lista de entrenadores Pokémon. De cada uno de estos se conoce: nombre, cantidad
# de torneos ganados, cantidad de batallas perdidas y cantidad de batallas ganadas. Y además
# la lista de sus Pokémons, de los cuales se sabe: nombre, nivel, tipo y subtipo. Se pide resolver
# las siguientes actividades utilizando lista de lista implementando las funciones necesarias:
# a. obtener la cantidad de Pokémons de un determinado entrenador;
# b. listar los entrenadores que hayan ganado más de tres torneos;
# c. el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados;
# d. mostrar todos los datos de un entrenador y sus Pokémos;
# e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %;
# f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador
# (tipo y subtipo);
# g. el promedio de nivel de los Pokémons de un determinado entrenador;
# h. determinar cuántos entrenadores tienen a un determinado Pokémon;
# i. mostrar los entrenadores que tienen Pokémons repetidos;
# j. determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Terrakion
# o Wingull;
# k. determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador
# como del Pokémon deben ser ingresados;


class Entrenador:
    def __init__(self, nombre, torneos, ganadas, perdidas):
        self.nombre = nombre
        self.t_ganados = torneos
        self.b_ganadas = ganadas
        self.b_perdidas = perdidas

class Pokemon:
    def __init__(self, nombre, nivel, tipo, subtipo):
        self.nombre = nombre
        self.nivel = nivel
        self.tipo = tipo
        self.subtipo = subtipo

lista_entrenadores = Lista()

entrenadores = [ {'nombre' : 'uno', 'torneos' : 15, 'ganadas' : 5, 'perdidas' : 2}]

for entrenador in entrenadores:
    lista_entrenadores.insertar(Entrenador(entrenador['nombre'], entrenador['torneos'], entrenador['ganadas'], entrenador['perdidas']), 'nombre')

pokemons = [{'nombre' : 'Victini', 'nivel' : 25, 'tipo' : 'fuego', 'subtipo' : 'psiquico'}]

for entrenador in entrenadores:
    for i in range(randint(1,6)):
        pokemon = choice(pokemons)
        pos = lista_entrenadores.busqueda(entrenador['nombre'], 'nombre')
        if pos:
            pos.sublista.insertar(Pokemon(pokemon['nombre'], pokemon['nivel'], pokemon['tipo'], pokemon['subtipo']), 'nombre')

#Punto a:
print('Ingrese el nombre del entrenador cuya cantidad de pokemon desea saber')
a_nombre = input()
pos = lista_entrenadores.busqueda(a_nombre, 'nombre')
if pos:
    a_cantidad = pos.sublista.tamanio()
    print('La cantidad de pokemon del entrenador es:' + a_cantidad)
else:
    print('El entrenador no se encuentra en la lista')

#Punto b:
lista_entrenadores.barrido_torneos_ganadas()

#Punto c:
mayor = lista_entrenadores.mayor_de_lista('torneos')
print('El entrenador con mayor cantidad de torneos ganados es: ' + mayor)
pokemon_mayor = mayor.sublista.mayor_de_lista('nivel')
print('Su pokemon de mayor nivel es: ' + pokemon_mayor)

#Punto d: 
print('Ingrese el entrenador cuyos datos y pokemon desea conocer')
d_entrenador = input()
d_buscado = lista_entrenadores.busqueda(d_entrenador, 'nombre')
if d_buscado:
    print('Los datos del entrenador son: ' + d_buscado.info)
    print('Los datos de sus pokemons son los siguientes: ' + d_buscado.sublista.barrido())

#Punto e:
lista_entrenadores.barrido_pocentaje_79()

#Punto f:
lista_entrenadores.barrido_tipo_subtipo()

#Punto g:
print('Ingrese el nombre del entrenador cuyo nivel de pokemon promedio desea saber')
g_nombre = input()
pos = lista_entrenadores.busqueda(g_nombre, 'nombre')
if pos:
    g_cantidad = pos.sublista.nivel_promedio()
    print('El nivel promedio de los pokemon del entrenador es:' + g_cantidad)
else:
    print('El entrenador no se encuentra en la lista')

#Punto h:
print('Ingrese el nombre del pokemon cuya cantidad de entrenadores desea conocer')
h_pokemon = input()
h_canti = lista_entrenadores.contador_de_entrenadores(h_pokemon)
if h_canti:
    print('La cantidad de entrenadores que tienen este pokemon es:' + h_canti)
else:
    print('El entrenador no se encuentra en la lista')

#Punto i:
lista_entrenadores.pokemon_repetido()

#Punto j:
nombres = ['Tyrantrum', 'Terrakion', 'Wingull']
for nombre in nombres:
    lista_entrenadores.barriduo_segun_nombres(nombre)

#Punto k:
print('Ingrese el nombre del entrenador')
k_entrenador = input()
print('Ingrese el nombre del pokemon')
k_pokemon = input()
k_pos = lista_entrenadores.busqueda(k_entrenador, 'nombre')
if k_pos:
    k_encuentra = k_pos.sublista.busqueda(k_pokemon, 'nombre')
    if k_encuentra:
        print('El entrenador posee el pokemon ingresado')
    else:
        print('El entrenador no posee el pokemon ingresado')
else:
    print('El entrenador no se encuentra en la lista')




#Ejercicio 21
# Se cuenta con una lista de películas de cada una de estas se dispone de los siguientes datos:
# nombre, valoración del público –es un valor comprendido entre 0-10–, año de estreno y recaudación.
# Desarrolle los algoritmos necesarios para realizar las siguientes tareas:
# a. permitir filtrar las películas por año –es decir mostrar todas las películas de un determinado
# año
# b. mostrar los datos de la película que más recaudo;
# c. indicar las películas con mayor valoración del público, puede ser más de una;
# d. mostrar el contenido de la lista en los siguientes criterios de orden –solo podrá utilizar una
# lista auxiliar–:
# I. por nombre,
# II. por recaudación,
# III. por año de estreno,
# IV. por valoración del público.

class Pelicula:
    def __init__(self, nombre, valoracion, anio, recaudacion):
        self.nombre = nombre
        self.valoracion = valoracion
        self.anio = anio
        self.recaudacion = recaudacion

pelis = [ {'nombre' : 'uno', 'valoracion' : 9, 'anio' : 1988, 'recaudacion' : 300000}]
lista_peliculas= Lista()
for peli in pelis:
    lista_peliculas.insertar(Pelicula(peli['nombre'], peli['valoracion'], peli['anio'], peli['recaudacion']), 'nombre')


#Punto a:
print('Ingrese el año cuyas peliculas desea conocer')
a_anio = input()
lista_peliculas.barrido_por_anio(a_anio)

#Punto b:
print('La pelicula que mas recaudacion tubo es: ' + lista_peliculas.mayor_de_lista('recaudacion'))

#Punto c:
mayor_valoracion = lista_peliculas.mayor_de_lista('valoracion')
lista_peliculas.barriduo_segun_resenia(mayor_valoracion.valoracion())

#Punto d:
lista_auxiliar = Lista()

def agregar_elementos(d_lista, d_lista_agregar, d_campo):
    for i in range(d_lista.tamanio()):
        aux = d_lista_agregar.obtener_elemento(i)
        d_lista_agregar.insertar(aux, d_campo)

def eliminar_elementos(d_lista_eliminar, d_campo):
    for i in range(d_lista_eliminar.tamanio()):
        aux = d_lista_eliminar.obtener_elemento(i)
        d_lista_eliminar.eliminar(aux, d_campo)

criterios = ['nombre', 'recaudacion', 'anio', 'valoracion']

for crit in criterios:
    agregar_elementos(lista_peliculas, lista_auxiliar, crit)
    lista_auxiliar.barrido()
    eliminar_elementos(lista_auxiliar, crit)


#Ejercicio 22
# Se dispone de una lista de todos los Jedi, de cada uno de estos se conoce su nombre, maestros,
# colores de sable de luz usados y especie. implementar las funciones necesarias para resolver las
# actividades enumeradas a continuación:
# a. listado ordenado por nombre y por especie;
# b. mostrar toda la información de Ahsoka Tano y Kit Fisto;
# c. mostrar todos los padawan de Yoda y Luke Skywalker, es decir sus aprendices;
# d. mostrar los Jedi de especie humana y twi'lek;
# e. listar todos los Jedi que comienzan con A;
# f. mostrar los Jedi que usaron sable de luz de más de un color;
# g. indicar los Jedi que utilizaron sable de luz amarillo o violeta;
# h. indicar los nombre de los padawans de Qui-Gon Jin y Mace Windu, si los tuvieron.

class Jedi:
    def __init__(self, nombre, especie, maestro, sable):
        self.nombre = nombre
        self.especie = especie
        self.maestro = maestro
        self.sable = sable

    def __str__(self):
        return f"{self.nombre} | {self.especie} | {self.maestro} | { self.sable}"

file = open('jedi.txt')
lineas = file.readlines()        
lineas.pop(0)                     
for linea in lineas:
    datos = linea.split(';')
    datos.pop(-1)                 
    print(datos)

lista_jedi = Lista()
lista_jedi.insertar(Jedi(datos[0], 
                        datos[2], 
                        datos[3], 
                        datos[4].split('/')),
                        campo = 'nombre')

#Punto A:
lista_jedi_especies = Lista()
lista_jedi_especies.insertar(Jedi(datos[0], 
                                 datos[2], 
                                 datos[3], 
                                 datos[4].split('/')),
                                 campo = 'especie')

lista_jedi.barrido()
lista_jedi_especies.barrido()

#Punto B:
ahsoka = lista_jedi.busqueda('Ahsoka Tano', 'nombre')
kit = lista_jedi.busqueda('Kit Fisto', 'nombre')

if ahsoka:
    print(f'Los datos de {ahsoka.info.nombre} son {ahsoka.info}')
else:
    print('El jedi no estaba en la lista')

if kit:
    print(f'Los datos de {kit.info.nombre} son {kit.info}')
else:
    print('El jedi no estaba en la lista')

#Punto C:
print()
lista_jedi.barrido_YODA_LUKE()
print()
#Punto D:
lista_jedi.barrido_por_especie()
print()
#Punto E: 
lista_jedi.barrido_comienza_con('A')
print()
#Punto F:
lista_jedi.barrido_mas_de_uno()
print()
#Punto G:
lista_jedi.barrido_violeta_amarillo()
print()
#Punto H:
lista_jedi.barrido_padawans()
print()

