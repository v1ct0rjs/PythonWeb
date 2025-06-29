#!/bin/bash

# Instalar Python y pip si no están disponibles
if ! command -v python &> /dev/null; then
    apt-get update && apt-get install -y python3 python3-pip
fi

# Instalar Reflex si no está disponible
if ! command -v reflex &> /dev/null; then
    pip3 install reflex
fi

# Instalar dependencias de Python
pip3 install -r requirements.txt

# Exportar el frontend de Reflex
reflex export --frontend-only

# Descomprimir el frontend en el directorio de salida 'public'
unzip frontend.zip -d public

# Limpiar el archivo zip
rm -f frontend.zip


