# Cifrado César: Espagueti vs. Capas

Este proyecto implementa el algoritmo de cifrado César con desplazamiento variable en dos estilos arquitectónicos diferentes para comparar la mantenibilidad y organización del código.

## Estructuras

### 1. Código Espagueti (`codigo_espagueti/`)
Un enfoque monolítico y desorganizado donde la lógica de negocio, la entrada de datos y la salida por consola están mezcladas en un solo archivo y función. Es difícil de testear y escalar.

### 2. Monolito por Capas (`monolito_capas/`)
Una arquitectura limpia dividida en responsabilidades claras:
- **Capa de Dominio (`domain.py`)**: Lógica pura del algoritmo.
- **Capa de Servicio (`service.py`)**: Orquestación de operaciones.
- **Capa de Presentación (`main.py`)**: Interfaz de usuario (CLI).

## Cómo ejecutar

### Versión Espagueti
```bash
python codigo_espagueti/main.py
```

### Versión por Capas
```bash
python monolito_capas/main.py
```

## Requisitos
Este proyecto utiliza únicamente la biblioteca estándar de Python (no requiere librerías externas), pero se incluye un archivo `requirements.txt` para seguir las mejores prácticas.
