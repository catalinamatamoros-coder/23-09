# Diccionario traductor de español a inglés
traductor = {
    "hola": "hello",
    "adiós": "goodbye",
    "gato": "cat",
    "perro": "dog",
    "casa": "house",
    "libro": "book",
    "escuela": "school",
    "comida": "food",
    "agua": "water",
    "gracias": "thank you"
}

# Solicita una palabra al usuario
palabra = input("Ingresa una palabra en español: ").lower()

# Busca la traducción y muestra el resultado
if palabra in traductor:
    print(f"La traducción de '{palabra}' es '{traductor[palabra]}'")
else:
    print("Lo siento, esa palabra no está en el diccionario")
