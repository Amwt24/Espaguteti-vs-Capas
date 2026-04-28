import sys

# Todo mezclado: lógica, entrada, salida
def run():
    print("--- CIFRADO CESAR (MODO ESPAGUETI) ---")
    while True:
        opt = input("¿Quieres (E)ncriptar, (D)esencriptar o (S)alir?: ").upper()
        if opt == 'S':
            break
        if opt not in ['E', 'D']:
            print("Opción no válida")
            continue
        
        texto = input("Introduce el texto: ")
        try:
            shift = int(input("Introduce el desplazamiento (número): "))
        except:
            print("Desplazamiento inválido")
            continue
            
        if opt == 'D':
            shift = -shift
            
        resultado = ""
        for char in texto:
            if char.isalpha():
                ascii_offset = 65 if char.isupper() else 97
                # Lógica de cifrado incrustada directamente
                resultado += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            else:
                resultado += char
        
        print(f"Resultado: {resultado}")
        print("-" * 20)

if __name__ == "__main__":
    run()
