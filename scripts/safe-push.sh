#!/bin/bash

echo "🔄 Sincronizando con repositorio remoto..."

# Hacer backup de cambios locales
echo "💾 Haciendo backup de cambios locales..."
git stash push -m "Backup automático $(date)"

# Traer cambios remotos
echo "⬇️ Descargando cambios remotos..."
git pull origin main

# Restaurar cambios locales
echo "🔄 Restaurando cambios locales..."
if git stash list | grep -q "Backup automático"; then
    git stash pop
fi

# Verificar si hay conflictos
if git status --porcelain | grep -q "^UU\|^AA\|^DD"; then
    echo "⚠️ HAY CONFLICTOS - Resuélvelos manualmente:"
    git status
    echo "Después ejecuta:"
    echo "  git add ."
    echo "  git commit -m 'Resuelve conflictos'"
    echo "  git push origin main"
else
    echo "✅ No hay conflictos"

    # Si hay cambios, commitear y pushear
    if ! git diff --quiet || ! git diff --cached --quiet; then
        echo "📝 Commiteando cambios..."
        git add .
        git commit -m "Actualización automática: $(date)"

        echo "🚀 Pusheando a remoto..."
        git push origin main

        echo "✅ ¡Listo! Cambios sincronizados"
    else
        echo "ℹ️ No hay cambios para commitear"
    fi
fi
