def potencia(base, potencia_n):
    if (potencia_n == 0):
        return 1
    else:
        return base * potencia(base, potencia_n-1)
print(potencia(3, 2))