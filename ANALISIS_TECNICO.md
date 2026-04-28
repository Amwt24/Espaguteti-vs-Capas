# Análisis Comparativo: Arquitectura de Software en el Cifrado César

## 1. Introducción
El presente análisis compara dos enfoques de implementación para el algoritmo de Cifrado César: el **Código Espagueti** y el **Monolito por Capas**. El objetivo es evaluar cómo la estructura del código afecta no solo el rendimiento, sino también la mantenibilidad, el testeo y la escalabilidad de una aplicación.

---

## 2. Implementación A: Código Espagueti
El término "Código Espagueti" se refiere a programas con una estructura de control de flujo compleja y enredada, carente de abstracción.

### Análisis del Código (`codigo_espagueti/main.py`):
- **Acoplamiento Fuerte**: La lógica del algoritmo, la gestión de la entrada del usuario (`input()`) y la salida por consola (`print()`) coexisten dentro de un mismo bucle `while` y una única función `run()`.
- **Falta de Cohesión**: La función `run()` tiene demasiadas responsabilidades. Si quisiéramos cambiar la interfaz de consola por una interfaz gráfica (GUI), tendríamos que reescribir prácticamente todo el script, ya que el algoritmo de cifrado está incrustado entre los mensajes de usuario.
- **Dificultad de Testeo**: No es posible realizar pruebas unitarias sobre el algoritmo de cifrado sin ejecutar toda la interacción por consola.

**Línea Crítica**: 
```python
resultado += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
```
Esta lógica está "enterrada" en el flujo de la UI, lo que impide su reutilización.

---

## 3. Implementación B: Monolito por Capas
Este enfoque aplica el principio de **Separación de Preocupaciones (SoC)**, dividiendo la aplicación en capas lógicas con responsabilidades definidas.

### Estructura y Flujo de Llamadas:
1.  **Capa de Dominio (`domain.py`)**: 
    - Contiene la "Lógica de Negocio" pura. 
    - La clase `CaesarCipher` no sabe que existe una consola o un usuario; solo procesa strings.
2.  **Capa de Servicio (`service.py`)**: 
    - Actúa como mediador. Orquesta cómo se usa el dominio.
    - Ejemplo: La función `decrypt` simplemente reutiliza el dominio pasando el desplazamiento en negativo.
3.  **Capa de Presentación (`main.py`)**: 
    - Es la única que interactúa con el mundo exterior. 
    - Llama al `CipherService`, delegando la complejidad.

**Ventaja Técnica**: Si el día de mañana se requiere que el desplazamiento sea validado contra una base de datos o se envíe por red, solo se modificaría la capa de Servicio, dejando el Dominio intacto.

---

## 4. Análisis de Eficiencia (Benchmark)
Basado en las pruebas de ejecución (10,000 iteraciones con un texto de ~1,000 caracteres):

- **Código Espagueti**: ~4.06s
- **Monolito por Capas**: ~4.81s
- **Diferencia**: **+18.5% de tiempo de ejecución** en la versión por capas.

### Justificación Técnica del "Overhead":
La diferencia de rendimiento se debe a la **pila de llamadas (Call Stack)** de Python. Cada vez que el código pasa de una capa a otra (de `main` a `service`, y de `service` a `domain`), el intérprete de Python debe:
1. Buscar el método en el espacio de nombres de la clase.
2. Crear un nuevo marco de stack para la función.
3. Pasar los argumentos por referencia/valor.

En el código espagueti, al estar todo en un solo bloque, estas operaciones se minimizan, permitiendo que el procesador ejecute las instrucciones de forma más lineal.

---

## 5. Casos de Relevancia y Conclusión

### ¿Cuándo usar Código Espagueti?
- **Scripts de "un solo uso"**: Automatizaciones rápidas que no se volverán a leer ni mantener.
- **Prototipado rápido (MVP)**: Cuando la velocidad de entrega inicial es crítica y el sistema es extremadamente simple.

### ¿Cuándo usar Monolito por Capas?
- **Proyectos Profesionales/Empresariales**: Donde el código será leído y modificado por múltiples ingenieros.
- **Sistemas que requieren Testing**: Permite crear "Mocks" o pruebas unitarias aisladas para asegurar que el algoritmo no falle tras cambios futuros.
- **Arquitecturas Evolutivas**: Cuando se prevé que el sistema crecerá (ej. añadir autenticación, persistencia de datos o múltiples interfaces).

### Conclusión Final
Para una tarea académica o un proyecto profesional, **el Monolito por Capas es el estándar de oro**. Aunque el código espagueti es marginalmente más rápido en micro-benchmarks, el costo humano de mantenerlo (deuda técnica) supera por mucho el ahorro de milisegundos en la CPU. La ingeniería de software moderna prioriza la **legibilidad y la robustez** sobre la optimización prematura.
