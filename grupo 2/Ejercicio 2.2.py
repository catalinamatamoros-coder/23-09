def es_palindromo(texto):
    texto = texto.lower()
    texto = texto.replace(" ", "")
    texto_invertido = texto[::-1]
    if texto == texto_invertido:
        return True
    else:
        return False
