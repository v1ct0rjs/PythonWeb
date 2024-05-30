import reflex as rx

config = rx.Config(
    app_name="PythonWeb",
    cors_allowed_origins=[
        "https://v1ct0r.dev",
        "http://localhost:3000"
    ]
)