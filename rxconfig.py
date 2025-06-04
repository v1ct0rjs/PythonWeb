import reflex as rx
import os

# Configuración para diferentes entornos
def get_api_url():
  # Como no hay backend, retornamos una cadena vacía o None.
  # Una cadena vacía suele ser segura para `reflex export`.
  return ""

config = rx.Config(
  app_name="PythonWeb",
  api_url="", # Esto ahora será ""
  cors_allowed_origins=[
      "https://www.v1ct0r.dev",
      "https://victorjs-web.vercel.app",
      "http://localhost:3000"
  ],
  #backend_port=int(os.getenv("PORT", "8000")),
  frontend_port=3000
)


