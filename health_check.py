"""
Endpoint de health check para Railway
"""
import reflex as rx

@rx.page("/ping")
def ping():
    return rx.text("OK")

# Agregar al app principal
def add_health_check(app):
    app.api.add_api_route("/ping", lambda: {"status": "ok"})
    return app
