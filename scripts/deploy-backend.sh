#!/bin/bash

echo "🚀 Desplegando Backend a Railway..."

# Verificar que Railway CLI está instalado
if ! command -v railway &> /dev/null; then
    echo "❌ Railway CLI no está instalado"
    echo "Instala con: npm install -g @railway/cli"
    exit 1
fi

# Login a Railway (si no está logueado)
railway login

# Crear proyecto si no existe
railway project create pythonweb-backend

# Configurar variables de entorno
railway variables set REFLEX_ENV=prod
railway variables set PORT=8000

# Deploy
railway up --dockerfile Dockerfile.backend

echo "✅ Backend desplegado en Railway"
echo "🔗 URL: https://pythonweb-backend-production.up.railway.app"
