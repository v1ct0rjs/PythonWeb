FROM python:3.11-slim

WORKDIR /app

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
  curl \
  build-essential \
  unzip \
  && rm -rf /var/lib/apt/lists/*

# Copiar archivos de dependencias
COPY requirements.txt .

# Instalar dependencias Python
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código de la aplicación
COPY . .

# Inicializar Reflex
RUN reflex init

# Exponer puerto (Railway usa PORT env var)
EXPOSE $PORT

# Comando para producción - ajustado.
# Si este Dockerfile se usa para correr la app completa (frontend + backend de Reflex),
# eliminamos --backend-only. El "backend" de Reflex ahora solo servirá la app.
CMD reflex run --env prod --backend-port ${PORT:-8000} --backend-host 0.0.0.0


