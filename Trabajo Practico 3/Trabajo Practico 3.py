
from clasescola import Cola
from clasespila import Pila
import random

#Ejercicios 16, 18 y 22. El 16 dejarlo para ultimo.

# 16) Utilice cola de prioridad, para atender la cola de impresión tomando en cuenta el siguiente
#criterio (1- empleados, 2- staff de tecnologías de la información “TI”, 3- gerente), y resuelva la
#siguiente situación:
#   a) cargue tres documentos de empleados (cada documento se representa solamente con
#      un nombre).
#   b) imprima el primer documento de la cola (solamente mostrar el nombre de este por pantalla).
#   c) cargue dos documentos del staff de TI.
#   d) cargue un documento del gerente.
#   e) imprima los dos primeros documentos de la cola.
#   f) cargue dos documentos de empleados y uno de gerente.
#   g) imprima todos los documentos de la cola de impresión.

cola_prioridad = Cola()
cuenta = 0
#Punto A:
for i in range(3):
    print('Ingrese el nombre del empleado: ')
    ingresa = input()
    cola_prioridad.arribo(ingresa)
#Punto B:
print(cola_prioridad.frente())
#Punto C:
for i in range(2):
    print('Ingrese el nombre del staff de TI: ')
    ingresa = input()
    cola_prioridad.arribo(ingresa)
#Punto D:
print('Ingrese el nombre del gerente: ')
ingresa = input()
cola_prioridad.arribo(ingresa)
#Punto E:
primero = cola_prioridad.frente()
print(primero)
cola_prioridad.mover_al_final()
print(cola_prioridad.frente())
while(cola_prioridad.frente() != primero):
    cola_prioridad.mover_al_final()
#Punto F:
for i in range(3):
    cola_prioridad.mover_al_final()

for i in range(2):
    print('Ingrese el nombre del empleado: ')
    ingresa = input()
    cola_prioridad.arribo(ingresa)

while(cola_prioridad.frente() != primero):
    cola_prioridad.mover_al_final()

print('Ingrese el nombre del gerente: ')
ingresa = input()
cola_prioridad.arribo(ingresa)

#Punto G:
while(cuenta < cola_prioridad.tamanio()):
    print(cola_prioridad.frente())
    cola_prioridad.mover_al_final()
cola_prioridad.mover_al_final()

    


# 18) Dada una cola con los códigos de turnos de atención (con el formato #@@@, donde # es una
#letra de la A hasta la F y “@@@” son tres dígitos desde el 000 al 999), desarrollar un algoritmo
#que resuelva las siguientes situaciones:
#   a) cargar 1000 turnos de manera aleatoria a la cola.
#   b) separar la cola con datos en dos colas, cola_1 con los turnos que empiezan con la letra A, C
#      y F, y la cola_2 con el resto de los turnos (B, D y E).
#   c) determinar cuál de las colas tiene mayor cantidad de turnos, y de esta cuál de las letras
#      tiene mayor cantidad.
#   d) mostrar los turnos de la cola con menor cantidad de elementos, cuyo número de turno sea
#      mayor que 506.

codigos_original = Cola()
cola_ACF = Cola()
cola_BDE = Cola()
letras1 = {'A', 'C', 'F'}
letras2 = {'B', 'D', 'E'}
cantidades_ACF = {'A' : 0, 'C' : 0, 'F': 0}
cantidades_BDE = {'B' : 0, 'D' : 0, 'E': 0}
contador = 0

#Punto a:

letras = {'A', 'B', 'C', 'D', 'E', 'F'}
numeros = {'0', '1', '2', '3', '4', '5', '7', '8', '9'}
while (contador < 1000):
    dato = random.choice(letras) + random.choice(numeros) + random.choice(numeros) + random.choice(numeros)
    codigos_original.arribo(dato)
    contador += 1 


#Punto b:
contador = 0
while(contador < codigos_original.tamanio()):
    dato = codigos_original.atencion()
    if 'A' in dato :
        cola_ACF.arribo(dato)
        cantidades_ACF['A'] += 1
    if 'C' in dato :
        cola_ACF.arribo(dato)
        cantidades_ACF['C'] += 1
    if 'F' in dato :
        cola_ACF.arribo(dato)
        cantidades_ACF['F'] += 1
    if 'B' in dato :
        cola_BDE.arribo(dato)
        cantidades_BDE['B'] += 1
    if 'D' in dato :
        cola_BDE.arribo(dato)
        cantidades_BDE['D'] += 1
    if 'E' in dato :
        cola_BDE.arribo(dato)
        cantidades_BDE['E'] += 1

    contador += 1

