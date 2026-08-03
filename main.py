def mostrar_menu():
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Saludar")
    print("2. Salir")
    opcion = input("Seleccione una opción: ")
    # Corrección: validación básica para evitar opciones vacías
    if not opcion:
        print("Error: No ingresó ninguna opción.")

def obtener_datos():
    nombre = input("Ingrese su nombre: ")
    print(f"Bienvenido {nombre} al sistema.")

def ejecutar():
    obtener_datos()
    mostrar_menu()

ejecutar()