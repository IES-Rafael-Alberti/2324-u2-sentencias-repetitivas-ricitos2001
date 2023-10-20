def crear_repeticiones(nombre):
    repeticiones =""
    if numero > 0:
        for contador in range(numero):
            repeticiones += nombre + "\n"
    return repeticiones





if __name__ == "__main__":
    
    # Entrada
    nombre = input("escriba su nombre: ")

    # Procesamiento
    numero = 10
    repeticiones = crear_repeticiones(nombre)

    # Salida
    print(repeticiones)