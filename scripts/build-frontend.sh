#!/bin/bash

echo "🔧 Configurando variables de entorno..."
export REFLEX_ENV=${REFLEX_ENV:-prod}
export API_URL=${API_URL:-https://pythonweb-backend-production.up.railway.app}

echo "📦 Instalando dependencias..."
python3 -m pip install -r requirements.txt

echo "🚀 Inicializando Reflex..."
reflex init

echo "🏗️ Building frontend con API_URL: $API_URL"
reflex export --frontend-only

echo "📁 Extrayendo archivos..."
unzip frontend.zip -d public

echo "✅ Build completado!"
echo "🔗 Frontend configurado para conectar a: $API_URL"
