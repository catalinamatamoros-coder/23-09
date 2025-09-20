# Entregable del Curso de Python Básico
Este entregable está diseñado para evaluar y consolidar los conocimientos adquiridos en el curso. Se divide en tres partes: ejercicios de lógica de programación en Python, desarrollo de una aplicación web básica con Flask y una introducción a la ciencia de datos utilizando Google Colab.

## Parte 1: 20 Ejercicios Intermedios de Python
El objetivo de esta sección es resolver problemas prácticos utilizando los fundamentos de Python, como estructuras de datos, funciones y lógica de control.

### Grupo 1: Fundamentos y Lógica (Ejercicios 1-5)

1. **Calculadora de Factorial:** Crea una función que reciba un número entero y devuelva su factorial.
2. **Verificador de Números Primos:** Escribe un programa que solicite un número al usuario e indique si es un número primo o no.
3. **Secuencia de Fibonacci:** Genera los primeros N números de la secuencia de Fibonacci, donde N es un número proporcionado por el usuario.
4. **Adivina el Número:** El programa genera un número aleatorio entre 1 y 100. El usuario debe adivinarlo y el programa le dará pistas ("más alto" o "más bajo").
5. **Conversor de Temperatura:** Crea dos funciones, una para convertir de grados Celsius a Fahrenheit y otra para hacer la conversión inversa.
def celsius_a_fahrenheit(c):
    return c * 9/5 + 32
def fahrenheit_a_celsius(f):
    return (f - 32) * 5/9


### Grupo 2: Manipulación de Cadenas y Listas (Ejercicios 6-10)

6. **Contador de Vocales y Consonantes:** Pide al usuario que ingrese una frase y cuenta cuántas vocales y consonantes contiene.
7. **Verificador de Palíndromos:** Crea una función que determine si una palabra o frase ingresada es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda, ignorando espacios y mayúsculas).
def es_palindromo(texto):
    texto = texto.lower()
    texto = texto.replace(" ", "")
    texto_invertido = texto[::-1]
    if texto == texto_invertido:
        return True
    else:
        return False


8. **Eliminar Duplicados de una Lista:** Dada una lista, crea una nueva lista que contenga solo los elementos únicos de la original, sin repetir ninguno.
9. **Buscador de Elementos Comunes:** Escribe una función que reciba dos listas y devuelva una nueva lista con los elementos que ambas tienen en común.
10. **Ordenamiento de Lista (Burbuja):** Implementa el algoritmo de ordenamiento de burbuja para ordenar una lista de números de menor a mayor sin usar la función sort().

>>> def burbuja(lista):
...  n = len(lista)
...  for i in range(n):
...   for j in range(0, n - i - 1):
...    if lista[j] > lista[j + 1]:
...     lista[j], lista[j + 1] = lista[j + 1], lista[j]
...  return lista

### Grupo 3: Diccionarios y Estructuras de Datos (Ejercicios 11-15)

11. **Frecuencia de Palabras:** Dado un párrafo de texto, cuenta la frecuencia de aparición de cada palabra y almacena el resultado en un diccionario.
12. **Agenda de Contactos:** Crea un programa que funcione como una agenda. Debe permitir al usuario añadir un contacto (nombre, teléfono), buscar un contacto por su nombre y eliminar un contacto. Usa un diccionario para almacenar la agenda.
13. **Gestor de Calificaciones:** Permite al usuario ingresar nombres de estudiantes y sus calificaciones. Almacénalos en un diccionario y luego calcula y muestra el promedio de calificaciones de toda la clase.
14. **Traductor Simple:** Crea un diccionario que funcione como un traductor de español a inglés. Debe contener al menos 10 palabras y permitir al usuario ingresar una palabra en español para obtener su traducción.
15. **Inventario de Tienda:** Define un diccionario para un inventario de productos. La clave será el nombre del producto y el valor será otro diccionario con su "precio" y "stock" (cantidad disponible).

### Grupo 4: Mini-proyecto "Caja de Ventas" (Ejercicios 16-20)

Estos ejercicios construyen de forma progresiva un sistema de caja registradora.

16. **Definir Productos:** Crea un diccionario que represente el catálogo de productos de una tienda, donde las claves son los nombres de los productos y los valores son sus precios.
17. **Agregar al Carrito:** Muestra al usuario los productos disponibles y permite que seleccione productos para agregarlos a una lista que simulará ser un "carrito de compras".
18. **Calcular Subtotal:** Crea una función que reciba el carrito de compras y el catálogo de productos, y calcule el costo total de la compra sin aplicar impuestos ni descuentos.
19. **Aplicar Descuentos:** Modifica el programa para que aplique un descuento del 10% si el subtotal de la compra supera un monto determinado (por ejemplo, $100).
20. **Generar Ticket de Compra:** Al finalizar la compra, muestra un resumen detallado que incluya los productos comprados, el subtotal, el descuento aplicado (si corresponde) y el total final a pagar.

## Parte 2: Aplicación Web Básica con Flask

El objetivo es crear una aplicación de "Lista de Tareas" (To-Do List) que permita añadir y eliminar tareas. Las tareas se almacenarán en una lista en la memoria del servidor.

- Debe poder crearse más tareas en la lista
- Debe poder eliminarse una tarea en la lista
- Debe poder editarse una tarea en específico de la lista
- Deben verse las tareas creadas

Lista para almacenar las tareas en memoria. Puedes inicializarla con algunas tareas de ejemplo.

`tareas = ["Aprender Python", "Crear un entregable", "Practicar Flask"]`

