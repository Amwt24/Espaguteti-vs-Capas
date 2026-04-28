import timeit
import sys
import os

# Preparar el camino para importar desde monolito_capas
sys.path.append(os.path.abspath("monolito_capas"))
from domain import CaesarCipher

# --- MÉTODO ESPAGUETI (Lógica extraída para el test) ---
def logic_espagueti(texto, shift):
    resultado = ""
    for char in texto:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            resultado += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            resultado += char
    return resultado

# --- MÉTODO CAPAS (Lógica de dominio) ---
def logic_capas(texto, shift):
    return CaesarCipher.transform(texto, shift)

def run_benchmark():
    test_text = "El veloz murcielago hindu comia feliz cardillo y kiwi. La cigueña tocaba el saxofon detras del palenque de paja." * 10
    shift = 7
    iterations = 10000

    print(f"--- BENCHMARK DE RENDIMIENTO ({iterations} iteraciones) ---")
    
    # Timer para Espagueti
    t_espagueti = timeit.timeit(lambda: logic_espagueti(test_text, shift), number=iterations)
    
    # Timer para Capas
    t_capas = timeit.timeit(lambda: logic_capas(test_text, shift), number=iterations)

    print(f"Tiempo Espagueti: {t_espagueti:.4f} segundos")
    print(f"Tiempo Capas:     {t_capas:.4f} segundos")
    
    diff = ((t_capas - t_espagueti) / t_espagueti) * 100
    print(f"\nDiferencia: {diff:.2f}% {'más lento' if diff > 0 else 'más rápido'} (Capas vs Espagueti)")

if __name__ == "__main__":
    run_benchmark()
