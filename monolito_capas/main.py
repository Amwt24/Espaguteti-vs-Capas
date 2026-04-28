# Capa de Presentación: Interfaz de usuario (Consola)
from service import CipherService

def main():
    service = CipherService()
    print("--- CIFRADO CESAR (MONOLITO POR CAPAS) ---")
    
    while True:
        print("\n1. Encriptar")
        print("2. Desencriptar")
        print("3. Salir")
        choice = input("Seleccione una opción: ")

        if choice == '3':
            break
        
        if choice in ['1', '2']:
            text = input("Texto: ")
            try:
                shift = int(input("Desplazamiento: "))
            except ValueError:
                print("Error: El desplazamiento debe ser un número.")
                continue

            if choice == '1':
                print(f"Cifrado: {service.encrypt(text, shift)}")
            else:
                print(f"Descifrado: {service.decrypt(text, shift)}")
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
