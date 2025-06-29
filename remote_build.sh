#!/bin/bash

if ! command -v python3 &> /dev/null; then
    apt-get update && apt-get install -y python3 python3-pip
fi

python3 -m venv .venv || { echo "Error: Falló la creación del entorno virtual."; exit 1; }
source .venv/bin/activate || { echo "Error: Falló la activación del entorno virtual."; exit 1; }

pip install --upgrade pip

pip install reflex || { echo "Error: Falló la instalación de 'reflex'."; deactivate; exit 1; }

pip install -r requirements.txt || { echo "Error: Falló la instalación de dependencias."; deactivate; exit 1; }

if ! command -v reflex &> /dev/null; then
    echo "Error: 'reflex' no está disponible después de la instalación."
    deactivate
    exit 1
fi

if ! reflex export --frontend-only; then
    echo "Error: El comando 'reflex export --frontend-only' falló."
    echo "Detalles del error:"
    reflex export --frontend-only 2>&1
    deactivate
    exit 1
fi

if [ ! -f frontend.zip ]; then
    echo "Error: No se encontró el archivo 'frontend.zip'."
    deactivate
    exit 1
fi

unzip frontend.zip -d public || { echo "Error: Falló la descompresión de 'frontend.zip'."; deactivate; exit 1; }

rm -f frontend.zip
deactivate