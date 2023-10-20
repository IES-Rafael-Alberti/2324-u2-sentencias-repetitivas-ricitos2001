def crear_impares(numero):
    if numero >= 0:
        impares = ""
        for i in range(1, numero + 1, 2):
            impares += str(i)
            if i < numero - 1:
                impares += ", "
    return impares
if __name__=="__main__":
    numero = int(input("introduce un numero: "))
    impares=crear_impares(numero)
    print(impares)
