import reflex as rx

config = rx.Config(
    app_name="PythonWeb",
    api_url="https://api.v1ct0r.dev",
    cors_allowed_origins=[
        "https://www.v1ct0r.dev",
        "https://api.v1ct0r.dev",
        "http://localhost:3000"
    ]
)

