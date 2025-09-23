inventario = {
    "manzana": {"precio": 500, "stock": 10},
    "pan": {"precio": 1000, "stock": 5},
    "leche": {"precio": 1500, "stock": 8}
}

def mostrar_inventario():
    for producto, info in inventario.items():
        print(f"{producto} - Precio: {info['precio']}, Stock: {info['stock']}")

# Prueba
mostrar_inventario()