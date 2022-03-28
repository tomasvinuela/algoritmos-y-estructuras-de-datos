vector = [1, 2, 3, 4, 5]
def determinar(lista, elemento, indice):
    if(lista[indice] == elemento):
        return "Esta en la lista"
    else:
        if (indice == -1):
            return "No esta en la lista"
        else:
            return determinar(lista, elemento, indice-1)
print(determinar(vector, 3, len(vector)))