import reflex as rx
import os

# Configuración para diferentes entornos
def get_api_url():
    env = os.getenv("REFLEX_ENV", "dev")
    if env == "prod":
        return "https://pythonweb-backend-production.up.railway.app"
    return "http://localhost:8000"

config = rx.Config(
    app_name="PythonWeb",
    api_url=get_api_url(),
    cors_allowed_origins=[
        "https://www.v1ct0r.dev",
        "https://victorjs-web.vercel.app",
        "http://localhost:3000",
        "http://localhost:8000"
    ],
    backend_port=int(os.getenv("PORT", "8000")),
    frontend_port=3000
)


