def calcular_factorial(numero):
    # Empezamos con 1 porque el factorial de 0 es 1
    resultado = 1

    # Multiplicamos desde 1 hasta el número
    for i in range(1, numero + 1):
        resultado = resultado * i

    return resultado


# Pedimos al usuario un número
numero = int(input("Ingresa un número entero positivo: "))

# Calculamos el factorial y lo mostramos
print("El factorial de", numero, "es", calcular_factorial(numero))
