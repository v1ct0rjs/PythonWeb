#!/bin/bash

# Verificar la versión de Python
PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
REQUIRED_VERSION="3.12"

if [[ "$PYTHON_VERSION" != "$REQUIRED_VERSION"* ]]; then
    echo "Error: Se requiere Python $REQUIRED_VERSION, pero se encontró Python $PYTHON_VERSION."
    exit 1
fi

# Crear y activar entorno virtual
python3 -m venv .venv || { echo "Error: Falló la creación del entorno virtual."; exit 1; }
source .venv/bin/activate || { echo "Error: Falló la activación del entorno virtual."; exit 1; }

# Actualizar pip e instalar dependencias
pip install --upgrade pip
pip install reflex || { echo "Error: Falló la instalación de 'reflex'."; deactivate; exit 1; }
pip install -r requirements.txt || { echo "Error: Falló la instalación de dependencias."; deactivate; exit 1; }

# Verificar disponibilidad de 'reflex'
if ! command -v reflex &> /dev/null; then
    echo "Error: 'reflex' no está disponible después de la instalación."
    deactivate
    exit 1
fi

# Ejecutar 'reflex export' y capturar errores
if ! reflex export --frontend-only; then
    echo "Error: El comando 'reflex export --frontend-only' falló."
    echo "Detalles del error:"
    reflex export --frontend-only 2>&1 | tee reflex_error.log
    deactivate
    exit 1
fi

# Verificar y descomprimir el archivo generado
if [ ! -f frontend.zip ]; then
    echo "Error: No se encontró el archivo 'frontend.zip'."
    deactivate
    exit 1
fi

unzip frontend.zip -d public || { echo "Error: Falló la descompresión de 'frontend.zip'."; deactivate; exit 1; }

rm -f frontend.zip
deactivate