def elementos_en_comun(lista1, lista2):
    """
    Devuelve una lista con los elementos que están en ambas listas.
    """
    return list(set(lista1) & set(lista2))


# Declaración de las listas
lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]

# Uso de la función y muestra del resultado
comunes = elementos_en_comun(lista1, lista2)
print(f"Elementos en común: {comunes}")
