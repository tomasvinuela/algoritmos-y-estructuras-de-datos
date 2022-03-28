
def ej2_recur(num):
    if (num == 0):
        return num
    else:
        return num + ej2_recur(num-1)
print(ej2_recur(4))
