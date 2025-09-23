# Indicar si es un número primo o no.
def es_primo(numero):
    if numero <= 1:
        return False

    # Verificamos si el número tiene algún divisor entre 2 y numero - 1
    for i in range(2, numero):
        if numero % i == 0:
            return False  # No es primo si se puede dividir sin resto

    return True  # Es primo si no encontró divisores


# Pedimos al usuario un número entero
numero = int(input("Ingresa un número entero: "))

# Verificamos si es primo
if es_primo(numero):
    print(numero, "es un número primo.")
else:
    print(numero, "NO es un número primo.")
