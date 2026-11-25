#!/bin/bash

echo "🔧 Configurando variables de entorno..."
export REFLEX_ENV=${REFLEX_ENV:-prod}
# API_URL ya no es necesaria aquí si rxconfig.py lo maneja
# export API_URL=${API_URL:-https://pythonweb-backend-production.up.railway.app}

echo "📦 Instalando dependencias..."
python3 -m pip install -r requirements.txt

echo "🚀 Inicializando Reflex..."
reflex init

echo "🏗️ Building frontend..."
reflex export --frontend-only

echo "📁 Extrayendo archivos..."
rm -rf public
unzip -q -o frontend.zip -d public
rm -f frontend.zip

echo "✅ Build completado!"
# echo "🔗 Frontend configurado para conectar a: $API_URL" # Mensaje ya no relevante

