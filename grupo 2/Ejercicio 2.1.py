def contar_vocales_consonantes(frase):
    frase = frase.lower()
    vocales = "aeiou"
    num_vocales = 0
    num_consonantes = 0

    for letra in frase:
        if letra.isalpha():
            if letra in vocales:
                num_vocales += 1
            else:
                num_consonantes += 1

    return num_vocales, num_consonantes

v, c = contar_vocales_consonantes("Hola Latinas in Cloud")
print(f"Vocales: {v}, Consonantes: {c}")
