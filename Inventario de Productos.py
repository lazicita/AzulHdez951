#Azul Fernanda Hernández García
# Grupo: 951
# Fecha: 30 de agosto de 2026
# Descripción: Sistema de gestión de inventario de productos utilizando
# diccionarios anidados, con funciones para agregar, editar, eliminar,
# vender e imprimir productos.
inventario = {
    "P001": {"nombre": "Peluche de Hello Kitty", "precio": 350, "cantidad_stock": 100},
    "P002": {"nombre": "Espejito de Hello Kitty", "precio": 100, "cantidad_stock": 150},
    "P003": {"nombre": "Cobija de SanrioFriends", "precio": 600, "cantidad_stock": 200},
    "P004": {"nombre": "Plato de Pompompurin", "precio": 100, "cantidad_stock": 250},
    "P005": {"nombre": "Termo de Pochacco 1L", "precio": 350, "cantidad_stock": 300},
}

def agregar_producto(codigo, nombre, precio, cantidad_stock):
    if codigo in inventario:
        print("Ese codigo ya existe, prueba con otro")
    else:
        inventario[codigo] = {"nombre": nombre, "precio": precio, "cantidad_stock": cantidad_stock}
        print("Codigo Disponible")

def eliminar_producto(codigo):
    if codigo in inventario:
        del inventario[codigo]
        print("Producto eliminado")
    else:
        print("Producto no existente")

def editar_producto(codigo, nombre, precio, cantidad_stock):
    if codigo in inventario:
        inventario[codigo]["nombre"] = nombre
        inventario[codigo]["precio"] = precio
        inventario[codigo]["cantidad_stock"] = cantidad_stock
        print("Producto Editado")
    else:
        print("Producto no existente")

def realizar_venta(codigo, cantidad):
    if codigo in inventario:
        if cantidad<=inventario[codigo]["cantidad_stock"]:
            print("Venta realizada con éxito")
            inventario[codigo]["cantidad_stock"] -= cantidad
            if inventario[codigo]["cantidad_stock"] == 0:
                print("El producto", codigo, "se ha agotado")
        else:
            print("La cantidad solicitada en el inventario es insuficiente")
    else:
        print("Producto no existente")

def imprimir_inventario():
    for codigo, datos in inventario.items():
        print("Código:",codigo,"\nNombre:",datos["nombre"],"\nPrecio:",datos["precio"],"\nCantidad de Stock:",datos["cantidad_stock"])



if __name__ == "__main__":
    print("Caso 1: Agregar un producto nuevo correctamente")
    print("-----------------------------------------------------")
    agregar_producto("P006", "Llavero de Cinnamoroll", 80, 120)
    imprimir_inventario()

    print("\nCaso 2: Intentar agregar un producto con código ya existente")
    print("-----------------------------------------------------")
    agregar_producto("P001", "Producto Duplicado", 100, 50)

    print("\nCaso 3: Eliminar un producto existente")
    print("-----------------------------------------------------")
    eliminar_producto("P006")
    imprimir_inventario()

    print("\nCaso 4: Intentar eliminar un producto que no existe")
    print("-----------------------------------------------------")
    eliminar_producto("P999")

    print("\nCaso 5: Editar un producto existente")
    print("-----------------------------------------------------")
    editar_producto("P001", "Termo de Badtz 1L", 350, 400)
    imprimir_inventario()

    print("\nCaso 6: Realizar una venta exitosa")
    print("-----------------------------------------------------")
    realizar_venta("P001", 3)
    imprimir_inventario()

    print("\nCaso 7: Intentar vender más cantidad de la que hay en stock")
    print("-----------------------------------------------------")
    realizar_venta("P002", 45645)

    print("\nCaso 8: Vender exactamente el stock disponible (para probar aviso de agotdo)")
    print("-----------------------------------------------------")
    realizar_venta("P003", 200)
    imprimir_inventario()


