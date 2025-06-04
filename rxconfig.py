import reflex as rx
import os

# Temporalmente, para asegurar que en producción la API_URL sea nula
# Asumimos que si se está construyendo con Vercel, es 'prod'
# O puedes basarte en una variable que Vercel sí establece por defecto, como VERCEL_ENV

prod_environment = os.getenv("VERCEL_ENV") == "production" or os.getenv("REFLEX_ENV") == "prod"

final_api_url = "" if prod_environment else "http://localhost:8000"


config = rx.Config(
    app_name="PythonWeb",
    api_url=final_api_url, # Usar la URL determinada
    cors_allowed_origins=[
        "https://www.v1ct0r.dev",
        "https://victorjs-web.vercel.app",
        "http://localhost:3000"
    ],
    frontend_port=3000
)


