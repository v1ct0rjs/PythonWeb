import reflex as rx

config = rx.Config(
    app_name="PythonWeb",
    api_url="https://api.v1ct0r.dev:8000",
    cors_allowed_origins=[
        "https://api.v1ct0r.dev",
        "http://localhost:3000",
    ]
)

