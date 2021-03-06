
#Informacion adicional:
# module_name: jurassic_park.py
# Puedes hacer lo siguiente:
# from jurassic_park import dinosaurs
# Devuelve una lista de diccionarios con información de todos los dinosaurios del parque con el
# siguiente formato: {'name': ..., 'type': ..., 'number': ..., 'period': ..., 'named_by': ...}
# Esta información te puede servir de ayuda para complementar los datos del archivo.

# El archivo alerts.txt tiene la siguiente info (time, zone_code, dino_number, alert_level) por
# columnas separados por ‘;’.

from datetime import date
from jurassic_park import dinosaurs
from claseslistaparcial import Lista
from clasescola import Cola
from random import randint, choice


class Alerta:
    def __init__(self, hora, zona, dinonumber, nivel, name):
        self.hora = hora
        self.zona = zona
        self.dinonumber = dinonumber
        self.nivel = nivel
        self.name = name

    def __str__(self):
        return f"{self.hora} | {self.zona} | {self.dinonumber} | { self.nivel} | { self.name}"


class Dinosaurio:
    def __init__(self, name, type, number, period, named_by, date):
        self.name = name
        self.type = type
        self.number = number
        self.period = period
        self.named_by = named_by
        self.date = date
    
    
    def __str__(self):
        return f"{self.name} | {self.type} | {self.number} | { self.period} | { self.named_by} | { self.date}"


#Consigna 1: Organizar el archivo, mostrar los datos y encontrar cual dinosaurio fue el ultimo en ser descubierto y por quien

listadinos = Lista()
for dino in dinosaurs:
    auxiliar = dino['named_by'].split(',')
    listadinos.insertar(Dinosaurio(dino['name'], dino['type'], dino['number'], dino['period'], auxiliar[0], auxiliar[1]), 'number')

dinomayor = listadinos.mayor_de_lista('date')
print('El ultimo dinosaurio en ser descubierto fue: ' + dinomayor.name)
print('Este fue descubierto por: ' + dinomayor.named_by)
print()


#Consigna 2: Procesar el archivo .txt, organizarlo en 2 estructuras 1 por fecha y 1 por nombre,
#Agregar el nombre de los dinosaurios de acuerdo a su numero

file = open('alerts.txt')
lineas = file.readlines()           
lista_alerta_fecha = Lista()
lista_alerta_nombre = Lista()
lineas.pop(0)  


for linea in lineas:
    datos = linea.split(';')        
    
    for dino in dinosaurs:
        if(dino['number'] == int(datos[2])):
            nombree = dino['name']

    datos[3] = datos[3].split('\n')[0]

    lista_alerta_fecha.insertar(Alerta(datos[0], 
                        datos[1], 
                        datos[2], datos[3], nombree), 'hora')
    lista_alerta_nombre.insertar(Alerta(datos[0], 
                        datos[1], 
                        datos[2], datos[3], nombree), 'name')

#Consigna 3: Eliminar la informacion de las zonas WYG075, SXH966 y LYF010. Modificar la zona
#HYD195 y cambiar el nombre a Mosasaurus.

lista_alerta_fecha.eliminar('WYG075', 'zona')
lista_alerta_fecha.eliminar('SXH966', 'zona')
lista_alerta_fecha.eliminar('LYF010', 'zona')

auxia = lista_alerta_fecha.eliminar('HYD195', 'zona')
auxia.name = 'Mosasaurus'
lista_alerta_fecha.insertar(auxia, 'hora')

lista_alerta_nombre.eliminar('WYG075', 'zona')
lista_alerta_nombre.eliminar('SXH966', 'zona')
lista_alerta_nombre.eliminar('LYF010', 'zona')

auxia = lista_alerta_nombre.eliminar('HYD195', 'zona')
auxia.name = 'Mosasaurus'
lista_alerta_nombre.insertar(auxia, 'hora')

