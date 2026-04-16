# Laboratorio: Estructura de los Bloques en Blockchain ⛓️

Este proyecto es una implementación educativa de una cadena de bloques (Blockchain) desarrollada en **Python**. El objetivo es demostrar los principios de inmutabilidad, encadenamiento criptográfico y el mecanismo de consenso de Prueba de Trabajo (Proof of Work).

## 🚀 Características
- **Estructura de Bloque Estándar**: Incluye índice, marca de tiempo, datos, hash previo, nonce y hash actual.
- **Criptografía SHA-256**: Generación de huellas digitales únicas para cada bloque.
- **Prueba de Trabajo (PoW)**: Sistema de minado que requiere encontrar un hash con un número específico de ceros iniciales.
- **Dificultad Dinámica**: El sistema asigna una dificultad aleatoria para cada nuevo bloque, simulando condiciones de red variables.
- **Bloque Génesis**: Creación automática del primer bloque de la cadena.

## 📁 Estructura del Repositorio
- `block.py`: Contiene la lógica de la clase `Block` y el algoritmo de minado.
- `blockchain.py`: Contiene la clase `Blockchain`, la gestión de la cadena y el script de ejecución principal.

## 🛠️ Requisitos
- **Python 3.x**
- No se requieren librerías externas (se utilizan `hashlib`, `datetime`, `random` y `time` de la biblioteca estándar).

## 💻 Instalación y Ejecución
1. Clona este repositorio en tu máquina local

## Realizado por: Luis Martin, Andres Guilarte y Massiel Perozo
