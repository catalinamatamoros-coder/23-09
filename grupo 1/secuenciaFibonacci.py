# Genera los primeros N números de la secuencia de Fibonacci,
# donde N es un número proporcionado por el usuario.
def generar_fibonacci(n):
    # Lista para guardar la secuencia
    secuencia = []

    # Empezamos con los dos primeros números
    a = 0
    b = 1

    for i in range(n):
        secuencia.append(a)   # Agregamos el número actual
        a, b = b, a + b       # Calculamos el siguiente número

    return secuencia


# Pedimos al usuario que ingrese un número entero
n = int(input("¿Cuántos números de Fibonacci quieres generar?: "))

# Generamos la secuencia y la mostramos
fibonacci = generar_fibonacci(n)
print("Los primeros", n, "números de la secuencia de Fibonacci son:")
print(fibonacci)
