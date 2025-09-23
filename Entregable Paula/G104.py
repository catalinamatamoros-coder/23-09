# Adivina el Número: El programa genera un número aleatorio entre 1 y 100.
# El usuario debe adivinarlo y el programa
# le dará pistas ("más alto" o "más bajo").
import random

print("¡Adivina el número entre 1 y 100!")
numero_secreto = random.randint(1, 100)
intentos = 0

while True:
    intento = int(input("Ingresa tu número: "))
    intentos += 1
    if intento < numero_secreto:
        print("Más alto")
    elif intento > numero_secreto:
        print("Más bajo")
    else:
        print(
            f"¡Correcto! El número era {numero_secreto}. "
            f"Lo lograste en {intentos} intentos."
        )
        break
    30
