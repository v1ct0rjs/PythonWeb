#!/bin/bash

echo "🚀 Desplegando Frontend a Vercel..."

# Configurar variables de entorno para el build
export REFLEX_ENV=prod
export API_URL=https://pythonweb-backend-production.up.railway.app

# Limpiar builds anteriores
rm -rf public
rm -f frontend.zip

# Instalar dependencias
python3 -m pip install -r requirements.txt

# Inicializar Reflex
reflex init

# Exportar frontend
reflex export --frontend-only

# Extraer archivos
unzip frontend.zip -d public

echo "✅ Frontend listo para deployment en Vercel"
echo "📁 Archivos en ./public/"
