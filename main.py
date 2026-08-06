# --- FUNCIONES DE INTERFAZ ---
def mostrar_menu():
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Saludar")
    print("2. Acerca del sistema")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")
    if not opcion:
        print("Error: No ingresó ninguna opción.")
    elif opcion == "2":
        mostrar_informacion()

def mostrar_informacion():
    print("\nSistema desarrollado para la gestión básica en consola v1.1.")

# --- FUNCIONES DE USUARIO ---
def solicitar_nombre_usuario():
    nombre_usuario = input("Ingrese su nombre: ")
    print(f"Bienvenido {nombre_usuario} al sistema.")

# --- FLUJO PRINCIPAL ---
def iniciar_programa():
    solicitar_nombre_usuario()
    mostrar_menu()
    print("\n¡Gracias por usar el sistema! Hasta pronto.")

if __name__ == "__main__":
    iniciar_programa()