# --- FUNCIONES DE INTERFAZ ---
def mostrar_menu():
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Saludar")
    print("2. Salir")
    opcion = input("Seleccione una opción: ")
    if not opcion:
        print("Error: No ingresó ninguna opción.")

# --- FUNCIONES DE USUARIO ---
def solicitar_nombre_usuario():
    nombre_usuario = input("Ingrese su nombre: ")
    print(f"Bienvenido {nombre_usuario} al sistema.")

# --- FLUJO PRINCIPAL ---
def iniciar_programa():
    solicitar_nombre_usuario()
    mostrar_menu()

if __name__ == "__main__":
    iniciar_programa()