#!/bin/bash

# Instalar Python y pip si no están disponibles
if ! command -v python3 &> /dev/null; then
    apt-get update && apt-get install -y python3 python3-pip
fi

# Instalar Reflex si no está disponible
if ! command -v reflex &> /dev/null; then
    pip3 install reflex
fi

# Instalar dependencias de Python
pip3 install -r requirements.txt

# Exportar el frontend de Reflex
if ! reflex export --frontend-only; then
    echo "Error: El comando 'reflex export --frontend-only' falló."
    exit 1
fi

# Verificar si el archivo frontend.zip fue generado
if [ ! -f frontend.zip ]; then
    echo "Error: No se encontró el archivo 'frontend.zip'."
    exit 1
fi

# Descomprimir el frontend en el directorio de salida 'public'
unzip frontend.zip -d public || { echo "Error: Falló la descompresión de 'frontend.zip'."; exit 1; }

# Limpiar el archivo zip
rm -f frontend.zip