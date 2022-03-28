def h(numero):
    if (numero == 1):
        return 1
    else:
        return 1 / numero + h(numero-1)
print(h(4))