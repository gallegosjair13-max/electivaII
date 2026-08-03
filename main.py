def mostrar_menu():
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Saludar")
    print("2. Salir")

def obtener_datos():
    nombre = input("Ingrese su nombre: ")
    print(f"Bienvenido {nombre} al sistema.")

def ejecutar():
    obtener_datos()
    mostrar_menu()

ejecutar()