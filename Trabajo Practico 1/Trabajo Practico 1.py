from contextlib import nullcontext
from clasespila import Pila

#5. Desarrollar una función que permita convertir un número romano en un número decimal.
def convertidor_romano(romano, decimal, longitud):
    valores_romanos = { 'X' : 10 , 'I' : 1, 'V' : 5, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000 }
    if(longitud == -1):
        return decimal
    else:
        letra = romano[longitud]
        numero = valores_romanos[letra]
        letra_2 = romano[longitud-1]
        numero_anterior = valores_romanos[letra_2]
        if(numero_anterior >= numero or longitud == 0):
            decimal += numero
            return convertidor_romano(romano, decimal, longitud-1)
        else:
            decimal += (numero - numero_anterior)
            return convertidor_romano(romano, decimal, longitud-2)

prueba = "MIX"
resultado_prueba = 0
print(convertidor_romano(prueba, resultado_prueba, len(prueba)-1))




#22. El problema de la mochila Jedi. Suponga que un Jedi (Luke Skywalker, Obi-Wan Kenobi, Rey u
#otro, el que más le guste) está atrapado, pero muy cerca está su mochila que contiene muchos
#objetos. Implementar una función recursiva llamada “usar la fuerza” que le permita al Jedi “con
#ayuda de la fuerza” realizar las siguientes actividades:
#     A). sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no
#queden más objetos en la mochila;
#     B). determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios sacar
#para encontrarlo;
#     C). Utilizar un vector para representar la mochila.


mochila = ['botella', 'comida', 'sable de luz', 'comunicador']
sables = False
pila1 = Pila()
cuenta = 0

for i in range(len(mochila)):
    pila1.apilar(mochila[i])

def usar_la_fuerza(pilas, sable, contador):
    if(pilas.pila_vacia() or sable == True):
        return sable, contador
    else:
        auxiliar = pilas.desapilar()
        if (auxiliar == 'sable de luz'):
            sable = True
            contador += 1
            return usar_la_fuerza(pilas, sable, contador)
        else:
            contador += 1
            return usar_la_fuerza(pilas, sable, contador)

resultado, cuenta = usar_la_fuerza(pila1, sables, cuenta)
if(resultado == True):
    print("Hay un sable de luz. Ademas, los objetos sacados fueron", cuenta)
else:
    print("No hay un sable de luz. Ademas, los objetos sacados fueron", cuenta )




#23. Salida del laberinto. Encontrar un camino que permita salir de un laberinto definido en una
#matriz de [n x n], solo se puede mover de a una casilla a la vez –no se puede mover en diagonal–
#y que la misma sea adyacente y no esté marcada como pared. Se comenzará en la casilla (0, 0)
#y se termina en la (n-1, n-1). Se mueve a la siguiente casilla si es posible, cuando no se pueda
#avanzar hay que retroceder sobre los pasos dados en busca de un camino alternativo.

ariadne = [ 
[1, 1, 1, 1, 1],
[1, 1, 0, 0, 0],
[0, 1, 0, 0, 0],
[1, 1, 1, 1, 1],
[0, 1, 0, 0, 2]
]

def teseo(laberinto, posicionx, posiciony):
    if(laberinto[posicionx][posiciony] == 2):
        laberinto[posicionx][posiciony] = 3
        print("Llego al final del laberinto")
    else:
        if(laberinto[posicionx][posiciony] == 1 and posicionx != len(laberinto)-1 and posiciony != len(laberinto)-1):
            laberinto[posicionx][posiciony] = 3
            teseo(laberinto, posicionx + 1, posiciony)
            teseo(laberinto, posicionx - 1, posiciony)
            teseo(laberinto, posicionx, posiciony + 1)
            teseo(laberinto, posicionx, posiciony - 1)


teseo(ariadne, 0, 0)