#Consigna 4: Generar un listado que solo incluya los dinosaurios: Tyrannosaurus Rex, Spinosaurus, Giganotosaurus con
#nivel  ́critical’ o ‘high’.

lista_critical_high = Lista()
contador = 0

print('Listado de alertas nivel critical o high de Tyrannosaurus Rex, Spinosaurus o Giganotosaurus: ')
while(contador < lista_alerta_fecha.tamanio()):
    auxxx = lista_alerta_fecha.obtener_elemento(contador)

    if (auxxx.name == 'Tyrannosaurus Rex') and ('critical' or 'high' in auxxx.nivel):
        lista_critical_high.insertar(auxxx, 'name')
    if (auxxx.name == 'Spinosaurus') and ('critical' or 'high' in auxxx.nivel):
        lista_critical_high.insertar(auxxx, 'name')    
    if (auxxx.name == 'Giganotosaurus') and ('critical' or 'high' in auxxx.nivel):
        lista_critical_high.insertar(auxxx, 'name')
    contador += 1

lista_critical_high.barrido()
print()
#Consigna 5: Tomar toda la información de alertas e insertarlas en 2 colas, una con los datos de dinosaurios
#carnívoros y otra con los herbívoros, descartando los de nivel ‘low’ y ‘medium’

cola_carnivoros = Cola()
cola_herbivoros = Cola()

while(contador < lista_alerta_fecha.tamanio()):
    auxxx2 = lista_alerta_fecha.obtener_elemento(contador)

    dino = listadinos.busqueda(auxxx2.name, 'name')

    if (auxxx2.nivel != 'low') and (auxxx2.nivel != 'medium'):
        if ('carn' in dino.type):
            cola_carnivoros.arribo(auxxx2) 
        if ('herb' in dino.type):
            cola_herbivoros.arribo(auxxx2) 
    contador += 1

print(cola_carnivoros.tamanio())

#Consigna 6: Mostrar las alertas de la cola de carnivoros, descartando las de la zona EPC944

contador = 0
print('Informacion de los carnivoros (a excepcion de la zona EPC944): ')
while(contador < cola_carnivoros.tamanio()):
    auxilia = cola_carnivoros.en_frente()
    if not ('EPC944' in auxilia.zona):
        print(auxilia)
    cola_carnivoros.mover_al_final()
    contador += 1
print()

#Consigna 7: Enviar toda la informacion de los Raptors y Carnotaurus, y los códigos de las zonas 
#donde hay dinosaurios Compsognathus.

print('Informacion de los Raptors:')
lista_alerta_nombre.barrido_segun_dino('Raptors')
print()
print('Informacion de los Carnotaurus:')
lista_alerta_nombre.barrido_segun_dino('Carnotaurus')
print()
print('Zonas con Compsognathus:')
lista_alerta_nombre.barrido_segun_dino_zona('Compsognathus')
print()


#Consigna 8: desde que Jurassic Park arranco la calve a ha sido ‘mosquito’ pero que
# significa esto realmente, si lo consideramos como si fueran números estas serian las situaciones:
# 1. si el número está entre 33 y 47 su valor alfanumérico esta ok.
# 2. caso contrario
# si número {es divisible por 3 entonces (número // 2) + 9 (es tu nuevo valor alfanumérico)
#           {sino número -14 (es tu nuevo valor alfanumérico)
# en cualquiera de los casos debes continuar procesandolo, es una solución parcial.
# 3. al final obtendrás la clave si sabes cómo hacer las cosas, pero recuerda ‘mosquito’ es la clave
# de todo.

clave = 'mosquito'
cuenta = 0
resolucion = 0
while (cuenta <= 7):
    aux3 = clave[cuenta]
    aux3 = ord(aux3)

    if(aux3 >= 33 and aux3 <= 47):
        if (aux3 % 3 == 0):
            aux3 = ((aux3 // 2) + 9)
        else:
            aux3 = -14
    resolucion += aux3
    cuenta += 1

resolucion = str(resolucion)
print('La contraseña es: ' + resolucion)







 
             