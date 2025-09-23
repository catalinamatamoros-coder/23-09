# Catálogo de productos
catalogo = {
    "Pan": 1.5,
    "Leche": 2.0,
    "Queso": 3.5,
    "Huevos": 2.8,
    "Café": 4.0,
    "Azúcar": 1.2
}


def mostrar_productos(catalogo):
    print("Productos disponibles:")
    for idx, (producto, precio) in enumerate(catalogo.items(), 1):
        print(f"{idx}. {producto} - ${precio:.2f}")


def agregar_al_carrito(catalogo):
    carrito = []
    while True:
        mostrar_productos(catalogo)
        eleccion = input(
            "Ingrese el número del producto para agregar al carrito \
                (o 'fin' para terminar): ")
        if eleccion.lower() == 'fin':
            break
        try:
            idx = int(eleccion) - 1
            producto = list(catalogo.keys())[idx]
            carrito.append(producto)
            print(f"{producto} agregado al carrito.\n")
        except (ValueError, IndexError):
            print("Selección inválida. Intente de nuevo.\n")
    return carrito


def calcular_subtotal(carrito, catalogo):
    return sum(catalogo[producto] for producto in carrito)


def aplicar_descuento(subtotal, umbral=100, descuento=0.10):
    if subtotal > umbral:
        return subtotal * descuento
    return 0


def generar_ticket(carrito, catalogo, subtotal, descuento):
    print("\n--- Ticket de Compra ---")
    for producto in carrito:
        print(f"{producto}: ${catalogo[producto]:.2f}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Descuento: -${descuento:.2f}")
    print(f"Total a pagar: ${subtotal - descuento:.2f}")
    print("------------------------")


def main():
    carrito = agregar_al_carrito(catalogo)
    if not carrito:
        print("No se agregaron productos al carrito.")
        return
    subtotal = calcular_subtotal(carrito, catalogo)
    descuento = aplicar_descuento(subtotal)
    generar_ticket(carrito, catalogo, subtotal, descuento)


if __name__ == "__main__":
    main()
