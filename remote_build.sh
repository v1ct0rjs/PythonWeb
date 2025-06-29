#!/bin/bash

if ! command -v python3 &> /dev/null; then
    apt-get update && apt-get install -y python3 python3-pip
fi

pip3 install --upgrade pip

if ! command -v reflex &> /dev/null; then
    pip3 install reflex || { echo "Error: Falló la instalación de 'reflex'."; exit 1; }
fi

pip3 install -r requirements.txt || { echo "Error: Falló la instalación de dependencias."; exit 1; }

if ! command -v reflex &> /dev/null; then
    echo "Error: 'reflex' no está disponible después de la instalación."
    exit 1
fi

if ! reflex export --frontend-only; then
    echo "Error: El comando 'reflex export --frontend-only' falló."
    exit 1
fi

if [ ! -f frontend.zip ]; then
    echo "Error: No se encontró el archivo 'frontend.zip'."
    exit 1
fi

unzip frontend.zip -d public || { echo "Error: Falló la descompresión de 'frontend.zip'."; exit 1; }

rm -f frontend.zip