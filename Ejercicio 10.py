def contador(numero):
    if (numero < 10):
        return 1
    else:
        return 1 + contador(numero / 10)
print(contador(850))