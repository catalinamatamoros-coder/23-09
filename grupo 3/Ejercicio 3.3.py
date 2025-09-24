calificaciones = {}

def agregar_calificacion(nombre, nota):
    calificaciones[nombre] = nota

def promedio():
    return sum(calificaciones.values()) / len(calificaciones)

# Prueba
agregar_calificacion("Luis", 5.5)
agregar_calificacion("Ana", 6.0)
agregar_calificacion("Juan", 6.5)

print("Promedio:", promedio())
