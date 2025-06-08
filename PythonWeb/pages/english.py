import reflex as rx
from PythonWeb.routes import Route
from PythonWeb.styles.styles import *

@rx.page(route=Route.ENG.value)

def language_button() -> rx.Component:
    """Botón para cambiar a la versión en inglés"""
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon("languages", size=20),
                rx.text("English version", font_size="14px"),
                spacing="2",
                align="center"
            ),
            variant="outline",
            size="2",
            style={
                "position": "fixed",
                "bottom": "20px",
                "right": "20px",
                "z_index": "1000",
                "background_color": "#1dd3b0",
                "color": "white",
                "border": "none",
                "_hover": {
                    "background_color": "#16a085",
                    "transform": "scale(1.05)"
                },
                "transition": "all 0.2s ease"
            }
        ),
        href=Route.ENG.value,
        style={"text_decoration": "none"}
    )

def language_button_index() -> rx.Component:
    """Botón para volver a la versión en español"""
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon("languages", size=20),
                rx.text("Versión Español", font_size="14px"),
                spacing="2",
                align="center"
            ),
            variant="outline",
            size="2",
            style={
                "position": "fixed",
                "bottom": "20px",
                "right": "20px",
                "z_index": "1000",
                "background_color": "#1dd3b0",
                "color": "white",
                "border": "none",
                "_hover": {
                    "background_color": "#16a085",
                    "transform": "scale(1.05)"
                },
                "transition": "all 0.2s ease"
            }
        ),
        href=Route.INDEX.value,
        style={"text_decoration": "none"}
    )

# Mantener compatibilidad con el código existente
float_button = language_button
float_button_index = language_button_index
