def frecuencia_palabras(texto):
    texto = texto.lower().replace(".", "").replace(",", "")
    palabras = texto.split()
    frecuencia = {}

    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
    return frecuencia

# Prueba
print(frecuencia_palabras("Hola mundo hola Python mundo"))
