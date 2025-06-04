import reflex as rx
import os



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


