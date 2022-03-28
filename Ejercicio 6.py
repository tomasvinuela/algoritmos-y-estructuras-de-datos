def invert_cadena(cadena, indice):
    if (indice == 1):
        return cadena[indice-1]
    else:
        return cadena[indice-1] + invert_cadena(cadena, indice-1)
print(invert_cadena("hola", len("hola")))