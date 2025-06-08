import reflex as rx
from PythonWeb.routes import Route
from PythonWeb.styles.styles import Size # Importar Size para padding

def language_button_style():
    return {
        "position": "fixed",
        "bottom": "20px",
        "right": "20px",
        "z_index": "1000",
        "background_color": "#1dd3b0", # Color primario
        "color": "white",             # Color del texto
        "border": "none",
        "width": "auto",              # Anular el width global
        "height": "auto",             # Anular el height global
        "padding": f"{Size.SMALL.value} {Size.LARGE.value}", # Padding vertical y horizontal (ej: 0.5em 1em)
        "border_radius": Size.MEDIUM.value, # Esquinas redondeadas (ej: 0.8em)
        "_hover": {
            "background_color": "#16a085", # Un tono más oscuro al pasar el ratón
            "transform": "scale(1.05)",
            "cursor": "pointer",
        },
        "transition": "all 0.2s ease"
    }

def language_button() -> rx.Component:
    """Botón para cambiar a la versión en inglés"""
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon("languages", size=18, style={"margin_right": Size.SMALL.value}), # Icono un poco más pequeño y con margen
                rx.text("English version", font_size="14px"),
                spacing="2", # Espaciado entre icono y texto
                align="center"
            ),
            style=language_button_style()
        ),
        href=Route.ENG.value,
        style={"text_decoration": "none"} # Quitar subrayado del enlace
    )

def language_button_index() -> rx.Component:
    """Botón para volver a la versión en español"""
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon("languages", size=18, style={"margin_right": Size.SMALL.value}),
                rx.text("Versión Español", font_size="14px"),
                spacing="2",
                align="center"
            ),
            style=language_button_style()
        ),
        href=Route.INDEX.value,
        style={"text_decoration": "none"}
    )

# Mantener compatibilidad con el código existente si es necesario,
# aunque las páginas ya fueron actualizadas para usar los nuevos nombres.
float_button = language_button
float_button_index = language_button_index
