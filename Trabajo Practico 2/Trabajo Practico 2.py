
from clasespila import Pila

#Ejercicios 19 y 24

# 19) Dada una pila de películas de las que se conoce su título, estudio cinematográfico y año de es-
#treno, desarrollar las funciones necesarias para resolver las siguientes actividades:
#   a) mostrar los nombre películas estrenadas en el año 2014.
#   b) indicar cuántas películas se estrenaron en el año 2018.
#   c) mostrar las películas de Marvel Studios estrenadas en el año 2016.
#NOTA: se asume que los elementos de la pila son vectores, cada uno con el titulo, estudio y año de la pelicula en ese orden
peliculas = Pila()
nombres_a = Pila()
cantidad_b = 0
titulos_c = Pila()

while(not peliculas.pila_vacia()):
    vector_auxiliar = peliculas.desapilar()
    if(vector_auxiliar[2] == 2014):
        nombres_a.apilar(vector_auxiliar[0])
    if(vector_auxiliar[2] == 2018):
        cantidad_b += 1
    if(vector_auxiliar[1] == 'Marvel Studios' and vector_auxiliar[2] == 2016):
        titulos_c.apilar(vector_auxiliar[0])

print("Las peliculas estrenadas en 2014 fueron:")
while(not nombres_a.pila_vacia()):
    print(nombres_a.desapilar() + "\n")

print("La cantidad de peliculas estrenadas en 2018 fue de: " + cantidad_b)

print("Las peliculas de Marvel Studios estrenadas en 2016 fueron:")
while(not titulos_c.pila_vacia()):
    print(titulos_c.desapilar() + "\n")

# 24) Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone de
#su nombre y la cantidad de películas de la saga en la que participó, implementar las funciones
#necesarias para resolver las siguientes actividades:
#   a) determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posi-
#      ción uno la cima de la pila;
#   b) determinar los personajes que participaron en más de 5 películas de la saga, además indi-
#      car la cantidad de películas en la que aparece;
#   c) determinar en cuantas películas participo la Viuda Negra (Black Widow);
#   d) mostrar todos los personajes cuyos nombre empiezan con C, D y G.
#NOTA: Se asume que la pila esta formada por vectores, cada uno con el nombre y cantidad de peliculas del superheroe en ese orden

personajes = Pila()
rocket_a = 0
groot_a = 0
mas_de_5_b = Pila()
blackwidow_c = 0
nombres_C_d = Pila()
nombres_D_d = Pila()
nombres_G_d = Pila()

def rocket_groot_a (personaje, rocket, groot, verificador1, verificador2):
    if(not personaje[0] == 'Rocket Raccoon' and verificador1 == False):
        rocket += 1
    else:
        rocket += 1
        verificador1 = True
    if(not personaje[0] == 'Groot' and verificador2 == False):
        groot += 1
    else:
        groot += 1
        verificador2 = True
    
def mas5_b (personaje, auxiliar_b):
    if(personaje[1] > 5):
        auxiliar_b.apilar(personaje)

def viudanegra_c (personaje, contador):
    if(personaje[0] == 'Black Widow'):
        contador += 1

def nombresCDG_d (personaje, nombres_C, nombres_D, nombres_G):
    if(personaje[0][0] == 'C'):
        nombres_C.apilar(personaje[0])
    if(personaje[0][0] == 'D'):
        nombres_D.apilar(personaje[0])
    if(personaje[0][0] == 'G'):
        nombres_G.apilar(personaje[0])

while(not personajes.pila_vacia()):
    auxiliar_personaje = personajes.desapilar()
    rocket_groot_a(auxiliar_personaje, rocket_a, groot_a, False, False)
    mas5_b(auxiliar_personaje, mas_de_5_b)
    viudanegra_c(auxiliar_personaje, blackwidow_c)
    nombresCDG_d(auxiliar_personaje, nombres_C_d, nombres_D_d, nombres_G_d)

print("Consigna a) Rocket esta en la posicion " + rocket_a + " y Groot esta en la posicion " + groot_a)

print("Consigna b) Los personajes y sus apariciones fueron:")
while(not mas_de_5_b.pila_vacia()):
    print(mas_de_5_b.desapilar() + '\n')

print("Consigna c) La Viuda Negra aparecio en " + blackwidow_c + " peliculas")

print("Consigna d) Los personajes cuyos nombres empiezan con C son:")
while(not nombres_C_d.pila_vacia()):
    print(nombres_C_d.desapilar() + '\n')
print("Los personajes cuyos nombres empiezan con D son:")
while(not nombres_D_d.pila_vacia()):
    print(nombres_D_d.desapilar() + '\n')
print("Los personajes cuyos nombres empiezan con G son:")
while(not nombres_G_d.pila_vacia()):
    print(nombres_G_d.desapilar() + '\n')
