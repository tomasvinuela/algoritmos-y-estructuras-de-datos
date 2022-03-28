matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
# se arma una lista o vector con otras listas o vectores dentro suyo, para asi generar una matriz. Cada vector sera una fila y cada elemento una columna
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[i][j])
