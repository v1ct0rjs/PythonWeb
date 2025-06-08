import reflex as rx
# No necesitamos Route aquí si vamos a usar URLs absolutas directamente
# from PythonWeb.routes import Route
from PythonWeb.styles.styles import Size # Importar Size para padding

def language_button_style():
    return {
        "position": "fixed",
        "top": "80px", # Ajustado para estar más abajo de una posible navbar alta
        "right": "20px",
        "z_index": "1000",
        "background_color": "#1dd3b0", # Color primario
        "color": "white",             # Color del texto
        "border": "none",
        "width": "auto",              # Anular el width global
        "height": "auto",             # Anular el height global
        "padding": f"{Size.SMALL.value} {Size.LARGE.value}", # Padding vertical y horizontal
        "border_radius": Size.MEDIUM.value, # Esquinas redondeadas
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
                rx.icon("languages", size=18, style={"margin_right": Size.SMALL.value}),
                rx.text("English version", font_size="14px"),
                spacing="2",
                align="center"
            ),
            style=language_button_style()
        ),
        href="https://www.v1ct0r.dev/eng/", # URL absoluta
        is_external=True, # Buena práctica para URLs absolutas
        style={"text_decoration": "none"}
    )

def language_button_index() -> rx.Component:
    """Botón para volver a la versión en español (desde la página en inglés)"""
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
        href="https://www.v1ct0r.dev/", # URL absoluta para la versión en español
        is_external=True, # Buena práctica para URLs absolutas
        style={"text_decoration": "none"}
    )

# Mantener compatibilidad por si acaso, aunque las páginas ya usan los nuevos nombres.
float_button = language_button
float_button_index = language_button_index