#Punto c y d:
mayor = 0
contador = 0

if (cola_ACF.tamanio() > cola_BDE.tamanio):
    print('La cola de mayor tamaño es la que contiene los turnos de inicial A, C y F')
    for letra in letras1:
        if(cantidades_ACF[letra] > mayor):
            mayor = cantidades_ACF
            mayorletra = letra
    print('Dentro de esta cola, la letra con mayor de turnos fue la ' + mayorletra + ' la cual contenia ' + mayor + ' turnos')

    while(contador < cola_BDE.tamanio()):
        elemento = cola_BDE.frente()
        elemento_2 = elemento[1:]
        int(elemento_2)
        if (elemento_2 > 506):
            print(elemento)
        contador +=0
        cola_BDE.mover_al_final()
    cola_BDE.mover_al_final()

else:
    print('La cola de mayor tamaño es la que contiene los turnos de inicial B, D y E')
    for letra in letras2:
        if(cantidades_BDE[letra] > mayor):
            mayor = cantidades_BDE
            mayorletra = letra
    print('Dentro de esta cola, la letra con mayor de turnos fue la ' + mayorletra + ' la cual contenia ' + mayor + ' turnos')

    while(contador < cola_ACF.tamanio()):
        elemento = cola_ACF.frente()
        elemento_2 = elemento[1:]
        int(elemento_2)
        if (elemento_2 > 506):
            print(elemento)
        contador +=0
        cola_ACF.mover_al_final()
    cola_ACF.mover_al_final()


    

# 22) Se tienen una cola con personajes de Marvel Cinematic Universe (MCU), de los cuales se conoce
#el nombre del personaje, el nombre del superhéroe y su género (Masculino M y Femenino F) por 
#ejemplo {Tony Stark, Iron Man, M}, {Steve Rogers, Capitán América, M}, {Natasha Romanoff,
#Black Widow, F}, etc., desarrollar un algoritmo que resuelva las siguientes actividades:
#   a. determinar el nombre del personaje de la superhéroe Capitana Marvel;
#   b. mostrar los nombre de los superhéroes femeninos;
#   c. mostrar los nombres de los personajes masculinos;
#   d. determinar el nombre del superhéroe del personaje Scott Lang;
#   e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan
#      con la letra S;
#   f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre
#      de superhéroes.

cola_mcu = Cola()
nombres_femeninos = Cola()
nombres_masculinos = Cola()
datos_s = Cola()
contador = 0

while(contador < cola_mcu.tamanio()):
    dato = cola_mcu.frente()
    if(dato[1] == 'Capitana Marvel'):
        nombre_capitana = dato[0]
    if(dato[2] == 'F'):
        nombres_femeninos.arribo(dato[1])
    if(dato[2] == 'M'):
        nombres_masculinos.arribo(dato[0])
    if(dato[0] == 'Scott Lang'):
        nombre_scott = dato[1]

    if(dato[0][0] == 'S' or dato[1][0] == 'S'):
        datos_s.arribo(dato)
    
    if(dato[0] == 'Carol Danvers'):
        nombre_carol = dato[1]

    cola_mcu.mover_al_final()
    contador += 1
cola_mcu.mover_al_final()


#Punto a:
print('El nombre de superheroe de la Capitana Marvel es: ' + nombre_capitana)

#Punto B y C:
contador = 0
print('Los nombres de los superheroes femeninos son: ')
while(contador < nombres_femeninos.tamanio()):
    print(nombres_femeninos.frente())
    nombres_femeninos.mover_al_final
    contador +=1
contador = 0
print('Los nombres de los personajes masculinos son: ')
while(contador < nombres_masculinos.tamanio()):
    print(nombres_masculinos.frente())
    nombres_masculinos.mover_al_final
    contador +=1

#Punto D:
print('El nombre de superheroe de Scott Lang es: ' + nombre_scott)

#Punto E:
contador = 0
print('Los datos de los personajes o superheroes cuyos nombres empiezan con S son: ')
while(contador < datos_s.tamanio()):
    print(datos_s.frente())
    datos_s.mover_al_final
    contador +=1

#Punto F:
if nombre_carol:
    print('El nombre de superheroe de Carol Danvers es: ' + nombre_carol)
else:
    print('Carol Danvers no se encuentra en la cola')


