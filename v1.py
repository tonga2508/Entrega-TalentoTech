import mysql.connector
from mysql.connector import Error
from colorama import init, Fore

# Inicializar colorama
init()

def crear_conexion():
    """Crear y devolver una conexión a la base de datos MySQL."""
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            user='tonga',
            password='cicsparg',
            database='inventario'
        )
        if conexion.is_connected():
            return conexion
    except Error as e:
        print(Fore.RED + f"Error al conectar con MySQL: {e}" + Fore.RESET)
        return None

def registrar_producto():
    """Registrar un nuevo producto en la base de datos."""
    nombre = input("Ingrese el nombre del producto: ")
    descripcion = input("Ingrese la descripción del producto: ")
    cantidad = int(input("Ingrese la cantidad disponible: "))
    precio = float(input("Ingrese el precio del producto: "))
    categoria = input("Ingrese la categoría del producto: ")

    conexion = crear_conexion()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("""
            INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria)
            VALUES (%s, %s, %s, %s, %s)
        """, (nombre, descripcion, cantidad, precio, categoria))
        conexion.commit()
        conexion.close()
        print(Fore.GREEN + "Producto registrado exitosamente." + Fore.RESET)

def mostrar_productos():
    """Mostrar productos del inventario por categoría o todos."""
    print(Fore.CYAN + "\nOpciones para mostrar productos:" + Fore.RESET)
    print("1. Mostrar todos los productos")
    print("2. Mostrar productos por categoría")
    opcion = input("Seleccione una opción: ")

    conexion = crear_conexion()
    if conexion:
        cursor = conexion.cursor()
        if opcion == "1":
            cursor.execute("SELECT * FROM productos")
            productos = cursor.fetchall()
            print(Fore.YELLOW + "\nTodos los productos:" + Fore.RESET)
        elif opcion == "2":
            categoria = input("Ingrese la categoría (A, B, C, etc.): ").upper()
            cursor.execute("SELECT * FROM productos WHERE categoria LIKE %s", (f"%{categoria}%",))
            productos = cursor.fetchall()
            print(Fore.YELLOW + f"\nProductos en la categoría '{categoria}':" + Fore.RESET)
        else:
            print(Fore.RED + "Opción no válida." + Fore.RESET)
            conexion.close()
            return

        if productos:
            print("ID | Nombre | Descripción | Cantidad | Precio | Categoría")
            print("-" * 50)
            for producto in productos:
                print(f"{producto[0]} | {producto[1]} | {producto[2]} | {producto[3]} | {producto[4]} | {producto[5]}")
        else:
            print(Fore.RED + "No se encontraron productos." + Fore.RESET)

        conexion.close()

def actualizar_producto():
    """Actualizar la cantidad de un producto específico."""
    id_producto = int(input("Ingrese el ID del producto a actualizar: "))
    nueva_cantidad = int(input("Ingrese la nueva cantidad: "))

    conexion = crear_conexion()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("""
            UPDATE productos
            SET cantidad = %s
            WHERE id = %s
        """, (nueva_cantidad, id_producto))
        conexion.commit()
        conexion.close()
        print(Fore.GREEN + "Cantidad actualizada exitosamente." + Fore.RESET)

def eliminar_producto():
    """Eliminar un producto del inventario."""
    id_producto = int(input("Ingrese el ID del producto a eliminar: "))

    conexion = crear_conexion()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("""
            DELETE FROM productos
            WHERE id = %s
        """, (id_producto,))
        conexion.commit()
        conexion.close()
        print(Fore.RED + "Producto eliminado exitosamente." + Fore.RESET)

def buscar_producto():
    """Buscar un producto por ID, nombre o categoría."""
    criterio = input("Buscar por (id/nombre/categoria): ").lower()
    valor = input("Ingrese el valor de búsqueda: ")

    conexion = crear_conexion()
    if conexion:
        cursor = conexion.cursor()
        if criterio == "id":
            cursor.execute("SELECT * FROM productos WHERE id = %s", (valor,))
        elif criterio == "nombre":
            cursor.execute("SELECT * FROM productos WHERE nombre LIKE %s", (f"%{valor}%",))
        elif criterio == "categoria":
            cursor.execute("SELECT * FROM productos WHERE categoria LIKE %s", (f"%{valor}%",))
        else:
            print(Fore.RED + "Criterio de búsqueda no válido." + Fore.RESET)
            return

        resultados = cursor.fetchall()
        conexion.close()

        if resultados:
            print(Fore.YELLOW + "\nResultados de la búsqueda:" + Fore.RESET)
            for producto in resultados:
                print(f"{producto[0]} | {producto[1]} | {producto[2]} | {producto[3]} | {producto[4]} | {producto[5]}")
        else:
            print(Fore.RED + "No se encontraron productos." + Fore.RESET)

def reporte_bajo_stock():
    """Generar un reporte de productos con bajo stock."""
    limite = int(input("Ingrese el límite de stock: "))

    conexion = crear_conexion()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM productos WHERE cantidad <= %s", (limite,))
        productos = cursor.fetchall()
        conexion.close()

        print(Fore.YELLOW + "\nReporte de bajo stock:" + Fore.RESET)
        for producto in productos:
            print(f"{producto[0]} | {producto[1]} | {producto[2]} | {producto[3]} | {producto[4]} | {producto[5]}")

def menu():
    """Mostrar el menú principal e interactuar con el usuario."""
    while True:
        print(Fore.CYAN + "\nMenú Principal" + Fore.RESET)
        print("1. Registrar producto")
        print("2. Mostrar productos")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Buscar producto")
        print("6. Reporte de bajo stock")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_producto()
        elif opcion == "2":
            mostrar_productos()
        elif opcion == "3":
            actualizar_producto()
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "5":
            buscar_producto()
        elif opcion == "6":
            reporte_bajo_stock()
        elif opcion == "7":
            print(Fore.GREEN + "Saliendo del programa..." + Fore.RESET)
            break
        else:
            print(Fore.RED + "Opción no válida." + Fore.RESET)

if __name__ == "__main__":
    menu()