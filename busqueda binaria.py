vector = [1, 30, 4, 5, 70, 100]
def bbinaria(vector, buscado, primero, ultimo):
    medio = (primero + ultimo) // 2
    if(primero > ultimo):
        return -1
    if(buscado == vector[medio]):
        return medio
    else:
        if(vector[medio]<buscado):
            bbinaria(vector, buscado, medio+1, ultimo)
        else:
            bbinaria(vector, buscado, primero, medio-1)
Para poder usar la busqueda binaria el vector debe estar ordenado, ya que sino las busquedas no serian correctas (ya que se cuenta con que primero y ultimo son los primero y ultimo numeros y que primero es menor que ultimo)
